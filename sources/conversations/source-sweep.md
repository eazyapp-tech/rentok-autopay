---
date: 2026-09-17
purpose: Which recent NeoSapien and Wispr Flow conversations touch Auto Pay, checked against full transcripts
related: "[[2026-09-16-autopay-merged-timeline]]"
tags: [autopay, sources]
---

# Auto Pay source sweep, 10 to 17 Sep (plus older Auto Pay hits)

How this was checked:
- NeoSapien: 7 recordings since 10 Sep, confirmed by two separate listings. None on 12 to 15 Sep. Nothing archived after 4 Sep.
- Wispr Flow: 10 meetings changed since 10 Sep. Search is by last edit, so nothing recorded in the window can be missed.
- Every transcript was read in full. The 90 minute onboarding call was scanned by keyword (romanised Hindi).

## Has Auto Pay content
| When | Source | What the transcript actually says |
|---|---|---|
| 7 Sep, 8:55 PM | NeoSapien | Fee rules: property level default for platform and gateway fee, package level override. Platform fee once per tenant per month; gateway fee on every payment. Custom display names for both fees. |
| 10 Aug, 10:02 PM | NeoSapien (summary read, transcript not yet) | Auto Pay on pay.rentok.com by default for all tenants. Tenant bears the fee (₹40 to ₹50). Auto Pay step comes after Aadhaar OTP in check-in, before the rent agreement, on purpose (tenants refused otherwise). Public releases 27 Aug and 24 Sep. |
| 11 Sep, 1:41 PM | Wispr | Auto Pay window T-3 to T+12 (15 days), decided. Auto Pay is on by default but its card does not show by default (bug). Nimit to make a separate Auto Pay dues card in payment settings. Sanchay to write the exact spec for gateway and platform fee. Benefit copy: 2 to 3 words, active voice ("No rent reminders"). Payment page redesign to go live. |
| 14 Sep, 3:24 PM | Wispr | Cashfree payment screen cleanup (Send receipt instead of Save, one of Download or Share, drop payment details). Cashfree test mode needs is-test true. Decided: close the P2 issues and ship first, then Auto Pay. Recording metadata says 11 seconds, but the transcript is several minutes. |
| 19 May | NeoSapien | Bulk Auto Pay reminder: today it sends to all tenants at once; Sanchay wanted a quick actions style UI, reachable from the tenant section. About bulk, not a single tenant button. |
| 11 Sep, 6:40 PM | NeoSapien | One line only: "90% of your work is stuck in PRs, unified still hasn't gone live." Same blocker as 16 Sep. |

## No Auto Pay content
- 9 Sep: custom enterprise websites.
- 11 Sep, 3:39 PM: dev sync (complaint bot, sign-up, co-tenants).
- 14 Sep, 2:36 PM: senior living client, advance payments via tenant or parent app. Payments, not Auto Pay.
- 14 Sep, 4:31 PM: photo tool and add-on services.
- 14 Sep, 5:13 PM: Meridian website and copywriting guide.
- 15 Sep, 3:30 PM: checklist and task module.
- 15 Sep, 4:25 PM: first party saving and multi-party agreements.
- 16 Sep, 3:58 PM: Riyo rental options; GST ticket for a user; delivery concerns.
- 16 Sep, 5:17 PM (90 min): property onboarding. No Auto Pay. Note: TDS and late fine were removed from the rental option billing screen for now (a different screen from Auto Pay).
- 16 Sep, 6:48 PM: interview remark.

## After reading the last two transcripts (17 Sep)
- 10 Aug, full transcript: confirms the summary. Adds that the senior voice asked for Auto Pay on the payment page "on day one, last April", and the check-in position is a setting that can move after the agreement.
- 7 Sep, full transcript: the fee rules are about platform and gateway fees only. The Auto Pay fee is never mentioned, so it does not answer "one time or monthly".
- All of this is now in the published page: https://claude.ai/code/artifact/001a1efe-871a-47fb-a9bb-97b46a642fee (new dated sections, a patterns section, the tenant journey with gaps, 16 decided, 8 conflicts, 13 open, 35 work items).

## New conflicts this adds
- Debit window: T-3 to T+12 (11 Sep) vs due date to end of grace period (15 Sep).
- Step order: Auto Pay after Aadhaar OTP, before agreement (10 Aug) vs renting terms, agreement, Auto Pay (16 Sep).
- Who pays: tenant bears ₹40 to ₹50 (10 Aug) vs owner chooses (16 Sep).
- Fee frequency: platform fee monthly, gateway fee per payment (7 Sep) answers part of the 16 Sep "one time or monthly" question.
