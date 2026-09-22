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
| 6 | What a tenant of a whitelabelled property (19.5% of tenants, #6883) sees on the setup screen and in messages: her property's brand or RentOk's | A monthly debit asked for by a name she does not know is more likely to be abandoned or disputed |
| 7 | "Pay now" links after a failed or paused month work at least until her grace days end, and the push list holds current tenants only | Links die after 7 days; messages to departed tenants lower the WhatsApp rating |
| 8 | Fixes are tested with real money on a few staff tenants, on small amounts | There is no sandbox for Autopay (#6866) |
| 9 | A RentOk-only switch that stops all debits, or one property's, and a floor on first-try success that pauses setup messages | There is no way to stop debits today if something goes wrong at scale |

| 10 | "Started" means she opened setup or began an approval without approving it | Decides who the Autopay list chases again, and who it leaves alone |
| 11 | The Autopay rate is tenants counted over current tenants, once each, CirclePe out, "not required" in | The list's own count and the daily target number must agree or managers stop trusting both |
| 12 | An active mandate with nothing queued shows "Failed: no debit booked" and is not counted | 473 of 781 current Autopay tenants had no debit queued on 18 Sep. Today they read as On |
| 13 | When two statuses apply, show Failed, then Needs new approval, Pause requested, Waiting on RentOk, Ending soon, then the rest | Every row in the Autopay list depends on it, and states overlap constantly |
| 14 | App-only managers get a daily WhatsApp link to the Autopay list during the push | The manager screens ship on web first, so without it they cannot act at all until the app release |
| 15 | A manager's send and RentOk's send share the one-a-day setup limit | Otherwise a tenant can get two setup messages on the same day from two directions |
| 16 | The property opt-out stops only RentOk's own sends, not the manager's | A manager who opted the property out still needs to be able to message her own tenants |
| 17 | Alerts with a clock fire at once (pause request, all retries failed, cancellation); the rest arrive in one 09:00 summary | Decides whether a manager is interrupted nine times a day or once |
| 18 | On day one, account owners and admins get all ten Autopay permissions; other members get "view the Autopay list" and "send setup" only if they already have "View Dues, Collection & Send Reminders" | Ten new switches default to off would leave every team unable to act on 1 Oct |

| 19 | The payment page says nothing about the new 0.4% UPI charge | Kamal's launch room PRD makes the charge the first thing she reads, and orders the payment methods by what each costs her. R11, N2, N6 and R63's fourth condition all forbid it. One of the two has to give, and it sets the tone of the whole surface |
| 20 | The sub-₹2,000 split session does not ship | N1 rules out splitting to avoid the charge. The PRD says legal cleared it, that N1 covers only an Autopay mandate's rent, and that we will not advertise it as charge avoidance; the prototype then labels it "no charge on the parts" and sorts it by cost. Also carries no refund path if she stops halfway |
| 21 | The virtual account stays parked until after 15 Oct | The map parks it pending Cashfree's written answer on settlement, and the legal check warns that rent landing in RentOk's own account is aggregation without a licence. The PRD says the Cashfree API is live and engineering can start now |
| 22 | Rent Points and the Hubble voucher store are not part of the 1 Oct scope | Points on every rupee of rent, a grant for setting up Autopay and a voucher catalogue are in the PRD and the prototype, and in no ruling. RentPass cashback is parked until a partner funds it, because RentOk absorbs nothing (R11) |

Items 10 to 18 were added on 22 Sep 2026 from the manager build tickets D1, D2 and D3, where they were recorded as proposals and would not have been seen here. Items 19 to 22 were added the same day from Kamal's launch room PRD and his payment page prototype, where each one is designed and built but disagrees with a ruling.

## 2. Waiting on Cashfree

Ask these in one written message. The first is the largest: the plan for dues above ₹15,000 rests on it.

1. **Dues taken in parts.** Can one mandate be debited several times on the same day, in parts of up to ₹15,000? If not, can the parts run on the following days? How do the notice and the retries work for each part? (18 Sep: Kamal heard from PhonePe that several debits in 24 hours are allowed. Vivek and Jatin found earlier that Cashfree allowed only one per 24 hours. Ask Cashfree which is true today. Other providers' docs (18 Sep, `research/psp-docs-crosscheck.md`): Razorpay says NPCI allows one successful debit per billing cycle; PhonePe's 20-a-day page is from 2024 and withdrawn. If one per period holds for on-demand mandates, both parts above ₹15,000 and "Request payment via Autopay" need a fallback.)
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
