# Cashfree documentation: answers to the open questions (17 Sep 2026)

Two Opus research runs read cashfree.com/docs, directly and through Context7, plus a few press sources. NPCI's site returned HTTP 403 on every fetch. Tags: [docs] confirmed in Cashfree's docs; [press] a credible secondary source; [not found] neither said it.

## What changes the design

1. **Retries** [docs]
   - **Standard charge:** Cashfree retries a failed UPI Autopay debit up to 3 times, an hour apart. RentOk cannot time those retries near salary days.
   - **Controlled flow** (we send the notice, then trigger the debit): Cashfree never retries, so every retry is ours to time and trigger.
   - "At most 3 retries per billing cycle" applies to merchant-triggered retries. "Billing cycle" is not defined for on-demand mandates.
   - https://www.cashfree.com/docs/payments/subscription/charge, https://www.cashfree.com/docs/payments/subscription/manage
2. **Controlled flow rules** [docs]
   - UPI and on-demand mandates only.
   - The notice date can be 1 to 7 days ahead; only the date part counts.
   - Wait at least 25 hours between the notice and the debit. One page says 24 hours; the FAQ says 25.
   - The debit amount must exactly match the notice.
   - Blocked-hour attempts are rejected, and the error gives the next allowed time.
   - An unpublished cap limits debit attempts per payment.
   - A new notice cannot be raised while an earlier one is still in progress (error "Prev_PDN_In_Progress").
   - https://www.cashfree.com/docs/api-reference/payments/latest/subscription/payment/controlled/overview
3. **Rent in parts (R16) is not confirmed** [not found]
   - Nothing in the docs says whether several debits can run on the same day or in the same cycle, or whether splitting one due is allowed.
   - The "one notice at a time" rule suggests parts may have to run one after another, on following days.
   - This is the largest unconfirmed assumption. Ask Cashfree in writing.
4. **Money split per due is not supported per debit** [docs]
   - Easy Split on subscriptions is a fixed percentage per vendor, set when the subscription is created (`subscription_payment_splits`).
   - The charge call has no split field.
   - So sending each due inside one debit to its own bank account (due-type bank routing) is not native. Ask Cashfree.
   - https://www.cashfree.com/docs/payments/subscription/faq

## Confirmed facts

- **On-demand limit** [docs]
  - `plan_max_amount` is the most that can be charged under the mandate. The FAQ adds: "charge any amount up to that maximum for each billing cycle". The sample mandate string is `amrule=MAX&recur=ASPRESENTED`, which reads as a cap on each debit.
  - `plan_max_cycles` caps the number of debits.
  - UPI debits above ₹15,000 need her PIN within 30 minutes.
- **Periodic (fixed-frequency) plans** [docs]
  - Cashfree debits them automatically at each interval.
  - A pending debit can be cancelled before it runs.
  - The merchant can PAUSE and ACTIVATE them; the docs mention no customer approval.
  - CHANGE_PLAN changes the amount without telling the customer, as long as it stays at or below the original maximum. Above the original maximum a new mandate is needed.
  - Only the customer can resume a pause she made in her UPI app.
  - PAUSE and CHANGE_PLAN do not work on on-demand mandates.
- **Standard charge timing** [docs]
  - Cashfree sends the notice and debits in one call.
  - A UPI debit cannot be scheduled for today. Tomorrow works if the charge is raised before 21:00. Up to 14 days ahead is allowed, and 15 days is not.
- **NPCI blocked hours** [docs, press]
  - Since 1 Aug 2025, Autopay debits run only before 10:00, between 13:00 and 17:00, or after 21:30.
  - Enforcement tightened on 1 Sep 2026 (TransactBridge, press).
  - A first debit within 5 minutes of mandate creation is exempt (TransactBridge, press).
  - A notice can be sent during blocked hours.
  - What the standard flow does with a scheduled time inside a blocked window is [not found].
- **First payment at approval** [docs]
  - `authorization_amount_refund: false` keeps the approval amount as a payment. The UPI minimum is ₹1.
  - Only one approval is allowed per mandate.
  - An upper limit, and whether the full first rent is allowed, are [not found].
- **Failed first debit cancels the mandate** [not found] in Cashfree's docs.
- **Expiry** [docs]
  - The field is `subscription_expiry_time`.
  - At expiry the status becomes EXPIRED or COMPLETED.
  - It **cannot be extended**: cancel and create a new mandate.
  - e-NACH allows up to 30 years; the sample UPI mandate shows 30 years.
- **Approval on RentOk's own screen** [docs]
  - The call is POST /pg/subscriptions/pay with payment_type AUTH and a UPI channel of link, qrcode or collect.
  - The response carries per-app links (GPay, PhonePe, Paytm, BHIM, Amazon Pay) or QR data.
  - UPI Autopay is switched on by the account manager; RentOk already has it.
  - e-NACH through hosted checkout can be approved by net banking, debit card or Aadhaar. Bank approval takes 24 to 48 hours, and the first debit is at least 4 days later.
- **Merchant name** [not found]
  - The plan name is shown during approval.
  - The display name comes from Cashfree's merchant setup. Ask the account manager.
- **Pricing** [docs]
  - The public list shows ₹7.5 per mandate, plus ₹15 per presentation for debits of ₹1,000 and above, plus a platform fee.
  - Whether failed attempts are billed is [not found].
- **Webhooks** [docs]
  - Status names: ACTIVE, ON_HOLD, COMPLETED, CUSTOMER_CANCELLED, CUSTOMER_PAUSED, EXPIRED, LINK_EXPIRED, BANK_APPROVAL_PENDING, CANCELLED, CARD_EXPIRED, all upper case.
  - A merchant pause has no webhook, so RentOk must track it itself.
  - A cancellation in the UPI app reaches RentOk in 30 to 45 minutes.
  - Missed webhooks cannot be replayed.
- **NPCI category rules for "as presented" and for rent (MCC 6513)** [not found]. The ₹1 lakh no-PIN limit covers only mutual funds, insurance and credit card bills.

## Design choices that follow (taken into the map, version 3)

- **Option 2 uses the controlled flow.**
  - RentOk sends the notice, the amount is fixed from that point, the debit follows at least 25 hours later, and RentOk times retries near salary days within blocked-hour rules.
  - Standard charges with Cashfree's hourly retries are the fallback.
- **Parts run one after another** (notice, debit, next notice). They are taken on her day and the days after, until Cashfree confirms same-day parts.
- **Option 1**
  - **Lasting drops** (rent cut, fee turned off): change the plan down; no approval is needed.
  - **One-off drops** (advance or credits): cancel that cycle's debit and send a link for the balance.
  - **Rises above the fixed amount:** a new approval.
  - **Pauses:** a merchant PAUSE after the property approves, and ACTIVATE at the resume date.
- **Renewals:** the mandate ends at the agreement end and cannot be extended, so a new approval is requested 15 days before it ends.
- **Due-type bank routing inside one debit** is waiting on Cashfree. If it is not possible, dues routed to a different bank account are requested separately.
