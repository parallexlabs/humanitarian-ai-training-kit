#!/usr/bin/env python3
"""Build accessible HTML site and PDF/UA-1 PDFs from markdown sources."""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
BUILD = ROOT / "build"
ASSETS = ROOT / "assets"
VERAPDF = Path("/opt/homebrew/bin/verapdf")

sys.path.insert(0, str(ROOT / "scripts"))
from render_pdf import markdown_to_pdf, validate_pdf  # noqa: E402

LANG_META = {
    "en": {"label": "English", "notice": ""},
    "fr": {
        "label": "Français",
        "notice": (
            "French version prepared with machine assistance; human review by a "
            "professional translator is recommended before use."
        ),
    },
}

NAV_ITEMS = [
    ("curriculum-overview.md", "Curriculum overview", "Aperçu du programme"),
    ("sessions/session-01-foundations/", "Session 1", "Séance 1"),
    ("sessions/session-02-verified-work/", "Session 2", "Séance 2"),
    ("sessions/session-03-governance/", "Session 3", "Séance 3"),
    ("sessions/clinic/", "Clinic", "Clinique"),
    ("sessions/short-source-check/", "Short activity", "Activité courte"),
    ("case-studies/", "Case studies", "Études de cas"),
    ("assessment/", "Assessment", "Évaluation"),
    ("tools/", "Tools", "Outils"),
    ("references.md", "References", "Références"),
]


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, capture_output=True, text=True, check=check)


def md_to_html_body(md_text: str) -> str:
    proc = subprocess.run(
        ["pandoc", "-f", "markdown", "-t", "html5", "--wrap=none"],
        input=md_text,
        capture_output=True,
        text=True,
        check=True,
    )
    return proc.stdout


def extract_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def wrap_page(
    body: str,
    title: str,
    lang: str,
    rel_path: str,
    is_home: bool = False,
) -> str:
    other_lang = "fr" if lang == "en" else "en"
    other_href = rel_path.replace(f"/{lang}/", f"/{other_lang}/", 1)

    nav_links = []
    for item_path, en_label, fr_label in NAV_ITEMS:
        label = en_label if lang == "en" else fr_label
        if item_path.endswith("/"):
            href = f"/{lang}/{item_path}index.html"
        else:
            href = f"/{lang}/{item_path.replace('.md', '.html')}"
        nav_links.append(f'<li><a href="{html.escape(href)}">{html.escape(label)}</a></li>')

    notice = LANG_META[lang]["notice"]
    notice_html = ""
    if notice:
        notice_html = f'<div class="lang-notice" role="note">{html.escape(notice)}</div>'

    lang_switch = (
        f'<a href="{html.escape(other_href)}" hreflang="{other_lang}" '
        f'lang="{other_lang}">{LANG_META[other_lang]["label"]}</a>'
    )

    h1 = f"<h1>{html.escape(title)}</h1>" if not is_home else ""
    skip = '<a class="skip-link" href="#main">Skip to main content</a>'
    header = f"""<header class="site-header" role="banner">
    <p><strong>ParalleX Labs</strong> Humanitarian AI Training Kit</p>
    <nav aria-label="Primary">
      <ul>
        {''.join(nav_links)}
        <li>{lang_switch}</li>
      </ul>
    </nav>
  </header>"""
    footer = """<footer class="site-footer" role="contentinfo">
    <p>© ParalleX Labs Inc. Content licensed <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.
    Code licensed <a href="https://www.apache.org/licenses/LICENSE-2.0">Apache-2.0</a>.</p>
    <p>Learning materials only. Not a record of delivered training.</p>
  </footer>"""

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | Humanitarian AI Training Kit</title>
  <link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>
  {skip}
  {header}
  <main id="main" role="main">
    {notice_html}
    {h1}
    {body}
  </main>
  {footer}
</body>
</html>"""


def build_slide_deck(slides_md: Path, out_html: Path, out_pdf: Path, lang: str, title: str) -> int:
    text = slides_md.read_text(encoding="utf-8")
    slides = re.split(r"\n---\n", text)
    slide_html_parts = []
    count = 0
    for slide in slides:
        slide = slide.strip()
        if not slide or slide.startswith("<!--"):
            continue
        count += 1
        body = md_to_html_body(slide)
        slide_html_parts.append(
            f'<section class="slide" id="slide-{count}" tabindex="-1" '
            f'aria-label="Slide {count}">'
            f'<p class="slide-number" aria-hidden="true">Slide {count} of ?</p>{body}</section>'
        )
    total = len(slide_html_parts)
    deck_body = (
        '<nav class="slide-nav" aria-label="Slide navigation">'
        '<button type="button" id="slide-prev" aria-label="Previous slide">Previous</button>'
        '<button type="button" id="slide-next" aria-label="Next slide">Next</button>'
        '</nav>'
        '<div class="slide-deck" role="region" aria-label="Slide deck" aria-live="polite">'
    )
    for i, part in enumerate(slide_html_parts, 1):
        part = part.replace("Slide {count} of ?", f"Slide {i} of {total}")
        deck_body += part.replace(f"Slide {i} of ?", f"Slide {i} of {total}")
    deck_body += "</div>"
    deck_body += """<script>
(function(){
  var slides=document.querySelectorAll('.slide-deck .slide');
  var idx=0;
  function show(i){
    if(i<0||i>=slides.length)return;
    idx=i;
    slides.forEach(function(s,j){s.hidden=j!==idx;});
    document.getElementById('slide-prev').disabled=idx===0;
    document.getElementById('slide-next').disabled=idx===slides.length-1;
    slides[idx].focus();
  }
  slides.forEach(function(s,j){if(j>0)s.hidden=true;});
  document.getElementById('slide-prev').addEventListener('click',function(){show(idx-1);});
  document.getElementById('slide-next').addEventListener('click',function(){show(idx+1);});
  document.addEventListener('keydown',function(e){
    if(e.key==='ArrowRight'||e.key==='PageDown'){e.preventDefault();show(idx+1);}
    if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();show(idx-1);}
  });
})();
</script>"""

    rel = "/" + str(out_html.relative_to(BUILD)).replace("\\", "/")
    page = wrap_page(deck_body, title, lang, rel)
    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(page, encoding="utf-8")
    markdown_to_pdf(slides_md, out_pdf, lang, is_slides=True)
    return total


def build_markdown_page(src: Path, dst: Path, lang: str) -> None:
    md = src.read_text(encoding="utf-8")
    title = extract_title(md, src.stem.replace("-", " ").title())
    body = md_to_html_body(md)
    if body.lstrip().startswith("<h1"):
        body = re.sub(r"^<h1[^>]*>.*?</h1>\s*", "", body, count=1, flags=re.I)
    rel = "/" + str(dst.relative_to(BUILD)).replace("\\", "/")
    page = wrap_page(body, title, lang, rel)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(page, encoding="utf-8")
    pdf_path = dst.with_suffix(".pdf")
    markdown_to_pdf(src, pdf_path, lang, is_slides=False)


def build_index(lang: str) -> None:
    title = "Humanitarian AI Training Kit" if lang == "en" else "Trousse de formation sur l'IA humanitaire"
    intro_en = """
<p>Open, bilingual training on using AI responsibly in humanitarian action.
Designed for staff of Canadian humanitarian and development organizations.</p>
<ul>
<li><a href="curriculum-overview.html">Curriculum overview</a></li>
<li><a href="sessions/session-01-foundations/index.html">Session 1: Responsible AI foundations</a></li>
<li><a href="sessions/session-02-verified-work/index.html">Session 2: Verified work by role</a></li>
<li><a href="sessions/session-03-governance/index.html">Session 3: Governance and adoption</a></li>
<li><a href="sessions/clinic/index.html">Follow-up clinic</a></li>
<li><a href="sessions/short-source-check/index.html">Optional 15-minute source-check activity</a></li>
<li><a href="case-studies/index.html">Synthetic case studies</a></li>
<li><a href="assessment/index.html">Assessment tools</a></li>
<li><a href="tools/index.html">Decision guide and checklists</a></li>
<li><a href="references.html">References</a></li>
</ul>
"""
    intro_fr = """
<p>Formation ouverte et bilingue sur l'utilisation responsable de l'IA dans l'action humanitaire.
Conçue pour le personnel d'organisations humanitaires et de développement canadiennes.</p>
<ul>
<li><a href="curriculum-overview.html">Aperçu du programme</a></li>
<li><a href="sessions/session-01-foundations/index.html">Séance 1 : Fondements de l'IA responsable</a></li>
<li><a href="sessions/session-02-verified-work/index.html">Séance 2 : Travail vérifié par rôle</a></li>
<li><a href="sessions/session-03-governance/index.html">Séance 3 : Gouvernance et adoption</a></li>
<li><a href="sessions/clinic/index.html">Clinique de suivi</a></li>
<li><a href="sessions/short-source-check/index.html">Activité optionnelle de vérification des sources (15 min)</a></li>
<li><a href="case-studies/index.html">Études de cas synthétiques</a></li>
<li><a href="assessment/index.html">Outils d'évaluation</a></li>
<li><a href="tools/index.html">Guide de décision et listes de contrôle</a></li>
<li><a href="references.html">Références</a></li>
</ul>
"""
    body = intro_en if lang == "en" else intro_fr
    rel = f"/{lang}/index.html"
    page = wrap_page(body, title, lang, rel, is_home=True)
    out = BUILD / lang / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")


def build_section_index(section_dir: Path, lang: str, title: str, items: list[tuple[str, str]]) -> None:
    links = "\n".join(f'<li><a href="{html.escape(href)}">{html.escape(label)}</a></li>' for href, label in items)
    body = f"<ul>{links}</ul>"
    rel = f"/{lang}/{section_dir.relative_to(CONTENT / lang)}/index.html"
    page = wrap_page(body, title, lang, rel)
    out = BUILD / lang / section_dir.relative_to(CONTENT / lang) / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")


def copy_assets() -> None:
    dst = BUILD / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(ASSETS, dst)


def build_site() -> dict:
    if BUILD.exists():
        shutil.rmtree(BUILD)
    BUILD.mkdir()
    copy_assets()

    stats = {"pages": 0, "slides": 0, "pdfs": 0}

    for lang in ("en", "fr"):
        lang_dir = CONTENT / lang
        build_index(lang)
        stats["pages"] += 1

        for md_file in sorted(lang_dir.rglob("*.md")):
            rel = md_file.relative_to(lang_dir)
            if rel.name == "index.md":
                continue
            out_html = BUILD / lang / rel.with_suffix(".html")
            if rel.name == "slides.md":
                title = extract_title(md_file.read_text(encoding="utf-8"), "Slides")
                n = build_slide_deck(
                    md_file,
                    BUILD / lang / rel.with_suffix(".html"),
                    BUILD / lang / rel.with_suffix(".pdf"),
                    lang,
                    title,
                )
                stats["slides"] += n
                stats["pages"] += 1
                stats["pdfs"] += 1
                continue
            build_markdown_page(md_file, out_html, lang)
            stats["pages"] += 1
            stats["pdfs"] += 1

        case_items = [
            (f.name.replace(".md", ".html"), extract_title((CONTENT / lang / "case-studies" / f.name).read_text(encoding="utf-8"), f.stem))
            for f in sorted((lang_dir / "case-studies").glob("*.md"))
            if f.name != "index.md"
        ]
        build_section_index(
            lang_dir / "case-studies",
            lang,
            "Case studies" if lang == "en" else "Études de cas",
            case_items,
        )
        stats["pages"] += 1

        assess_items = [
            (f.name.replace(".md", ".html"), extract_title(f.read_text(encoding="utf-8"), f.stem))
            for f in sorted((lang_dir / "assessment").glob("*.md"))
            if f.name != "index.md"
        ]
        build_section_index(
            lang_dir / "assessment",
            lang,
            "Assessment" if lang == "en" else "Évaluation",
            assess_items,
        )
        stats["pages"] += 1

        tools_items = [
            (f.name.replace(".md", ".html"), extract_title(f.read_text(encoding="utf-8"), f.stem))
            for f in sorted((lang_dir / "tools").glob("*.md"))
        ]
        build_section_index(
            lang_dir / "tools",
            lang,
            "Tools" if lang == "en" else "Outils",
            tools_items,
        )
        stats["pages"] += 1

        session_dirs = (
            "session-01-foundations",
            "session-02-verified-work",
            "session-03-governance",
            "clinic",
            "short-source-check",
        )
        for session in session_dirs:
            sdir = lang_dir / "sessions" / session
            if not sdir.exists():
                continue
            items = [
                (f.name.replace(".md", ".html"), extract_title(f.read_text(encoding="utf-8"), f.stem))
                for f in sorted(sdir.glob("*.md"))
            ]
            labels = {
                "session-01-foundations": ("Session 1", "Séance 1"),
                "session-02-verified-work": ("Session 2", "Séance 2"),
                "session-03-governance": ("Session 3", "Séance 3"),
                "clinic": ("Clinic", "Clinique"),
                "short-source-check": ("Short activity", "Activité courte"),
            }
            build_section_index(sdir, lang, labels[session][0 if lang == "en" else 1], items)
            stats["pages"] += 1

    (BUILD / "index.html").write_text(
        """<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>Humanitarian AI Training Kit</title>
<meta http-equiv="refresh" content="0; url=/en/index.html">
<link rel="canonical" href="/en/index.html"></head>
<body><p><a href="/en/index.html">English</a> | <a href="/fr/index.html">Français</a></p></body>
</html>""",
        encoding="utf-8",
    )
    stats["pages"] += 1

    manifest = BUILD / "build-manifest.json"
    manifest.write_text(json.dumps(stats, indent=2), encoding="utf-8")
    return stats


def check_pdfs() -> dict:
    results: dict = {"verapdf": [], "qpdf": [], "passed": True, "total": 0, "passed_count": 0}
    pdfs = sorted(BUILD.rglob("*.pdf"))
    results["total"] = len(pdfs)
    for pdf in pdfs:
        vr = validate_pdf(pdf, VERAPDF if VERAPDF.exists() else None)
        rel = str(pdf.relative_to(ROOT))
        results["qpdf"].append({"file": rel, "ok": vr["qpdf_ok"]})
        if vr.get("verapdf_ok") is not None:
            results["verapdf"].append({"file": rel, "ok": vr["verapdf_ok"]})
        if vr["passed"]:
            results["passed_count"] += 1
        else:
            results["passed"] = False
    qa_path = BUILD / "pdf-qa.json"
    qa_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
    return results


def check_links() -> dict:
    results = {"broken": [], "checked": 0}
    for html_file in BUILD.rglob("*.html"):
        text = html_file.read_text(encoding="utf-8")
        for match in re.finditer(r'href="(/[^"]+)"', text):
            href = match.group(1).split("#")[0]
            if not href or href.startswith("http"):
                continue
            target = BUILD / href.lstrip("/")
            results["checked"] += 1
            if not target.exists():
                results["broken"].append({"file": str(html_file.relative_to(ROOT)), "href": href})
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Build humanitarian AI training kit site")
    parser.add_argument("--check-pdfs", action="store_true")
    parser.add_argument("--check-links", action="store_true")
    parser.add_argument("--all", action="store_true", help="Build and run all checks")
    args = parser.parse_args()

    if args.all or not (args.check_pdfs or args.check_links):
        stats = build_site()
        print(f"Built {stats['pages']} pages, {stats['slides']} slides, {stats['pdfs']} PDFs")

    if args.all or args.check_pdfs:
        pdf_results = check_pdfs()
        print(json.dumps(pdf_results, indent=2))
        if not pdf_results["passed"]:
            return 1

    if args.all or args.check_links:
        link_results = check_links()
        print(json.dumps(link_results, indent=2))
        if link_results["broken"]:
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
