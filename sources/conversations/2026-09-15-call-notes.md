---
date: 2026-09-15
time: about 10:50 PM IST
source: Wispr Flow shared note "Auto Pay Setup Discussion", full transcript read (not truncated)
related: "[[2026-09-16-evening]]"
tags: [wispr, autopay]
---

# Auto Pay Setup Discussion (15 Sep, late night)

A screen walkthrough of the tenant payment page, the night before the 16 Sep payment discussion ("kal payment wali discussion hai"). Speaker 2 shares the screen and builds it. Speaker 1 (and a "Speaker 3" late on, possibly the same person) reviews. "Bhaiya" is the senior person who is not on the call. Speaker labels are guesses.

## How does the current setup flow work?
1. The payment page shows an Auto Pay card with benefits and a **Setup** button.
2. Tapping it shows the details: debited each month, when the first debit happens, "Make it automatic", "Change the date".
3. "Make it automatic" opens a calendar. Benefits sit below the calendar. Tenant picks a date.
4. Auto Pay is live. Today it covers **rent only**.
5. After setup, the card says Auto Pay takes this charge. The label should show the **property name, not "RentOk"**.
6. Auto Pay is being switched **on by default for everyone**.

## What is broken or missing on these screens?
- **Bug:** the orange benefit image on the payment page is covered, so it does not show.
- Only **bank account** showed as a method on one screen. Speaker 2 said UPI is built but that state is missing. (Same symptom as the 16 Sep review, where UPI did not show.)
- "Nothing to pay now" state: needs an option to pay **advance** right after. Speaker 2 noted it down.
- **Missing workflow (Speaker 2's words):** paying rent and setting up Auto Pay at the same time.

## What are the date and grace period rules?
- Calendar allows due date up to due date plus grace period. Later dates are disabled.
- Grace period is 7 days today and comes from the property's **late fine settings**.
- Example: due on the 1st, 7 day grace, tenant can pick 1st to 7th.
- **Open:** if a tenant picks a date after the due date, Speaker 2 said the extra amount would be charged pro rata from the cycle after next, then said "I am very confused about this". Not settled.
- **Decision:** tenants do not get "Change date" for now. The operator changes it (for example date of joining).

## What does setup cost, and what do we earn?
- Setup debit today: "about ₹50 or ₹30" in normal cases. If nothing is due, ₹2.
- Rent being due does **not** block setup. Tenant can pay rent separately and set up separately.
- Per "bhaiya": we pay ₹30 a quarter and can debit any number of times in those 3 months.
- "How much do we save or earn on Auto Pay?" Nobody knew. Needs asking.

## What is the new combined flow?
- Pay rent and set up Auto Pay in one go. The rent payment counts as the first Auto Pay payment. Reference: micro-drama story apps do exactly this.
- A small checkbox on the final payment (cart) screen, like a T&C tick: "Enable AutoPay, Save Money" or a reward line. Speaker 1 said off by default. A hyperlink on it opens the Auto Pay details screen.
- When ticked, the **Pay** button changes to **"Pay with AutoPay"**, skips the setup screen, and goes straight to payment.
- If the tenant did not enable Auto Pay earlier, show the tick again on the final page.
- In properties running a discount, the line becomes "Set up Auto Pay and get ₹100 off" or "get ₹50 cashback". Temporary.
- Speaker 2 worried about placement: the final screen would then show Auto Pay in three places. Settled on one small tick on the final page.
- **Open:** Speaker 2 not sure the backend can take rent and set up Auto Pay together. Will ask [[Nimit]].

## Opening the UPI app directly
- Ask: open the UPI app straight away (skip the Cashfree page), as story apps do.
- **Decision for now:** the Cashfree page opens. Direct UPI later.
- Asked which is used most, UPI or e-NACH. Answer leaned UPI, with a worry about high amounts.
- (On 16 Sep this moved on: direct UPI app handoff for payments under ₹15,000, from 1 Oct.)

## Cashback and discounts
- Someone (name sounds like "Jiya") had promised something for Auto Pay on a call, then went quiet.
- **RentOk will not give cashback.** It can only come from the owner or operator.
- After launch, ask operators and add a per property **extra discount** option in the app. The existing discount package can handle it.
- Why operators may agree now: UPI charges are now being passed on.
- Long term: like the early cashback on online payments; cashback stays below what we earn.
- Risk: operators may say "we asked for this a year ago, now you come with cashback".
- Speaker 1 to raise cashback and incentives in the 16 Sep payment discussion.

## Action items
1. Speaker 1: raise cashback and Auto Pay incentives in the 16 Sep payment discussion.
2. Speaker 3/2: fix the covered benefit image.
3. Speaker 3/2: confirm with Nimit that rent plus Auto Pay setup together is possible in the backend.
4. Speaker 3/2: add the "Enable AutoPay" checkbox; ticking it changes the button to "Pay with AutoPay".
5. Speaker 3/2: explore opening the UPI app directly.
6. Speaker 2: advance payment option on "Nothing to pay now".
7. Speaker 2: fix the missing UPI state.
8. Property name instead of "RentOk" on the card.

## Where this disagrees with 16 Sep
| Topic | 15 Sep (this call) | 16 Sep |
|---|---|---|
| Change date | Deliberately not given; operator changes it | Reviewer flagged it as missing |
| Grace period | 7 day grace is live, tied to late fine | "Late fine and grace do not seem live" |
| Gateway cost | ₹30 per quarter, unlimited debits | ₹15 per quarter (PayU, PhonePe) or ₹5 per debit (Cashfree) |
| Setup debit | ₹50 or ₹30, or ₹2 if nothing due | ₹1 (or ₹2) seen in the test |
| Default | Checkbox off by default | UPI should be the default method (different thing) |
| Cashback | To be raised on 16 Sep | "Rewards" raised on 16 Sep, never detailed; 0.4% extra charge for not using Auto Pay instead |
