# The 22 September implementation call, checked against the rulings

Sanchay walked a backend engineer through how Autopay should work end to end, on the evening of 22
September. It is the most recent statement of the design in his own words, five days after most of
the rulings it touches. The transcript is in the private repo,
`rentok-autopay-internal/meetings/2026-09-22-autopay-implementation-call.md`; timestamps below are
minutes into that recording.

Read 23 September, in full, against rulings R1 to R67, the feature map, and the payment page on
`eazypg-marketplace` origin/main (`components/PayPage/`).

## What it changes

### 1. The limit she approves is a ceiling RentOk sets above her fixed dues, not her dues

His example (09:16 to 11:40): rent ₹10,000 and food ₹2,000 are fixed, so ₹12,000 recurs. Electricity
is by consumption, ₹500 one month and ₹4,000 another. "Hum 15 ka set kar denge. 15 ka capture
karenge, ya 20 ka." Option 2 then takes whatever dues are open on her day, "12,000 nahi hoga, 15 bhi
ho sakta hai, 16 bhi". If the dues are above the ceiling, the debit is split (19:02 to 20:21).

**This contradicts two lines of ours.** R46 carries a design note that the limit "equals her regular
dues", and the feature map says "no round-number buffer". Both are Claude's, not Sanchay's: R46 says
"My design details are in 18-discussion-17sep-night.md", and "my" in the log is Claude's voice. His
own words, later, set a buffer. The rule for the ceiling is open; see the end of this file.

**Consequence for R67 and the R16 note.** Both say the mandate is approved "at her full amount". That
came from the same R46 note. They are correct on the part that matters, that each debit stops at
₹15,000, and need rewording once the ceiling rule is set.

### 2. The payment page's setup sheet carries two decisions the rulings retired on 17 September

`components/PayPage/` on origin/main was built on R9 of 11 September. Two of R9's clauses were
replaced six days later, and the page still carries both:

| R9 said (11 Sep) | Replaced by | Still on the page |
| --- | --- | --- |
| Rent only | R18: all monthly dues | `state.js:255`, `state.js:356`, `AutopayCard.jsx:197`, `:286` |
| Any day of the month, which becomes her rent date | R41: due day to due day plus grace; her due date does not move | `autopay.js:7`, `state.js:271`, `AutopayCard.jsx:43`, `:175` |

The call restates R41 in Sanchay's own words (46:12 to 49:30): her day may move within due date plus
grace, "kyunki management decide karegi na ki uska bill kab karta hai". A genuine salary-date change
is the manager's, by changing the rent cycle date on her profile.

**One benefit line is now untrue.** `AutopayCard.jsx:43` promises "No late fines" because "the day you
pick becomes your rent date". The reason is gone under R41, and the call says a failed debit past
grace takes a late fine (37:23). The page promises something the product will break on every failed
debit.

## New, and in no document of ours

- **The platform fee needs an invoice** (01:10 to 01:56). "Abhi tak koi bhi invoice nahi... invoice
  generation hoga iska." Our I7 says the fee prints as "Payment processing charges" on the property's
  receipt with no RentOk GST invoice. These are not the same thing, and the call is later.
- **Same fee for every tenant in a property, stored so it could differ per tenant later** (05:26 to
  05:58). "Backend extendable rakhna hai, but user wise platform fee in one property will be same."
- **At check-in, "pay and set up" is a checkbox** (07:08 to 09:03). Checked: her pending dues plus the
  ₹1 authorisation go in one approval. Unchecked: setup only. He suggested labelling it as an opt-in.
- **Dues packages, and one mandate per due date, are the direction** (21:11 to 23:38). Rent, food and
  electricity each become a package with its own allowed payment modes, and packages due on different
  days need separate mandates, because one mandate has one date. **Not for 1 October:** "abhi ke liye
  full dues ya only rent, but singular date." The backend is to be built so this can come later; to be
  discussed with Jatin and Nimit.
- **The pause window ends at the eviction date where there is one, otherwise the agreement end** (42:09
  to 44:20). R50 names only the agreement end. She gets a message when the pause starts and another
  when it resumes.
- **The Pay button** (35:05 to 39:14). Paying by another method before her day stays allowed. Wherever
  a surface blocks Pay while Autopay is due, it must unblock on cancellation and once retries are
  exhausted. He was not sure what is built today. The payment page does not block it; the other
  surfaces are not checked.
- **Settlement takes the platform fee out before paying the owner**, and one debit is recorded against
  every invoice it paid (39:14 to 41:18).

## Answers one of our open questions, pending his confirmation

**Open question 2** (no late fine while retries are running) was Claude's call under R41. On the call
Sanchay corrected the engineer when he tied late fines to the failure reason: "insufficient ko mat
likho. Just write it as: after grace period has passed and tenant has not paid, then late fine
applicable" (37:23 to 37:50). Read plainly, that is the ordinary grace rule with no exception for
retries. Not logged as a ruling until he confirms it.

## Two engineering facts the call's workflow runs into

- **The daily job at 12:00 sits inside NPCI's blocked window of 10:00 to 13:00** (14:17 to 15:46). The
  job can pick up tomorrow's debits and send their notices at noon. The debits themselves must be
  presented outside 10:00 to 13:00 and 17:00 to 21:30.
- **Rechecking her dues before the debit has to happen before the notice** (26:37 to 29:02). The call
  says a cash payment or an advance adjustment made after the bill lowers the debit to what is left.
  Cashfree fixes the amount at the notice, at least 24 hours ahead. So the recheck runs before the
  notice, and a payment made inside those 24 hours means cancelling that debit and notifying again,
  not changing it.

## Agrees with what we already have

Platform fee on every payment mode and never exclusive to Autopay (02:42, R15, R64). Two options with
one date (R46). Parts a set gap apart (R67). A heads-up two days before and the bank's notice the day
before (R36). Webhooks for mandate and payment status, with a job that asks Cashfree after 24 hours
when a webhook is missing. A failure reason saved and sent to both tenant and manager. Retries capped,
with bounce charges named as the cost. Cancellation takes her out of the next run.

## The one thing still open for Sanchay

**The rule for the ceiling.** Recommended: her fixed monthly dues plus ₹2,000, rounded up to the next
₹5,000, and never above ₹15,000. His own example lands on ₹15,000 (₹12,000 plus ₹2,000 is ₹14,000,
rounded up). A ₹6,000 tenant approves ₹10,000, not ₹15,000, which is the difference between a number
she recognises and one that frightens her off. Anything above the ceiling on her day is split into
parts of up to the ceiling, two minutes apart (R67), so the ceiling never needs approving again. It
stops at ₹15,000 because any single debit above that asks for her PIN, so a higher ceiling buys
nothing.

Checked against rulings R1 to R67.
