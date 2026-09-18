# Kamal's two pages from 18 Sep: what is new (checked 18 Sep 2026)

Kamal shared two things on Slack on 18 Sep:
- a Notion copy of his plan, "RentOk UPI AutoPay: Product Flow Redesign & Adoption Plan";
- a published page, "RentOk Autopay Flows", with 9 figures.

Both were read in full.

## The Notion page

It is **identical in content to his plan version 2** (`sources/2026-09-17-kamal-plan-v2.md`), which is already reconciled in `research/kamal-plan-v2-review.md`.

In Notion, two of its three Mermaid diagrams fail to render: section 1.1 (setup) and section 1.4 (payment link). The cause is quotation marks inside node labels, for example `"change" link visible`. The state diagram in section 1.6 renders.

## The flows page (9 figures)

| # | Figure | Status against our rulings |
| --- | --- | --- |
| 01 | "The same rent, two rails": ₹12,000 by link costs ₹48 a month; by mandate, ₹0 | Useful framing, used in our visual. The ₹48 leaves out GST on the charge (₹56.64 with it). Autopay still has Cashfree's own per-debit fee (about ₹15). |
| 02 | The ₹15,000 line where a PIN is needed | Agrees with our research |
| 03 | "Split the mandate, not the debit": three mandates | Replaced by R16: one mandate, debits in parts |
| 04 | Setup at check-in with all 31 days to pick from | Replaced by R41 (due day to due day plus grace days) and R46 (two options) |
| 05 | Payment link, then Autopay on the success screen, by device | Taken: "pay now and turn on Autopay", and phone versus computer |
| 06 | CRED's checkbox, and RentOk's empty slot | Taken |
| 07 | Mandate states, including "Required" and "Snoozed" | Adapted into our state diagram. "Required" is now a setting, not a state (R20, R21) |
| 08 | WhatsApp messages around a debit; the notice 24 hours ahead is the legal one | Corrected: the bank sends the legal notice through Cashfree. Our WhatsApp heads-up goes 2 days ahead |
| 09 | Four phases, October to March | Replaced: the target is 1 Oct, and there are no waves (R1, R37) |

**Nothing new** needs a ruling. The copy of the page itself is in `sources/2026-09-18-kamal-flows-page.md`.
