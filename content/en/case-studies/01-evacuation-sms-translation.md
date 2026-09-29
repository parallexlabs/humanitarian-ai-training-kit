# Case study 1: Evacuation alert SMS (EN to FR translation)

<div class="synthetic-label"><strong>SYNTHETIC</strong> Training exercise only. All names, locations, and details are invented. Not an operational alert.</div>

## Scenario

Your team must review a French draft of an evacuation SMS before any authorized person sends it. You may not publish the message yourself.

**Source W1 (fictional authorized bulletin, 10:00):** "Reception Centre A is open. Only Entrance E provides step-free access. This bulletin does not confirm any road route. Updates must come through the local authority's established alert service."

**AI-assisted French draft:** "La route B est ouverte vers le centre d'accueil A. Toutes les entrées sont accessibles sans marches. Rendez-vous là immédiatement."

**English back-translation of draft (for reviewers who do not read French):** "Road B is open to Reception Centre A. All entrances are step-free. Go there immediately."

## Your task (12 minutes)

1. Compare each statement in the draft to W1. Mark each as supported, contradicted, or not established.
2. Who could be harmed if this draft were sent?
3. What is your green/amber/red decision?
4. Who must approve a corrected version?

## Model answer

| Draft statement | W1 check | Action |
|-----------------|----------|--------|
| Road B is open | Not established | Remove; ask authorized local source |
| All entrances step-free | Contradicted (only Entrance E) | Correct accessibility wording |
| Go there immediately | Outside reviewer authority | Stop; use established alert process |

**Decision:** Red for this draft. Local communications lead reviews a corrected version grounded in W1.

**Human control:** Named communications lead; established manual alert process if AI or approval path fails.

## Common errors

- Approving because the French "sounds professional"
- Missing the dropped/contradicted accessibility detail
- Treating AI translation as authorization to send
- Ignoring that route status is not in the source

## Principle taught

**Verification of translations:** Consequential alerts require source-grounded review. A fluent translation can still be wrong or unsafe.
