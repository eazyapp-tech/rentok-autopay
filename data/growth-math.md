# Where 70,000 mandates can come from by 1 Oct (Metabase, 17 Sep 2026)

## Today

Autopay records by status (distinct tenants):
- active: 1,254
- started but not finished ("initialized"): 1,348
- waiting on bank approval: 78
- cancelled by the tenant: 437
- cancelled: 162
- paused by the tenant: 66

New mandates in the last 14 days: about 5 a day.

**Gap:** about 68,750 mandates in 14 days (17 Sep to 1 Oct), which is about 4,900 a day.

## Sources

**Online payments through RentOk (payment mode 205), last 30 days:** 141,798 payments, average ₹10,748, and 82% above ₹2,000. Mode 205 includes Autopay debits.
- **By day of the month (August 2026):**
  - the 1st: 18,049;
  - the 2nd to the 5th: 42,284;
  - the 17th to the 31st: 27,142.
- **So between 17 and 30 Sep, expect about 25,000 online payments.** Each one is a moment for "pay now and turn on Autopay".

**Payments recorded by hand, last 30 days** (cash and other offline modes, 2040 to 2048): about 87,000.

**New active tenants per week** (by `tenant.createdAt`), last 8 weeks: 4,164 (partial week), 12,484, 11,321, 8,548, 9,725, 6,881, 10,692, 8,536, and 5,062 (week in progress). That is about 9,000 a week, or 1,300 a day.

## What each source can give before 1 Oct (my estimates, to check against the first days of live data)

| Source | Pool by 1 Oct | Needs | Rough yield |
| --- | --- | --- | --- |
| New tenants, Autopay a required step at check-in (R20) | about 18,000 | required step live, manager-added tenants sent to setup | 9,000 to 12,000 |
| Online payers, 17 to 30 Sep, "pay now and turn on Autopay" | about 25,000 | the new payment page with setup switched on, Cashfree confirming first payment at setup | 7,500 to 12,500 |
| Existing tenants not paying in the window, pushed by managers and WhatsApp | about 300,000 | bulk and single send, status list, direct link to the approval step, WhatsApp template | 30,000 to 45,000 at 10 to 15% |
| Finishing the 1,348 who started | 1,348 | resume link | about 700 |
| 1 Oct itself, if the day counts | about 18,000 payments | same as the online payers row | 5,000 to 9,000 |

**Reading:**
- The target is reachable only if all three big sources run together.
- The existing-tenant push carries the largest share, and it depends on managers.
- Mandates approved by 30 Sep can collect October dues from 1 Oct, because UPI Autopay can take its first debit the day after approval (T+1).
