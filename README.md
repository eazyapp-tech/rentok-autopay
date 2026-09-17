# RentOk Autopay

Everything behind the Autopay push: what we decided, why, the research it rests on, and what is still open.

**The target, set by the CEO and fixed:** 70,000 to 75,000 tenants with an approved, active Autopay or e-NACH mandate by the end of 1 Oct 2026.

**Why now:** from 15 Oct 2026, UPI payments above ₹2,000 made to a business carry a charge of 0.4%, capped at ₹300. The business pays it and may not pass it to the customer. Autopay debits carry no such charge.

**Where we start (17 Sep 2026):** 778 current tenants on Autopay. The gap is about 69,200 in 14 days, or about 4,950 a day.

**Status:** the feature map is at version 3. Five points inside it are marked "(proposed)" and need Sanchay's yes, and several answers depend on Cashfree. See `decisions/open-questions.md`.

## Read in this order

1. **[map/feature-map.md](map/feature-map.md)** is the document. It covers how Autopay works for every tenant, parent, manager, owner and for RentOk, moment by moment, and what we are not building.
2. **[decisions/decision-log.md](decisions/decision-log.md)** holds every ruling (R1 to R51), what each one replaced, the things ruled out, and the facts checked by hand.
3. **[decisions/open-questions.md](decisions/open-questions.md)** is the list of what is still unanswered, and who can answer it.
4. **[data/growth-math.md](data/growth-math.md)** shows where the mandates can come from, with the numbers behind them.
5. **[research/cashfree-docs-answers.md](research/cashfree-docs-answers.md)** is what Cashfree's documentation says, question by question, with links.

## What is in each folder

| Folder | What it holds |
| --- | --- |
| `map/` | The feature map, the single document to build from |
| `decisions/` | The decision log, the success metrics, and the open questions |
| `research/` | Legal research, the systems map, the Cashfree answers, market research, reviews of Kamal's plan and recording, and older drafts marked superseded |
| `walkthroughs/` | The role-by-role walks: tenant, manager and owner, finance and operations, and two code walks |
| `data/` | Numbers pulled from RentOk's data tool, with the workings |
| `sources/` | Original documents: the Finance Ministry FAQ on the new UPI charge, Kamal's plan, and the transcript of his recording |
| `handoffs/` | The session record, so anyone can pick the work up |

## Rules that shape everything

- RentOk pays no payment cost, on any method, because rent is not RentOk's money.
- RentOk charges management ₹49 plus GST per billed tenant a month. Management decides whether to absorb it or pass it on as the property's "Platform fee" line.
- A tenant is never charged for Autopay itself.
- Autopay is on and required by default for every property and tenant. Required means chase, never block.
- At setup a tenant picks one of two options: her rent on a fixed schedule, or all her dues on demand.
- Payment gateway charges stay separate from the platform fee, and unchanged.

## Work already filed

In [eazyapp-tech/rentok-backend](https://github.com/eazyapp-tech/rentok-backend), all linked on epic [#6846](https://github.com/eazyapp-tech/rentok-backend/issues/6846):

| Issue | What it is |
| --- | --- |
| [#6816](https://github.com/eazyapp-tech/rentok-backend/issues/6816), [#6861](https://github.com/eazyapp-tech/rentok-backend/issues/6861) | Autopay routes that need no login |
| [#6995](https://github.com/eazyapp-tech/rentok-backend/issues/6995) | Two debit engines can charge the same tenant twice |
| [#6996](https://github.com/eazyapp-tech/rentok-backend/issues/6996), [#6998](https://github.com/eazyapp-tech/rentok-backend/issues/6998) | Payout deductions are wrong |
| [#6999](https://github.com/eazyapp-tech/rentok-backend/issues/6999) | One empty month ends a tenant's Autopay |
| [#7000](https://github.com/eazyapp-tech/rentok-backend/issues/7000) | Dues that include GST are collected short |
| [#7002](https://github.com/eazyapp-tech/rentok-backend/issues/7002) | A tenant who paid another way is still debited |
| [#7003](https://github.com/eazyapp-tech/rentok-backend/issues/7003) | The wrong amount is saved for each debit |
| [#7004](https://github.com/eazyapp-tech/rentok-backend/issues/7004) | The debit time is sent in 12-hour format |
| [#7005](https://github.com/eazyapp-tech/rentok-backend/issues/7005) | Mandates stay live after a tenant moves out |
| [#7006](https://github.com/eazyapp-tech/rentok-backend/issues/7006) | The setup reminder skips anyone who ever tried |

In [eazyapp-tech/eazypg-marketplace](https://github.com/eazyapp-tech/eazypg-marketplace), the web check-in: [#915](https://github.com/eazyapp-tech/eazypg-marketplace/issues/915), required Autopay blocks check-in.

## How this repo is kept

- **The map is the only place to build from.** Older files carry a banner saying what replaced them.
- **Every ruling goes in the decision log,** with its date and what it replaced.
- **Numbers carry their source and date,** and anything unverified says so.
- Written in plain English: short sentences, no jargon, and every reference explained where it sits.
