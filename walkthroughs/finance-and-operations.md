# Walkthrough: RentOk accountant, operations, property accountant, data (17 Sep 2026)

Agent (opus), backend master 33b64a1e3; "verify" marks code read but not run. Product word should be "Autopay".

## Headline risks before 15 Oct
1. The Autopay fee prints on the property's receipt as "Payment processing charges" (invoices.ts 874 to 876; gst-receipt-template.ejs 428; receipt-template.ejs 700) under the property's name and GSTIN (invoices.ts 984 to 990), with no RentOk GST invoice. Reads as MDR passed to the tenant; RentOk collects a fee without charging GST.
2. Payout amounts look wrong in several places (below). Verify with tests.
3. No way to deduct MDR from a payout, invoice it, and reconcile it.

## RentOk's accountant
- Autopay debit: fee split by `computeWebhookChargeAmounts` (helpers 175 to 205), merged into receipt gateway charges. Fix: RentOk tax invoice line "Autopay service fee" with RentOk's GSTIN; daily combined invoice for unregistered tenants under ₹200 (Rule 46); reuse the plans invoice code (invoices.ts 878 to 958). Needs a tax view on service code and principal vs agent.
- Transaction row stores plan amount (autopayV2.ts 438 to 445). Fix: store charged amount.
- Debited but not recorded: marked "manual review" (autopayV2.ts 618 to 627) with no alert or queue. Fix: daily queue, alert after 4 hours, month close only when empty.
- Setup: RentOk pays about ₹8.85 per mandate (setup payer RentOk only, property.ts 9274 to 9282). Proposal: activation line on first debit (see file 10: the e-mandate rule may forbid this).
- Cashfree fees and GST: reconciliation is a one-off sampling script (cashfreeMdrReconciliation.ts 1 to 28), default account only; fees per transaction not stored. Fix: nightly settlement-file import, matched to payments and payouts.
- MDR from 15 Oct: only a flat `settlement_charges` deduction exists (settlementFlow.ts 539 to 541); no percentage deduction or owner invoice. Fix: "UPI MDR recovery" on UPI link payments only (0.4%, cap ₹300, plus 18% GST), monthly RentOk invoice to the owner, signed owner terms. Pure-agent route (Rule 33) unlikely because Cashfree's contract is with EAZYAPP; treat as RentOk's own taxable service.
- Settlement V2 base `payment.net_amount` includes tenant gateway charges (payment.ts 2289) while the wallet entry leaves them out (settlementFlow.ts 460); owner-paid fee deducted only on the older path (#6996). Fix: one payout formula with a test.
- `getRentokCharges` (settlementFlow.ts): subtracts scheduled amounts for all properties, not this one (1573), can go negative; may take charges twice in the due-type split (1485 to 1500); leftover also sent to the owner (1532). Verify; file as P1.
- Refunds, double debits, chargebacks: no Cashfree refund call; no dispute handling; money already paid out. Fix: Cashfree refund before settlement, else recovery from next payout; GST credit note for refunded fees; dispute payout hold.
- Failed attempts: Cashfree prices "per debit attempt"; at about 2.4 attempts per success, cost about ₹43 against a ₹20 fee. Confirm with Cashfree; retries 1 plus 3 on salary day; price the fee on successful debits.
- Books: rent as "held for properties" (liability); fee income monthly on success; activation per auditor; MDR recovery as income with GST; Cashfree fees as expense with input credit.
- Example journal for ₹10,000 at ₹20 plus GST fee: receivable ₹10,023.60 / held ₹10,000, fee ₹20, output GST ₹3.60; bank ₹10,005.90, fee expense ₹15, input GST ₹2.70 / receivable; held ₹10,000 / bank.

## Operations and support
- Stuck "initialized" (46% of starters): expire after 48 hours; resume link to the approval; ops list by property.
- Failed debit (about 41,000 in October at today's rate): tell tenant same day with virtual account and link; no fine inside the window; save the reason.
- Double debit: amount fixed when requested (autopayV2.ts 310 to 339); link payment after the notice not subtracted; V1 route reachable. Fix: #6830; block links inside the notice window or cancel the debit; V1 off; runbook: excess to advance, refund within 5 working days on request.
- Wrong amount: re-approval on rent change; fix copy and receipt label.
- Move-out: cancel; hold the debit during final settlement; keep grace on cancel.
- Notice: confirm Cashfree sends the bank notice; RentOk WhatsApp notice for all.
- Cashfree outage: global pause; retry at next allowed time; late fines off.
- Offsite 24 to 27 Sep: named on-call for engineering and ops; daily 10 am dashboard review; rollback owner; freeze other changes.
- Ticket tags: setup, failed, double, amount, cancel, move-out, receipt, fee.

## Property's accountant
- Payout report (report.ts 310 to 318) lacks payment method, deductions, bank reference, RentOk invoice number. Add them, plus a monthly statement matched to bank credits.
- Monthly RentOk tax invoice for deductions.
- GST on rent: code applies 0% up to ₹20,000 a month and 5% above (FIN-013). Law: PG stays up to ₹20,000 per person per month for 90 days or more exempt (Notification 04/2024); tariffs up to ₹7,500 a day at 5% without input credit (Notification 15/2025). A 5% PG cannot reclaim GST on MDR, so its MDR cost is ₹47.20. The 90-day condition in code not checked.
- Residential flat to a GST-registered tenant: reverse charge since 18 Jul 2022 (Notification 05/2022); receipt needs the marker.
- TDS on rent (section 393 of the Income-tax Act 2025 from 1 Apr 2026; above ₹50,000 a month; 10% businesses, 2% individuals once a year): add a "TDS deducted" field that lowers the debit, and certificate tracking.
- TDS on RentOk's own fees: owner cannot deduct because RentOk takes fees first; reuse the plans invoice TDS field (invoices.ts 905).
- Seven accounts hardcoded to a ₹20,000 online cap (FIN-043): cannot put higher rent on Autopay; decide policy.

## Data to measure daily
Setup funnel by source and property; debit success and reasons by bank and day; cancellations and pauses with reason; fee income vs Cashfree cost including failed attempts; MDR saved and paid (0.4% above ₹2,000, cap ₹300, times 1.18) per property; manual-review count, double debits, refunds, payout mismatches; ticket tags; rent split around ₹15,000 (not yet measured).

## Cost per ₹10,000 rent from 15 Oct (agent's model; fee ₹20 plus GST assumed)

| Method | Tenant pays | Cost incl. GST | RentOk keeps | Owner gets | MDR pass-through risk |
| --- | --- | --- | --- | --- | --- |
| Autopay, code today | ₹10,050 | ₹17.70 per attempt + ₹8.85 setup (RentOk) | ₹50, GST unclear | ₹10,000 | Yes (receipt label) |
| Autopay, proposed fee | ₹10,023.60 (+₹11.80 activation month 1) | Same | ₹5 at one attempt; loss of ₹16 at 2.4 attempts | ₹10,000 | Low if flat, named, invoiced (but see e-mandate rule, file 10) |
| Autopay price (post ₹10,040, ₹40 off) | ₹10,023.60; link payer ₹10,040 | Same | ₹5 | ₹10,000 | Medium (file 10 says high) |
| e-NACH (example ₹10 fee) | ₹10,011.80 | ₹8.85 per debit + ₹8.85 setup | ₹2.50 | ₹10,000 | Low |
| Virtual account transfer | ₹10,000 | Cashfree ₹20 per credit | Recovery plus GST | ₹10,000 minus fee | Low (UPI to its UPI ID carries MDR) |
| UPI link | ₹10,000 | ₹47.20 MDR incl. GST | ₹40 recovery | ₹9,952.80 | Yes if any reaches the tenant |
| UPI link at ₹10,040 | ₹10,040 | ₹47.39 | ₹40.16 | ₹9,992.61 (a raise of about ₹48 covers it) | Yes if only link payers pay it |
| Cash with OTP | ₹10,000 | None | ₹0 | ₹10,000 | No |
| Flat platform fee (B) | +₹35.40 | none | ₹30 | none | Low if identical for every method |

## Places a charge could read as MDR passed on
Receipt label on the Autopay fee; any gateway charge on UPI link payments (server does not force 0); any percentage fee; a rent raise only for link payers or worded as "UPI charges"; a platform fee waived for cash or Autopay; a fee on the virtual account's UPI route; owner-created due types like "Online charges" (block such names, as FIN-002 does for protected names); the platform fee built as a property due type (wrong supplier for GST, constants.ts 83 to 91); check-in copy striking the fee or calling it one-time.

## Ranked problems (money and compliance)
1. Fee printed as payment charges on the property's receipt, no RentOk invoice.
2. Unsigned webhooks can fake a payment (#6816).
3. `getRentokCharges` payout errors (verify, P1).
4. Settlement V2 payout base (#6996 and gateway charges).
5. No MDR deduction and invoicing from 15 Oct.
6. Fee pricing (₹50 exceeds link cost to tenant; ₹40 raise leaves owner ₹7.39 short).
7. Is RentOk an e-commerce operator (GST section 9(5), TCS section 52, TDS 194-O equivalent) and a payment aggregator? Counsel opinion before scaling.
8. No daily reconciliation; debited money left unrecorded.
9. Failed attempts possibly billed; 5 retries; 59% failures.
10. Setup fee paid by RentOk.
11. No refund, double-debit or dispute path.
12. Platform fee built as a property due type.
13. TDS and reverse-charge cases.
14. Move-out, grace wipe, silent cap.
15. Ops readiness (notice locked, no kill switch, offsite soak).

Sources opened by the agent: taxguru (PG 90-day exemption; hotel rates 22 Sep 2025), Taxmann (residential renting), TDSMAN and Ollvy (section 393), ClearTax (194O; section 9(5)), taxguru (GST TCS rate), GSTZen (Rule 33; Rule 46), Finance Ministry FAQ (sources/).
