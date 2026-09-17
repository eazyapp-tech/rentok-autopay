# Gap review before writing the feature map (17 Sep 2026)

An Opus reviewer read files 03 to 16 and checked the code and live data. I re-checked the key claims by hand.

## Verified by me

- **Current tenants on active Autopay: 778** (768 UPI, 8 e-NACH, 2 with no method recorded). About 470 active mandates belong to tenants who are not current. Filed as #7005 (P1).
  - **The gap to the target is about 69,300, not 68,750.**
- **Required Autopay blocks check-in:** "Setup Later" is hidden, and the button is disabled when rent is ₹0. Filed as marketplace#915 (P1).
- **The setup reminder skips anyone with any Autopay record** (`propertyDetails.ts:1516`). Filed as #7006 (P2).
- **Late-month online payments are few:** about 1,810 a day on 17 to 31 Aug (my own query), so "pay now and turn on" before 1 Oct is small. The 1 Oct surge counts (R23).

## From the reviewer, not re-checked by me

- **New tenants:** it says 1,900 to 2,100 a day. My weekly query says about 1,300.
- **Mandates tied to one due type:**
  - The mandate is tied to one due type (`entities/autopay.ts:72`), and the active check is per due type (`autopayV2.ts:67`).
  - Due types can route to their own bank account (`dueTypeBankMapping.ts`) and carry their own GST number.
  - `due_type.is_recurring` exists (`dueType.ts:122`).
- **Properties with instant payout off:** 40% of active tenants (payout_flag off). RentOk may not see their rent, so the ₹49 fee there needs a monthly invoice to the property.
- **Non-monthly rent:** about 9,500 active tenants. The meaning of the `rental_frequency` codes is not confirmed; my own counts use different code values.
- **e-NACH already exists at check-in** (`setupEnach`, `autoPayDetails.js:40`); the systems map was wrong on this. 480 unfinished setups are above ₹15,000.
- **Parents:** reminders already reach parents (`send_to_parent`), and `parent_tenant_id` is empty for active tenants.
- **No-app-release path:** the tenant app shows home cards sent by the server (`home_pending_tasks_widget.dart:82`), and an "AutoPay Setup Incomplete" card exists (`services/tenant/tenant.ts:9673-9692`).
- **WhatsApp template:** the tenant reminder uses a generic template in the owner's name, and there is no dedicated setup template.
- **Permissions:** none of the team permission keys covers Autopay.
- **RentPass:** old owner copy sells "RentPass" at ₹49 per tenant (`others.ts:3141`).
- **CirclePe:** 40 tenants have CirclePe e-NACH.

## Plan changes taken without a ruling (they follow from rulings)

- **Two lanes:**
  - Before 1 Oct: backend, the new payment page, manager web, WhatsApp, and server-sent home cards in the tenant app, with no app release needed.
  - After the freeze: manager app and tenant app screens.
- **A one-screen approval page** that works on the web and opens straight at the approval, used by every link and card.
- **A send plan** by day and by source, with the biggest wave on 30 Sep and 1 Oct.
- **The debit amount is frozen at notice time.** Anything added later waits for the next cycle.
- **A confirm step** when a debit is far above her usual dues (needed because of the ₹15,000 limit for everyone).
- **Mandates stop being tied to one due type.** The debit is split by bank routing.
- **Tenant gateway charge set to zero on link payments**, which follows from R21.
- **Four new permissions:** grant an exception, turn "required" off, change a tenant's debit day, cancel.
- **A "paused" state** in the status list. Paused mandates do not count.
- **Count only current tenants, once per person.**
- **Chase pending e-NACH setups now**, since e-NACH takes about 4 days to activate.
- **Retire the old "RentPass ₹49" copy.**
- **Leave CirclePe tenants out.**
