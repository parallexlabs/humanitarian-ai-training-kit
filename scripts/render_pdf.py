#!/usr/bin/env python3
"""Render accessible PDF/UA-1 documents from markdown via pandoc, LibreOffice, and pypdf."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject

LANG_CODES = {"en": "en-CA", "fr": "fr-CA"}


def preprocess_slides(md_text: str) -> str:
    """Convert slide deck separators into page breaks for DOCX export."""
    slides = re.split(r"\n---\n", md_text.strip())
    parts: list[str] = []
    for slide in slides:
        slide = slide.strip()
        if not slide or slide.startswith("<!--"):
            continue
        parts.append(slide)
        parts.append("\n\n\\newpage\n\n")
    return "\n\n".join(parts).rstrip()


PDF_TRUNCATE_AT_HEADING = {
    "transparency-card-template.md": (
        "## Session 3 exercise (facilitation only; not part of the printable card)",
        "## Exercice de la séance 3 (animation seulement; ne fait pas partie de la fiche imprimable)",
    ),
}


def truncate_for_pdf(md_text: str, md_path: Path) -> str:
    markers = PDF_TRUNCATE_AT_HEADING.get(md_path.name)
    if not markers:
        return md_text
    for marker in markers:
        idx = md_text.find(marker)
        if idx != -1:
            return md_text[:idx].rstrip() + "\n"
    return md_text


def preprocess_markdown(md_text: str, is_slides: bool, md_path: Path | None = None) -> str:
    if is_slides:
        return preprocess_slides(md_text)
    if md_path is not None:
        md_text = truncate_for_pdf(md_text, md_path)
    return md_text


REPO_ROOT = Path(__file__).resolve().parents[1]


def _document_title(md_text: str, md_path: Path) -> str:
    """Use the page's first level-one heading, so acronyms keep their case ("AI", not "Ai")."""
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip().replace("*", "").replace("`", "")
    return md_path.stem.replace("-", " ").capitalize()


def md_to_docx(md_path: Path, docx_path: Path, lang: str, is_slides: bool = False) -> None:
    md_text = md_path.read_text(encoding="utf-8")
    processed = preprocess_markdown(md_text, is_slides, md_path)
    # Site-root image paths ("/assets/...") mean the repository assets folder when building the PDF.
    processed = processed.replace("](/assets/", f"]({REPO_ROOT / 'assets'}/")
    lang_code = LANG_CODES.get(lang, lang)
    cmd = [
        "pandoc",
        "-f",
        "markdown",
        "-t",
        "docx",
        "--metadata",
        f"lang={lang_code}",
        "--metadata",
        f"title={_document_title(md_text, md_path)}",
        "-o",
        str(docx_path),
    ]
    proc = subprocess.run(cmd, input=processed, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        raise RuntimeError(f"pandoc failed for {md_path.name}: {proc.stderr}")


def render_pdf(docx: Path, output: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="lo_pdfua_") as profile:
        profile_uri = Path(profile).as_uri()
        subprocess.run(
            [
                "soffice",
                f"-env:UserInstallation={profile_uri}",
                "--headless",
                "--convert-to",
                'pdf:writer_pdf_Export:{"PDFUACompliance":{"type":"boolean","value":"true"},"UseTaggedPDF":{"type":"boolean","value":"true"}}',
                "--outdir",
                str(docx.parent),
                str(docx),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    generated = docx.with_suffix(".pdf")
    if not generated.exists():
        raise RuntimeError(f"LibreOffice did not render {docx.name}")
    reader = PdfReader(generated)
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    for page in writer.pages:
        for ref in page.get("/Annots", []):
            annotation = ref.get_object()
            if annotation.get("/Subtype") == "/Link" and not annotation.get("/Contents"):
                action = annotation.get("/A")
                label = str(action.get("/URI", "Source link")) if action else "Source link"
                annotation[NameObject("/Contents")] = TextStringObject(label)
    temporary = output.with_suffix(".validated-links.tmp.pdf")
    with temporary.open("wb") as stream:
        writer.write(stream)
    temporary.replace(output)
    if output != generated and generated.exists():
        generated.unlink()


def markdown_to_pdf(md_path: Path, output: Path, lang: str, is_slides: bool = False) -> None:
    with tempfile.TemporaryDirectory(prefix="pdf_build_") as tmp:
        docx = Path(tmp) / f"{md_path.stem}.docx"
        md_to_docx(md_path, docx, lang, is_slides=is_slides)
        render_pdf(docx, output)


def validate_pdf(pdf: Path, verapdf: Path | None = None) -> dict:
    result: dict = {"file": str(pdf), "qpdf_ok": None, "verapdf_ok": None, "passed": True}
    qpdf = subprocess.run(
        ["qpdf", "--check", str(pdf)],
        capture_output=True,
        text=True,
        check=False,
    )
    result["qpdf_ok"] = qpdf.returncode == 0
    if not result["qpdf_ok"]:
        result["passed"] = False
        result["qpdf_detail"] = (qpdf.stderr or qpdf.stdout).strip()[:300]

    verapdf_bin = verapdf or Path("/opt/homebrew/bin/verapdf")
    if verapdf_bin.exists():
        vp = subprocess.run(
            [str(verapdf_bin), "-f", "ua1", "--format", "xml", str(pdf)],
            capture_output=True,
            text=True,
            check=False,
        )
        result["verapdf_ok"] = 'isCompliant="true"' in vp.stdout
        if not result["verapdf_ok"]:
            result["passed"] = False
            result["verapdf_detail"] = "PDF/UA-1 non-compliant"
    return result


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Render PDF/UA-1 from markdown")
    parser.add_argument("markdown", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--lang", default="en", choices=["en", "fr"])
    parser.add_argument("--slides", action="store_true")
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args(argv)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    markdown_to_pdf(args.markdown, args.output, args.lang, is_slides=args.slides)
    if args.validate:
        print(json.dumps(validate_pdf(args.output), indent=2))
        return 0 if validate_pdf(args.output)["passed"] else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
