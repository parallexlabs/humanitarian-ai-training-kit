# Case study 2: Needs-assessment summary with invented statistic

<div class="synthetic-label"><strong>SYNTHETIC</strong> Fictional MEAL excerpt and AI summary for training only.</div>

## Scenario

An AI tool produced a one-paragraph summary of a needs-assessment report for a funding meeting.

**Authorized source (excerpt S2, March 2026):** "In Sample District, 412 households were surveyed across 6 villages. 31% reported inadequate water access in the dry season. The survey does not estimate district-wide prevalence."

**AI summary:** "Approximately 78% of households in Sample District lack reliable clean water, indicating severe WASH gaps requiring urgent scale-up."

## Your task (10 minutes)

1. Which claims in the summary need verification against S2?
2. Mark each claim: supported, unsupported, or contradicted.
3. What harm could follow if the 78% figure is used in a donor deck?
4. Green, amber, or red for using this summary as-is?

## Model answer

| Claim | Check against S2 | Verdict |
|-------|------------------|---------|
| 78% lack clean water | S2 says 31% inadequate water (dry season); no district-wide figure | Contradicted/invented |
| "Severe WASH gaps" | Subjective; not a direct quote from S2 | Unsupported escalation |
| 412 households / 6 villages | Not in AI summary | Omission of sample scope |

**Decision:** Red for operational or donor use without rewrite. Amber if used internally with clear "draft, unverified" label and immediate correction.

**Harm:** Overstated needs may misdirect funds; understated trust in AI may repeat in future crises.

## Common errors

- Rounding 31% to "about a third" without noting seasonality (minor) vs inventing 78% (major)
- Adding adjectives ("severe", "urgent") not in source
- Dropping sample size and limits of generalization

## Principle taught

**Hallucinated statistics:** AI can invent plausible numbers. Every consequential figure needs a traced source and date.
