# Autopay for every tenant: the feature map

This map sets out how Autopay works for every tenant, parent, manager, owner and for RentOk, moment by moment, and why each piece is in or out. It is written as requirements: what the product does. How to build it belongs in engineering documents.

**How to read the markers**
- **R numbers** are Sanchay's rulings, made on 17 Sep 2026 unless marked.
- **N numbers** are things he ruled out.
- **(agreed)** marks something that follows from the rulings and that he has confirmed. **(proposed)** marks one still waiting for his yes.
- **#number** is a GitHub issue already filed, in the backend repository unless it says marketplace.
- **[Cashfree]** marks a behaviour confirmed in Cashfree's documentation; **[ask Cashfree]** marks one their documentation does not answer.

The full record is `05-inventory.md` in this folder. Cashfree answers are in `19-cashfree-docs-answers.md`.

*Version 3, 17 Sep 2026. Owner: Sanchay.*

**Words used in this map**
- **Mandate:** the standing permission a tenant approves once. For UPI Autopay it is approved in her UPI app. For a bank-account mandate (**e-NACH**) it is approved with her bank. It lets RentOk take money on her day.
- **Approved limit:** the amount she approves in the mandate. It is the most a single debit can take.
- **Regular dues:** what her property bills her every rent period at a fixed amount: rent (with GST if charged), fixed recurring charges such as a food or amenity package, and the platform fee line. Electricity bills, repairs, one-off charges, deposits and late fines are not regular dues.
- **Grace days:** the 7 days after her rent due date before a late fine applies, for Autopay tenants (R9).
- **Cashfree:** RentOk's payment provider. **NPCI:** the body that runs UPI. **RBI:** India's central bank.
- **Signing step:** the step where a tenant signs her agreement online, at check-in, at renewal or after a rent change.
- **Manual-schedule tenants:** tenants billed on dates the manager sets.
- **Start rate:** the share of reached tenants who open setup. **Finish rate:** the share who then finish the approval.

---

## Why this exists

From 15 Oct 2026, every UPI payment above ₹2,000 made to a business carries a charge of 0.4%, capped at ₹300 (Finance Ministry FAQ, 15 Sep 2026). The business pays it and may not pass it to the customer. This map calls it "the new 0.4% UPI charge".

In the last 30 days, 82% of online payments through RentOk were above ₹2,000, with an average of ₹10,748. Autopay debits carry no such charge.

RentOk does not pay any payment cost, on any payment method, because rent is not RentOk's money (R11). RentOk charges management for its service. Management decides whether to absorb that charge or pass it on to tenants as a platform fee (R35).

**The target**, set by the CEO and fixed (R1): **70,000 to 75,000 tenants on Autopay by the end of 1 Oct 2026** (R23).

## How we count

A tenant counts when she has an approved, active UPI Autopay or e-NACH mandate (R8), subject to these rules:
- **Current tenants only, each person once** (agreed).
- **A parent's mandate counts for the tenant** (R24).
- **A paused mandate does not count** while paused, whether the pause was approved in RentOk or made in her UPI app (agreed). A pause still waiting for approval counts (proposed).
- **The property's or tenant's "required" switch does not change the count.** Any active mandate that is not paused counts.
- **A mandate that has reached its end date does not count** until she approves the new one.
- **One mandate per tenant.** A parent paying for two children sets up one mandate for each. CirclePe's own bank mandates do not count.

**Starting point (17 Sep): 778 current tenants.** About 470 more active mandates belong to tenants who have left; those are being cancelled (#7005). The gap is about 69,200 in 14 days, **about 4,950 a day**. Today about 5 new mandates are approved a day.

**The health number is rent paid by Autopay on the first try.** It sits next to the target, and the target must not be reached by pushing this number down. It is not measured yet. Today about 41% of debit attempts succeed. Failure reasons are not recorded yet; an empty account is the likely main cause.

## The rules everyone lives by

### Who is on Autopay

- **Everyone, from the start** (R20, R37). Autopay is on and required by default for every tenant and every property, existing and future. There are no waves and no priority groups.
- **Two switches can turn "required" off:**
  - for a whole property, in its settings (R20);
  - for one tenant, from her profile, by a team member with access, with a reason such as "no supported bank" or "no smartphone" (R38, R21). The manager can also send a bank-account (e-NACH) setup instead.
- **Required means chase, never block** (R21). Nothing in the app is locked, and she can always pay any bill another way.
- **Non-monthly tenants are included** (R28). Quarterly, yearly and manual-schedule tenants are debited on their own billing cycle. A period with nothing to collect never ends their Autopay.
- **CirclePe tenants are left out** (agreed). CirclePe is a rent-finance partner, and these tenants already pay through their own bank mandate with it.

### Two options, and she picks one (R46)

| | Option 1: "My rent, every {her rent period}" | Option 2: "All my dues, when they're due" (recommended, highlighted) |
| --- | --- | --- |
| Mandate type | A fixed schedule (monthly, quarterly, half-yearly or yearly), matching her rent period. Cashfree debits it on that schedule [Cashfree] | On demand, shown as "as presented" in her UPI app. RentOk raises each debit |
| What she approves | A **fixed amount**: her regular dues for the period, listed line by line | An **approved limit** equal to her regular dues, listed line by line, for example "₹10,000 rent + ₹58 platform fee = up to ₹10,058 per debit". No round-number buffer |
| What is taken on her day | That fixed amount, once per period | Her regular dues for the period, in parts of up to ₹15,000 when the total is higher (R16) |
| Extra bills (electricity, repairs, one-off charges) | Sent to her as a "Pay now" request, with an offer to switch to Option 2 | "Request payment via Autopay" (R47), described below |
| Above ₹15,000 | Her bank asks for her UPI PIN on every debit [Cashfree]. Setup says so and points her to Option 2 or to a bank-account mandate | Taken in parts, so no PIN each time |
| Pause after approval | RentOk pauses the mandate at her bank through Cashfree and resumes it on the date [Cashfree] | RentOk raises no debits for those periods |
| Changing her day | Needs a change on Cashfree's side, possibly a new approval [ask Cashfree] | Takes effect the next period |
| Her dues go down for good (rent cut, fee turned off) | RentOk lowers the fixed amount; no new approval is needed [Cashfree] | Nothing to do: RentOk takes less |
| Her dues go down once (advance or credits used) | That period's debit is cancelled and she gets a link for the balance [Cashfree] | RentOk takes the lower amount |
| Her regular dues go above what she approved | She is asked to approve a new mandate at once. Until she does, the old amount is taken and she gets a link for the difference | She is asked to approve a new limit at once. Until she does, up to the old limit is taken and she gets a link for the rest |

**Both options**
- The setup screen says "every {period}, cancel anytime".
- Late fines are never taken by Autopay (R29, R51).
- Prepaid electricity recharges are topped up by her (R30).
- Deposits are never part of a regular debit.
- **No questions before a regular debit** (R36). She gets notices only.
- RentOk can move her between options, with her approval of a new mandate.
- **One active mandate per tenant.** If she or her parent already has one, setup shows it and replaces it only with consent.
- **A platform fee already announced but not yet started** is included in what she approves at setup, labelled "from {date}", so its start does not force a new approval.
- **e-NACH** ("Use bank account instead") follows the option she picked. There is no PIN rule, so no parts are needed. Cashfree sends its notices, and it does not retry e-NACH automatically [Cashfree]; RentOk sends its own retries.

### Request payment via Autopay (R47, R51)

- **Where:** on every due, next to "Record payment" and "Remind to pay", the manager can "Request payment via Autopay". This works for any due except late fines, one at a time or in bulk.
- **Who can receive it:** only Option 2 tenants whose mandate is active and not paused. Everyone else, meaning Option 1, paused, cancelled or not set up, gets the same request as a normal "Pay now" request.
- **The message:** she and her parent get "{Property} has requested ₹X for {due}. It will be paid from your Autopay after 24 hours." The buttons are "Approve now" and "Pay manually". There is no reject.
  - "Approve now" confirms it, and the screen shows "Will be paid on {date}", because the debit still waits for the bank's notice period.
  - If she does nothing, the debit runs after the notice period.
  - Requests are separate from the regular debit. The rule that later additions wait for the next period applies only to the regular debit.
  - Requests above ₹15,000 are taken in parts, like regular dues.
  - A failed request debit is retried within the same retry rules, and after that she gets a link.
  - "Pay manually" cancels the debit and opens "Pay now".
- **Above her approved limit:** "Approve" opens her UPI app to approve a new limit, the larger of her regular dues and this request (a deposit top-up, for example). Otherwise she pays manually.
- **Late fines:** the backend can request them, but this is switched off for tenants. It can be turned on later without new build work (R51).

### Her day and late fines

- **She picks her Autopay day** between her rent due day and the last of her grace days (R41, R9).
- **Her due date for late fines does not move.**
- **She can change her day once a month,** and the change takes effect the next period (R9, R40).
- **No late fine while retries are still running** (proposed).

### How long a mandate lasts (R49, R50)

- **Start and end:** from setup to her agreement end date. Cashfree cannot extend a mandate [Cashfree], so every renewal needs a new one.
- **Renewal:** 15 days before the end date, RentOk asks whoever pays (the tenant or her parent) to approve the new term, in the renewal signing step, the app card and WhatsApp. If it is not approved by the end date, Autopay stops, she drops out of the count, and her dues show "Pay now".
- **No end date:** where a tenancy has no end date, the mandate runs until she moves out (proposed).

### Links and messages

- **No reminder links for dues Autopay will take** (R9). A reminder link goes out only after a debit fails, or for dues Autopay will not take.
- **She can still pay any bill** by link, cash or any other method, whenever she wants.
- **The pitch:** "never miss rent, nothing to remember, no extra charge for Autopay" (R11). Nothing ever mentions the new 0.4% UPI charge.

## Charges: three separate things

These are three different charges, made by different parties for different reasons. Keep them apart.

| Charge | Who charges whom | Rule |
| --- | --- | --- |
| **RentOk's service charge** | RentOk charges management **₹49 plus GST per billed tenant per month** (R22, R31, R35) | Always, whatever way the tenant pays, on RentOk's invoice. It is taken from the money RentOk sends to the property. In a month when nothing is sent, the property gets a monthly invoice with a payment link (R32). |
| **Platform fee** (on the tenant's bill) | **The property** charges its tenant, if management chooses (R35) | On by default and the same for every payment method. A GST-registered property shows **₹49 plus GST**. A property without GST registration shows **₹58**, one amount that covers RentOk's ₹49 plus GST (R42, R43). Management can change the amount, or turn it off and absorb RentOk's charge. |
| **Payment gateway charges** | Charged on the tenant's chosen method (card, net banking, IMPS, NEFT and others), as today (R34) | **Unchanged, and separate from the platform fee.** One exception: the new 0.4% UPI charge on link payments can never reach the tenant, and management pays it from 15 Oct (R15, R6). |

### The platform fee line

- **Name: "Platform fee"** (R26). Never "convenience fee", "processing charge" or anything tied to paying.
  - It is the property's charge for running the tenancy on RentOk: the app, receipts, agreements and reminders.
  - It is never described as a charge for Autopay (RBI e-mandate rules, para 10(a)).
- **Same for every payment method:** cash, link, bank transfer and Autopay (R15). It makes no method cheaper or more expensive (N5, N6).
- **Who pays it:** each person who gets her own rent invoice (R31). Co-tenants and parents who only sign pay nothing.
- **When it starts:** with October 2026 dues (R25), once notice has reached the tenant (R13).
  - If her agreement asks for a longer notice period, it starts when that period ends.
  - Until then, the property covers RentOk's charge for her.
  - RentOk sends the notice to every tenant before 1 Oct, on the property's behalf.
- **Changing or turning it off:** goes through the same notice rule as a rent change (R13). A rise that takes a tenant above her approved limit is flagged in the preview, and she is asked for a new approval.
- **How it is collected** (R32):
  - As part of her regular dues, including in the Autopay debit.
  - If she pays rent in cash, the line stays open in the app and on her next bill until she pays it online.
- **Where it shows:** check-in, the agreement, every bill, every receipt and the tenant app. Nothing is hidden (N5).
- **What it replaces:**
  - the ₹30 platform fee that one account (FNF, a large operator) charges today (R15);
  - the old tenant "Autopay fee" and setup fee;
  - the "Payment processing charges" label on receipts.

RentOk's setup and debit costs (about ₹7.5 per mandate and ₹15 per debit, plus GST [Cashfree price list]) are covered by its ₹49 service charge (R12). Dues taken in parts cost RentOk more, but the charge stays ₹49. RentOk checks whether the charge covers its costs across all tenants together, not tenant by tenant (R17).

### Passing costs on through rent instead

Management can turn the platform fee line off and raise rent instead, using the rent change flow below (R12). RentOk's ₹49 is charged either way.

---

## A tenant's life with Autopay, moment by moment

### 1. First contact

She meets Autopay wherever she already is (R7):
- **Check-in.** Autopay is a required step after the agreement, never before it. The step has a "Set up later" option (R21). The agreement carries the Autopay terms and the platform fee line.
- **Tenants a manager adds directly**, who never go through web check-in, get the setup link on WhatsApp and a card in the app.
- **WhatsApp from RentOk.**
  - RentOk messages every property's tenants directly, on the property's behalf (R27).
  - The manager is told 24 hours before and can opt the property out.
  - A dedicated setup message, approved by Meta before sending starts, is needed. Today's reminder borrows a general template in the owner's name.
- **WhatsApp from the manager,** to one tenant, a selection, or everyone not set up.
- **The tenant app home.** A setup card stays until she is set up. It appears without anyone updating the app.
- **The payment page and every payment screen.**
  - A tick above Pay reads "Pay now and turn on Autopay. Cancel any time · know more".
  - She ticks it herself; it is never pre-ticked (agreed).
  - Once ticked, "know more" becomes "edit", where she picks her option and day. The Pay button stays the same. This is the pattern CRED, a bill-payment app, uses.
  - This payment is a one-time amount shown separately, and it can be larger than her approved limit [ask Cashfree]. Her limit is still her regular dues.
- **The signing step.** Whenever she signs an agreement, including after a rent change or at renewal, Autopay is the step after signing.
- **Her parent.** Any of these can go to her parent or guardian instead, through the parent app and WhatsApp, and the parent sets it up from their own account (R24). She can also forward it with "Share setup link on WhatsApp", the same way the payment screen already offers "Share Payment link on WhatsApp".
- **The Autopay page** ("know more" everywhere).
  - Headline: "Rent that pays itself. Never miss a due date."
  - Five plain benefits: never miss rent, no late fine when Autopay pays on time, you stay in control, help when something fails, safe.
  - An FAQ that answers, in our words, the questions CRED answers: what it is; the two options; how to set up; what gets paid; is it safe; what if a debit fails; notices before and after; low balance; payment requests; pause, cancel or change the day; change bank; the ₹15,000 rule and parts; a limit she sets in her UPI app; is there a charge for Autopay (no); when it happens; receipts; bank downtime; renewal; and the bank-account option (e-NACH).

**Who gets these:** everyone not on Autopay, including tenants who started and stopped, cancelled or failed before. Today's reminder skips anyone who ever tried (#7006); that changes.

### 2. Setting it up

**One screen, opened straight from any link or card.** No app install, and no earlier check-in steps. It shows:
- "Autopay takes ₹{amount} every {period} on your day." (her real numbers)
- **The two options side by side** (R46), with her real amounts and Option 2 highlighted. She must pick one.
- "We never take more than your bill, and your bank tells you before every debit."
- **Her day,** from her allowed days (her due day to the last grace day), with the next three debit dates written out.
- **Her bank accounts** that can do UPI Autopay, with a "check balance" link, where her UPI app shares them.
- **If her regular dues are above ₹15,000:**
  - Option 2: "Your ₹20,000 is taken in 2 parts, ₹15,000 and ₹5,000, starting on your day."
  - Option 1: "Your bank will ask for your UPI PIN each time."
- **If October dues are already on her bill** (setup between 25 Sep and 1 Oct): "October dues ₹X will be taken on {date}" (R33).
- **The platform fee line,** if her property charges it.
- **The end date:** "Valid until {agreement end date}; we'll ask you to renew."
- "Cancel or pause any time, here or in your UPI app. Change your day once a month, here."
- **The merchant name** she will see in her UPI app [ask Cashfree how it is set].

**The approval**
- **UPI, on our own screen, never Cashfree's page** (R44) [Cashfree]. Her UPI apps (GPay, PhonePe, Paytm, BHIM, Amazon Pay) are listed. The one she paid with last is first, and tapping one opens it straight at the approval.
- **On a computer:** she scans a QR code or enters her UPI ID, also on our screen [Cashfree].
- **"Use bank account instead"** is a small link that opens Cashfree's page for e-NACH (R44). Approval takes 24 to 48 hours, and the first debit comes at least 4 days later [Cashfree]. There is no card Autopay.
- **If she is paying now:** this payment and the Autopay approval are one approval.
  - The approval amount can be kept as a real payment [Cashfree]. The upper limit is [ask Cashfree].
  - A first debit within 5 minutes of setup is also allowed during NPCI's blocked hours (press report).
- **If a parent sets it up:** the mandate is in the parent's name, and notices go to both (R24).
- Existing e-NACH mandates keep working and count.

**After the approval**
- **Success screen:** "Autopay is on", her option, her next three dates and what gets taken. Buttons to change her day, pause or cancel are as easy to find as setup was.
- **If she leaves halfway:** the card and the WhatsApp message bring her back to the same screen.

### 3. Every period

1. **Bill ready.** Her dues are raised as usual. Any advance or credits she holds (including RentPass cashback, RentOk's tenant rewards) are used first, before the notice, and shown in it.
   - The tenant app shows "Autopay takes ₹X in N days" on the home card, with the breakdown.
2. **Two days before her day,** RentOk sends a WhatsApp heads-up in the property's name.
   - "₹X will be taken on {date}. Keep it in your account."
   - It lists what the amount covers and carries a "check balance" link.
   - It is a courtesy, aimed at the likely main cause of failed debits.
3. **The bank's notice.**
   - **Option 2:** RentOk sends the notice itself through Cashfree's controlled flow, and the debit follows at least 25 hours later [Cashfree].
   - **Option 1:** Cashfree sends the notice on its own schedule [Cashfree].
   - From the notice on, the amount is fixed and must match exactly [Cashfree]. Anything added later waits for the next period.
4. **On her day,** the debit runs, only in the hours NPCI allows: before 10:00, from 13:00 to 17:00, or after 21:30 [Cashfree].
   - **Option 2 parts:** only one notice can be open at a time [Cashfree], so parts run one after another, on her day and the days after, until Cashfree confirms same-day parts [ask Cashfree].
   - **Option 1:** takes the fixed amount.
5. **If the debit succeeds:**
   - She gets a confirmation on WhatsApp and in the app, and one receipt for the payment, showing any parts, marked "Paid by Autopay".
   - Her dues show as paid in the app, on the payment page, in the manager's list and for the owner.
6. **If the debit fails:**
   - **RentOk tells her the same day,** in the property's name, with the reason in plain words, a pay-now button and the next retry time.
   - **Retries, Option 2:** RentOk times up to 3 retries near salary days, within the grace days where possible, because Cashfree's controlled flow never retries by itself [Cashfree]. Only a failed part is retried.
   - **Retries, Option 1:** Cashfree retries up to 3 times, an hour apart [Cashfree].
   - **Paid means every part is in.** Dues are marked paid only then.
   - **No late fine** while retries are running (proposed).
   - **If all retries fail:** she gets a link for the balance only, and the manager is alerted.
7. **If she pays another way first:**
   - Option 2: the pending debit is cancelled, and a new notice goes out for anything left.
   - Option 1: that period's debit is cancelled [Cashfree], and she gets a link for anything left.
   - She is never charged twice.
8. **If she refuses one debit in her UPI app,** she gets a link for the amount she refused.
9. **If she has set a lower limit in her UPI app** (her bank lets her) and the bill is above it:
   - Option 2: the debit takes what fits, and she gets a link for the rest the same day.
   - Option 1: the debit fails, and she is asked to fix the limit or pay by link.
10. **If her bank or Cashfree is down on her day:** the debit is retried when it is back, she is told, and no late fine applies for the delay.
11. **If something looks wrong,** she taps "I was charged wrongly" on the debit in the app. It reaches her manager and RentOk support, and a refund follows if the debit was wrong.

### 4. When things change

**Her Autopay settings** are in the tenant app and on the payment page (R45). Every action there is confirmed to her on screen and on WhatsApp. It is also told to the manager in the list, as an alert and in the activity log, and it changes what her dues show.

- **Changing her day.** Within her allowed days, once a month, effective the next period (R40, R41).
- **Changing her option or bank.** She approves a new mandate from the same screen. The old one is cancelled once the new one is active.
- **Rent change.** Handled by the rent change flow below. The two-option table above covers what happens when her dues go up or down.
- **Room change or transfer to another property.**
  - Autopay moves with her.
  - Her allowed days, regular dues and platform fee line follow the new property's settings.
  - If her new dues are above what she approved, she is asked for a new approval.
  - She is told what changed.
- **Pausing** (R45, R48, R50).
  - **In RentOk:** she asks for "Skip next debit" or "Pause until {month}", for any length up to her mandate end date.
    - While a request is pending, the next debit is held until the request is decided (proposed).
    - The manager or owner approves or declines it. They get an alert, and her status shows "Pause requested". If nobody acts within 48 hours, the pause counts as approved.
    - **Once approved:** Option 2 gets no debits for those periods. Option 1 is paused at Cashfree and resumed on the date [Cashfree]; RentOk records this itself, because Cashfree sends no update for it [Cashfree].
    - If the bank notice for the next debit has already gone out, that debit is cancelled, provided it has not run yet.
  - **In her UPI app:** the pause takes effect at once, and the manager is told [Cashfree: CUSTOMER_PAUSED]. Only she can resume it, from her UPI app [Cashfree].
  - **Her dues:** the dues for paused periods show "Pay now", reminder links come back for them, and the usual late fine rules apply.
  - **Resuming:** she can resume at any time. An approved pause ends on its own on the chosen month, with a message before the next debit.
  - **The manager cannot pause for her;** the manager can only ask RentOk (R39).
- **Cancelling** (R45).
  - She can cancel from the app, the payment page or her UPI app. RentOk ends the mandate through Cashfree, and any debit that has not run is cancelled. A cancellation made in her UPI app reaches RentOk within about 45 minutes [Cashfree].
  - Giving a reason is optional.
  - **Her dues:** from then on, all dues show "Pay now", and reminder links come back.
  - **The manager** is told, and she shows as "Cancelled".
  - **Where Autopay is required for her,** she is asked again later, within the message limits, and never blocked (R21).
  - **A mandate her parent set up:** she can pause or cancel it, and the parent is told (proposed).
- **Autopay no longer required for her** (R38). Her mandate keeps working if she has one, and setup messages stop.
- **Agreement renewal.** Covered under "How long a mandate lasts" above.
- **Re-joining.** A returning tenant gets the same one-screen setup and is counted once.
- **Non-monthly billing** (R28). Debits follow her billing period. Under Option 2, amounts above ₹15,000 go in parts. Under Option 1, her bank asks for the PIN. If her agreement ends partway through a billing period, the renewal ask covers the next period.

### 5. Moving out

- The final settlement dues are taken as usual. Under Option 1, amounts that differ from the fixed amount go by link.
- After the last debit, the mandate is cancelled and she is told. Nothing is debited after she leaves (#7005).
- Eviction, deletion and transfer out end the mandate the same way.

---

## Who can do what

"Parent" means a parent who set up the mandate as the payer.

| Action | Tenant | Parent | Manager or team member with access | Owner | RentOk support |
| --- | --- | --- | --- | --- | --- |
| See Autopay status, next debit, breakdown and past debits | Yes | Yes, for that tenant | Yes | Yes, as a summary | Yes |
| Set up Autopay and choose Option 1 or 2 | Yes (R46) | Yes (R24) | Sends the link only | Sends the link only | Sends the link only |
| Approve a payment request, or pay it manually | Yes | Yes | No | No | No |
| Resume a pause | Yes | Yes | No | No | No |
| Excuse a tenant at check-in, or send e-NACH setup instead | No | No | Yes (R21) | No | Yes |
| Change option or bank (new approval) | Yes | Yes | No | No | No |
| Change the Autopay day, within the allowed days | Yes (R40) | Yes | Yes, when she asks (agreed) | No | Yes |
| Ask for a pause | Yes, in the app or on the payment page (R45, R48) | Yes | Asks RentOk on her behalf (R39) | No | No |
| Pause in the UPI app | Yes, takes effect at once | Yes | No | No | No |
| Approve or decline a tenant's pause request | No | No | Yes; silence for 48 hours counts as approval (R48, R50) | Yes | No; acts only on the manager's requests |
| Pause or stop at the manager's request | No | No | Asks (R39) | No | Yes |
| Cancel | Yes, in the app, on the payment page or in her UPI app (R45) | Yes | Asks RentOk (R39) | No | Yes, when asked, and automatically at move-out |
| Edit or delete the Autopay record (R49) | Edit day and option, cancel | Same as tenant | Asks RentOk | No | Yes |
| Make Autopay not required for one tenant | No | No | Yes, from her profile, with a reason (R38) | No | Yes |
| Make Autopay not required for the property | No | No | Yes, in property settings (R20) | No | Yes |
| Platform fee line: on or off, amount | No | No | Yes, in property settings (R35, R43) | Through the manager (R12) | No |
| Request a due through Autopay | No | No | Yes, any due except late fines (R47, R51) | No | No |
| Opt the property out of RentOk's direct messages | No | No | Yes (R27) | No | No |
| Send setup to one tenant, a selection or everyone | No | No | Yes | Yes, from the owner's monthly Autopay tile | Yes (R27) |
| Pay a bill another way | Yes | Yes | Records cash, as today | No | No |
| Report "charged wrongly" | Yes | Yes | Yes, for her | No | Handles it |
| Change rent (rent change flow) | No | No | Yes | Through the manager (R12) | No |

**Team permissions** (agreed). Each manager action has its own permission, and every action is recorded in the activity log:
- view the Autopay list;
- send setup;
- make Autopay not required for a tenant;
- make Autopay not required for a property;
- ask RentOk to pause or stop;
- approve or decline pause requests;
- change a tenant's day;
- request payment via Autopay;
- edit the platform fee line;
- change rent.

**Asking RentOk to pause or stop** (R39)
- The manager app has "Request to pause or stop Autopay" on the tenant's profile. The manager adds a reason and, for a pause, the months to skip.
- RentOk support acts on it and records what it did, and both the tenant and the manager are told.
- While the request is open, her status shows "Waiting on RentOk".

---

## The rent change flow (bulk, also for one tenant)

This flow lets a property pass costs to tenants through rent (R12), and it works for any rent revision.

1. **Choose.**
   - Pick properties and tenants, the change (+₹, +% or a new amount), a start date, and a reason the tenant will see.
   - Tenants cannot be picked by how they pay.
   - The reason cannot mention Autopay, UPI or payment charges (N5).
2. **Preview.** Each tenant's old and new rent is shown, with flags for:
   - tenants whose new regular dues will be above what they approved (they will be asked for a new approval);
   - Option 1 tenants whose fixed amount will be lowered;
   - tenants crossing ₹15,000 (Option 2: taken in parts; Option 1: PIN on every debit, so offer Option 2);
   - tenants crossing ₹20,000, where GST may apply;
   - tenants on the seven accounts that cap online payments at ₹20,000 today;
   - tenants leaving before the start date;
   - tenants whose agreement ends first;
   - tenants with another change already pending.
3. **Schedule.** The change is saved as pending. Rent changes only on the start date, so this period's bills stay as they are.
4. **Sign.**
   - An updated agreement goes to every party in one signing round.
   - She sees "Your rent changes from ₹X to ₹Y from {date}" and signs.
   - Next she approves a new Autopay amount if needed, or is offered Autopay if she is not on it.
5. **Notice and start** (R13).
   - Notice is delivered and recorded before the start date, which is never earlier than her agreement's notice period allows.
   - The new rent applies to everyone on the start date, signed or not.
   - Not signing does not stop the change. A tenant who does not accept it gives notice before it starts, and the manager sees her in the notice list.
6. **Track.**
   - Reminders go out on days 0, 3 and 7.
   - The manager and owner see "N of M signed", pending and refused.
7. **One record for every change.** Rent changes from renewal, the 2.5% quarterly rise set up for one account, room changes, package edits and platform fee changes all go through the same pending-change record. They never collide, and the tenant is always told.

---

## The manager's line

Existing tenants are the largest source of the 69,200, reached by managers and by RentOk's direct messages.

**Autopay list**
- Per property and across properties, with filters and exports by status and option.
- Statuses:
  - Not set up
  - Started
  - On (Option 1 or Option 2)
  - Pause requested
  - Paused until {month}
  - Waiting on RentOk
  - Waiting for bank approval (e-NACH)
  - Needs new approval (her dues are above what she approved)
  - Failed, with the reason
  - Ending soon (mandate ends within 15 days)
  - Ended (agreement end reached, not renewed)
  - Cancelled
  - Not required

**Autopay section on the tenant profile**
- Her status, option, day, approved limit or fixed amount, end date, next debit and amount, and past debits with reasons.
- Buttons:
  - send setup;
  - change her day (on her request);
  - make Autopay not required for her;
  - request a pause or stop;
  - send bank-account (e-NACH) setup.

**On every due**
- "Record payment", "Remind to pay" and "Request payment via Autopay" (R47).
- The due shows "Requested, debit on {date}", then "Paid by Autopay" or "Pay manually chosen".
- For tenants who cannot receive it, the request goes as a normal "Pay now".

**Pause requests:** a queue of tenant requests to approve or decline, each with a 48-hour clock (R48, R50).

**Sending setup:** to one tenant, a selection, or everyone not set up, in one tap, to the tenant or to her parent.

**Alerts** go to the manager for:
- a failed debit, with the reason;
- all retries failing;
- a tenant changing her day, asking for a pause, resuming or cancelling (R45, R48);
- a payment request she approved, paid or moved to manual (R47);
- renewals due in 15 days.

**Autopay rate:** per property, trended, next to the portfolio's.

**Property settings**
- Autopay required: on by default, with a switch to turn it off (R20).
- Platform fee line: on by default. A GST-registered property shows ₹49 plus GST; any other property shows ₹58. The amount can be edited, or the line turned off (R35, R43).
- Opt out of RentOk's direct messages (R27).

**Rent change flow:** bulk or single rent changes with notice, signing and an Autopay step, as described in the rent change section.

**Where it ships.** These features ship on manager web before 1 Oct. Until the next app release, managers who use only the app get these actions through WhatsApp messages with links to manager web: pause approvals, payment requests and the Autopay list. The manager app's own screens, including "Request to pause or stop" and the pause queue, come with that release.

## The owner's line

- **"Paid by Autopay"** on every receipt, payout line and owner message.
- **A monthly Autopay tile:** "UPI charges you paid on link payments this month: ₹X" and "Tenants not on Autopay: N", with a button to send setup.
- **Pause requests** for approval, if the owner handles them.
- **One monthly RentOk statement** covering:
  - RentOk's service charges;
  - platform fee lines collected;
  - UPI charges taken;
  - what was deducted from the money sent to the property;
  - any invoice still to pay.
- **Payout lines** showing the payment method, each deduction and the RentOk invoice number.

## RentOk's line

**Billing**
- RentOk's ₹49 service charge goes on RentOk's own invoice, with GST. It is taken from the money sent to the property; in a month with nothing to send, the property gets a monthly invoice with a payment link (R32).
- Deductions are correct: RentOk's charge, UPI charges on link payments, and nothing taken twice (#6996, #6998).

**Routing of money**
- Cashfree's split for Autopay is a fixed percentage per vendor, set when the mandate is created [Cashfree]. Sending each due within one debit to a different bank account is therefore [ask Cashfree].
- If Cashfree cannot do this, dues set to pay a different bank account are sent as a separate payment request rather than joined into the regular debit.

**Removed from today's product**
- The tenant Autopay fee line, and the "Payment processing charges" label on receipts.
- The "RentOk pays" choice in Autopay settings.
- The old "RentPass ₹49" wording in owner messages, so it is not confused with the new charge.

**Clean-up**
- Cancel mandates of tenants who have left, and tell each one (#7005).
- Today's mandates take only rent, capped at the tenant's old amount. Each of those tenants is asked to choose Option 1 or Option 2 and approve a new mandate at her regular dues before her October debit. Until then, the old mandate keeps working and counting.

**Support**
- Handle pause and stop requests.
- Handle "charged wrongly" cases, with a refund path.
- Keep a record of every action.
- Track pauses RentOk itself makes, since Cashfree sends no update for them [Cashfree].

**Daily numbers**
- Count against the target.
- Reach, starts, finishes and mandates turned on, by source, option and property.
- First-try success, and failure reasons.
- Cancellations, pause requests and renewals missed, with reasons.
- Service charges billed against Cashfree cost.
- UPI charges avoided.

**A daily money check:** every debit matches a recorded payment. Cashfree does not resend missed updates [Cashfree], so RentOk also checks mandate and debit statuses directly.

**On call:** named people during the team offsite, 24 to 27 Sep, when most of the team is away.

## Property lifecycle

- **A new property onboards.** Autopay required and the platform fee line are on. The manager sees both during onboarding and can change them.
- **"Required" is turned off for a property.** Existing mandates keep working, and setup messages stop.
- **The platform fee is changed or turned off.** A rise goes through the notice rule (R13), and Option 1 fixed amounts are re-approved. A cut or removal applies from the next bill, and Option 1 fixed amounts are lowered.
- **A property leaves RentOk.** Every mandate there is cancelled after the last debit, and every tenant is told.

---

## The push to 1 Oct

Everyone is on from the start (R37). Setup messages go to every tenant not on Autopay, within the message limits below. Figures are from RentOk's data tool on 17 Sep; workings are in `16-growth-math.md` and `17-gap-review.md`.

| Source | Pool by end of 1 Oct | Needs |
| --- | --- | --- |
| **Existing tenants**, reached by RentOk and managers | about 300,000 not on Autopay and not paying online before 1 Oct | the one-screen setup, the WhatsApp message, the manager list and sends, the app home card |
| **New tenants at check-in** | about 18,000 to 29,000 (1,300 to 2,100 a day over 14 days) | the required step with "Set up later", and the tenant-level switch |
| **Paying on 1 Oct** | about 18,000 online payments (August's 1st: 18,049) | "pay now and turn on Autopay" on the payment page |
| **Paying late in September** | about 1,800 online payments a day | the same |
| **Started but not finished, or cancelled** | about 1,950 (1,348 started, 599 cancelled), less any who have left | messages by current status |
| **e-NACH waiting on bank approval** | 78 | a follow-up now, since e-NACH takes 24 to 48 hours to approve |

**What it takes.** At 10 to 15% of 300,000, existing tenants give 30,000 to 45,000. With the other sources, low estimates reach about 52,000 and high estimates about 79,000. **The target is reachable only if existing tenants, check-in and the 1 Oct payers all run at once.**

**Two lanes**
- **By 1 Oct:** the backend, the payment page, manager web, WhatsApp, and app home cards that need no app update.
- **In the app release after 1 Oct** (nothing new enters the apps after the 18 Sep freeze): the manager app and tenant app screens, including "Request to pause or stop" and the pause queue.

**Order.** Before Autopay is switched on and required for everyone, these must be in place, in this order (R10):
1. **Login fix:** the Autopay routes that need no login (#6816, #6861).
2. **Fixes that make debits safe:**
   - two engines charging twice (#6995);
   - charging a tenant who already paid (#7002);
   - one empty month ending Autopay (#6999);
   - debits after move-out (#7005);
   - the debit time sent wrong (#7004);
   - the allowed-days window, which today is the due day plus 0 days, set to 7 grace days (R41).
   - **Before the first October debit, the money fixes:** payout deductions (#6996, #6998), dues with GST collected short (#7000), and the amount saved for each debit (#7003).
3. **Check-in:** "Set up later" and the tenant-level switch (web check-in issue #915).
4. **Setup:** the one-screen setup with the two options.

**Timing**
- The manager is told 24 hours before RentOk first messages their tenants (R27).
- The biggest push goes on 30 Sep evening and 1 Oct morning (R23).
- A UPI debit can be scheduled for the next day only if raised before 9 pm [Cashfree]. Mandates approved late on 30 Sep therefore take their first debit on 2 Oct, unless the first payment is taken at approval.

**Message limits**
- During the push: at most one setup message a day per tenant.
- After the push, per tenant:
  - one welcome;
  - one reminder before dues;
  - the debit heads-up and the result message;
  - payment requests;
  - the renewal ask;
  - at most one "still not on Autopay" message a month.

**Send capacity.** Daily sends are planned against the tenant WhatsApp number's daily limit and quality rating. That one number decides how fast the push can go.

## How we judge it

- **Target:** tenants on Autopay, counted as above.
- **Health:** rent paid by Autopay on the first try.
- **Inputs:**
  - properties and tenants where Autopay is required;
  - tenants reached, by source;
  - start rate;
  - finish rate (54% today);
  - option chosen;
  - managers sending, and sends per manager;
  - payment requests sent and paid.
- **Guardrails:**
  - first-debit success in October;
  - cancellations within 30 days, pause requests and missed renewals, with reasons;
  - zero wrong late fines;
  - zero double charges;
  - "charged wrongly" cases and disputes;
  - support tickets per 1,000 new Autopay tenants;
  - WhatsApp number quality;
  - zero debits after move-out;
  - zero security incidents on Autopay.

## The mechanics that run through everything

- **One setup screen, every door.** Every link, card, message and payment screen opens the same page at the approval step.
- **What she was told is what is taken.** The amount is fixed at the bank's notice.
- **Paid means paid everywhere.** Any payment on any method updates the debit, the bill, the receipt, the manager list and the reminders at once.
- **Messages go by her current Autopay status,** even if she tried before.
- **Her approved limit is her own bill.** It changes only with her approval.
- **Three charges, never mixed.** RentOk's service charge, the property's platform fee and gateway charges stay separate on every screen and receipt.
- **Managers ask, RentOk acts,** for anything that stops money moving.
- **Chase, never block.**

---

## Supporting

| Item | Why it supports and does not lead |
| --- | --- |
| CRED splits a bill above the mandate limit into several payments (its own FAQ, seen in Kamal's recording; Kamal is RentOk's payments product manager) | A live precedent for taking dues in parts (R16); still [ask Cashfree] |
| Streak note ("6 months on time with Autopay") | Builds the habit once people are on; does not bring them on |
| "Ask your flatmates" after setup | Spreads within shared rooms, which suits co-living |
| A merchant name she recognises, instead of EAZYAPP (RentOk's company name) | Raises the finish rate at approval; depends on Cashfree |
| Money settled through Cashfree's split payouts, with owners as verified vendors [Cashfree supports splits on Autopay] | Keeps RentOk in control of the flow the right way; no change for tenants |
| Asking NPCI, through Cashfree and the industry, to add rent to the ₹1 lakh no-PIN list | Would remove the need for parts; long term |

## Parked, and what brings each back

| Parked | Brought back by |
| --- | --- |
| A bank account number per tenant (virtual account) as another way to pay | After 15 Oct, once Cashfree confirms how its money settles |
| UPI inside the tenant app (UPI plugin) | Early 2027, for repeat payers |
| BBPS (bill-pay apps) for rent | Large registered operators asking for it |
| RentPass cashback for turning on Autopay | A partner paying for it, since RentOk absorbs nothing (R11) |
| Joint promotion with UPI apps | Adoption big enough to interest them |

## Not building, and why

| Not building | Why |
| --- | --- |
| Tenants paying owners directly, outside RentOk | RentOk keeps control of the payment flow (R4) |
| Becoming a UPI app ourselves (TPAP, a licensed UPI app like PhonePe) | Removes no charge, allows no fee, and takes 8 to 12 weeks |
| "Autopay price": a lower rent only for Autopay tenants | Reads as passing the UPI charge to link payers (N6) |
| Any charge named or sized like the new 0.4% UPI charge | That charge cannot reach the customer (N2) |
| A charge for Autopay itself | RBI does not allow charging the customer for the mandate (e-mandate rules, para 10(a); R11) |
| Any charge hidden from the tenant | Unlawful, and breaks trust (N5) |
| RentOk absorbing any cost | Ruled out (R11) |
| One ₹15,000 limit for everyone | Replaced: her approved limit is her own regular dues, for trust (R46) |
| Choosing due by due what Autopay covers (CRED lets users pick billers) | She picks between two options instead (R46) |
| A reject button on payment requests | She approves or pays manually (R47) |
| Waves or priority groups | Everyone is on from the start (R37) |
| A confirm step before regular debits | No extra input from the tenant (R36) |
| Managers pausing or stopping Autopay themselves | They ask; RentOk acts (R39) |
| Splitting dues into pieces of ₹2,000 or less | Splitting to dodge the 0.4% charge is not allowed (N1) |
| Taking dues above ₹15,000 with a PIN every time, under Option 2 | Parts under one mandate instead (R16). Option 1 does ask for the PIN, and says so at setup |
| Any day of the month as the Autopay day | The allowed days are her due day to the last grace day (R41) |
| Extending a mandate past the agreement end | Cashfree cannot extend a mandate [Cashfree]; renewal asks for a new one (R50) |
| Locking app features until Autopay is set up | Chase, never block (R21) |
| Taking late fines or prepaid recharges in a debit | Late fines are paid by link only; she tops up prepaid meters herself (R29, R30, R51) |

## Outside this map (handled separately, not product decisions)

- **Written questions to Cashfree**
  - Several debits on the same day or in one period for the same mandate (parts), and how retries and notices work for them.
  - Whether a large approval amount can be kept as the first real payment, and whether it avoids the 0.4% charge.
  - Whether a failed first debit cancels the mandate.
  - Sending dues within one debit to different bank accounts.
  - Whether failed attempts are billed.
  - How the merchant name is set.
  - What the standard flow does with a debit time inside NPCI's blocked hours.
  - Whether NPCI limits "as presented" mandates for rent.
- **Legal wording** for the agreement and the platform fee line, and a lawyer's view on the start-date rule.
- **A tax opinion** on RentOk's position, including how a GST-registered property's platform fee line is taxed.
- **Mirroring into Linear,** only after Sanchay says go.

## Why this holds together

One mandate per tenant, two plain options, one approval screen, and an approved limit she recognises from her own bill. That makes Autopay simple enough to switch on for everyone without blocking anyone:
- **The tenant** gets "never miss rent", pays nothing for Autopay itself, and stays in control of her day, pauses and cancellation.
- **The manager** gets a list to chase, a switch for exceptions, a request button that collects extra bills without reminders, and a way to ask RentOk for anything that stops money.
- **The owner** sees what link payments cost and decides how RentOk's charge is passed on.
- **RentOk** pays for none of it, and charges the same way whatever way the tenant pays.

The first day of every month is when rent moves, and every door leads to the same approval. Even with everything running, the low estimate is about 52,000, so each day's numbers are watched from the first day of the push.

---

## Appendix: facts checked on 17 Sep, and work already filed

**Cashfree documentation** (details and links in `19-cashfree-docs-answers.md`)
- **Plan types:** fixed-schedule plans are debited by Cashfree automatically. The merchant raises each debit on on-demand plans.
- **Changes and pauses:** plan changes and merchant pauses work only on fixed-schedule plans.
- **Limits:** the approved maximum caps each debit, and a debit above it needs a new mandate.
- **Expiry:** a mandate cannot be extended.
- **Standard debits:** Cashfree sends the notice and retries up to 3 times, an hour apart.
- **Controlled debits:** RentOk sends the notice, waits at least 25 hours, takes the exact notified amount, and does its own retries.
- **Scheduling:** a UPI debit can be scheduled from the next day (if raised before 9 pm) up to 14 days ahead.
- **Blocked hours:** NPCI allows debits only before 10:00, 13:00 to 17:00, or after 21:30.
- **Approval:** UPI approval can run on RentOk's own screen, and e-NACH takes 24 to 48 hours to approve.
- **Price list:** about ₹7.5 per mandate plus ₹15 per debit of ₹1,000 or more, plus GST.
- **Status updates:** a cancellation or pause in the UPI app reaches RentOk; a merchant pause does not.

**RBI e-mandate rules 2026**
- No PIN up to ₹15,000 per debit (para 8).
- A notice at least 24 hours before each debit, with the right to refuse any one debit (para 6).
- No charge to the customer for the mandate (para 10(a)).
- The first debit may be combined with setup (para 5(a)).

**Filed in eazyapp-tech/rentok-backend,** linked on epic #6846
- #6816 and #6861: Autopay routes that need no login.
- #6995: two debit engines can charge twice.
- #6996 and #6998: payout deductions are wrong.
- #6999: one empty month ends Autopay.
- #7000: dues with GST are collected short.
- #7002: a tenant who paid another way is still debited.
- #7003: the wrong amount is saved for each debit.
- #7004: the debit time is sent in 12-hour format.
- #7005: mandates stay live after move-out.
- #7006: the setup reminder skips anyone who ever tried.
- #6829 (debits on any day) is replaced by R41.

**Filed in eazypg-marketplace (web check-in):** #915, required Autopay blocks check-in.

**Supporting files in this folder**
- 02: Kamal's recording, both passes and the voice-over transcript, with CRED's full Autopay FAQ.
- 06 and 07: tenant, manager and owner walkthroughs.
- 10: legal notes.
- 11: systems map.
- 12: finance and operations.
- 13: covering costs and the rent change flow (written before R35 and R46; this map wins where they differ).
- 15: Kamal's plan, version 2.
- 16: growth numbers.
- 17: gap review.
- 18: the team discussion of 17 Sep night, and research on how other apps use Autopay.
- 19: Cashfree documentation answers.
