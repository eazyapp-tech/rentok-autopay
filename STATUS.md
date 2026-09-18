# Where the work stands

Update this at the end of every session. Newest entry on top.

## Now

- **Feature map:** version 4 (PR #5, 18 Sep), in `map/feature-map.md`.
- **Rulings:** R1 to R54, in `decisions/decision-log.md`.
- **Code check, 18 Sep:** every older issue is still true, 26 new issues filed (3 P0). 473 of 781 current Autopay tenants have no debit queued. See `research/code-check-18sep.md`; epic #6846 lists what to fix before 30 Sep.
- **Waiting on Sanchay:** which brand whitelabelled tenants see, link life and push list, testing with real money, the stop-all switch (open questions 6 to 10), #7055 (what Autopay off means for running mandates), and five points marked "(proposed)" in the map. They are listed in `decisions/open-questions.md`.
- **Waiting on Cashfree:** ten written questions, the first being whether one mandate can be debited in parts on the same day. Also in `decisions/open-questions.md`.
- **Waiting on advisers:** the agreement wording and the platform fee line (a payments lawyer), and RentOk's tax position.
- **Cashfree email:** drafted for Kamal in `drafts/cashfree-email.md`, not sent.
- **Not done yet:** engineering tickets from the map, mirroring into Linear (only on Sanchay's go), and linking this repo from epic #6846.
- **Access:** public until Kamal has GitHub access, then private. Until then Kamal sends his work to Sanchay, who adds it here.
- **Working now:** nobody. Put your name here when you start.

## Log

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
