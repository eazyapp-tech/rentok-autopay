---
title: Auto Pay discussions, 15 to 16 Sep 2026, in order
sources:
  - "[[2026-09-15-wispr-autopay-setup]] (Wispr Flow, full transcript)"
  - "[[2026-09-16-evening]] (NeoSapien, 3 recordings, full transcripts)"
tags: [autopay, timeline]
---

# Auto Pay discussions, in the order they happened

Read top to bottom. Where a later conversation changes an earlier point, the later one is marked **Changed later** or **Still conflicting**. The last two sections list where things stand now.

Speaker names in both tools are guesses. About 6 minutes of the 16 Sep recordings were not transcribed (end of each recording), so anything said there is missing.

---

## 15 Sep, about 10:50 PM: screen walkthrough of the payment page (Wispr Flow)

Screen share of the tenant payment page. One person built it and walked through it (Speaker 2); one or two reviewed. "Bhaiya", the senior person, was not on the call. The group called the next day's meeting "the payment discussion".

### How setup works today (as shown)
1. Payment page shows an Auto Pay card with benefits and a **Setup** button.
2. Tapping it shows: debited every month, when the first debit happens, "Make it automatic", "Change the date".
3. "Make it automatic" opens a calendar with benefits below it. Tenant picks a date.
4. Auto Pay is live. Rent only for now.
5. Auto Pay is being turned **on by default for everyone**.

### Problems seen
- Orange benefits image on the payment page is covered, so it does not show.
- One screen showed only **bank account** as a method. Speaker 2: UPI is built, but that state is missing.
- After setup the card should show the **property name, not "RentOk"**.
- "Nothing to pay now" screen needs an option to **pay advance** right after.
- Speaker 2: the **pay rent and set up Auto Pay together** workflow is missing.

### Dates and grace period
- Calendar allows from due date to the end of the grace period. Later dates are greyed out.
- Grace period is 7 days, taken from the property's **late fine settings**. Speaker 2 says this is live.
- **Decided:** no "Change date" for tenants for now. The operator changes it.
- **Open:** if a tenant picks a date after the due date, Speaker 2 floated charging the extra pro rata from the cycle after next, then said "I am very confused". Not settled.

### Money
- Setup debit: "about ₹50 or ₹30" normally, ₹2 if nothing is due.
- Rent being due does not block setup. Tenant can pay rent and set up separately.
- Per bhaiya: ₹30 a quarter, any number of debits in those 3 months.
- How much RentOk earns or saves per Auto Pay: nobody knew.

### New combined flow (proposed)
- Rent payment counts as the first Auto Pay payment (like micro-drama apps).
- Small tick on the final payment screen, like a T&C tick: "Enable AutoPay, Save Money" or a reward line. Off by default. A link on it opens the Auto Pay details.
- Tick on: button changes to **"Pay with AutoPay"**, skips the setup screen, goes straight to payment.
- If the tenant did not enable it earlier, show the tick again on the final screen.
- In properties with a discount: "Set up Auto Pay and get ₹100 off" or "get ₹50 cashback". Temporary.
- Worry: Auto Pay would show in three places on one screen. Settled on one small tick on the final page.
- **Open:** can the backend take rent and set up Auto Pay in one go? Ask Nimit.

### Opening the UPI app directly
- Ask: skip the Cashfree page and open the UPI app, like story apps.
- **Decided:** Cashfree page for now, direct UPI later.
- Which is used most, UPI or e-NACH? Leaned UPI, with a worry about large amounts.

### Cashback
- Someone (sounds like "Jiya") had promised something for Auto Pay on a call, then went quiet.
- **Decided:** RentOk does not fund cashback. Only owners or operators can.
- After launch: ask operators, add a per property **extra discount** option. The existing discount package can handle it.
- Operators may agree now because UPI charges are being passed to them. Risk: "we asked for this a year ago".
- Long term: like early cashback on online payments; cashback stays below what we earn.
- To be raised in the 16 Sep payment discussion.

### Action items from 15 Sep
1. Raise cashback and incentives on 16 Sep.
2. Fix covered benefits image.
3. Ask Nimit: rent plus Auto Pay setup together.
4. Add "Enable AutoPay" tick; button becomes "Pay with AutoPay".
5. Explore opening the UPI app directly.
6. Advance payment option on "Nothing to pay now".
7. Fix missing UPI state.
8. Property name instead of "RentOk" on the card.

---

## 16 Sep, 9:00 to 9:10 PM: Auto Pay rollout plan (NeoSapien)

Sanchay with a senior voice, probably Srijan.

### Goal
- About 1.5 lakh tenants pay rent through RentOk. Move **70,000 to 75,000** to Auto Pay, e-NACH or a virtual account by **1 October**.
- IDFC approval mentioned at the start, next to virtual account number.
- Payment link feature: done.

### Where tenants are pushed to set it up
- Tenant app: right after sign-up, and first thing on app open for anyone without it.
- Check-in: Auto Pay is a mandatory step.
- WhatsApp: a separate message after the rent agreement message, with a button and steps.
- Tenants not on Auto Pay pay **0.4% of rent plus GST** extra each month.
- Tenants must be able to **pause and delete** their mandate, or they will not trust it.
- "Rewards side" was raised, then not discussed. **Changed later / still open:** the 15 Sep cashback question does not appear in the recordings. A charge for not using Auto Pay appears instead.

### Rent above ₹15,000
- Split the debit: 3 x 5,000 or 2 x 10,000.

### Gateway cost
- Cashfree: about ₹5 per debit. PayU and PhonePe: about ₹15 per quarter, unlimited debits.
- Which is cheaper depends on how long the tenant stays and how many debits a month. Electricity is a separate debit. Today only rent is on Auto Pay; can extend to everything.
- **Still conflicting** with 15 Sep's ₹30 a quarter.

### Check-in flow, the blocker
- A combined check-in is live for Millennial Living. A newer version (Harsh's work) is still waiting for code review.
- Senior voice: "no time" is why Auto Pay took two years and BBPS three. Will speak to Nimit and Jatin.
- **Decided:** park the combined check-in. Build a new **web check-in** on the revamped payment page (electricity already there), with login and Auto Pay. Same backend, new front end. Sanchay checks the layers with Nimit.

### Owners
- Manager app: Auto Pay settings **on by default for all properties** (matches 15 Sep "on for everyone").
- Property settings get platform charge and gateway charge options.
- Bottom sheet to every owner: charges start **15 October** ("government decision"), then asks them to act.
- Service agreement for payment cases added to owner T&C, as a tick box because people will not read it.

### Tenants, legal
- Tenant T&C at setup covers bounce charges and disputes.
- Rent agreement becomes an annexure, used to fight chargebacks.

### Manager app
- Show per tenant whether Auto Pay is live. Sanchay: settings and status colour **done 17 Sep**.
- **Bug:** on the senior person's own property, payments were not going through.
- Sending a link: Auto Pay only goes inside the check-in link (4 steps: renting terms, rental agreement, Auto Pay). A bulk "Auto Pay reminders" button exists. Single tenant send: not confirmed.
- A small amount (₹2) is debited at setup. "Paid by tenant / paid by owner" options are visible.
- An owner refused something and it was stopped. Unclear what.

---

## 16 Sep, 9:11 to 9:24 PM: live test of Auto Pay on a phone (NeoSapien)

Several people. The reviewer turned Auto Pay on for his own property, added himself as a tenant, opened the tenant profile and shared the check-in link.

### Problems found
- **No separate Auto Pay link or button.** Only a bulk option is visible; single sends go inside the check-in link. Reviewer: "it will not get adopted", a jugaad (workaround), and he had asked for this before. Sanchay apologised.
- A tenant who is already verified is **not taken straight to the Auto Pay step**; he had to click through the earlier steps.
- Too much empty space and too much text. PAN step confused people. Screen to be redesigned like the pay.rentok.com page.
- **A setting does not save.** "No QA was done."
- **No option to change the debit date.** **Still conflicting:** 15 Sep deliberately left this out for tenants.
- **Late fine and grace period do not seem live.** Features were cut in the rush to launch. **Still conflicting:** 15 Sep said the 7 day grace is live.
- **UPI option did not appear**, probably because rent plus a ₹50 charge crossed ₹15,000. Same symptom as 15 Sep's missing UPI state.
- Point repeated: above ₹15,000, do not force net banking if UPI can do several debits.
- UPI should be the default method.
- Some UPI apps allow up to ₹1 lakh; add that to settings.
- ₹26 charge seen in the test. ₹1 debited at setup, which seems to be reversed.
- A setup fee is shown. Unclear if the Auto Pay fee is one time or monthly. Owner must set the fee and choose who pays it. "Need to sit on this."
- Past case: a tenant hit with repeated ₹200 bounce and debit charges.
- Asked whether debit alerts go out: notifications are not happening.
- Cashless deposit still shows in one or two places.
- Process: "don't ship like this in future". Someone "waiting for the next crisis" for 15 days to a month.

### Decided
- Under ₹15,000: skip the extra screen and **open the UPI app directly** (PhonePe, Paytm), like micro-drama apps. Live from **1 October**. **Changed later:** 15 Sep had said Cashfree page for now.

### Side topic: bot for stores
- A store (Allahabad mentioned) wants a full cart on the bot and its own website; coverage could reach all of Gurgaon.
- Stores hold cash. Bot tried at 2 or 3 stores, running at one. A walk-in issue to fix.
- In-store marketing: printed carry bags, stickers, flyers, pamphlets.

---

## 16 Sep, 9:24 to 9:29 PM: with Diwakar (NeoSapien)

- Bot: ₹25,000 a month for adoption, heavy discounts on bot orders. Works in any category. Only worth building if **payments and order flow** both work.
- **No message goes to tenants before a debit.** The 24 hour notice is missing. Nobody is sure whether Cashfree sends one. Risk: a tenant reports the merchant.
- Mandate is on demand: one authentication, then several debits, even next day. ₹20,000 rent can be two ₹10,000 debits. (Confirms the split idea from 9:00.)
- A payment is found in our system only when there is a transaction ID.
- Sanchay to share an ID and password for a login, using that person's phone number.
- Founder's Office JD is live on Wellfound.
- December transactions being checked; some show a "UGR" number (probably UTR).

---

## Where things stand now

### Decided (latest version wins)
| Topic | Decision | Date |
|---|---|---|
| Target | 70,000 to 75,000 tenants on Auto Pay, e-NACH or virtual account by 1 Oct | 16 Sep |
| Default | Auto Pay on by default for all properties | 15 Sep, confirmed 16 Sep |
| Where it is pushed | Sign-up, app open, mandatory in check-in, WhatsApp | 16 Sep |
| Nudge | 0.4% plus GST extra for tenants not on Auto Pay | 16 Sep |
| Under ₹15,000 | Open UPI app directly, from 1 Oct (replaces "Cashfree page for now") | 15 Sep, changed 16 Sep |
| Above ₹15,000 | Split into smaller debits on the same mandate | 16 Sep |
| Date range | Due date to end of grace period only | 15 Sep |
| Cashback | Not funded by RentOk; owner or operator discount only | 15 Sep |
| Combined check-in | Parked; build web check-in with Auto Pay on the payment page | 16 Sep |
| Owners | Bottom sheet on charges from 15 Oct, service agreement tick in T&C | 16 Sep |
| Tenants | T&C on bounce and disputes; rent agreement as annexure | 16 Sep |

### Still conflicting (need one answer)
| Topic | 15 Sep | 16 Sep |
|---|---|---|
| Change date for tenants | Left out on purpose | Flagged as missing |
| Grace period | Live, 7 days, from late fine | "Does not seem live" |
| Gateway cost | ₹30 a quarter | ₹15 a quarter or ₹5 per debit |
| Setup debit | ₹50 or ₹30, or ₹2 | ₹1 or ₹2 seen |
| Incentive | Operator cashback, to be raised 16 Sep | Not discussed in recordings; 0.4% extra charge instead |

### Still open
1. Can rent payment and Auto Pay setup happen in one go? (Nimit, from 15 Sep)
2. Date after due date: pro rata or not? (15 Sep)
3. Auto Pay fee: one time or monthly; who pays; owner sets it. (16 Sep)
4. How much RentOk earns per Auto Pay. (15 Sep)
5. Is a 24 hour pre-debit notice sent at all? (16 Sep)
6. Single tenant Auto Pay send: exists or not? (16 Sep)
7. What the rewards side looks like. (15 and 16 Sep)

### Work list, merged
| # | Item | First raised |
|---|---|---|
| 1 | Separate Auto Pay link and button, single and bulk | 16 Sep (he says asked earlier too) |
| 2 | Verified tenant lands straight on the Auto Pay step | 16 Sep |
| 3 | Pay rent and set up Auto Pay together; "Enable AutoPay" tick; "Pay with AutoPay" button | 15 Sep |
| 4 | UPI option missing (state missing / ₹15,000 cap) | 15 Sep, seen again 16 Sep |
| 5 | Direct UPI app handoff under ₹15,000, 1 Oct | 15 Sep idea, decided 16 Sep |
| 6 | Split debits above ₹15,000; no forced net banking | 16 Sep |
| 7 | UPI as default method; ₹1 lakh limit in settings | 16 Sep |
| 8 | Setting not saving; full QA pass | 16 Sep |
| 9 | Covered benefits image | 15 Sep |
| 10 | Property name instead of "RentOk" on the card | 15 Sep |
| 11 | Advance payment on "Nothing to pay now" | 15 Sep |
| 12 | Screen redesign: space, text, PAN step | 16 Sep |
| 13 | Late fine and grace period working in Auto Pay | 15 Sep said live, 16 Sep said not |
| 14 | Change date: decide, then build or not | 15 Sep vs 16 Sep |
| 15 | Fee rules and owner fee setting | 16 Sep |
| 16 | Pre-debit notice 24 hours before each debit | 16 Sep |
| 17 | Pause and delete mandate for tenants | 16 Sep |
| 18 | Remove cashless deposit leftovers | 16 Sep |
| 19 | Manager app Auto Pay status per tenant (promised 17 Sep) | 16 Sep |
| 20 | Payments failing on the senior person's property | 16 Sep |
| 21 | Web check-in with Auto Pay; unblock with Nimit and Jatin | 16 Sep |
| 22 | Owner bottom sheet and T&C for 15 Oct charges | 16 Sep |
| 23 | Tenant T&C and rent agreement annexure | 16 Sep |
| 24 | Push points: sign-up, app open, check-in, WhatsApp | 16 Sep |
| 25 | Per property operator discount option after launch | 15 Sep |
| 26 | Bot: payments and order flow first | 16 Sep |
