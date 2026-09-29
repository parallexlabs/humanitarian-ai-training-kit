# Humanitarian AI Training Kit

Open, bilingual (English and French), accessible training on using AI responsibly in humanitarian action. Designed for staff of Canadian humanitarian and development organizations.

**These are learning materials, not a record of delivered training.**

| | |
|---|---|
| **Owner** | ParalleX Labs Inc. |
| **Content licence** | [CC BY 4.0](LICENSE) |
| **Code licence** | [Apache-2.0](LICENSE-CODE) |
| **Languages** | English (`content/en/`), French (`content/fr/`) |

French versions were prepared with machine assistance; human review by a professional translator is recommended before use.

## Open by design

**We build in the open.** ParalleX Labs Inc. publishes its tools, methods and learning materials under open licences, so public-interest teams can use them, check how they work and adapt them freely. Open work is easier to trust, because anyone can see exactly how a result is produced.

**Our own work, and only ours.** Everything in this repository was created by ParalleX Labs Inc. from public guidance and synthetic examples. It contains no client data, no client projects, and no one else's confidential information or intellectual property.

## What is included

- [Curriculum overview](content/en/curriculum-overview.md) with learning outcomes, time plan, and adaptation guidance for 15 to 40 participants
- Three 90-minute sessions plus a 60-minute follow-up clinic (facilitator run sheets, slides, worksheets, answer keys)
- Optional [15-minute source-check activity](content/en/sessions/short-source-check/activity.md) with breakout, plenary, and text-only routes
- Eight synthetic case studies
- Pre/post assessment, skills rubric, evaluation form, and [sample final-report page](content/en/assessment/sample-final-report-page.md)
- [AI use decision guide](content/en/tools/ai-decision-guide.md), [data-responsibility checklist](content/en/tools/data-responsibility-checklist.md), and [deliverables acceptance checklist](content/en/tools/deliverables-acceptance-checklist.md)
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

**PDF/UA-1 (last build):** 92 of 92 PDFs pass veraPDF `-f ua1` and `qpdf --check`. HTML remains the primary accessible format (WCAG 2.2 AA).

### Accessibility audit

```bash
python3 scripts/axe_audit.py
```

Runs axe-core with WCAG 2.2 A and AA rule tags on every built page in English and French. **Last audit:** 0 violations across 110 pages.

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
