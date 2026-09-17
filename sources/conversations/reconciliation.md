---
date: 2026-09-17
purpose: Auto Pay joined up across rulings, code in every app, GitHub issues, Linear, plans and meetings
related:
  - "[[2026-09-17-autopay-code-check]]"
  - "[[2026-09-17-autopay-source-sweep]]"
  - "[[2026-09-16-autopay-merged-timeline]]"
page: https://claude.ai/code/artifact/001a1efe-871a-47fb-a9bb-97b46a642fee
tags: [autopay, reconciliation]
---

# Auto Pay, reconciled (17 Sep 2026)

## Two tracks that never met
- Written track, 10 to 14 Sep: Sanchay's rulings (11 Sep) in the payment page design ledger and ~30 GitHub issues filed from 5s10r2, assigned to Nimit. Epic rentok-backend #6846 sets the build order: #6816 first, then #6829, then default-on, with #6830 live.
- Spoken track, 15 and 16 Sep: 1 Oct target 70-75k tenants, 0.4% + GST for non-Auto Pay tenants, split debits above ₹15,000, direct UPI app from 1 Oct, owner sheet for charges from 15 Oct. In no written record.
- Linear has no Auto Pay item. REN-927 (QA backlog) lists Auto Pay under "no real QA pass yet" and 80 unauthenticated endpoints never checked live.
- Nimit's September plan: Auto Pay "held ready to push the moment MDR lands"; no kill switch; release soaks during the 24-27 Sep offsite.

## Rulings (11 Sep, Sanchay), none built
Default on for every Manager App property; default Auto Pay grace 7 days (also existing properties at 0); any day of the month, that day becomes the rent due date for late fine; day change once a month from next month; owner setting "limit tenants to grace window" on by default; early debit pays most recently raised rent (#6828); reminder links stop for active Auto Pay (#6830); Auto Pay on the bill by default, never a gate, rent only. Stop-gap allowed by #6829: window = due to due + min(Auto Pay grace, late-fine grace). Open: #6817 split grace into two (recommended A).

## Numbers
1,226 active mandates of ~413k tenants (0.3%); 427 of 83,495 properties on; 1.9% of link recipients offerable; 95.6% of those grace 0; 59% of real debits fail (65% insufficient funds), saved as "Unknown failure"; #859: 46% of starts never finish (1,042 of 2,285), one tried 38 times.

## Surfaces (main branches, 17 Sep)
- Backend (master b72e2490d): see code-check note.
- Web check-in (marketplace main fd5a57d9): Auto Pay after ID verification, before agreement; V2 createSubscription; plan_amount = rent + fee if tenant bears it; picker min = move-in day (default 5), max = end day or 31, so it disagrees with backend's due..due+grace; `termsAccepted` hard-set true; Cashfree return via pages/api/cashfree-return.js.
- Live /p: no Auto Pay. /p2 (merged 16 Sep): full Auto Pay design, `CAN_SET_UP = false`, Approve calls nothing, payload fields not sent (#6825), no routing from /p; gtag excludes /payment-pages.
- Tenant app (package main afea1abe): banner, profile row, scheduled tag; status from getTenantAppStatus is never saved to prefs, so banner and row never show (host app not checked); no app-open prompt.
- Manager Flutter (main 2e91d8ce): settings on/off, mandatory, eligible since, setup and monthly payer; no grace field; tenant profile set up or not; bulk reminder to whole property only; no cancel, history, failed state.
- Manager web (main 58583ff3): same settings plus grace days (max 20) with a label that describes the late fine; sends bearer 3 for RentOk, which backend treats as tenant (#6880); no tenant status or reminders.
- Cashless deposit (Eqaro) still live everywhere.

## Blockers filed (none merged)
#6816 P0, #6861 P0, #6828, #6829 P1, #6830 P1, #6880 P1, marketplace #859 P1, marketplace #841 electricity, #6866 P1. Related: #6817, #6825, #6835, marketplace #771.

## New findings, not filed
A move-out/deletion keeps Auto Pay active (P1). B cancel empties tenant grace incl. 1000 = late fine off (P1). C rent rise past plan amount silently capped (P1). D check-in picker vs backend window mismatch (P1). E pre-debit reminder locked to a test record (P2). F legacy V1 bulk charge route reachable, check cron (P2). G tenant app status never saved (P2). H terms tick hard-set (P2). I web grace label wrong, phone app lacks grace (P2). J manager web lacks tenant status and reminders (P2).

## Recommendation
1 Oct = Auto Pay safe and on for a first group of properties, not 70k. Order: #6816 and #6861; money bugs (#6880, A, B, C, #6817 reasons); split grace; stop-gap window 7 days; #6830 and D; pilot, watch a week, widen. After: any-day, /p2 Auto Pay, split debits, direct UPI. Write rules first for 0.4% charge, 15 Oct owner sheet, gateway/platform fee payer. Mirror into Linear as one Release 36 parent (needs Sanchay's go). Decision asked: 1 Oct first group or every property.

Correction logged: my earlier "needs a ruling: debit window" and pick contradicted the 11 Sep ruling; removed from the page.
