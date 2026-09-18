# Handoff: 18 Sep 2026 evening, older lists and code check

**Objective.** Check two older Autopay lists and the 18 Sep Nimit call against the record, and every issue against current code, before the 1 Oct push.

**Done**
- `research/older-lists-check.md`: what was taken from the older lists, what the map already covers, what later rulings replaced, and notes on the Nimit call.
- R52: one Autopay link per tenant. A tenant still in check-in sets it up there, and everyone else uses the payment page.
- Open questions 6 to 8: fee floor and ceiling, whitelabel brand, stop-all switch. Also the Cashfree one-debit-a-day evidence, Kamal and Srijan's IDFC workflow, and bank bounce charges.
- Five reviewers, with the most serious findings checked again by hand. 26 issues filed, 13 existing issues commented, epic #6846 updated. Summary in `research/code-check-18sep.md`.
- Full reviewer reports are at `~/Sanchay Personal Projects/rentok/autopay-push/code-check-18sep/`, kept out of this public repo. **Once the repo is private, copy them into `research/code-check-18sep/`.**

**Next**
1. Sanchay rules on open question 6, the platform fee floor and ceiling, and the other waiting items.
2. A map pull request adds the order changes proposed at the end of `research/code-check-18sep.md`.
3. Kamal adds the one-debit-a-day question to the Cashfree email (rentok-autopay#2).
4. When Kamal has GitHub access: add him with write access, make the repo private, and copy the reports in.

**Not verified.** Clarity on the payment page (needs a browser check); the old engine's outside scheduler; the Pay button on `/p2` in production; Cashfree's single-charge cancel.
