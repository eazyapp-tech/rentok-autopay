# Autopay push: running inventory (feature-map gather stage)

Rulings are numbered R, my calls W, exclusions N, open questions Q. Nothing here is the final map; the map is written once, after the full picture is stated back and Sanchay says go.

## Rulings

- R1 (CEO, relayed 17 Sep) Target 70,000 to 75,000 tenants on Autopay by 1 Oct 2026. Fixed; plan to hit it.
- R2 (17 Sep) Autopay live for every property, optional for tenants, pushed by RentOk, management and owners.
- R3 (17 Sep) Tenant pays Autopay setup and monthly charges by default; management can switch them to itself. RentOk absorbs nothing; owners absorb nothing and will raise rent instead.
- R4 (17 Sep) RentOk keeps control of the payment flow. Owner-direct payments rejected (option C).
- R5 (17 Sep) Current code and data are today's reality, not a limit.
- R6 (17 Sep) Link-payment MDR: property bearing it (A) and a flat platform fee for all (B) make sense; Autopay discount (D) maybe.
- R7 (17 Sep) Every surface counts: tenant app, new payment page, web check-in, manager app (bulk and single reminders), manager web, WhatsApp.
- R8 (17 Sep) A tenant counts toward the target when she has an approved, active Autopay (UPI) or e-NACH mandate covering her rent, counted once.
- R9 (11 Sep, earlier) Autopay default on; Autopay grace 7 days; any day of the month, which becomes her rent due date for late fines; day change once a month from next month; reminder links stop on active Autopay; offered on the payment page by default; rent only.
- R11 (17 Sep, replaces the tenant-pays part of R3) RentOk bears no payment cost on any method, because rent is not RentOk's money. RBI allows the operator or owner to pay the tenant's charges. The tenant must not bear Autopay charges. Where management says the cost is on the tenant's side, find a lawful way for it to reach tenants (rent raise or similar) that keeps RentOk safe under RBI and NPCI rules.
- R12 (17 Sep) Owners get both tenant-side routes (RentOk platform fee, rent raise). Setup cost moves off RentOk to management or tenant. Bulk rent change is needed. Agreement term edits unsign and re-send to every party. Detail and open questions: 13-cost-cover-and-rent-change.md.
- R13 (17 Sep) A rent change or new platform fee starts on its start date for every tenant, signed or not. Guardrails I added: notice sent and delivery recorded before the start date, start date no earlier than the agreement's notice period, the tenant can decline by giving notice before it starts.
- R14 (17 Sep) Default for a property that has not chosen: tenant side through the RentOk platform fee (flat, same for every method, RentOk's invoice). Rent raise is the manager's alternative; management is the third choice.
- R15 (17 Sep) Default platform fee ₹49 plus GST per tenant per month, same for every payment method, on RentOk's invoice; covers Autopay setup and debits. UPI link charges from 15 Oct stay with management (from the payout). Replaces FNF's ₹30.
- R16 (17 Sep, after my one pushback) Rent above ₹15,000: one on-demand UPI Autopay mandate with a ₹15,000 limit; each month the rent is taken in parts of up to ₹15,000 (₹20,000 = ₹15,000 + ₹5,000; two or three debits). The split is shown to the tenant at setup; she approves once. e-NACH stays available but is not shown as a separate choice, only as a short FAQ answer. Cashfree's written confirmation still requested (not a blocker).
- R17 (17 Sep) Rent in parts: the tenant fee stays ₹49 plus GST for everyone; no extra charge for extra parts. Margin is checked on the whole base (cash and link payers pay ₹49 with no debit cost), not per tenant.
- R18 (17 Sep, replaces 'rent only' in R9) Each month's Autopay debit collects all monthly dues: rent, the platform fee, electricity bills, food and other recurring dues, up to her limit, in parts of up to ₹15,000. Deposits and one-off charges are not included.
- R19 (17 Sep) Every mandate has a ₹15,000 maximum per debit, for everyone, so the same mandate can collect rent, electricity and any other bill without a new approval.
- R20 (17 Sep, replaces 'optional for tenants' in R2) Autopay is required for every tenant: on and required by default for every property, because of the new rules. A property can turn "required" off in its settings. The setting already exists (`property.autopay_mandatory`, `property.ts:9483-9696`; read at `tenant.ts:8361`, alongside a hard-coded list at `tenant.ts:8178`).
- R21 (17 Sep) "Required" means chase, never block.
  - New check-in: Autopay is a required step. The manager can grant an exception (no supported bank, no smartphone) or send e-NACH.
  - Existing tenants, and anyone who cancels: a persistent card in the app and on the payment page, capped WhatsApp nudges, and the manager's status list with follow-up.
  - She can always pay the same bill by link or cash, with no extra charge or penalty.
  - Nothing in the app is locked.
- R22 (17 Sep) When management covers costs, RentOk charges the operator ₹49 (plus GST on RentOk's invoice) per tenant per month, from the payout. Read as every tenant at the property, whatever way they pay, the same as the tenant fee. Sanchay's words: "Charge operator the cost Rs 49".
- R23 (17 Sep) The target counts mandates approved up to the end of 1 Oct 2026. The biggest push goes on 30 Sep evening and 1 Oct morning.
- R24 (17 Sep) A parent or guardian can set up Autopay from their own UPI account for the tenant's dues. The setup link goes to the parent through the parent app and WhatsApp. The mandate is in the parent's name and counts for the tenant, and notices go to both.
- R25 (17 Sep) The default ₹49 plus GST platform fee starts with October 2026 dues (1 Oct).
  - Consequence under R13: the fee notice must reach tenants before 1 Oct.
  - Where a tenant's agreement needs a longer notice period, her fee starts once that period has passed.
  - Management covers costs until her fee starts.
- R26 (17 Sep) Tenants see the charge as "Platform fee" (₹49 plus GST a month). It is never called "convenience fee" or anything tied to paying.
- R27 (17 Sep) RentOk sends the Autopay setup message directly to every property's tenants on WhatsApp. The manager gets a heads-up 24 hours before and can opt the property out.
- R28 (17 Sep, against my pick) Tenants who pay quarterly, yearly or on a manual schedule (about 9,500, by the reviewer's count) are included: required and pushed like everyone else.
  - Consequences: #6999 (an empty month ends Autopay) must be fixed before 1 Oct.
  - Debits follow each tenant's own billing cycle.
  - Large amounts go in ₹15,000 parts.
- R29 (17 Sep) Late fines are never taken by the Autopay debit. They are paid by link only.
- R30 (17 Sep) Prepaid electricity recharges are not taken by the debit; the tenant tops up herself. Electricity bills raised by the property are included. *(The second sentence was replaced later the same day by R46 and R47: electricity bills are not regular dues, so they are taken through "Request payment via Autopay" under Option 2, or sent as "Pay now" under Option 1. Noted 18 Sep.)*
- R31 (17 Sep) The ₹49 is charged per billed tenant (the person who gets the rent invoice). Co-tenants and parents who only sign pay nothing.
- R32 (17 Sep) How the ₹49 is collected:
  - **Management pays:** RentOk takes it from the tenant's online payment before paying the property.
  - **Tenant pays:** it is an added due on her bill. If she pays rent in cash, the fee stays open as a due in the app and on her next bill, to be paid online.
  - **When no online payment happens at all** (so there is nothing to deduct from): RentOk sends the property a monthly invoice for the fees owed.
- R33 (17 Sep) If a tenant sets up Autopay between 25 Sep and 1 Oct, the first debit takes the October dues already on her bill. Setup shows the amount and date before she approves.
- R34 (17 Sep, correction) Payment gateway charges and the platform fee are separate things.
  - When a tenant pays by card, net banking, IMPS, NEFT and so on, those methods keep their own gateway charges as today. The platform fee does not change them, and they do not change the platform fee.
  - My call to set tenant gateway charges to zero is withdrawn. The UPI charge still cannot reach the tenant (R15).
- R35 (17 Sep, correction, replaces "RentOk's own invoice to the tenant" in R14, R15 and R32) RentOk does not charge tenants the platform fee.
  - RentOk charges management ₹49 per billed tenant.
  - Management decides whether it absorbs that or passes it on to the tenant as a "Platform fee" line on her bill. The line is the property's charge, not RentOk's.
  - Default: passed to the tenant.
- R36 (17 Sep) No extra tenant input before a debit. The confirm step for unusual amounts (my call 6) is removed.
- R37 (17 Sep) No waves or priority groups. Autopay is enabled by default for every tenant and every property, existing and future, from the start.
- R38 (17 Sep) Tenant-level exception. In a property where Autopay is required, a team member with access can turn "required" off for one tenant from her profile.
- R39 (17 Sep) Managers cannot pause or stop Autopay. The manager app has a button to ask RentOk to pause or stop Autopay for a tenant.
- R40 (17 Sep) Tenants can change their own Autopay day within the allowed window.
- Calls 1, 2, 3, 5, 7, 8, 9 and 10 confirmed. Call 4 withdrawn (R34), call 6 removed (R36), call 11 removed (R37). Call 8 is refined by R39 and call 9 by R38.
- R41 (17 Sep, replaces "any day of the month" in R9 and in #6829) The allowed window for her Autopay day runs from her rent due day to her due day plus grace. Autopay grace is 7 days (R9). Her due date for late fines does not move.
  - Consequence: retries can run past the last grace day when she picks a late day.
  - My call: no late fine while retries are still running.
- R42 (17 Sep) The tenant's "Platform fee" line defaults to ₹58. That covers RentOk's ₹49 plus ₹8.82 GST, so a property that passes the fee on is left at zero cost. Management can edit the amount.
- R43 (17 Sep, refines R42) A GST-registered property shows the platform fee as ₹49 plus a GST line. A property without GST registration shows one combined amount, ₹58.
- R44 (17 Sep, adjusts R16) The approval step lives on RentOk's own screen.
  - **UPI:** her UPI apps are listed there and open directly, with no Cashfree page.
  - **e-NACH:** a small "Use bank account instead" link goes to Cashfree's hosted page.
  - **Cards:** no card Autopay.
  - **Verified in Cashfree's docs (Context7, 17 Sep):**
    - For UPI, "raise a charge or create an auth" (POST /pg/subscriptions/pay, payment_type AUTH) takes the upi channel link, qrcode or collect, and link returns app deep links (for example gpay tez://upi/mandate, phonepe://upi/mandate).
    - For e-NACH, the same call takes an enach block, or the hosted subscription checkout opens from subscription_session_id (cashfree.subscriptionsCheckout).
- R45 (17 Sep) Tenant self-service, from the tenant app and the payment page: change her day, pause her Autopay, and cancel it.
  - Management is told of every one of these actions.
  - Depending on the action, her dues switch to the normal "Pay now" state.
- My calls that follow from it:
  - A pause means RentOk raises no debits for the cycles she picks: skip the next debit, or pause until a month she chooses, up to 3 cycles, and at most 3 paused cycles in any 12 months.
  - A pause chosen after the bank notice cancels that queued debit if it has not run.
  - Autopay resumes on its own after the pause, with a message before the next debit.
  - A paused tenant does not count toward the target.
  - Cancelling ends the mandate through Cashfree. She can give a reason if she wants to; it is not required.
  - A tenant can pause or cancel a mandate her parent set up, and the parent is told.
- R46 (17 Sep, replaces R19 and adjusts R18) At setup the tenant sees two options and must pick one.
  - (1) Rent on her rent frequency: a fixed-frequency mandate for a fixed amount.
  - (2) All dues, on demand: an "as presented" mandate. Recommended and highlighted.
  - Extra bills go through the "Request payment via Autopay" flow (R47).
  - My design details are in 18-discussion-17sep-night.md: the fixed amount and the limit both equal her regular dues, itemised; above ₹15,000, Option 1 means a PIN each time; Option 1 cannot take extra bills.
- R47 (17 Sep, team discussion) Managers get "Request payment via Autopay" next to "Record payment" and "Remind to pay", for any due.
  - The tenant and parent get "requested ₹X, will be paid after 24 hours through your Autopay", with "Approve" and "Pay manually". There is no reject.
  - A request above her limit needs a new approval.
- R48 (17 Sep, team discussion; changes R45) A tenant's pause is a request that the property (manager or owner) approves. After approval RentOk raises no debits until the resume month, then debits restart on their own. Cancel stays direct. My pause limits (call 1) are confirmed.
- R49 (17 Sep, team discussion) The Autopay record follows the tenancy's start and end. Pause, edit and delete are all available.
- R50 (17 Sep, replaces the pause limits in call 1 and the "until move-out" idea)
  - **Pause length:** a tenant can pause up to the mandate's end.
  - **Mandate end:** the mandate ends on the tenant's agreement end date.
  - **Unanswered pause request:** counts as approved after 48 hours (my recommendation, noted by Sanchay as sensible).
  - **Consequences:**
    - Every agreement renewal needs a new Autopay approval, so the renewal signing visit carries it.
    - Tenants with no agreement end date need a default end. My call: until move-out, cancelled automatically when she moves out.
- R51 (17 Sep) "Request payment via Autopay" works for any due except late fines, which stay link-only for tenants (R29). The backend still supports requesting late fines, switched off for tenants, so turning it on later needs no build work.
- R10 (earlier record) Build order in epic #6846: #6816 security fix before any-day, before default-on.

## Calls I made (to confirm in the complete picture)

- W1 Health metric: rent paid by Autopay on the first try.
- W2 Guardrails: first-debit success, 30-day cancellations, zero wrong late fines, zero double charges, disputes, tickets, WhatsApp number quality, zero security incidents.
- W3 Autopay service fee named for the service, flat, own GST line, consented; setup fee collected on the first debit.
- W4 Payment ladder: Autopay, e-NACH, RentOk virtual account, link fallback, cash with OTP.
- W5 Core shift: Autopay is how every monthly payment is collected; PIN approval above ₹15,000; link as fallback.
- W6 Use the product's word "Autopay" everywhere (fix "Auto Pay" in my files).

## Excluded

- N6 "Autopay price" (lower rent only for Autopay tenants): dropped 17 Sep; reads as passing UPI charges to link payers. Pitch instead: no extra charge, never miss rent.
- N1 Splitting rent into pieces of ₹2,000 or less (structuring). Parts of up to ₹15,000 under one mandate are allowed (R16).
- N2 Any tenant fee named or sized like MDR (FAQ Q34).
- N3 RentOk absorbing Autopay cost (overruled by R3 and R11).
- N5 Any charge hidden from the tenant (rent shown lower than what is debited, or a fee inside rent only for Autopay tenants): unlawful under the e-mandate rule and consumer rules on hidden charges.
- N4 Phasing the target to a first group of properties (overruled by R1).

## Open questions (ask one at a time)

- Q4 (ruled 17 Sep: dropped, see N6)
- Q5 (settled by R16 and R18)
- Q6 (ruled as R16) Rent above ₹15,000: Sanchay proposes one ₹15,000 UPI mandate debited more than once (₹15,000 plus ₹5,000), with e-NACH also offered. Checked 17 Sep (10-legal-research addendum): not forbidden in RBI text, but it exists only to avoid the PIN step; my pick is e-NACH default, split only on Cashfree's written yes.
- Q-audio Transcribe Kamal's recording (local tool or OpenAI) or skip?

## New information after R3 (17 Sep, verified by hand)

- I1 RBI Digital Payments E-mandate Framework, 2026 (21 Apr 2026), para 10(a): "No charges shall be levied to the customer for availing the e-mandate facility for recurring transactions." Para 10(c): the acquirer (Cashfree) must ensure its merchants comply. Read on taxguru's copy of the RBI text. Bears on R3 (tenant pays Autopay charges). Raised once with Sanchay as new information.
- I2 Payment aggregator risk: if rent lands in EAZYAPP's own account and RentOk pays owners, that is likely unlicensed aggregation (RBI PA directions, 15 Sep 2025). Keep control through Cashfree Easy Split with owners as KYC-checked vendors. Needs Cashfree's written confirmation of how each flow settles.
- I3 TPAP: removes no MDR, allows no fee (FAQ Q17), adds liability, 8 to 12 weeks; not a 15 Oct path. UPI plugin in the tenant app later for repeat payers.
- I4 BBPS: rent category exists only for registered entities; most owners are individuals; rent likely at 0.4%; reach channel for large operators later.
- I5 Split mandates or split rent: likely read as avoiding the PIN rule; excluded (N1 widened).
- I6 Tenants already pay `gateway_charges` on online payments (payment.ts 241 to 243, 1300, 1983); reads as MDR pass-through after 15 Oct.
- I7 Autopay fee prints as "Payment processing charges" on the property's receipt, with no RentOk GST invoice.
- I9 (Metabase 17 Sep) Median rent ₹8,250; 36.5% of tenants pay above ₹10,000. Details in 13.
- I8 Possible e-commerce operator exposure (GST section 9(5), TCS, TDS) for RentOk; tax opinion needed.

- R52 (18 Sep, Sanchay on the call with Nimit) One Autopay link per tenant at a time. A new tenant still in check-in sets Autopay up inside check-in, and the check-in link opens at the Autopay step. Everyone else, including a tenant who chose "Set up later", gets the payment page as the Autopay link. Outside check-in, Autopay does not wait for KYC.

- R53 (18 Sep, Sanchay on the call with Nimit, amounts confirmed in chat) A property can turn the platform fee line off, or set it anywhere from ₹58 to ₹118 a month (₹49+GST to ₹100+GST). The floor stops the line suggesting RentOk costs less than it does. Above the ceiling, the change is really a rent rise and goes through the rent change flow.

- R54 (18 Sep, Sanchay) A mandate counts toward the target only if a debit is queued for it, or it is waiting for its first due. An active mandate with nothing queued does not count, so the target cannot be met by Autopays that never collect.

- R55 to R61 (18 Sep, decided by Claude on Sanchay's instruction "u the expert, figure out & decide"; Sanchay can overturn any of them)
  - R55 Live payment links move from the old page to the new page in engineering steps, finished by 25 Sep. This is a safe rollout, not tenant waves (R37 unaffected). Electricity links stay on the old page until the new meter screen matches it.
  - R56 Before the next app release, the tenant app shows Autopay through a server-sent home announcement, because the frozen app cannot show a new card.
  - R57 When the WhatsApp number's daily limit binds, sends go first to tenants whose dues come soonest, and every tenant is reached before 30 Sep. This orders sending; it is not a priority group.
  - R58 An e-NACH tenant whose approved limit already covers her regular dues is not asked to approve again.
  - R59 Manual-schedule tenants are offered Option 2 only, because a fixed schedule cannot follow dates a manager sets.
  - R60 Outside check-in, the setup screen has one terms tick she sets herself, saved with the terms version and time, the same as check-in (#935).
  - R61 The property-level "Autopay off" switch is removed; only "required" can be turned off, and existing mandates keep running (settles #7055).

- R62 (18 Sep, Sanchay) Both options ship for 1 Oct, and the build tickets plan the full scope without trimming for the deadline; engineering finds how to build it in time. If a cut is ever needed, it follows a fixed cut order: Option 1 (the fixed-schedule mandate) is cut first and Option 2 stays, because Option 2 fits every tenant and Option 1 carries the most new risk on a money path. Every build ticket carries its place in the cut order; Sanchay makes any actual cut.

## Issues filed today (rentok-backend)

- #6995 P0 two Autopay engines can debit the same tenant twice.
- #6996 P1 Settlement V2 pays the owner the full rent when the owner chose to pay the Autopay fee.
- #6998 P1 Settlement V2 takes RentOk charges from the wrong total, can take them twice, and still pays them to the owner.
- #6999 P1 one month with nothing to collect ends a tenant's Autopay for good.
- #7000 P2 Autopay debits tenants short every month when rent includes GST.
- #7002 P1 a tenant who pays another way is still debited (skip field never written).
- #7003 P2 debit records store the approved amount, not the amount charged.
- Linked all five on epic #6846.

- I10 (17 Sep, Cashfree docs) Cashfree sends the pre-debit notice on standard charges; pause and plan change are not supported on on-demand mandates; at most 3 retries per billing cycle; a charge above the approved maximum needs a new mandate. Details in 15.
- #7004 P2 debit time sent in 12-hour format (noon).

## Walkthrough files

06 tenant, 07 manager and owner, 13 cost cover and rent change, 08 payment path code, 09 engines, routes, links, 10 legal, 11 systems map, 12 finance and operations.

## Sources gathered

- 15 and 16 Sep conversations (Wispr, NeoSapien); 10 Aug, 7 Sep, 11 Sep, 14 Sep conversations.
- Code in five repos (17 Sep); 30 GitHub issues; Linear (no Autopay items); payment page design record; Nimit's September plan; onboarding sheets.
- MDR FAQ and PIB release (15 Sep); research on Autopay rules and Cashfree pricing.
- Kamal's written plan and recording (17 Sep).
- Five walkthroughs running: tenant, manager and owner, finance and operations, legal (including TPAP), systems map.
