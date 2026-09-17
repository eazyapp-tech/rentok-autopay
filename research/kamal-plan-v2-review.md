# Kamal's plan, version 2, and his context file: what to take (17 Sep 2026)

Sources:
- `~/Downloads/RentOk UPI AutoPay — Product Flow Redesign & Adoption Plan (1).md`
- `~/Downloads/RentOk-UPI-Autopay-context-handoff.md`, which reproduces the plan with notes.

Each claim below was checked against rulings R1 to R18, the code on origin/master, Cashfree's docs (through Context7) and the RBI text.

## New facts found while checking (verified 17 Sep)

1. **Cashfree sends the notice before each debit** when we use its standard "raise a charge" call, which is what our code uses (`cashfree.ts:537`, `/pg/subscriptions/pay`). The notice is the bank's job (RBI para 6), triggered through Cashfree.
   - Our own WhatsApp notice is therefore not the legal notice. It is a courtesy that helps debits succeed, because most failures are an empty account.
   - This corrects both Kamal's plan and item 1 of my own sorted picture.
2. **Pause and plan change don't work on on-demand mandates** (Cashfree "Manage Subscriptions": "CHANGE_PLAN and PAUSE actions are not supported for On-Demand Subscriptions").
   - A "pause" from RentOk can only mean not raising charges for a while.
   - A higher limit needs a new approval from the tenant.
   - She can still pause from her own UPI app.
3. **At most 3 retries per billing cycle** (Cashfree "Manage Payment API"). For rent taken in parts, it is not yet known whether the retries are shared across the parts. Added to the Cashfree questions.
4. **A charge above the approved maximum needs a new mandate** (Cashfree FAQ). This matters for rent changes and for variable monthly dues (R18).
5. **Earliest first debit:** UPI Autopay T+1 (T+2 if approved after 9 pm); e-NACH T+4.
6. **"Controlled" charge option:** we can send the notice ourselves and debit at least 24 hours later with our own retry timing, for UPI Autopay only. The debited amount must match the notified amount. This fits rent in parts (one notice per part) and salary-day retries.
7. **Setup can take this month's payment at the same time** (RBI para 5(a) allows the first debit to be combined with setup). Cashfree setup has `authorization_amount` and `authorization_amount_refund`; ours is ₹1, refunded.
   - Open for Cashfree: can the setup amount be the tenant's dues, kept as a payment, and is it free of the UPI charge?
8. **Collect requests:** NPCI stopped person-to-person collect requests on 1 Oct 2025. Merchants can still send them, so the "enter your UPI ID" path on desktop is still possible. A QR code is the other option.
9. **Bug #7004 (filed):** debit times go to Cashfree in 12-hour format, so every schedule is sent as noon, which falls inside NPCI's blocked window.

## Take (fits the rulings, adds something)

- **"Pay now and turn on Autopay" in one approval**, the CRED checkbox above Pay:
  - This month's payment becomes the first Autopay debit, so the tenant approves once and pays once.
  - If Cashfree confirms point 7, this month's payment also avoids the new UPI charge.
  - It goes on the new payment page, the in-app Pay screen and the payment-link success screen.
- **Show the next three debit dates** before she approves ("₹12,000 on 5 Oct, 5 Nov, 5 Dec"), with parts shown for rent above ₹15,000 (R16).
- **Success screen** with the next dates plus cancel. Cancel is as easy as setup, in the tenant app and on the payment page.
- **Autopay step after the agreement** in check-in, with the Autopay wording inside the agreement.
- **A heads-up two days before each debit** ("keep ₹X in your account") on top of Cashfree's notice. It targets the main failure reason.
- **Same-day message on a failed debit** with pay-now and retry timing. The manager gets an alert with the reason.
- **Manager tools:**
  - status column: not set up, started, on, failed, cancelled;
  - bulk send;
  - Autopay rate per property.
- **Owner tile:** "UPI charges you paid on link payments this month" next to "tenants not on Autopay". Under R15, link charges are the owner's cost, so this gives owners a reason to push Autopay.
- **Tenant pitch never mentions MDR:** "never miss rent, nothing to remember, no extra charge for Autopay".
- **Nudge cap:** welcome, one reminder before rent is due, the debit heads-up, the result message, and one "still not on Autopay" message a month.
- **Choose by device:** open the UPI app on a phone; show a QR code or ask for her UPI ID on a computer.
- **Cheap habit boosters:** "6 months on time" streak; asking flatmates on the same property.
- **Ask the industry body and NPCI to add rent to the ₹1 lakh no-PIN list** (long term, no cost now).

## Adapt

- **Rent above ₹15,000:** Kamal suggests 2 or 3 separate mandates. The ruling (R16) is one mandate with debits in parts, which means one approval instead of three. Keep his disclosure line.
  - His claim that fintechs did this for SIPs has no source; his own file says none was found.
- **Agreement clause:** his text fixes the amount ("₹{amount} on {date}"). Under R18 the debit is variable: "your monthly dues shown on your bill, up to ₹{limit} per debit, in parts if above ₹15,000". Add the platform fee line, and do not say "no fees at all".
- **"We'll retry in 24 hours":** use at most 3 retries per cycle, inside NPCI's allowed hours, timed near salary day.
- **Manager "pause":** means RentOk stops raising charges (fact 2). The tenant's own pause stays in her UPI app.
- **Day grid:** any day of the month, which becomes her rent due date for fines (R9, #6829). Kamal's reading of the "1st to 1st" bug is right; the cause is a window of due day to due day plus 0 grace days.

## Leave

- **"Autopay is free forever, ₹0 fee as policy":** replaced by R11 and R15. There is no Autopay charge, and a ₹49 platform fee applies to every payment method. The struck-through "₹50 → ₹0" lines go.
- **Phased adoption (Oct 2026 to Jan 2027, 50% in 90 days, 85% by mid-2027):** the target is 70,000 to 75,000 by 1 Oct (R1). Phasing is excluded (N4).
- **"Autopay keeps rent collection free to process":** Cashfree charges about ₹17.70 per debit attempt. It is only free of the new UPI charge.
- **"Failure rates 8 to 15%":** our own rate is 59%. Plan for ours.
- **"The 24-hour notice is our WhatsApp and a compliance blocker":** the bank sends it through Cashfree (fact 1).
- **"1-tap PIN approval every month above ₹15,000":** replaced by R16.
- **RentPass cashback for turning on Autopay:** someone has to pay for it, and R11 says RentOk absorbs nothing. Parked unless a partner pays.
- **Co-marketing with UPI apps:** parked until the numbers are big enough.

## Open, raised by the plan

- **"Required by the property" state** (Figma frame 04, `is_autopay_mandatory` in code) against R2 ("optional for tenants"). My legal notes say Autopay should never be a condition of the tenancy.
- **Maximum per debit for tenants at ₹15,000 or less** (fact 4 plus R18). The choice is between a limit close to her dues and a ₹15,000 limit that never needs re-approval.
- **The Payment Page Revamp Figma** (node 5:28) was never reviewed by Kamal. RentOk's design record in the payment-redesign worktree covers it.

## Added to the Cashfree question list

- Can setup take this month's dues as a kept payment, and is it free of the UPI charge?
- For rent in parts: is the retry budget per debit or per cycle, and does each part get its own notice?
- What does Cashfree do with a charge time inside NPCI's blocked window (#7004)?
