# Where the work stands

Update this at the end of every session. Newest entry on top.

## Now

- **Feature map:** version 4 (PR #5, 18 Sep), in `map/feature-map.md`.
- **Rulings:** R1 to R77, in `decisions/decision-log.md`. R63 and R16 both carry corrections, marked, dated and attributed.
- **Code check, 18 Sep:** every older issue is still true, 26 new issues filed (3 P0). 473 of 781 current Autopay tenants have no debit queued. See `research/code-check-18sep.md`; epic #6846 lists what to fix before 30 Sep.
- **Waiting on Sanchay:** which brand whitelabelled tenants see, link life and push list, testing with real money, the stop-all switch (open questions 6 to 10), #7055 (what Autopay off means for running mandates), five points marked "(proposed)" in the map, and **open questions 10 to 30 (28 and 29 now answered as R65 and R66), added 22 Sep from the manager tickets, from Kamal's PRD and prototype, from the tenant app, from the 23-section check of his launch room, and from re-checking his three earlier documents**. All listed in `decisions/open-questions.md`.
- **Waiting on Cashfree:** Kamal's launch room says his list of fifteen went to Cashfree on **21 Sep**, three of them marked blocking. Our ten are in `decisions/open-questions.md` and `drafts/cashfree-email.md` still says draft. **Reconcile the two lists and correct whichever record is wrong.**
- **Waiting on advisers:** the agreement wording and the platform fee line (a payments lawyer), and RentOk's tax position.
- **Cashfree email:** our copy is still marked draft. Kamal's launch room says a fifteen-item list was sent on 21 Sep. See `research/kamal-launch-room-check.md`, item 1.
- **Build tickets:** 36 filed 18 Sep under epic #6846, listed in `map/build-tickets.md`, with cut ranks (R62).
- **Not done yet:** engineering tickets from the map, and linking this repo from epic #6846. Linear mirroring is done: project Autopay, 7 parents and 57 sub-issues, 21 Sep.
- **Surface documents: all five are written** (22 Sep): `surfaces/manager-app.md`, `surfaces/payment-page.md`, `surfaces/tenant-app.md`, `surfaces/web-check-in.md` and `surfaces/manager-web.md`.
- **Access:** public until Kamal has GitHub access, then private. Until then Kamal sends his work to Sanchay, who adds it here.
- **Next step:** take the corrected UPI charge sizing to Srijan and Kamal (open question 27) before the provider terms are settled. Then the dated work: the payment page link move by 25 Sep (R55), and the six web check-in fixes before D4 turns Autopay on by default.
- **Working now:** nobody. Put your name here when you start.

## Log

### 23 Sep 2026 (the workflow and UI call, read and checked), Sanchay with Claude Code

- Read the full recording of the afternoon's call with Kamal and the tech team (NeoSapien `a3adbea1`, about 133 minutes, not the 78 the summary says) in `research/2026-09-23-workflow-and-ui-call-check.md`; cleaned transcript in the private repo.
- **Agreed in the room:** launch first with the Autopay already built, on the payment page; an unticked "Set up autopay" checkbox with "Know more"; a two-step flow (benefits and option, then day and a preview of the next debits); Cashfree's hosted page for launch, our own screen later; confirmation, then a manage screen with the next three debits and change date, pause, cancel; pause is RentOk's own, to a date she picks, from the next cycle; the Pay button never blocked. Method: Sanchay builds the UI mocks, the room sits on them at 8:30 p.m., the backend contract follows.
- **Disagrees with the record in six places**, tabled in the file. Two became open questions: 31, the ceiling at launch (flat ₹15,000 said in the room against R68), and 32, launching on today's charge settings against R64. Open question 30 (who pauses) now carries the call's lean.
- **Confirms two known defects in the engineers' own words:** Cashfree cancellations are missed (#7124) and the notice before a debit is never sent (#7078).
- Two remarks in the call were about the setup sheet built earlier: "looks completely broken" and "the bottom sheet is completely full". Both support the two-step flow.

### 23 Sep 2026 (R67, and the prototype read properly), Sanchay with Claude Code

- **R67:** rent above ₹15,000 is collected as several debits **two minutes apart by default**, the gap being a setting rather than a hardcoded wait. The mandate is approved at her full amount; only each debit stops at ₹15,000. It rests on two things not in hand: Cashfree accepting same-day parts, and AFA/2FA being enabled on our account.
- The ruling carries one consequence marked as Claude's reading: `research/legal.md`'s addendum assessed this split at **24 to 48 hours** between parts and worried about bank velocity checks. Two minutes is a sharper version of the same pattern, so the interval now goes into the written question to Cashfree, not just the fact of splitting.

- Sanchay: rent above ₹15,000 is handled by taking the mandate at the full amount and running several debits a short gap apart, the gap being a variable. He asked how that had been missed, and what else had.
- **It was not missed as a design.** R16 rules it, the feature map carries it, diagram and ticket B1 (#7078) build it, and Kamal's payment page prototype ships it in code (`DEBIT_CAP = 15000`, a `debitParts()` function, and tenant copy reading "taken as ₹15,000 + ₹5,000, minutes apart"). **Four things around it were wrong or missing:**
  1. **R16's own text still said the mandate carries a "₹15,000 limit".** R46 replaced that the same evening: the limit equals her full regular dues, and it is each debit that stops at ₹15,000. R16 is now annotated, not rewritten. Anyone building from R16 alone would have built the wrong mandate.
  2. **The gap between parts was in no document of ours.** The launch room says five minutes, Sanchay says two and calls it a variable. Now in the feature map and on #7078, as a setting rather than a hardcoded wait.
  3. **AFA and 2FA are not enabled on RentOk's Cashfree account,** so nothing above ₹15,000 reaches Autopay there today. Found on 22 Sep and written into `research/kamal-launch-room-check.md`, then left there: no open question, no Cashfree question, no ticket. Now Cashfree question 11, marked blocking, and on #7078.
  4. **Calling open question 24 "half the prize" was wrong**, and is corrected in the log above. It read as though high rent were not automated. It is. That question picks the cheaper rail for the segment, it does not unblock it.
- **The pattern worth keeping:** a finding written once into a research file and never carried into an open question, a ticket or the map does not exist. Three of the four above are that same failure, not four separate ones.
- One divergence surfaced that had never been named: **our map defaults the parts to one a day** pending Cashfree, while Kamal's launch room and prototype both design for the same day, minutes apart. Both positions are now in the map with what each depends on.

- **Then the second question: what else had been missed against the two HTML files.** The answer starts with how they were read. **Kamal's payment page prototype renders its entire content in JavaScript**: the page's own HTML is one empty `<div id="app">`, so stripping the tags returns nothing at all. Every earlier check of it had gone by the launch room's description of the prototype rather than by the prototype. Reading the script itself, 16 screens and their copy, turned up three things.
  1. **A fifth conflict between his prototype and a ruling, now open question 30.** R48 makes a pause a **request** the property approves, with silence counting as yes after 48 hours (R50). His mandate screen gives the tenant a plain "Pause one month" button with no request and no approval. Open questions 19 to 22 had caught four conflicts; this is the fifth, and it was invisible because it lives in a screen, not in the PRD text.
  2. **Underneath it, a rail question.** The same screen tells her "you can also pause or stop this from your own UPI app", and our own reading of Cashfree's docs (I10) says pause is **not supported on on-demand mandates**, which is the option most tenants are meant to pick. The screen may be promising something the rail does not do.
  3. **One line of open question 20 was wrong and is withdrawn.** It said the sub-₹2,000 split flow "carries no refund path if she stops halfway". The prototype decides that on purpose and tells the tenant so, and the launch room's task line reads "no refunds, balance stays due". A decision recorded as an omission. The rest of question 20 stands.
- **Checked and found already correct**, so they are not misses: the 15-day renewal ask, e-NACH's 24 to 48 hour activation and today's dues being paid separately, the payee-name line, the forwardable QR, the next three debit dates, the "no PIN, no confirmation step" rule, the virtual account's do-not-pay-by-UPI warning, and partial payments.

### 22 Sep 2026 (R66, the eligibility control), Sanchay with Claude Code
- **R66: the "Eligible for tenants joined since" control is removed.** It is on both manager surfaces, saves a date, writes an activity log line, and no Autopay path reads it. Filed as rentok-backend#7162. Open question 29 closed.
- Checked every consumer before recording the removal: it is in the manager app as well as manager web, and **the app's copy-to-properties action copies the date to every property in the copy**, so one wrong date spreads.
- Order matters and is in the ruling: **the backend stops accepting the field first**, which ends both writers and the bulk copy in one place; web drops the control with D4; the app drops it in the release after 1 Oct.
- Nine properties have a date saved, eight with Autopay on, one dated 2007. Null them; drop the column after 1 Oct.
- **D4 needs two edits from tonight's rulings:** its settings screen lists three items and does not mention this control, and its fee range still reads ₹58 to ₹118, which R65 replaced.

### 22 Sep 2026 (R65, the fee ladder), Sanchay with Claude Code
- **R65: the Platform fee ladder runs ₹58 to ₹399, suggested from the property's average rent, and both ends are suggestions.** Management may set any amount above or below them. This replaces the hard ₹58 to ₹118 band in R53. Open question 28 is closed.
- Two consequences written into the ruling: below ₹58 a property is absorbing part of RentOk's ₹49 plus GST, which costs RentOk nothing and turns absorbing into a dial rather than a switch; and above ₹399 the only requirement is R13's notice rule, which applies to every change anyway, so R53's "it is really a rent rise" escalation has nothing left to trigger on.
- What keeps the fee lawful is unchanged and was never the band: same on every method including cash, never computed from the payment, and nothing anywhere prices UPI.

### 22 Sep 2026 (session close, R64 filed), Sanchay with Claude Code
- **R64 added to `decisions/decision-log.md`** on Sanchay's instruction: one tenant-facing charge, the Platform fee, borne by the tenant by default with management free to absorb it; the Autopay setup and monthly fees deleted; and the amount suggested from the property's average rent, with ₹58 as a placeholder rather than the price.
- It carries one paragraph marked as Claude's reasoning rather than his words: why R64 does not reopen R11, which turns on the Platform fee being the same on cash and therefore not an Autopay charge.
- Swept the five surface documents and STATUS: they said R64 was missing and were stamped "R1 to R63, R64 pending". Both now read R1 to R64. The handoffs were left as written, because they are a record of what was true on the day.

### 22 Sep 2026 (session close), Sanchay with Claude Code
- **All five surface documents are written**, 1,654 lines: manager app, payment page, tenant app, web check-in, manager web. Handoff in `handoffs/2026-09-22-all-five-surfaces.md`.
- Close-out check across the five found two drifts and fixed both: three documents were missing the ruling range they were checked against, and the manager app document had lost its record of R64 in an edit earlier the same evening. All five now carry both.

### 22 Sep 2026 (late, fifth pass), Sanchay with Claude Code
- Wrote `surfaces/manager-web.md`, the fifth and last surface. **All five surfaces are now written.**
- **The one rule: manager web is the only manager surface that can ship before 1 Oct, and it holds the least Autopay of any of them.** Two files in the whole repository. It is behind the manager app, which at least has a per-tenant row and the per-tenant grace.
- The old charge model is still on screen there and still being sold to owners: a setup fee, a monthly fee, two "who bears it" dropdowns with **RentOk as the unset default**, and an illustrated modal with a struck-out price. R11, R35 and R61 deleted all of it, and the same fields are what refuse setup under #7054.
- An Autopay debit shows as "RentOk Bank Transfer" in the passbook, so no screen on web can tell it from a link payment. The display exists; the data does not (#6835).
- Found a control nobody has ruled on: "Eligible for tenants joined since". It saves a date and writes an activity log line, and **no Autopay path reads it.** Open question 29.
- Corrected a row in `surfaces/manager-app.md`: manager web does have a passbook; what it lacks is the per-tenant late fine and grace.

### 22 Sep 2026 (late, fourth pass), Sanchay with Claude Code
- Wrote `surfaces/web-check-in.md`, the fourth surface, pointing at A3 with A1, A4, A9, D4, D5, E5 and S1.
- **The one rule for this surface: it is the only place a tenant can be blocked, and today it blocks.** The forward gate passes only on an active mandate, against R21.
- **The finding that sets the ship order:** the Autopay step reaches 0.51% of properties today (438 of 85,591), so six open defects reach almost nobody. D4's default-on takes them to every check-in at once, and August ran at 1,774 new tenants a day. The six fixes are D4's precondition, not parallel work.
- Check-in is also the only Autopay door that needs no app release and no link move, so it is the shortest path from a fix to a live tenant.
- Every one of the nine blocking issues was open on 22 Sep. One line in check-in is holding the P0 security gate open.

### 22 Sep 2026 (late, third pass), Sanchay with Claude Code
- **Sanchay: the Platform fee is suggested on the manager app from the property's average rent. ₹58 is a placeholder, not the price.** A clause Claude had added under R63 on 22 Sep said "no band that rises with rent", which over-reached and contradicted that. Corrected in the log, visibly and attributed, not rewritten.
- The narrow rule that survives: a ladder of fixed published prices is ordinary pricing; a fee computed as 0.5% of rent, chosen because 0.5% is the UPI charge plus tax, is that charge under another name. Ladder, never rate.
- Measured the portfolio and proposed a ladder in `research/platform-fee-ladder.md`. **R53's ₹118 ceiling cannot serve 5.7% of tenants, and its ₹58 floor is above what 0.5% would give for 57.6% of them.** The flat fee is wrong at both ends, and more often at the cheap one, because RentOk's ₹49 is flat while the charge it replaces rises with rent. They cross at about ₹11,600 of average rent.
- Open question 28 carries the two numbers only Sanchay can set.

### 22 Sep 2026 (late, second pass), Sanchay with Claude Code
- Re-checked Kamal's three earlier documents in `research/kamal-earlier-material-check.md`: the plan in both versions, the context handoff, and the flows page. The first check of them was made against R1 to R18 and there are now 63 rulings, so five of its own conclusions had gone stale.
- **Measured the figure the whole project is sized on.** Both of Kamal's documents say about ₹75 lakh a year of UPI charge exposure on ₹150 crore of annual rent. August's UPI volume alone was ₹140.7 crore, and the annual exposure is about ₹6.6 crore. Workings in the private repo; open question 27 takes it to Srijan and Kamal.
- Sized the ₹15,000 segment for the first time: 15.7% of billed tenants, carrying 48.7% of the charge. That is the segment open question 24 is about. **Corrected 23 Sep: calling it "half the prize" was wrong**, because it read as though high rent were not automated. It is. R16 splits it into parts of up to ₹15,000 on one mandate, the map and ticket B1 carry it, and Kamal's prototype ships it. Open question 24 chooses the cheaper rail for that segment, it does not unblock it.
- The saved copy of the flows page is a dead shell with no content in it. The text in `sources/` is the only record of that page.

### 22 Sep 2026 (late), Sanchay with Claude Code
- Checked **all 23 sections** of Kamal's launch room against the rulings, in `research/kamal-launch-room-check.md`. The payment page document had used six of them; the other seventeen had been read but never diffed.
- Added open questions 24 to 26: e-NACH as the default rail above ₹15,000, the challan removal, and filing the two missing tickets.
- Two of his sections answer our own open questions without a ruling: the payee-name framing answers 6, and the forwardable QR answers 23.
- Found a contradiction in our own record: we say the Cashfree email is not sent, his page says fifteen questions went out on 21 Sep.

### 22 Sep 2026 (night), Sanchay with Claude Code
- Wrote `surfaces/tenant-app.md`, the tenant app seen as one surface, pointing at A1 to A6, B1 to B4, C1 to C6 and D5.
- The framing: there are two tenant apps in this plan and only one exists before 1 Oct. The app has had no commit since 26 Aug, so the push gets one thing from this surface, the server-sent announcement (R56), and everything else is the release after 1 Oct.
- Answered an engineering question A4 had left open: the home announcement can be targeted by Autopay status and can carry a link. It is one slot with three claimants and the last write wins.
- Traced five things first-hand: three Autopay doors built and dark from two missing wires (#42), the one live door pointing at check-in against R52, the app offering rent that Autopay will take, no parent app while R24 and A6 assume one, and the announcement mechanism.
- Added open question 23, the parent app that does not exist.

### 22 Sep 2026 (evening), Sanchay with Claude Code
- Wrote `surfaces/payment-page.md`, the payment page seen as one surface, pointing at A1 to A9, B1 to B4, C1, C2, D5 and E5. Three flows drawn that `map/diagrams.md` does not already carry.
- Read Kamal's launch room PRD and his sixteen-screen payment page prototype in full, and sorted every idea in them into take, do not take, and needs a ruling.
- Added open questions 19 to 22, all four from that pair of documents: the UPI charge notice, the sub-₹2,000 split, the virtual account, and Rent Points with the Hubble store.
- Traced eight things first-hand on origin/main and origin/master, 22 Sep. The largest: the Autopay system on the payment page is finished and reaches nobody, and the move of live links to the new page has not started with three days left to R55's date.

### 22 Sep 2026, Sanchay with Claude Code
- Wrote `surfaces/manager-app.md`, the manager app seen as one surface, then rewrote it to point at D1 to D7 rather than restate them. 558 lines down to 295.
- Added open questions 10 to 18, nine proposals that were buried inside D1, D2 and D3.
- Traced five things first-hand: rent and agreement paths against the mandate ceiling, grace precedence, the manager app inventory, app versus web parity, and the charges. Findings are in the surface document, section 5.
- Ruled by Sanchay: the tenant bears one Platform fee, the Autopay setup and monthly fees are deleted. Recorded as **R64**, added to the decision log on 22 Sep.

### 18 Sep 2026 (night), Sanchay with Claude Code
- Turned the map into 36 build tickets (drafted in parallel, then checked for map coverage, plain language and rulings, and against the code), filed them, and rebuilt epic #6846 with every ticket and bug nested under it.
- Filed 7 more bugs found while drafting (#7059 to #7064, marketplace#943). Answered engineering's fee plan #7022 with the rulings.
- Rulings R55 to R61 (decided by Claude on Sanchay's instruction), R62 (both options, full scope, cut order). Other providers' docs cross-checked (`research/psp-docs-crosscheck.md`); Cashfree email sharpened.

### 18 Sep 2026 (evening), Sanchay with Claude Code
- Checked two older Autopay lists and the 18 Sep call with Nimit against the record (`research/older-lists-check.md`). Logged R52: one Autopay link per tenant.
- Five reviewers read every app's code against every issue and claim. Filed 26 issues and commented on 13, plus the epic (`research/code-check-18sep.md`). The full reports are kept outside this public repo until it goes private.

### 18 Sep 2026, Sanchay with Claude Code
- Drew the feature map as nine Mermaid diagrams (`map/diagrams.md`), and as an interactive page: https://claude.ai/artifact/UoeBeNA6YPLcd6eSA7gL94
- Read Kamal's two pages from 18 Sep (the Notion plan and the "Autopay Flows" page). Nothing new needs a ruling; see `research/kamal-artifacts-check.md`. Two of the Notion diagrams do not render.
- Added the missing conversation notes, Kamal's plan version 2 and session handoff, the Metabase queries, CLAUDE.md, STATUS.md and the handoff template.

### 17 Sep 2026, Sanchay with Claude Code
- Read every recorded Autopay conversation from 15 and 16 Sep, and merged them in date order.
- Walked the product as tenant, manager, owner, RentOk finance and operations, and through the code in five repositories.
- Filed 11 issues on the backend and one on web check-in, all linked to epic #6846.
- Settled rulings R1 to R51, including: RentOk pays no payment cost; the platform fee is the property's charge; Autopay is required by default but never blocks; two setup options; and payment requests for extra bills.
- Read Kamal's plan, his screen recording (both passes) and its transcript.
- Checked Cashfree's documentation against 14 open questions.
- Wrote the feature map, versions 1 to 3, after two cold reviews.
- Created this repo.
