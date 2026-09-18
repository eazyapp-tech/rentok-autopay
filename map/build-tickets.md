# Build tickets, filed 18 Sep 2026

36 tickets, written from the feature map (version 4) in the format in `drafts/ticket-format.md`, and checked in three passes: map coverage, plain language and rulings, and code. They sit as sub-issues under the Autopay epic, eazyapp-tech/rentok-backend#6846, and each filed bug sits under the ticket it blocks. Each ticket carries its cut rank (R62: 1 keep, 2 cut second, 3 cut first).

The ticket texts, as filed, are kept outside this public repo until it goes private, because the security tickets describe holes that are still open. GitHub is the live copy; edit tickets there.

| Id | Issue | Ticket |
| --- | --- | --- |
| S0 | eazyapp-tech/rentok-backend#7072 | Every Autopay fix is tried with real money on staff tenants, and signed off, before it reaches real tenants |
| S1 | eazyapp-tech/rentok-backend#7073 | Nobody can change, fake or trigger Autopay money without the right login (security gate before Autopay goes on for everyone) |
| S2 | eazyapp-tech/rentok-backend#7074 | Every active mandate takes the right amount, once, on her day, before Autopay is switched on for everyone |
| A1 | eazyapp-tech/eazypg-marketplace#959 | Tenant sets up Autopay on one screen, from any link or card, and approves it in her own UPI app |
| A2 | eazyapp-tech/eazypg-marketplace#960 | Tenant pays her dues and turns on Autopay in the same approval |
| A3 | eazyapp-tech/eazypg-marketplace#961 | New tenant sets up Autopay as the step after her agreement at web check-in, or chooses "Set up later", and is never blocked |
| A4 | eazyapp-tech/rentok-backend#7075 | Every door leads a tenant to the same setup screen: her app, every signing, a link she shares, and tenants a manager added directly |
| A5 | eazyapp-tech/eazypg-marketplace#962 | Tenant or parent reads what Autopay is, in plain words, from "know more" anywhere, and goes back to set it up |
| A6 | eazyapp-tech/rentok-backend#7076 | A parent or guardian sets up Autopay for a tenant's dues from their own UPI account, and both are kept informed |
| A8 | eazyapp-tech/eazypg-marketplace#963 | Every payment link a tenant already has opens the new payment page, where Autopay lives, and keeps working as long as she needs it |
| A9 | eazyapp-tech/rentok-backend#7077 | A tenant or parent who sets up Autopay outside check-in sees the Autopay terms, agrees to them herself, and RentOk can always show what she agreed to |
| B1 | eazyapp-tech/rentok-backend#7078 | Every period, an Option 2 tenant is told what will be taken, it is taken on her day (in parts above ₹15,000), and her dues show paid everywhere at once |
| B2 | eazyapp-tech/rentok-backend#7079 | Every period, an Option 1 tenant's fixed amount is taken by Cashfree on schedule, recorded as paid everywhere, lowered when her dues drop for good, and cancelled for one period when she owes less |
| B3 | eazyapp-tech/rentok-backend#7080 | When a debit fails, she is told the same day why, how to pay now and when the next try is, retries are timed to find money, and she is never fined while they run |
| B4 | eazyapp-tech/rentok-backend#7081 | When a period goes off the usual path (she paid another way, refused one debit, set a lower limit in her UPI app, or was charged wrongly), she is never charged twice and always has one clear next step |
| B5 | eazyapp-tech/rentok-backend#7082 | Tenants on today's rent-only Autopay pick an option and approve at their regular dues before their October debit, with no gap and no double debit, and tenants who left have their mandates stopped and are told |
| B6 | eazyapp-tech/rentok-backend#7083 | Money taken by Autopay reaches the owner's right bank accounts once, with nothing taken but RentOk's service charge, and Sanchay picks how Autopay money settles |
| B7 | eazyapp-tech/rentok-backend#7084 | A tenant who picks Option 1 gets a real fixed-schedule mandate at her bank, and RentOk can lower it, skip one period, pause, resume and end it |
| C1 | eazyapp-tech/rentok-backend#7085 | Tenant sees her Autopay and changes her day, her option or bank, or cancels it herself, and her manager is told |
| C2 | eazyapp-tech/rentok-backend#7086 | Tenant asks to skip a debit or pause Autopay, the property approves or lets it pass in 48 hours, and Autopay restarts on its own |
| C3 | eazyapp-tech/rentok-manager-web#1023 | Manager asks RentOk to pause or stop a tenant's Autopay, sees "Waiting on RentOk", and is told what RentOk did |
| C4 | eazyapp-tech/rentok-backend#7087 | Manager collects any extra due through the tenant's Autopay, one or many at a time, and the tenant approves or chooses to pay herself |
| C5 | eazyapp-tech/rentok-backend#7088 | Every mandate ends at her agreement end, and whoever pays is asked to renew it 15 days before, so Autopay never stops by surprise |
| C6 | eazyapp-tech/rentok-backend#7089 | When a tenant's dues, room, property, billing period or stay changes, her Autopay follows, asks for a new approval only when needed, and ends cleanly when she leaves |
| D1 | eazyapp-tech/rentok-manager-web#1024 | Manager sees every tenant's Autopay status, across properties, and acts on one tenant from her profile |
| D2 | eazyapp-tech/rentok-backend#7090 | Manager sends Autopay setup to one tenant, a selection, or everyone not set up, in one tap, to the tenant or her parent |
| D3 | eazyapp-tech/rentok-backend#7091 | Manager is told about every Autopay event that needs her, only her team can act, and every action is recorded |
| D4 | eazyapp-tech/rentok-backend#7092 | Manager sets a property's Autopay and platform fee rules once, with safe defaults, and the old tenant Autopay fees are gone |
| D5 | eazyapp-tech/rentok-backend#7093 | Tenant is told before 1 Oct, then sees one "Platform fee" line on every bill, the same whatever way she pays |
| D6 | eazyapp-tech/rentok-backend#7094 | Owner sees exactly what RentOk charged, what was taken from each payout and why, and how many tenants still pay by link |
| D7 | eazyapp-tech/rentok-backend#7095 | Manager changes rent for one tenant or many, with a preview, notice and one signing round, and each tenant's Autopay follows |
| E1 | eazyapp-tech/rentok-backend#7096 | Every Autopay WhatsApp message exists, is approved by Meta, goes from the right name, and never floods a tenant |
| E2 | eazyapp-tech/rentok-backend#7097 | RentOk runs the push to 1 Oct: every current tenant not on Autopay is asked, on the property's behalf, within the WhatsApp number's limits, with people on call |
| E3 | eazyapp-tech/rentok-backend#7098 | RentOk support handles pause, stop and "charged wrongly" cases, records every action, checks every debit against a recorded payment each day, and can stop debits if something goes wrong |
| E4 | eazyapp-tech/rentok-backend#7099 | RentOk sees, every morning, how many tenants count toward the target, whether their rent is really being paid by Autopay, and where they came from |
| E5 | eazyapp-tech/eazypg-marketplace#964 | Every Autopay setup is counted by the door it came through, and the payment page records no tenant's private details |
