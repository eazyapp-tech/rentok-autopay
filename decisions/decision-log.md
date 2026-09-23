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
- R16 (17 Sep, after my one pushback) Rent above ₹15,000: one on-demand UPI Autopay mandate with a ₹15,000 limit; each month the rent is taken in parts of up to ₹15,000 (₹20,000 = ₹15,000 + ₹5,000; two or three debits). The split is shown to the tenant at setup; she approves once. e-NACH stays available but is not shown as a separate choice, only as a short FAQ answer. Cashfree's written confirmation still requested (not a blocker). *(Two corrections, noted 23 Sep. First, the "₹15,000 limit" in this line was replaced the same evening by R46: the limit she approves equals her full regular dues, and it is each debit, not the mandate, that stops at ₹15,000. Sanchay restated it on 23 Sep: "take the mandate amount to be 15,000 or greater". Second, the parts run one after another with a gap between them, and the gap is a setting rather than a fixed number: Kamal's launch room draws five minutes, Sanchay's example is two, "2 being our variable". Whether Cashfree accepts two debits in the same day is still the open question, not whether we split.)*
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

- R63 (19 Sep, Sanchay, after the 18 Sep meeting with Srijan) **Autopay promotion on the platform fee.** Tenants on Autopay get a recurring discount on the platform fee, for example ₹30 off a ₹50 fee, so they pay ₹20. The backend supports both forms, switchable per property: an instant discount on the bill (the first to run), and cashback or RentOk Coins after the debit. Experiments run by property, not by tenant. Conditions that keep it lawful:
  - the platform fee stays a flat amount on every payment method, cash included, never sized as a share of rent;
  - the discount is a promotion shown as "₹30 off with Autopay", never an extra charge on UPI link payments.

  **Four conditions added 22 Sep, after the check on whether a discount is lawful where a charge is not** (the reasoning and sources are in `discount-route.md` in the private repo, meetings folder for 18 Sep):
  - **the posted fee is real:** a tenant paying cash pays the same fee, and that is what proves the price is not a UPI price;
  - **nothing about the fee is worked out from the payment:** no share of rent, no 0.4% plus tax. The fee must not be computed from the payment at run time, and must not be set at "0.5% of average rent" on the ground that 0.5% is the UPI charge plus tax;

    **Correction, 22 Sep 2026, by Claude, not by Sanchay.** The four conditions above were added from `discount-route.md`, which is research, and this one first read "no share of rent, no 0.4% plus tax, **no band that rises with rent**". The last clause over-reached and Sanchay has since said so plainly: the manager app suggests the fee from the property's average rent, and ₹58 is a placeholder that cannot serve a property whose tenants pay ₹1,00,000. **A ladder of fixed published prices by rent band is ordinary pricing and is allowed.** What is not allowed is the arithmetic: a fee computed as a percentage of the payment, or sized to the UPI charge, is that charge under another name. The wrong clause is struck here rather than removed, because it was quoted in `surfaces/manager-app.md` before this correction. The ladder itself is proposed as open question 28 and is Sanchay's to rule;
  - **the discount is for the mandate and open to everyone:** any tenant, any UPI app, any bank, or e-NACH. Never tied to one app;
  - **no wording anywhere prices UPI:** "Save ₹30 with Autopay" is fine. "UPI costs 0.5% more", "MDR charges on UPI" and "flat ₹15 or ₹20 charge on rent payment" are not, and the last one is separately banned by the RBI rule that no charge may be levied on a customer for using a mandate. This applies to the product, the owner screens and our own internal documents.

  This changes N6 ("Autopay price" as a lower rent): the discount is on the platform fee, not on rent. R53's ₹58 floor would move if the fee is set at ₹50. **Open:** who funds the ₹30, RentOk or the property (recommended: RentOk, which is the merchant that saves the UPI charge).

- R64 (21 and 22 Sep, Sanchay) **One tenant-facing charge, and its amount is suggested from the property's average rent.**

  **The charge (21 Sep, confirmed and narrowed 22 Sep).** The tenant bears the property's charge by default, and management can take it onto itself instead. The switch lives in Autopay settings in the manager app.

  **What it is, and what it is not (22 Sep).** There is exactly one tenant-facing charge: the **Platform fee**. The old **Autopay setup fee and Autopay monthly fee are deleted and must not return**. Both are still live in code: the struck-out setup fee at web check-in (marketplace#938) and the two "who bears it" dropdowns in manager web property settings, where the unset default is RentOk. D4 removes them.

  **Why this does not reopen R11** (this paragraph is Claude's reasoning, not Sanchay's words, and is here because R64 reads as a contradiction without it). R11 says the tenant must not bear Autopay charges. The Platform fee is not an Autopay charge: it is the property's charge for running the tenancy on RentOk, it is the same amount on cash, bank transfer, link and Autopay, and a tenant who never uses Autopay pays it too. That is also what keeps it lawful under the RBI e-mandate framework 2026 para 10(a), which bans a charge for availing the mandate, and under the Finance Ministry UPI MDR FAQ Q34, which bans passing the UPI charge to a customer. A charge that varied by method, or that existed only for Autopay tenants, would be the thing both forbid.

  **The amount (22 Sep).** **₹58 is a placeholder, not the price.** The manager app suggests a fee from the property's average rent, and a property whose tenants pay ₹1,00,000 does not get the same figure as one whose tenants pay ₹8,000. This modifies the flat default in R42 and R43, which stays as the middle of the range rather than the answer, and puts R53's ₹58 to ₹118 band in question: measured on 22 Sep, 57.6% of tenants sit at properties below that floor and 5.7% above the ceiling.

  **The one thing the amount must never be.** A ladder of fixed published prices by rent band is ordinary pricing. A fee **computed** as a percentage of the payment, or set at 0.5% because 0.5% is the UPI charge plus tax, is that charge under another name. Ladder, never rate. This is R63's second condition as corrected on 22 Sep.

  **Still open:** the two numbers in the ladder, its floor and its ceiling, are open question 28, with a proposal and the portfolio bands in `research/platform-fee-ladder.md`.

- R65 (22 Sep, Sanchay, answering open question 28) **The Platform fee ladder, and its ends are suggestions.**

  **The ladder runs from ₹58 to ₹399**, suggested by the property's average rent, with the rungs and the portfolio bands in `research/platform-fee-ladder.md`.

  **Management can set any amount above ₹399 or below ₹58.** The two ends are where the suggestion stops, not where the setting stops.

  **This replaces the hard band in R53**, which allowed ₹58 to ₹118 and nothing outside it.

  **Below ₹58, the property is absorbing part of RentOk's charge.** RentOk still charges management ₹49 plus GST per billed tenant (R22, R35), so a property that sets ₹30 is passing on ₹30 and paying ₹28 itself. This makes absorbing continuous rather than the on or off choice it was, and it costs RentOk nothing, because RentOk's charge does not change.

  **Above ₹399, nothing extra is required beyond the notice rule.** R53 said a change above the ceiling was really a rent rise and went through the rent change flow; with no hard ceiling that escalation has nothing to trigger on, so it goes. **What survives from R53 and applies to every change, up or down: notice is delivered and recorded before the new amount starts (R13), and a rise that takes a tenant above her approved limit is flagged in the preview and she is asked to approve again.** (The removal of the escalation is Claude's reading of the ruling, not Sanchay's words.)

  **What keeps the fee lawful is not the band, and never was.** Three things do, and all of them are untouched: the fee is the same on every payment method including cash (R15, R63's first condition); it is never computed from the payment (R63's second condition as corrected on 22 Sep); and nothing anywhere prices UPI (R63's fourth condition). A manager typing his own figure is his pricing decision. What RentOk must never do is suggest a figure worked out from a share of rent.

  **Recommended guardrail, not ruled:** when a manager sets an amount well outside the ladder, show a plain warning that his tenants see it on every bill and that it needs notice before it starts. **It must not show the amount as a share of rent**, which is the arithmetic R63's second condition forbids.

- R66 (22 Sep, Sanchay, answering open question 29) **The "Eligible for tenants joined since" control is removed.**

  It is on both manager surfaces, it saves a date to the property and writes an activity log line, and **no Autopay path reads it**. An owner who sets it is told his older tenants are excluded, and every one of them is still asked. It also travels: the manager app's copy-to-properties action copies the date to every property in the copy (`copy_details_bottom.dart:341`, origin/main).

  **The order it comes out in, because the two front ends move at different speeds.**
  1. **The backend stops accepting the field.** That ends both writers at once, including the bulk copy, and it is one place: `src/controllers/property.ts:9450` and `:9715-9737`, origin/master. Do this first.
  2. **Manager web removes the control** (`PaymentSettings.tsx`, `types/propertySettings/settings.ts`). D4 rewrites that screen to three items and does not list this one, so the removal lands with D4.
  3. **The manager app removes it in the release after 1 October** (`autopay_settings_bottom.dart`, `dues_payment.dart`, `copy_details_bottom.dart`, and the config model). Until then the app can still show it, and with step 1 done it saves nothing.

  **The saved dates: nine properties**, eight of them with Autopay on, measured 22 Sep. One is dated 2007, which is what a control nobody reads looks like after a year. **Null the nine**, because the danger was never the control but the data waiting for someone to wire it up. Dropping the column itself is cleanup after 1 October, not now.

  **This is not a change to R37.** There are still no waves. It removes a control that looked like one and did nothing. Filed as rentok-backend#7162.

- R67 (23 Sep, Sanchay) **Rent above ₹15,000 is collected as several debits a set gap apart, and the gap is two minutes by default.**

  His words: "we take the mandate amount to be 15,000 or greater... hit multiple reductions subsequently, within a gap of, let's say, 2 minutes, 2 being our variable. It can be 5, it can be 1."

  **Three parts to this.**
  1. **The mandate is approved at her full amount**, not at ₹15,000. *(Replaced 23 Sep by R68: she approves a ceiling set from her fixed dues, never above ₹15,000. Noted by Claude.)* This was already R46 and is restated here because R16's own text still said ₹15,000 and has now been annotated. It is each debit, never the mandate, that stops at ₹15,000.
  2. **The parts run one after another on the same day**, each with its own pre-debit notice, and the rent reads paid only when the last one lands.
  3. **The gap is a setting with a default of two minutes.** Not a hardcoded wait. Kamal's launch room draws five minutes; two is the default because it is the value Sanchay named, and the setting is what matters: if Cashfree turns out to refuse same-day parts, the fallback to one part a day is then a configuration change rather than a rebuild.

  **What this rests on, and neither is in hand.** Cashfree must accept two debits on one mandate inside 24 hours, which PhonePe has confirmed and Cashfree has not (Cashfree question 1). And **AFA and 2FA must be enabled on RentOk's Cashfree account**, which Kamal's launch room says they are not (Cashfree question 11). Until both land, one part a day collects the same money more slowly.

  **One consequence worth naming, and it is Claude's reading rather than Sanchay's words.** `research/legal.md`'s addendum of 17 September assessed this split at **24 to 48 hours** between parts, and its main worry was that "bank velocity checks exist to catch exactly that pattern". A two-minute gap is a sharper version of the same fact pattern, not a different one: two debits two minutes apart read more like one payment cut in half than two debits on consecutive days do. The risk named there is declines, or Cashfree acting on all RentOk mandates rather than only the split ones. **This does not change the ruling**, because the purpose of the split is to stay under RBI's PIN threshold and not to avoid a charge (Autopay has no prescribed MDR, so splitting saves nothing there, which is also why N1 does not reach it). It does mean **the gap goes into the written question to Cashfree alongside the same-day question**, so the answer covers the interval we actually intend to use.

- R68 (23 Sep, Sanchay) **The Autopay ceiling: her fixed monthly dues plus ₹2,000, rounded up to the next ₹5,000, never above ₹15,000. Every number in that rule, and R67's gap, is a backend setting, not a constant in any app.**

  His words, approving the rule: "we will keep these numbers as variables, to be able to change from backend".

  **What the ceiling is.** The largest single debit her mandate allows, which she approves once at setup. It comes from his 22 Sep implementation call: ₹12,000 of fixed dues gets a ₹15,000 ceiling so a variable electricity bill fits without asking her again. On her day, Option 2 takes whatever monthly dues are open, and anything above the ceiling is split into parts of up to the ceiling, the set gap apart (R67). So the ceiling never needs approving again.

  **Worked through.** ₹6,000 of fixed dues gets ₹10,000. ₹12,000 gets ₹15,000, his own example. ₹18,099 gets ₹15,000, and her ₹18,099 is taken as ₹15,000 plus ₹3,099. It stops at ₹15,000 because a single debit above that needs her PIN (RBI e-mandate framework, para 8(a)), so a higher ceiling buys nothing.

  **The four settings, with today's values.** Per-debit cap ₹15,000. Buffer ₹2,000. Rounding step ₹5,000. Gap between parts two minutes. They live in one row of the backend's existing `internal_config` table, which four other features already read, so changing any of them needs no release of any app.

  **One place computes the ceiling: the backend.** It is the same number the backend sends Cashfree as the mandate's maximum, so the screen and the mandate cannot disagree. The apps display it, and never recompute it.

  **"Fixed monthly dues"** means her recurring dues of a fixed amount: rent, fixed packages such as food, and the platform fee. Variable dues such as metered electricity are left out of the ceiling but are still taken on her day if they are open (R18). Late fines are never taken by Autopay (R29).

  **This corrects two lines, marked here rather than rewritten.** R67 and the note under R16 both say the mandate is approved "at her full amount". That wording came from Claude's design note under R46, "the limit equals her regular dues", which is now replaced by this ruling. What both got right stands: each debit stops at ₹15,000.

- R69 (23 Sep, Sanchay) **"All my monthly dues" takes the current month only, by default. Older unpaid bills are not swept into her debit.**

  His words: "current month only, go ahead, can be selected as default."

  **What "current month" has to mean.** The rent period her debit is paying, not the calendar month the debit falls in. They differ when her window crosses the month end (R41): rent due on the 30th, debit on the 3rd. The engine today uses the calendar month, so it would miss that rent; filed as rentok-backend#7179. For the ordinary case the engine already does this: it ties each debit to that month's bills by id, not oldest first, and 1,392 of 1,408 bills linked in production sit in the right month.

  **Settled the same day as R70, below:** the edit belongs to what she pays today.

- R70 (23 Sep, Sanchay) **The amount she can edit is what she pays today, never the monthly debit.**

  His words: "yes, edit belongs to today's payment, go ahead."

  **Two amounts at setup, kept apart.** What she pays today goes through the payment page's existing pay screen, where she may type more or less only if her property allows partial payment (78.6% of tenants can). Older unpaid bills are cleared there, on purpose. What autopay takes each month follows R69, the current month only, and is never editable: the bank fixes it at the notice 24 hours ahead, and a debit she has to adjust each month is no longer automatic. The partial payment setting therefore changes what she may type today and nothing about the monthly rule.

  **The setup sheet shows both,** the monthly terms and what is still hers to pay now, and the second is the same number as the page's "Pay all", computed in one place.

  **Paying today inside the same approval ("pay and set up", his 22 Sep call) waits for Cashfree:** whether the approval can carry a real first payment, kept rather than refunded, and up to what amount (Cashfree question 2). Until then she pays today first, then sets up.

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
