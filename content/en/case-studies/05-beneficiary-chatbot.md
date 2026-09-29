# Case study 5: Chatbot answer to beneficiaries

<div class="synthetic-label"><strong>SYNTHETIC</strong> Fictional chatbot transcript for training only.</div>

## Scenario

Your organization pilots a beneficiary-facing chatbot for FAQ about registration hours and document requirements.

**Approved FAQ source F1:** "Registration at Site South is Tuesdays 09:00 to 14:00. Bring national ID or referral letter from Partner Gamma."

**Beneficiary question:** "Can I register on Monday at Site North?"

**Chatbot reply:** "Yes. Registration at Site North is open Monday to Friday 08:00 to 17:00. Bring any photo ID."

## Your task (10 minutes)

1. Compare the reply to F1.
2. Who could be harmed?
3. Should the chatbot answer stand without human review?
4. What monitoring or stop rule would you recommend?

## Model answer

| Element | F1 | Chatbot | Problem |
|---------|----|---------|---------|
| Site | South only in F1 | North | Wrong location |
| Day | Tuesday | Monday-Friday | Wrong schedule |
| Documents | ID or Gamma referral | Any photo ID | Wrong requirements |

**Harm:** Exclusion (travel to wrong site), denial of service (wrong documents), loss of trust.

**Decision:** Red for auto-send. Human review required for any answer outside exact FAQ match. Stop pilot if wrong-site answers exceed agreed threshold (e.g., any confirmed wrong location).

## Common errors

- Assuming the chatbot only uses the FAQ file without testing edge questions
- Measuring success by volume of chats rather than accuracy
- No escalation path to a human caseworker

## Principle taught

**Humanitarian chatbots:** Beneficiaries may treat answers as authoritative. Wrong logistics information causes real harm. Test and monitor continuously.
