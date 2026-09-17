---
date: 2026-09-17
source: rentok-backend origin/master b72e2490d (17 Sep 2026), three code traces, key lines re-read by hand
related: "[[2026-09-16-autopay-merged-timeline]]"
tags: [autopay, code-check]
---

# What the backend does for Auto Pay today (17 Sep)

Live engine: V2 (src/services/autoPay/autopayV2.ts, autopayV2Helpers.ts). Cashfree subscriptions, ON_DEMAND, max 60 debits, ₹1 refundable authorisation.

## Verified by reading the lines
- Debit day window: due day to due day + Auto Pay grace (+ month-end buffer). `property.autopay_grace_period` default 0. No T-3 option. (autopayV2Helpers.ts 38-69; property.ts 988)
- Grace coupling: setup raises `tenant.grace_period` to the property Auto Pay grace; cancel sets it to null. Late fine reads `tenant.grace_period`. Cancel wipes a manager-set grace. (autopayV2.ts 837-839, 864-870; dues.ts 116-122)
- Fee: `autopay_monthly_charge` 0 means ₹50; bearer 1 owner, else tenant (entity comment says 0 = RentOk). Added per monthly debit. `autopay_setup_bearer` unused. (autopayV2Helpers.ts 122-139; property.ts 955-978)
- One debit per due cycle, amount = unpaid invoices capped at plan amount minus fee; excess stays unpaid. Hard reject if amount > plan amount. No split, no ₹15,000 rule in code. (autopayV2.ts 296-352, 410-420)
- Pre-debit reminder `POST /tenant/autopayDebitReminder` filtered to one hardcoded schedule id, "TODO: remove this". No caller in repo. (tenant.ts 27920-27936)
- Failure webhook: transaction FAILED, schedule back to PENDING (max 5 retries), manager remark only. No tenant message, no bounce charge. (autopayV2.ts 681-715)
- Eviction and tenant delete never cancel Auto Pay. (evictionService.ts only has an icon key "autopay_incomplete")
- Property `autopay_status` and `autopay_mandatory` default 0; no migration or script turns them on; 4 pg_ids hardcoded on in check-in. (property.ts 938-948; tenant.ts 8170-8182)
- Bulk reminder link = check-in link + `?autopay=true`; no standalone Auto Pay link; no single send. (propertyDetails.ts 1540)

## From the traces, not re-read line by line
- Cancel endpoint exists; no pause; editDetails reschedules the debit date with no role check.
- Payment page APIs return no Auto Pay data; Auto Pay flags come via getCheckIn and getTenantAppStatus.
- Manager status is set up or not; no failed state.
- Cashless deposit (Eqaro) still live in backend.
- "Unified" in code is the booking payment page, no Auto Pay.
- Legacy V1 bulk charge still reachable via payment.ts 8476; confirm its cron is off.

Published in the page's "Proposed Auto Pay rulebook" section: https://claude.ai/code/artifact/001a1efe-871a-47fb-a9bb-97b46a642fee
