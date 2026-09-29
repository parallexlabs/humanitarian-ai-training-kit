# Changelog

All notable changes to this project are documented here.

## [1.1.0] - 2026-09-29

### Added

- PDF/UA-1 pipeline: pandoc to DOCX, LibreOffice tagged export, pypdf link descriptions (`scripts/render_pdf.py`)
- axe-core WCAG 2.2 audit via Playwright (`scripts/axe_audit.py`); CI integration
- EN/FR parity checker (`scripts/compare_en_fr.py`)
- Deliverables acceptance checklist, sample final-report template, 15-minute source-check activity (EN/FR)
- Slide deck keyboard navigation (arrow keys, Previous/Next buttons)
- `build/pdf-qa.json` and `build/axe-report.json` build artifacts

### Changed

- Replaced Chromium/Playwright PDF generation with LibreOffice PDF/UA-1 recipe (92/92 pass veraPDF ua1)
- Verified ICRC AI Policy 2024 URL; UNHCR AI Approach PDF URL; IFRC data protection policy PDF URL
- French references aligned with English (ICRC handbook 3rd edition, Canadian privacy sections)
- Navigation CSS touch targets meet WCAG 2.2 target-size (axe: 0 violations)

## [1.0.0] - 2026-09-28

### Added

- Bilingual (English and French) curriculum for three 90-minute sessions and a 60-minute follow-up clinic
- Eight synthetic case studies with tasks, model answers, and debrief guidance
- Pre/post assessment, skills rubric, and session evaluation form
- AI use decision guide and data-responsibility checklist
- Accessible HTML site and tagged PDF build pipeline (`scripts/build.py`)
- References with verified public primary sources
- CC BY 4.0 content licence and Apache-2.0 code licence

### Notes

- French translations prepared with machine assistance; professional human review recommended
- Learning materials only; not a record of delivered training
