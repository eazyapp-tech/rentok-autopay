# Where the work stands

Update this at the end of every session. Newest entry on top.

## Now

- **Feature map:** version 4 (PR #5, 18 Sep), in `map/feature-map.md`.
- **Rulings:** R1 to R62, in `decisions/decision-log.md`.
- **Code check, 18 Sep:** every older issue is still true, 26 new issues filed (3 P0). 473 of 781 current Autopay tenants have no debit queued. See `research/code-check-18sep.md`; epic #6846 lists what to fix before 30 Sep.
- **Waiting on Sanchay:** which brand whitelabelled tenants see, link life and push list, testing with real money, the stop-all switch (open questions 6 to 10), #7055 (what Autopay off means for running mandates), five points marked "(proposed)" in the map, and **open questions 10 to 26, added 22 Sep from the manager tickets, from Kamal's PRD and prototype, from the tenant app, and from the 23-section check of his launch room**. All listed in `decisions/open-questions.md`.
- **Waiting on Cashfree:** Kamal's launch room says his list of fifteen went to Cashfree on **21 Sep**, three of them marked blocking. Our ten are in `decisions/open-questions.md` and `drafts/cashfree-email.md` still says draft. **Reconcile the two lists and correct whichever record is wrong.**
- **Waiting on advisers:** the agreement wording and the platform fee line (a payments lawyer), and RentOk's tax position.
- **Cashfree email:** our copy is still marked draft. Kamal's launch room says a fifteen-item list was sent on 21 Sep. See `research/kamal-launch-room-check.md`, item 1.
- **Build tickets:** 36 filed 18 Sep under epic #6846, listed in `map/build-tickets.md`, with cut ranks (R62).
- **Not done yet:** engineering tickets from the map, and linking this repo from epic #6846. Linear mirroring is done: project Autopay, 7 parents and 57 sub-issues, 21 Sep.
- **Surface documents:** `surfaces/manager-app.md`, `surfaces/payment-page.md` and `surfaces/tenant-app.md` (all 22 Sep). Manager web and web check-in are left.
- **Access:** public until Kamal has GitHub access, then private. Until then Kamal sends his work to Sanchay, who adds it here.
- **Working now:** nobody. Put your name here when you start.

## Log

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
- Ruled by Sanchay: the tenant bears one Platform fee, the Autopay setup and monthly fees are deleted. Recorded as R64 in the document and **not yet in the decision log**.

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
