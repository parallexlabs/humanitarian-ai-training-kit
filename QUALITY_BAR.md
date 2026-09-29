# Quality bar

Acceptance criteria for publishing the Humanitarian AI Training Kit. Run all checks before release.

## Build and validation

| Check | Command | Pass criterion |
|-------|---------|----------------|
| Site and PDFs | `python3 scripts/build.py --all` | Exit code 0 |
| PDF/UA-1 | Included in `--all` | Every PDF passes `verapdf -f ua1` and `qpdf --check` |
| Links | Included in `--all` | 0 broken internal links |
| axe WCAG 2.2 | `python3 scripts/axe_audit.py` | 0 violations on all built pages |
| EN/FR parity | `python3 scripts/compare_en_fr.py` | 0 mismatches |

## Content honesty

- Learning materials only. No invented delivery history, cohort data, testimonials, or translator credentials.
- Sample final-report page stays a clearly labelled template.
- AAP design note describes how adopting organizations should consult affected communities; never claim consultation already occurred for this kit.
- French materials include machine-assistance notice and plain statement that no professional translator has reviewed them yet.

## Accessibility

- HTML is the primary accessible format (WCAG 2.2 AA).
- Every diagram has full alt text and a text equivalent in the same page.
- Slide decks support keyboard navigation.
- Technology checklist includes captioning plan and synchronous low-bandwidth route (audio or phone plus chat).

## Bilingual parity

- Every markdown page in `content/en/` has a matching file in `content/fr/`.
- Parity checker compares numbers, dates, times, list counts, table rows, and negation markers.

## Style

- No em dashes in content.
- No AI tool or model named as an author.
- README "Open by design" section is fixed text; do not edit without explicit approval.

## References

- Every reference entry includes a publisher-stated publication or version date and `Accessed 2026-09-29` (update access date on each release).
- Directive on Automated Decision-Making includes scope note: binds Canadian federal institutions; context, not a legal obligation, for NGOs.
