# Autopay push: how we judge whether a proposal is good (draft, 17 Sep 2026)

> The target and health metric still hold. The starting count of 1,226 was later corrected to 778 current tenants; see data/growth-math.md.

Built with the north-star-metric skill. Business game: transactions (rent that collects itself, on time, with no chasing).

## The two numbers that matter

| Layer | Metric | Definition (proposed) | Today | Goal |
| --- | --- | --- | --- | --- |
| Target (CEO, fixed) | **Tenants on Autopay** | Tenants with an approved, active Autopay (UPI) or e-NACH mandate that covers their rent, counted once per tenant | 1,226 | 70,000 to 75,000 by 1 Oct |
| Health (the value) | **Rent paid by Autopay on the first try** | Share of monthly rent due from tenants on Autopay that was collected on the first debit attempt | About 41% (59% of real debits fail) | Rising every month from October |

A proposal is good if it moves the first number fast without pushing the second one down.

## What drives the target (input metrics)

Needed pace: about 69,000 new tenants in about 13 days, so about 5,300 a day. At today's finish rate that is about 9,800 starts a day.

| Input | Definition | Today | What moves it |
| --- | --- | --- | --- |
| **Properties switched on** | Share of active properties where Autopay is on | 427 of 83,495 (0.5%) | Default on for every property |
| **Tenants reached** | Tenants who received a working one-tap Autopay path this week, by surface | Unknown; the bulk link lands on the wrong step | WhatsApp, payment page, tenant app, check-in, managers |
| **Start rate** | Reached tenants who opened the setup | Not measured (payment page analytics are off) | Message, timing, who sends it |
| **Finish rate** | Started tenants who approved in their bank app | 54% (1,042 of 2,285 did not finish) | Fewer steps, clear fee and dates, trusted name on the bank screen, one approval |
| **Managers pushing** | Managers who sent at least one Autopay push this week, and tenants pushed per manager | Not measured | Single and bulk send, targets, leaderboard, incentives |

## Guardrails (must not get worse while we push)

| Guardrail | Why it matters | Limit (proposed) |
| --- | --- | --- |
| First-debit success in October | New tenants judge Autopay by the first debit | Above today's 41%, measured weekly |
| Cancellations within 30 days of setup | Signals regret or a bad surprise | Tracked with reason |
| Wrong late fines on Autopay tenants | Breaks the core promise | Zero |
| Double charges (Autopay plus link for the same rent) | Money and trust | Zero |
| Disputes and chargebacks | Legal and cost | Tracked weekly |
| Support tickets per 1,000 new tenants on Autopay | Load on operations during the offsite | Tracked daily |
| WhatsApp number quality (blocks, reports, Meta rating) | Mass sends can get our numbers restricted, which would stop every rent reminder | No drop in rating |
| Security incidents on Autopay | Anyone could change a mandate without logging in today | Zero |

## Money, measured alongside

- MDR avoided each month (link payments that became Autopay debits, times 0.4% plus GST).
- Autopay service fee billed, split by who pays (tenant or management).
- Share of rent collected by each rail (Autopay, e-NACH, virtual account, link, cash).

## Where the numbers come from (to build for the push)

- Daily funnel by surface and by property: reached, started, finished, active.
- Payment page analytics are switched off today; they need switching on.
- Failure reasons are all saved as "Unknown failure" today; they need the real reason.
