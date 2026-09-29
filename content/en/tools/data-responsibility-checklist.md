# Data-responsibility checklist for AI tools

Use before entering any data into an AI tool. Aligns with [IASC Operational Guidance on Data Responsibility (2023)](https://centre.humdata.org/revised-iasc-operational-guidance-on-data-responsibility-in-humanitarian-action/) and [OCHA Data Responsibility Guidelines (January 2025)](https://centre.humdata.org/data-responsibility-guidelines-2025/).

![Data responsibility lifecycle: plan, assess, collect, share, analyse, store, close](/assets/images/data-responsibility-lifecycle.svg)

**Text equivalent:** Plan, assess, collect, share, analyse, store, close. Apply at each stage before using AI on operational data. See [visual aids](visual-aids.md).

## Before you type

- [ ] I know what data classification applies (public, internal, confidential, sensitive operational, personal).
- [ ] I confirmed this tool is approved for this data type in my organization.
- [ ] I am using only the minimum data needed for the task.
- [ ] I removed names, contact details, case numbers, and precise locations where not required.
- [ ] I checked whether the vendor may use my input for model training or share it with third parties.
- [ ] I know where data is processed and stored (country/region).

## Safeguarding and protection

- [ ] I am not entering child protection case notes, GBV survivor records, or other highly sensitive protection information unless explicitly approved for this tool and role.
- [ ] I know my organization's safeguarding, PSEA, and protection focal points before handling disclosures or incidents.
- [ ] If someone discloses harm in a meeting or chat, I will pause, avoid plenary detail, and refer to those focal points (not investigate myself).
- [ ] I treat re-identification risk seriously: combined fields can identify people even without full names.

Primary sources: [ICRC Handbook on Data Protection (3rd ed.)](../references.md); [Core Humanitarian Standard (2024)](../references.md) (Commitment 5). Not legal advice.

## During the task

- [ ] I am not combining datasets in ways that could re-identify people.
- [ ] I am not uploading beneficiary lists, protection case notes, or medical records unless explicitly approved.
- [ ] I saved a record of what I entered and when (without copying sensitive content into unsecured notes).

## After the output

- [ ] I verified consequential claims against an authorized source.
- [ ] I checked translations for dropped negations, wrong numbers, or changed meaning.
- [ ] I named who will approve before any operational use.
- [ ] I deleted unnecessary copies from the tool if the platform allows it.
- [ ] I reported a data incident to my organization's contact if sensitive data was entered by mistake.

## Red flags: do not proceed

| Red flag | Why it matters |
|----------|----------------|
| Beneficiary phone numbers in a public AI chat | Re-identification and privacy breach |
| Shelter locations tied to named individuals | Safety risk |
| Donor financial details | Confidentiality and fraud risk |
| Unvetted vendor with unclear data retention | Loss of control over sensitive data |
| GBV or child protection details in unapproved tools | Severe harm and policy breach |

## Need help?

Escalate to your privacy lead, protection adviser, safeguarding or PSEA focal point, or IT security team. Amber and red decisions require organizational review, not individual judgment alone.

See [Session 3 safeguarding module](../sessions/session-03-governance/safeguarding-module.md) and [facilitator guide](facilitator-guide.md) for training-room escalation.
