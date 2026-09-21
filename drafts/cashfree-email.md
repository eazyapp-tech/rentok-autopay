# Draft email to Cashfree (for Kamal to send)

Status: draft, 18 Sep 2026, sharpened the same day with other providers' docs (`research/psp-docs-crosscheck.md`). Kamal owns the Cashfree relationship, so he edits and sends it. Answers go into `research/cashfree-docs-answers.md` with the date and who replied.

---

**Subject:** RentOk: 12 questions on Subscriptions (UPI Autopay and e-NACH) before our 1 Oct rollout

Hi [name],

RentOk is turning on Subscriptions for all its properties from 1 October. We expect 70,000 or more active mandates within weeks. Before we finish the build, we need written answers to the questions below. The first three decide our design, so an answer to those by **Tuesday 22 Sep** would help most.

We use PG Subscriptions (`/pg/subscriptions`), mostly ON_DEMAND plans with the controlled flow (notify, then execute), and some PERIODIC plans.

**Most urgent**
1. **More than one successful debit per period on one "as presented" (on-demand) UPI mandate.**
   - Tenant rent is often above ₹15,000, so we plan to take it in parts of up to ₹15,000 each on one mandate. We also plan to raise extra debits in the same month for other bills (electricity, repairs), with the tenant's approval.
   - Razorpay's docs say "NPCI allows only one successful debit on a token per billing cycle". What is a billing cycle for an "as presented" mandate on Cashfree?
   - Can two or more successful debits run in one month on the same mandate, on consecutive days (one open notice at a time)? Our engineers found earlier that only one per 24 hours went through.
   - Does NPCI's limit of 4 attempts per mandate (August 2025) count per debit or per period?
2. **Cancelling one scheduled debit.**
   - Your Manage Payment API says it can "stop a pending charge before it is debited". Does that work after the pre-debit notice has gone out in the controlled flow (notify, then execute), and does the mandate stay active?
   - Does a notice that was never executed block the next notice?
   - Same question for PERIODIC plans.
3. **Please enable UPI Autopay on our sandbox account.** Your docs say the account manager can switch it on. We need to create, notify, execute, fail and cancel mandates there this week.

**Setup**

4. **The first payment at setup.**
   - Can the authorisation amount be the tenant's real first payment, kept rather than refunded (`authorization_amount_refund: false`)?
   - RBI allows the first debit with registration. Is there an upper limit on this amount, and does it count as a mandate transaction (no new 0.4% UPI charge from 15 Oct)?
5. **The name and logo the tenant sees, and whitelisting brands under one merchant id.**
   - What name does the tenant see in her UPI app at approval, and in her bank's pre-debit notice, and where is each one set?
   - We understand additional brand names and logos can be whitelisted under a single merchant id, after verification. Is that right, and does it apply to UPI Autopay approval and the bank notice, or only to the hosted checkout page?
   - What do you need from us per brand, how long does approval take, and is there a limit on how many?
   - Can the name be chosen per mandate at creation, or is it fixed per whitelisted brand?
   - This is urgent for us. About 20% of our tenants belong to properties trading under their own brand. They have never seen our name, and 790 of our last 1,037 failed setups are tenants who opened their UPI app and did not approve.
6. **Opening the tenant's UPI app directly.**
   - We want our own approval screen with deep links to UPI apps (the `/pg/subscriptions/pay` flow with `channel` link, qrcode or collect).
   - Anything we should know for iOS and for desktop?

**Debits and money**

7. **A failed first debit.** Is the mandate cancelled, as some sources say NPCI requires?
8. **Failed attempts.**
   - Are they billed like successful debits?
   - Your FAQ says a failed NACH debit costs the customer the bank's cheque bounce charge. Do banks charge anything for a failed UPI Autopay debit? One of our tenants was charged ₹200 several times.
9. **Money routed per due.**
   - Split on a subscription is a fixed percentage per vendor, set at creation.
   - Can different dues inside one debit settle to different bank accounts?
   - If not, what do you recommend?
10. **Blocked hours.** NPCI's peak hours are 10:00 to 13:00 and 17:00 to 21:30. In the standard flow, is a debit scheduled inside them moved to the next allowed window, or rejected?
11. **Changing a PERIODIC mandate.** Can the debit day or the amount change without a new approval from the customer, up to the original maximum?
12. **Cancelling mandates made on the new API.**
    - Our code cancels through `/api/v2/subscriptions/{id}/cancel`, but the mandates were created on `/pg/subscriptions`.
    - Is that supported, or must we use the PG endpoint?

**Regulation and settlement**

- Is the "as presented" mandate type limited by merchant category? Does anything specific apply to rent?
- How does each of our flows settle today: payment links, subscriptions, instant settlement and virtual accounts? What do we need so money settles to owners as KYC-verified vendors?

Thanks,
Kamal
