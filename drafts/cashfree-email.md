# Draft email to Cashfree (for Kamal to send)

Status: draft, 18 Sep 2026. Kamal owns the Cashfree relationship, so he edits and sends it. Answers go into `research/cashfree-docs-answers.md` with the date and who replied.

---

**Subject:** RentOk: 12 questions on Subscriptions (UPI Autopay and e-NACH) before our 1 Oct rollout

Hi [name],

RentOk is turning on Subscriptions for all its properties from 1 October. We expect 70,000 or more active mandates within weeks. Before we finish the build, we need written answers to the questions below. The first three decide our design, so an answer to those by **Tuesday 22 Sep** would help most.

We use PG Subscriptions (`/pg/subscriptions`), mostly ON_DEMAND plans with the controlled flow (notify, then execute), and some PERIODIC plans.

**Most urgent**
1. **More than one debit a day on one mandate.**
   - Tenant rent is often above ₹15,000, so we plan to take it in parts of up to ₹15,000 each on one UPI mandate.
   - Can one mandate be debited more than once in 24 hours? Our engineers found earlier that only one debit per 24 hours went through.
   - If more than one is not allowed, can the parts run on consecutive days?
   - For each part: is a separate pre-debit notice needed, and how do retries work?
2. **Cancelling one scheduled debit.**
   - When a tenant pays by another method after we have sent the notice, can we cancel that one debit and keep the mandate?
   - Which API does this, for ON_DEMAND and for PERIODIC plans?
3. **A sandbox for Subscriptions.**
   - Can we create, notify, execute and cancel mandates in sandbox, with sandbox keys?
   - If not, what do you recommend for testing before going live?

**Setup**

4. **The first payment at setup.**
   - Can the authorisation amount be the tenant's real first payment, kept rather than refunded (`authorization_amount_refund: false`)?
   - Is there an upper limit, and does it count as a mandate transaction for the new UPI charge from 15 Oct?
5. **The merchant name.**
   - What name does the tenant see in her UPI app and in her bank's pre-debit notice?
   - Can it carry the property's name? About 20% of our properties use their own brand.
6. **Opening the tenant's UPI app directly.**
   - We want our own approval screen with deep links to UPI apps (the `/pg/subscriptions/pay` flow with `channel` link, qrcode or collect).
   - Anything we should know for iOS and for desktop?

**Debits and money**

7. **A failed first debit.** Is the mandate cancelled, as some sources say NPCI requires?
8. **Failed attempts.**
   - Are they billed like successful debits?
   - Do banks charge the customer for a failed UPI Autopay or e-NACH debit, and do you have data by bank? One of our tenants was charged ₹200 several times.
9. **Money routed per due.**
   - Split on a subscription is a fixed percentage per vendor, set at creation.
   - Can different dues inside one debit settle to different bank accounts?
   - If not, what do you recommend?
10. **Blocked hours.** What happens to a debit scheduled inside NPCI's blocked hours in the standard flow?
11. **Changing a PERIODIC mandate.** Can the debit day or the amount change without a new approval from the customer, up to the original maximum?
12. **Cancelling mandates made on the new API.**
    - Our code cancels through `/api/v2/subscriptions/{id}/cancel`, but the mandates were created on `/pg/subscriptions`.
    - Is that supported, or must we use the PG endpoint?

**Regulation and settlement**

- Is the "as presented" mandate type limited by merchant category? Does anything specific apply to rent?
- How does each of our flows settle today: payment links, subscriptions, instant settlement and virtual accounts? What do we need so money settles to owners as KYC-verified vendors?

Thanks,
Kamal
