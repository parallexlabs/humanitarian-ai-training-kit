# Changelog

All notable changes to this project are documented here.

## [1.3.0] - 2026-09-30

### Added

- 30-day workplace transfer follow-up tool (Kirkpatrick level 3, self-reported) with analysis guidance (EN/FR)
- Facilitator reflection log with per-session entries and end-of-series synthesis (EN/FR)
- Kirkpatrick levels 1 to 3 named on evaluation pages; level 4 noted as outside kit scope (EN/FR)
- Session 3 transparency card exercise (15 minutes) with printable template and optional online tool link (EN/FR)
- SAFE AI v1.2 crosswalk in the AI use decision guide (EN/FR)
- ParalleX Labs brand mark in site header and README; favicon and apple-touch icon
- References: SAFE AI v1.2 and Kirkpatrick (2016) (EN/FR)

### Changed

- Session 3 timing: challenge block shortened by 15 minutes for transparency card exercise; total session length unchanged (EN/FR)
- Facilitator guide cut list documents challenge block as the permanent time source (EN/FR)
- Sample final-report page includes 30-day transfer summary section (EN/FR)
- README "What is included" updated for new tools and Kirkpatrick framing

## [1.2.1] - 2026-09-29

### Fixed

- Published site: stylesheet, images and every internal link now resolve under the project sub-path; root-absolute links had returned 404 on GitHub Pages
- Cross-references between pages now point at the built HTML pages instead of markdown sources
- Diagrams now appear in the PDFs; the image path was not found, so only the alt text had been rendered
- Each page links to its tagged PDF; PDF titles come from the page heading (for example "AI use decision guide")
- CI installs librsvg for SVG conversion; the link check now resolves relative links and fails on any root-absolute link

## [1.2.0] - 2026-09-29

### Added

- Facilitator delivery guide with per-session cues, misconceptions, cut lists, and safeguarding escalation (EN/FR)
- Safeguarding and protection module in Session 3 and data-responsibility checklist (EN/FR)
- Delivery artifacts: sample invitation email, participant handbook, facilitator preparation checklist, technology and accessibility checklist (EN/FR)
- AAP adaptation design note for adopting organizations (EN/FR)
- Visual aids page with AI decision flow and data-responsibility lifecycle diagrams plus text equivalents (EN/FR)
- Optional Session 2 live-tool lab route for org-approved tools with synthetic data only (EN/FR)
- `QUALITY_BAR.md` acceptance criteria

### Changed

- Pre/post assessment: performance scenarios with skills rubric as primary measure; self-efficacy secondary (EN/FR)
- References: publisher dates, Accessed 2026-09-29, OCHA January 2025 / published 20 February 2025, Directive scope note for NGOs (EN/FR)
- Curriculum overview, facilitation tips: synchronous low-bandwidth phone-plus-chat route (EN/FR)
- README: French quality, parity checks, terminology glossary, professional review status

### Fixed

- References: removed a literature citation that could not be verified and a pointer to an internal verification log; the themes table now maps only to the verified sources listed in the same file (EN/FR)
- Pre/post knowledge item 12: the marked answer was wrong; the correct option now states that role play is practice only and does not replace consultation with affected people (EN/FR)
- Pre/post knowledge items: correct answers are now spread across options A to D (previously 10 of 12 were B) (EN/FR)
- Directive on Automated Decision-Making: link moved to the Treasury Board policy page after the Canada.ca address stopped resolving (EN/FR)

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
