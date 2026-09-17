# Autopay push: the sorted picture (17 Sep 2026)

> Superseded by map/feature-map.md. This was the first sort into must-have, supporting, parked and cut, before rulings R22 to R51.

Built from rulings R1 to R18 in 05-inventory.md. This is the feature-map sort: **spine** means the 1 Oct target fails without it; **supporting** makes the spine work better; **parked** has a condition that brings it back; **cut** has a reason.

The target is 70,000 to 75,000 tenants with an approved, active Autopay or e-NACH mandate by 1 Oct. That needs about 5,300 new mandates a day.

## Spine

1. **Safe to switch on for every property.** Everything below has to be fixed first.
   - Anyone can change or cancel Autopay without logging in (#6816, and the login check in #6861).
   - Two debit engines can charge one tenant twice (#6995).
   - A tenant who paid another way is still debited (#7002).
   - One empty month ends Autopay for good (#6999).
   - Moving out does not cancel Autopay.
   - Cancelling Autopay wipes her late fine setting.
   - Debit times go to Cashfree in 12-hour format (#7004).
   - Autopay required by default for every property (R20), using the existing `autopay_mandatory` setting, with the hard-coded list removed; the property can turn it off.
2. **One tenant flow, everywhere.**
   - **Where she meets it:**
     - check-in;
     - the new payment page (set-up switched on);
     - the tenant app;
     - WhatsApp links that open straight at the approval step.
   - **What the flow must get right:**
     - honest wording ("no extra charge for Autopay", her day, cancel any time);
     - a consent box she ticks herself;
     - a success screen showing the next three debit dates and cancel;
     - "pay now and turn on Autopay" in one approval on every payment screen, if Cashfree confirms (15);
     - rent above ₹15,000 shown as parts, with e-NACH only in the FAQ;
     - required means chase, never block (R21): a required step at check-in with a manager exception or e-NACH, a persistent card and capped nudges for everyone else, and link or cash always available at the same price.
3. **Who covers payment costs.**
   - **The setting:** management, or the tenant through the ₹49 plus GST platform fee (the default), or the tenant through rent.
   - **Billing:** RentOk bills under its own GSTIN, and payout deductions work correctly (#6996, #6998).
   - **Removed:** the tenant Autopay fee line, and the "Payment processing charges" label.
   - **Setup cost** moves off RentOk.
4. **The monthly debit.**
   - It collects all monthly dues, in parts of up to ₹15,000.
   - It follows NPCI's timing rules: one attempt plus three retries, outside peak hours.
   - A heads-up two days before each debit ("keep ₹X in your account"). RentOk's own notice is locked to a test record today; Cashfree already sends the legally required notice (15, fact 1).
   - It saves real failure reasons and tells her the same day (#6817).
   - Her Autopay day becomes her due date for late fines (#6829).
   - Every mandate allows up to ₹15,000 per debit (R19), so rent changes and bills never need a new approval.
   - GST is included in her approved amount (#7000).
5. **Manager and owner push.**
   - Status list: not started, started, active, failed, cancelled, exception.
   - Grant an exception or send e-NACH for a tenant who cannot use UPI Autopay.
   - Send to one tenant or in bulk from the manager app and manager web.
   - No payment links to tenants on active Autopay (#6830).
   - The owner sees "paid by Autopay" (#6835).
6. **Measurement.**
   - A daily count against the target.
   - The health metric: rent paid by Autopay on the first try.
   - Funnel and guardrails, as in 04-success-metrics.md.

## Supporting

- Bulk rent change with a scheduled start date, a signing round for all parties, and an Autopay step on the signing page (13).
- From 15 Oct, UPI link charges deducted from the owner's payout, with a monthly RentOk invoice and statement.
- A merchant name the tenant recognises instead of EAZYAPP.
- Money settled through Cashfree Easy Split, with owners as verified vendors.
- A daily reconciliation queue and a refund path for double debits.
- Ops runbook, and named on-call people during the 24 to 27 Sep offsite.

## Parked (and what brings each back)

- **Per-tenant bank account number (virtual account):** after 15 Oct, once Easy Split settlement is confirmed.
- **UPI inside the tenant app (UPI plugin):** early 2027, for repeat payers.
- **BBPS:** later, for large registered operators.

## Cut

- **Becoming a UPI app (TPAP):** removes no charge, allows no fee, takes 8 to 12 weeks.
- **"Autopay price":** reads as passing UPI charges to link payers.
- **RentOk absorbing any cost.**
- **Any charge hidden from the tenant.**
- **Phasing the target to a first group of properties.**
- **Splitting rent into pieces of ₹2,000 or less.**

## Not product decisions, still open

- A written question list to Cashfree:
  - how each flow settles;
  - rent in parts;
  - PIN debits;
  - whether failed attempts are billed;
  - the merchant name.
- A lawyer's opinion on the platform fee and the start-date rule.
- A tax opinion on whether RentOk is an "e-commerce operator".
- Kamal's recording audio.
- Mirroring this into Linear, only after Sanchay says go.
