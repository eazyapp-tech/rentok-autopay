# What is still open (17 Sep 2026)

Three lists: what needs Sanchay's yes, what only Cashfree can answer, and what needs outside advice. Everything else is settled in `decision-log.md`.

## 1. Waiting on Sanchay

These follow from his rulings, and are marked "(proposed)" in the feature map.

| # | Proposal | Why it matters |
| --- | --- | --- |
| 1 | A tenant whose pause request is still waiting for approval keeps counting toward the target | Decides how requests made on 30 Sep are counted |
| 2 | No late fine while retries are still running | Her Autopay day can fall on the last grace day, so retries can run past it |
| 3 | Where a tenancy has no end date, the mandate runs until she moves out | Mandates end at the agreement end date, and some tenancies have none |
| 4 | While a pause request is pending, her next debit is held | Otherwise a request made a day before her debit is pointless |
| 5 | A tenant can pause or cancel a mandate her parent set up, and the parent is told | Parents can be the payer |
| 6 | A floor and a ceiling for the platform fee line when a property changes it (said on the 18 Sep call with Nimit, amounts not set) | Without them a property can set any amount on every tenant's bill |
| 7 | What a tenant of a whitelabelled property (19.5% of tenants, #6883) sees on the setup screen and in messages: her property's brand or RentOk's | A monthly debit asked for by a name she does not know is more likely to be abandoned or disputed |
| 8 | A RentOk-only switch that stops all debits, or one property's, and a floor on first-try success that pauses setup messages | There is no way to stop debits today if something goes wrong at scale |

## 2. Waiting on Cashfree

Ask these in one written message. The first is the largest: the plan for dues above ₹15,000 rests on it.

1. **Dues taken in parts.** Can one mandate be debited several times on the same day, in parts of up to ₹15,000? If not, can the parts run on the following days? How do the notice and the retries work for each part? (18 Sep: Kamal heard from PhonePe that several debits in 24 hours are allowed. Vivek and Jatin found earlier that Cashfree allowed only one per 24 hours. Ask Cashfree which is true today.)
2. **The first payment at setup.** Can the approval amount be the tenant's real first payment, kept rather than refunded? Is there an upper limit? Does it avoid the new 0.4% UPI charge?
3. **A failed first debit.** Does the mandate get cancelled, as some sources say NPCI requires?
4. **Money routed per due.** Can different dues inside one debit go to different bank accounts? Cashfree's split is a fixed percentage per mandate, set at creation.
5. **Failed attempts.** Are they billed like successful ones?
6. **The merchant name** the tenant sees in her UPI app and in bank notices: how is it set, and can it carry the property's name?
7. **Blocked hours.** What does the standard flow do with a debit scheduled inside NPCI's blocked hours?
8. **Fixed-schedule mandates.** Can the debit day or the amount change without a new approval from the tenant?
9. **NPCI rules.** Is the "as presented" mandate type limited by merchant category, and does anything specific apply to rent?
10. **How each flow settles today:** links, Autopay, instant settlement and virtual accounts, and what is needed to settle to owners as verified vendors.

## 3. Waiting on advisers

- **A payments lawyer:** the wording of the Autopay terms in the agreement and of the platform fee line; whether a rent or fee change may start on its date for tenants who have not signed.
- **A tax adviser:** RentOk's position, including whether it counts as an "e-commerce operator", and how a GST-registered property's platform fee line is taxed.

## 4. Inside RentOk

- **Kamal:** anything from his recording that the transcript missed.
- **Engineering:** whether the old debit engine's scheduled job is off.
- **Kamal and Srijan:** the IDFC workflow they drew, which Sanchay wants to go through again.
- **Research:** which banks charge a tenant for a failed UPI Autopay or e-NACH debit, and how much. A past tenant was charged ₹200 several times.
- **Whoever holds the Meta account:** the tenant WhatsApp number's daily send limit and quality rating. That number decides how fast the push can go.
