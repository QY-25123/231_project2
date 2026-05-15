# Knowledge Base Health Check Report

# Knowledge Base Health Check Report
## U.S. Apartment Rental Wiki for International Students

---

## 1. Cross-Link Completeness

### Missing Links — By Article

**`concepts/lease-terms.md`**
- Should link to `guides/maintenance-requests` — the article discusses the landlord's obligation to maintain habitable conditions but never points readers to the maintenance guide
- Should link to `guides/parking-rules` — parking is a common lease clause not mentioned in the "key clauses" section
- Should link to `guides/utilities-setup` — utilities responsibility is a key lease question but no link is present
- Should link to `templates/move-out-notice` — the article discusses notice requirements to move out but only links to `guides/move-out`, not the ready-to-use template

**`concepts/security-deposit.md`**
- Should link to `templates/maintenance-email` — the article advises sending demand letters but provides no link to the closest available template

**`concepts/renters-insurance.md`**
- Should link to `guides/move-in` (currently listed under Related, ✅) — **already present**
- Should link to `guides/move-out` — a student canceling their policy at move-out is a natural follow-on concern; not currently linked

**`guides/move-in.md`**
- Should link to `guides/utilities-setup` — students setting up their apartment on Day 1 will immediately need utility setup guidance; not currently linked
- Should link to `guides/parking-rules` — parking permits are often needed on or before move-in day (the parking article itself says so), but `move-in` never references it
- Should link to `concepts/renters-insurance` — many leases require proof of insurance before or on move-in day; this is mentioned in `lease-terms` but the move-in checklist doesn't link to it
- Should link to `templates/maintenance-email` — the article tells students to file maintenance requests for issues found at move-in but only links to `guides/maintenance-requests`, not the template

**`guides/move-out.md`**
- Should link to `templates/maintenance-email` — Template 4 (disputing a charge) is directly relevant to deposit disputes after move-out; not currently linked
- Should link to `concepts/renters-insurance` — students need to remember to cancel or transfer their policy when moving out; not currently linked

**`guides/maintenance-requests.md`**
- Should link to `concepts/lease-terms` — tenant rights to repairs stem from lease obligations; already listed ✅
- Should link to `concepts/security-deposit` — already listed ✅
- Should link to `templates/move-out-notice` — the article mentions lease termination as a remedy for unresolved repairs; the template is relevant but not linked

**`guides/parking-rules.md`**
- Should link to `guides/utilities-setup` — both are "move-in logistics" guides; cross-linking would help navigation
- Should link to `guides/move-out` — students need to know to return parking permits/fobs at move-out; not linked

**`guides/utilities-setup.md`**
- Should link to `guides/move-out` — canceling utilities at move-out is the natural endpoint of this guide; not linked
- Should link to `guides/parking-rules` — both are practical setup guides; not linked

**`templates/maintenance-email.md`**
- Should link to `concepts/security-deposit` — already listed ✅
- Should link to `templates/move-out-notice` — already listed ✅

**`templates/move-out-notice.md`**
- Uses informal relative links (`[[move-out]]`, `[[security-deposit]]`) inconsistent with the full-path format used everywhere else (`[[guides/move-out]]`, `[[concepts/security-deposit]]`) — these should be normalized

---

## 2. Content Gaps

### Topics Mentioned But Not Fully Covered

- **Credit history and credit checks** — `lease-terms` mentions that landlords may require a co-signer due to lack of U.S. credit history, but there is no guidance on what a credit check involves, how to build U.S. credit as an international student, or alternatives (prepaid rent, larger deposit). This is a critical gap for new arrivals.

- **Demand letter for security deposits** — `security-deposit` tells students to "send a written demand letter" but there is no template for this, unlike the maintenance and move-out scenarios. Template 4 in `maintenance-email` covers disputing a charge but is not clearly framed as a deposit demand letter.

- **Early lease termination in specific circumstances** — `move-out` mentions military deployment, domestic violence, and health issues as grounds for penalty-free early termination but gives no further detail. International students have a unique additional scenario: visa denial, OPT expiration, or deportation. This is unaddressed.

- **Renewing or not renewing a lease** — `lease-terms` mentions auto-renewal risk but there is no dedicated guide on how to formally decline renewal, negotiate rent at renewal time, or request a lease extension.

- **Roommate agreements** — Roommates are mentioned in `renters-insurance` (each needs their own policy) and implied in `utilities-setup` (Splitwise), but there is no guidance on roommate agreements, joint lease liability, what happens if a roommate stops paying, or how to add/remove a roommate from a lease.

- **What to do when moving to a new apartment vs. leaving the U.S.** — The move-out template notes that students returning home should consider a U.S. forwarding address for the deposit, but there is no fuller treatment of the logistical differences (closing U.S. bank accounts, utility account closure, forwarding mail internationally).

### Important Questions a Student Might Have That Go Unanswered

- *"Can my landlord raise my rent mid-lease?"* — Rent increases are mentioned only in the context of month-to-month tenancy; fixed-term protections are not explicitly stated.
- *"What do I do if I have a bad landlord or a dispute I can't resolve?"* — There is no guide to tenant rights organizations, legal aid clinics, or housing courts beyond brief mentions scattered across articles.
- *"What is a guarantor service, and can I use one instead of a person?"* — `lease-terms` mentions co-signers but not commercial guarantor services (e.g., Insurent, The Guarantors), which are increasingly common options for international students.
- *"How do I pay rent? What if I don't have a U.S. bank account yet?"* — Payment methods are mentioned (check, portal, bank transfer) in `lease-terms` but there is no guidance on opening a U.S. bank account or paying rent before one is available.
- *"What if my building has a fire or I am displaced?"* — ALE coverage in `renters-insurance` is mentioned, but there is no procedural guide for emergencies beyond calling 911.
- *"How do I read a U.S. apartment listing?"* — No pre-lease apartment-hunting guidance exists. Students arrive at the wiki after signing, but many will find it before.

---

## 3. Inconsistencies

### Factual and Advisory Conflicts

- **Security deposit return timeline stated inconsistently.** `security-deposit` states the return window is "14–30 days after move-out." `move-out` repeats the same range. `templates/move-out-notice` (Important Notes section) also says "14–30 days." These are consistent with each other but should note that the actual range across all U.S. states is broader — some states allow up to 45 or 60 days. The current framing may create false expectations for students in states like Kentucky (60 days) or Massachusetts (30 days after receiving the forwarding address).

- **Certified mail notice requirement stated differently in two articles.** `guides/maintenance-requests` states: *"if you send certified mail, you only need to send one written notice. Otherwise, send two written notices."* `guides/landlord-communication` repeats the same advice. However, this is framed as a Texas-specific rule in both places ("Under Texas law (and similar laws in many states)"). The qualification is important but inconsistently emphasized — one instance calls it out more prominently than the other. Students in other states may incorrectly apply Texas-specific rules.

- **Renters insurance cost range has a minor internal inconsistency.** The introduction of `renters-insurance` states *"$10–$20 per month,"* and
