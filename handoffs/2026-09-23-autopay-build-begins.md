# Handoff: the ₹15,000 tail, two rulings, and the first build on the payment page (23 Sep 2026)

Sessions `0e35cba0-3058-47ee-8b79-45518c156d94`, `e561c4b0-737d-4ece-978e-fe271ccb98e4` and
`690537f1-75e5-41c8-9340-5f717381ef55`, continuing
`18944ffa-833a-4cff-9dd9-7ddf336bc380`.
The earlier record from this run is `2026-09-22-all-five-surfaces.md`.

## What I set out to do

Three things, in the order Sanchay asked. First, check what had been missed on rent above ₹15,000
and against Kamal's two HTML files. Second, read the 22 September implementation call before
building anything. Third, start building Autopay: the setup screen first.

## What changed

**Rulings.**
- **R67:** rent above ₹15,000 goes in several debits a set gap apart, two minutes by default, the
  gap being a setting. It carries one consequence marked as Claude's reading: the legal note assessed
  the split at 24 to 48 hours apart, so the interval now goes into the Cashfree question too.
- **R68:** the ceiling she approves is her fixed monthly dues plus ₹2,000, rounded up to the next
  ₹5,000, never above ₹15,000. Every number in it, and R67's gap, is a backend setting in one
  `internal_config` row. The backend alone computes the ceiling, because it is the figure sent to
  Cashfree.
- **R16's note and R67's first point are marked replaced, not rewritten.** Both said the mandate is
  approved "at her full amount". That came from Claude's design note under R46 ("limit equals her
  regular dues, no buffer"). Sanchay's own words on the 22 Sep call set a buffer.

**Open questions.** 30 added: Kamal's prototype pauses directly, R48 makes pause a request the
property approves. One line of question 20 withdrawn: the split flow's "no refunds" is a decision
the prototype states, not an omission. Question 24 reworded: e-NACH is a cheaper rail for high rent,
not the only way to collect it. Cashfree question 11 added: AFA and 2FA are not enabled on our
account, which blocks every debit above ₹15,000.

**Research.** `research/2026-09-22-implementation-call-check.md` checks the call against R1 to R67.
The transcript is in the private repo, `meetings/2026-09-22-autopay-implementation-call.md`.

**Kamal's prototype** is in the private repo on branch `proto/payment-page-autopay`, unchanged first,
then with the Platform fee on the bill and two "free" promises narrowed.

**The build.** `eazypg-marketplace`, branch `feat/autopay-setup-screen` (`1ddb3749`, then `47007e70`; pushed, no PR).
The setup sheet now asks what autopay pays, reads the ceiling and window from the payload, keeps her
day inside her grace days, and no longer promises what R41 took away. The branch carries its own
handoff, `docs/handoffs/2026-09-23-autopay-setup-screen.md`.

**Issues.** Comments on `rentok-backend#7078` (the gap and the AFA precondition, then R67) and
`rentok-backend#6825` (the payload fields R41, R46 and R68 need, `next_debit.due_ids`, and the
window using the smaller of the two graces).

**Cashfree's server-to-server flow, added late on 23 Sep.** Cashfree calls it "Seamless", against
"Hosted checkout". `research/cashfree-s2s-seamless.md` maps its six steps against our code. We
already create mandates and take debits seamlessly. The approval still goes through Cashfree's hosted
page, and **the pre-debit notice call (`notify-mandate`) is called nowhere**, which Option 2 cannot
run without. Added to `rentok-backend#7078`. UPI Collect is being withdrawn: intent on mobile, QR on
desktop.

**Reviewing the sheet on the team's own property, late on 23 Sep.** Sanchay asked to see it on the
team's own account rather than a real tenant's. The property to review against is **Ishika**, the
account's first property (the one the manager app shows as 1220096612A), which takes both online and
cash. Its tenants have live links, and one of them has ₹12,000 rent due on the 30th. That single case
checks two things: his own example (₹12,000 of fixed dues gets a ₹15,000 ceiling) and a window that
crosses the month end (the 30th, 31st and 1st to 6th open). A ₹50,000 tenant there shows the PIN
line under Rent only. Fresh link codes come from Metabase at review time; none are written here.

Two things came out of that review. **A copy bug of mine:** the note under the day grid said "The
30th is the last day in shorter months", which is garbled and false for February. It now says "In a
month with no 30th, it goes on the last day" (`47007e70` on the branch). And **a test property,
Candidate Booking Test, was cash-only**, so the page offered it no autopay, which is correct. Sanchay
switched its online payments on.

The local review server runs from the worktree through `eazypg-marketplace/.claude/launch.json`
(name `pay-autopay`, port 3012, `http://pay.localhost:3012`). That file is local and not committed.

## Decisions, with reasons

- **The setup screen was built on /p2, not in Kamal's HTML.** Every number on it was ruled, so there
  was nothing left to explore in a prototype. /p2 already had a preview harness, and it is where
  every live link moves on 25 September.
- **"Pay all" still leaves out only the rent row.** That is correct for every mandate that exists
  today. What Option 2 takes is the backend's to send; a page that guesses charges twice or leaves a
  bill unpaid.
- **No offer without a window and a ceiling from the backend.** An offer that cannot state its terms
  is not made.

## What I checked, and how

- `npm run paypage:test`: 103 of 103, up from 101.
- Rendered on the preview harness at 375 and 1440 against two live links, a ₹6,000 tenant (ceiling
  ₹10,000) and an ₹18,000 tenant (ceiling ₹15,000, PIN line under Rent only). No sideways scroll.
- Code read on `eazypg-marketplace` origin/main `0f016992` and `rentok-backend` origin/master.
- **Not verified:** the pause and Pay-button behaviour on the tenant app and manager surfaces; the
  staged "circle the day" chip in the one-decision sheet, which renders empty mid-animation and is
  unchanged by this work.

## Patterns found, three times over

- **A finding filed only in a research file does not exist.** Three of the four things wrong around
  the ₹15,000 split were found on 22 Sep and never carried into a ruling, question or ticket.
- **Kamal's payment page prototype renders everything in JavaScript**, so a text extraction returns
  an empty page. Every earlier check of it read the launch room's description instead.
- **/p2 was built on R9 of 11 Sep.** Two of R9's clauses were replaced six days later and the page
  still carried both. Sweep the rest of the page for R9 before calling it current.

## What is now waiting

- **On Sanchay:** whether Option 2's first debit takes arrears or only the current month (Claude's
  pick: current month only); whether open question 2 is answered by his words on the call; open
  question 30; eyeballing the sheet in the browser pane, then whether to open the PR.
- **On Kamal:** whether the Cashfree list went out on 21 Sep; AFA and 2FA on our account; the
  interval between parts, asked in writing.
- **On the backend:** the #6825 fields. Until they ship, no real tenant sees an offer.
- **Dated:** R55 moves every live payment link to the new page by 25 Sep.

## The next step

Build the seamless approval into the setup sheet (UPI app buttons on mobile, QR on desktop, behind
`CAN_SET_UP`), which was recommended and is waiting on Sanchay's go. Alongside it: his ruling on
arrears, the setup-screen PR, and the Cashfree note to Kamal with AFA and 2FA, the interval, and the
corrected ₹6.6 crore sizing.
