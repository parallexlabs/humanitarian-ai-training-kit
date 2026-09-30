# Humanitarian AI Training Kit

<img src="assets/images/brand/parallex-mark.png" alt="ParalleX Labs" width="64" height="64">

Open, bilingual (English and French), accessible training on using AI responsibly in humanitarian action. Designed for staff of Canadian humanitarian and development organizations.

**These are learning materials, not a record of delivered training.**

| | |
|---|---|
| **Owner** | ParalleX Labs Inc. |
| **Content licence** | [CC BY 4.0](LICENSE) |
| **Code licence** | [Apache-2.0](LICENSE-CODE) |
| **Languages** | English (`content/en/`), French (`content/fr/`) |

French versions were prepared with machine assistance; human review by a professional translator is recommended before use.

### French quality and parity

- **Parity checks:** `scripts/compare_en_fr.py` compares every EN/FR file pair for numbers, dates, times, ordered and unordered list counts, table rows, and negation markers. Release requires 0 mismatches.
- **Terminology glossary (key terms):** *green / amber / red* = vert / ambre / rouge; *affected people* = personnes touchées; *data responsibility* = responsabilité des données; *safeguarding* = sauvegarde; *PSEA* = PSEA (Protection contre l'exploitation et les atteintes sexuelles); *accountability* = responsabilité (rendered *responsabilité envers les personnes touchées* where the English means accountability to affected people).
- **Professional review:** No professional translator has reviewed the French materials yet. Treat them as draft until your organization completes review for your context.
- **Machine assistance:** French files were produced with machine assistance and edited for structural parity with English; they are not certified translations.

## Open by design

**We build in the open.** ParalleX Labs Inc. publishes its tools, methods and learning materials under open licences, so public-interest teams can use them, check how they work and adapt them freely. Open work is easier to trust, because anyone can see exactly how a result is produced.

**Our own work, and only ours.** ParalleX Labs Inc. created the learning design and synthetic examples. Public-source quotations are attributed and retain their original licences. This repository contains no client data, client projects or confidential material.

## What is included

- [Curriculum overview](content/en/curriculum-overview.md) with learning outcomes, time plan, and adaptation guidance for 15 to 40 participants
- Three 90-minute sessions plus a 60-minute follow-up clinic (facilitator run sheets, slides, worksheets, answer keys)
- Optional [15-minute source-check activity](content/en/sessions/short-source-check/activity.md) with breakout, plenary, and text-only routes
- Eight synthetic case studies
- Pre/post assessment (Kirkpatrick level 2), session evaluation form (level 1), [30-day transfer follow-up](content/en/tools/transfer-follow-up.md) (level 3, self-reported), skills rubric, and [sample final-report page](content/en/assessment/sample-final-report-page.md)
- [AI use decision guide](content/en/tools/ai-decision-guide.md) with SAFE AI crosswalk, [transparency card template](content/en/tools/transparency-card-template.md), [facilitator reflection log](content/en/tools/facilitator-reflection-log.md), [data-responsibility checklist](content/en/tools/data-responsibility-checklist.md), [deliverables acceptance checklist](content/en/tools/deliverables-acceptance-checklist.md), [facilitator guide](content/en/tools/facilitator-guide.md), [participant handbook](content/en/tools/participant-handbook.md), and [technology checklist](content/en/tools/technology-accessibility-checklist.md)
- [References](content/en/references.md) with public primary sources

## Build the site and PDFs

Requires Python 3.11+, [Pandoc](https://pandoc.org/), [LibreOffice](https://www.libreoffice.org/) (headless), [qpdf](https://qpdf.readthedocs.io/), and optionally [veraPDF](https://verapdf.org/) for local PDF/UA-1 validation.

```bash
pip install -r requirements.txt
python -m playwright install chromium
curl -sL -o scripts/axe.min.js https://cdn.jsdelivr.net/npm/axe-core@4.10.2/axe.min.js
python3 scripts/build.py --all
python3 scripts/axe_audit.py
python3 scripts/compare_en_fr.py
```

This generates an accessible static HTML site in `build/`, PDF/UA-1 tagged PDFs for each markdown page (pandoc to DOCX, LibreOffice export with tagged PDF, pypdf link descriptions), and writes `build/pdf-qa.json` and `build/axe-report.json`.

### PDF validation

```bash
python3 scripts/build.py --check-pdfs
```

veraPDF path used locally: `/opt/homebrew/bin/verapdf` (profile `-f ua1`)

**PDF/UA-1 (last build):** See `build/pdf-qa.json` after `python3 scripts/build.py --all`. HTML remains the primary accessible format (WCAG 2.2 AA).

### Accessibility audit

```bash
python3 scripts/axe_audit.py
```

Runs axe-core with WCAG 2.2 A and AA rule tags on every built page in English and French. **Last audit:** see `build/axe-report.json` after build.

### Link check

```bash
python3 scripts/build.py --check-links
```

### EN/FR parity

```bash
python3 scripts/compare_en_fr.py
```

Compares numbers, dates, times, list and step counts, and negation markers across EN/FR file pairs.

## CI

GitHub Actions runs the full build, link check, qpdf validation, axe audit, and EN/FR parity check on every push. veraPDF runs when installed on the runner.

## Citation

See [CITATION.cff](CITATION.cff).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).
