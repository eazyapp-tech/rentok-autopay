# Two older Autopay lists, checked against the record (18 Sep 2026)

Sanchay shared two lists from earlier sessions:
- **The backend requirements list:** about 50 rentok-backend issues in six groups (security, money, links, page data, Autopay, electricity).
- **"What we need from Nimit":** a product view, stage by stage, written before the rulings of 17 Sep.

Each item below is marked **taken**, **already covered**, or **overtaken by a ruling**. All issue numbers were checked on GitHub on 18 Sep: every one is still open.

## Taken: gaps in our record

### 1. Faked payment messages belong in the first step
Our order starts with the login fix for Autopay routes (#6816, #6861). Three more holes sit on the same path:
- **#7019:** no payment webhook checks its signature, including Autopay's. Anyone can send RentOk a fake "debit succeeded" message.
- **#6851:** a payment can be marked paid without asking Cashfree.
- **#7018:** the add-payment route accepts calls with no login.

A fake "succeeded" message marks rent as paid when no money moved, and it also counts toward the target. **Proposed:** add all three to step 1 of the order.

### 2. Filed issues the map promises but the order leaves out
The map's own rules depend on these. None is in the build order.

| Issue | What the map promises that needs it |
| --- | --- |
| #6817 (failure reason saved as "Unknown failure") | The same-day failure message with the reason, and the failure-reason numbers |
| #6830 (reminder links keep going to Autopay tenants) | No reminder links for dues Autopay will take (R9) |
| #6835 (payments do not record that Autopay made them) | "Paid by Autopay" receipts, and counting the UPI charges avoided |
| #6825 (the payment page does not know her Autopay state) | The tick above Pay, and showing what Autopay will take |
| #6828 (the two debit-day helpers disagree) | The due-day-plus-7 window (R41) changes these same helpers |
| #6866 (payments cannot be tested end to end) | Any safe testing of the debit fixes before 1 Oct |

Also: cancelling Autopay today wipes her grace days, which switches her late fine off. This is noted in `research/systems-map.md` and tied to #6817, but has no issue of its own.

**Proposed:** add these to the order, under "safe debits" or "before the first October debit".

### 3. A way to stop all debits at once
Nimit's plan says there is none. The map has none. With tens of thousands of new mandates and debit fixes landing in 13 days, a mistake could repeat across every tenant before anyone can stop it.
- **Proposed:** a RentOk-only switch that stops raising new debits, for everyone or for one property, with a record of who used it.
- Setup and approvals keep working while it is on. Only debits stop.

### 4. A stop rule, without waves
The Nimit list proposed a pilot with a pass mark. The pilot is overtaken by R37 (no waves), but the stop signal is not.
- **Proposed:** the health number already in the map (rent paid by Autopay on the first try) gets a floor.
- Any double debit, or first-try success below the floor, pauses setup messages and triggers a review. The stop-all switch from point 3 is used only if debits themselves are wrong.

### 5. Payment page analytics in the build order
`decisions/success-metrics.md` notes that the payment page sends no analytics. The build order does not include switching them on. Without them, the "pay now and turn on Autopay" source (about 18,000 payments on 1 Oct) cannot be counted by source.
- **Proposed:** add it to the "by 1 Oct" lane.

### 6. Whitelabelled properties
- 19.5% of tenants belong to whitelabelled properties (#6883).
- The map already asks Cashfree about the merchant name in the UPI app. It does not say what these tenants see on the setup screen and in the WhatsApp messages: RentOk's name, or their property's.
- A tenant who has only ever seen her property's brand, and is then asked by "RentOk" or "EAZYAPP" to approve a monthly debit, is more likely to stop halfway, or to dispute a debit later.
- **Question for Sanchay:** which brand these tenants see.

### 7. Who the push messages reach
Two facts from #6822:
- 63% of tenants sent payment links owe nothing.
- 19,444 of the tenants sent links have moved out.

The push goes out through a WhatsApp number whose daily limit and quality rating decide its speed (the map's "Send capacity"). Messages to people who have left, or who owe nothing, lower that rating.
- **Proposed:** the push list is built from current tenants only.
- **Not verified:** whether the link messages and the push use the same number. Check before 30 Sep.

### 8. Links that die
Links expire after 7 days (#6869). The map sends a "Pay now" link after a failed debit and for paused periods. A link sent on the 1st is dead by the 8th, which is inside her 7 grace days.
- **Proposed:** these links live at least until the end of her grace days.

### 9. Terms she never saw (filed today)
At web check-in, her agreement to the Autopay terms is set to yes before she sees anything:
- the checkbox is commented out;
- the terms link has no address.

Filed as **eazypg-marketplace#935 (P1)**.

## Already covered by the map
- **Pay now and turn on Autopay:** the tick above Pay, with the first debit taken at approval.
- **Per-tenant and bulk sends:** manager sends, one tenant or many.
- **Tenant app card:** appears without an app update.
- **Setup reminders:** go to anyone not on Autopay (#7006).
- **Dues above ₹15,000:** parts under Option 2.
- **A tick she sets herself:** never pre-ticked.
- **Pre-debit notice:** sent by the bank through Cashfree, with our heads-up 2 days before.
- **Failure messages and retries:** failure message, pay-now link, retries near salary day, no late fine while retries run (proposed).
- **Pause and cancel:** pause as a request, cancel with no block.
- **Move-out and rent changes:** cancel on move-out (#7005); a rent rise leads to a new approval.
- **Payouts and "RentOk pays":** payout fixes (#6996, #6998), and the "RentOk pays" choice is removed.
- **Paid another way, empty months, double debit:** #7002, #6999 and #6995.
- **Support:** a "charged wrongly" path and support numbers.
- **Other dues:** Option 2 takes all regular dues, and payment requests cover the rest.

## Overtaken by a ruling (not taken)
| Older item | Ruling that replaced it |
| --- | --- |
| Any day of the month, which becomes her due date (#6829) | R41: due day to due day plus 7; her due date for late fines does not move |
| A first group or pilot on 1 Oct | R37: everyone at once, no waves |
| A 0.4% charge on tenants not on Autopay | The platform fee line (R35, R42, R43); never presented as a UPI charge |
| Autopay for rent only | R46: two options, Option 2 takes all regular dues |
| Setup charge of ₹1, ₹2, ₹30 or ₹50 | No charge to the tenant for the mandate; the ₹49 service charge goes to management |
| Can she change her own day | R45: yes, inside the allowed window |
| "RentOk pays" should mean RentOk pays (#6880) | The choice is removed from the product |

## Not relevant here
- The electricity group.
- Links wrongly labelled as electricity (#6823).
- Collectors from other buildings (#6864).
- The receipt host (#6969).
- The ₹0 bill (#7036).

All are real, but outside Autopay.

---

# The call with Nimit, 18 Sep 2026, 16:44 to 17:02

Recorded on Sanchay's NeoSapien pendant. Sanchay read the "What we need from Nimit" list aloud, and Nimit answered item by item. A 1-minute follow-up at 17:02 added the tenant's own controls. Notes below, checked against the code where Nimit's answer disagreed with a filed issue.

## What Nimit confirmed or offered
- **Autopay state on the payment page is cheap.** An existing call (tenant details for the payment page) already returns subscription details. The same logic can be pulled out and reused (#6825).
- **Pay now and turn on Autopay in one step works** when her pending dues are at most the mandate amount: the dues go in as the approval amount, are debited at approval, and are set against her dues. If dues are higher, a second payment is needed.
- **Opening her UPI app directly** needs RentOk's own approval screen instead of Cashfree's default page, and the allowed methods passed when the Cashfree token is made. Matches the map.
- **Autopay grace days already exist on manager web**, as a setting separate from the normal grace days. Missing on the phone app. Most properties have it at 0 today, so the 7-day default (R9, R41) still has to be set.
- **The terms tick:** Nimit says the backend already takes it and only the screen needs to show it. The code shows the tick pre-set to yes and hidden, filed as eazypg-marketplace#935.
- **Reminder links to Autopay tenants** will be stopped (#6830).
- **Move-out cancels the mandate** (#7005): agreed.
- **Paid another way before the debit:** "we can cancel that" (#7002).

## Where Nimit disagreed, and what the code says
| Nimit's view | Code on backend `master`, 18 Sep (dc98a0d78) | Result |
| --- | --- | --- |
| An empty month does not end Autopay: no dues, no debit | True for that month. But the "no unpaid invoices" branches (`autopayV2.ts:314-315`, `:342-343`) mark it skipped and never book the next month. The other skip branches (`:255-256`, `:261-262`) do. | #6999 stands |
| Payments already record their mode, so Autopay payments are known | They carry mode 205, the general online mode. The `is_autopay` flag sent with them is read and dropped (`payment.ts` around 1334 and 1576, per #6835). | #6835 stands |
| The Pay button is not blocked for Autopay tenants | Sanchay thinks it is blocked on the payment page. | Not verified; check before 1 Oct |
| Double debit: "there is a cron, we need to review" | Not rechecked today. | #6995 stands, Nimit to review |
| The 12-hour time bug: "not sure" | Not rechecked today. | #7004 stands |

## New facts from the call
1. **More than one debit a day.** Kamal heard from PhonePe that several debits within 24 hours are allowed. Vivek and Jatin tested it on Cashfree earlier and found only one debit per 24 hours worked. This is the main question in the Cashfree list (rentok-autopay#2). Until Cashfree answers, a ₹30,000 due in two parts takes at least two days. The map already runs parts one after another.
2. **GST taken as a separate small debit.** Nimit's idea for #7000: take ₹10,000 and ₹1,180 as two debits. Under R46 the approved limit already includes GST in regular dues, so one debit is enough. The two-debit route is not needed.
3. **The manager's single-tenant Autopay reminder** exists on the tenant profile, but managers read it as a KYC reminder. **Needed:** its own "Autopay" button with a message that is plainly about Autopay.
4. **Web check-in does not open at the Autopay step.** A tenant sent back to check-in starts from the top. Nimit: quick to fix.
5. **Which link a tenant gets** (Sanchay's ruling on the call, recorded as R52):
   - a new tenant still in check-in sets it up inside check-in;
   - everyone else, including a tenant who chose "Set up later", gets the payment page as the one Autopay link.

   Nimit's concern was that one person should never get two different links. This rule meets it: each tenant gets one link at a time. Nimit also asked why Autopay should wait for KYC. Under this rule it does not, outside check-in.
6. **Tenant app:** a bottom sheet that opens by itself, can be closed, and comes back until she is set up. This needs the app release after 1 Oct.
7. **Manager app Autopay settings are buggy.** Changing who bears the fee from owner to tenant does not save unless the other field is picked again. The map removes that setting, so no fix is needed; the removal must ship to the phone app.
8. **Failure reason for the manager:** on the dues card, where "paid" is already shown.
9. **Retry limit, then a manual link.** After N failed tries she gets a pay link. Nimit: 5 tries is common. The map uses Cashfree's retries plus RentOk's own under Option 2, and sends "Pay now" the same day as the first failure.
10. **Bounce charges.** A past tenant was charged ₹200 by her bank several times. **Needed:** research on which banks charge for a failed UPI Autopay or e-NACH debit, and how much. Not in the map yet.
11. **No late fine when the failure is RentOk's fault.** The map already covers a bank or Cashfree outage; this extends it to RentOk's own faults.
12. **Pricing with a floor and a ceiling.** Sanchay said on the call that the price must be adjustable, within a lowest and a highest amount. The map lets a property change or turn off the platform fee line, but sets no floor or ceiling. **Open question.**
13. **Kamal and Srijan's IDFC workflow.** Sanchay wants to go through it again with them. This repo has only a note on bill payments through IDFC (`research/systems-map.md`) and a mention of a virtual account. **Needed:** Kamal to send it.
14. **Tenant controls** (follow-up call): see on or off, debit day and last debit; pause and cancel; change the day inside the allowed window, starting next month. All are in the map (R45).
