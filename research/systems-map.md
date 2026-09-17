# Systems map: money features and Autopay (17 Sep 2026)

> Written 17 Sep, before the two-option design (R46). The feature interactions still hold; the mandate design does not.

Agent (opus), lines read by hand across five repos (backend master 33b64a1e3; manager Flutter 2e91d8ce; manager web 58583ff3; tenant app afea1abe; marketplace fd5a57d9). "Not confirmed" marks inferences. Product word should be "Autopay".

## How the debit works today
- The monthly job raises rent for the month first (autopayV2.ts 300), then takes only unpaid invoices whose due type is exactly "Rent" in that calendar month (802 to 817), capped at approved amount minus the monthly fee (318 to 339). Anything above the cap stays unpaid, silently.
- Job runs the day before her day (autopayV2Helpers.ts 75); Cashfree told to debit next day (autopayV2.ts 355 to 360).
- Failure: back to pending, retried next day, up to 5 (helpers 9; autopayV2.ts 260, 693 to 695).
- Mandate: on-demand, ceiling = approved amount, 60 months, ₹1 refundable authorisation (cashfree.ts 459 to 467). No ₹15,000 handling anywhere.
- Recorded through /payment/addPayment as mode 205 against scheduled invoice ids (helpers 235 to 264; autopayV2.ts 605 to 614).
- One grace number sets both the debit window (helpers 11 to 16, 38 to 69) and the late fine start (dues.ts 116 to 125); setup raises it (autopayV2.ts 864 to 870); cancel empties it (837 to 839); 1000 means fine off (tenant.ts 7563, 23307 to 23319).
- `resolved_payment_id` skip check (autopayV2.ts 254) is dead: never set.
- No login on any Autopay route (routes/autopayV2.ts 6 to 17); change-date has no once-a-month limit (autopayControllerV2.ts 159 to 205).
- Transaction row stores the approved amount, not the debited amount (autopayV2.ts 440).

## Feature interactions (existing)

| Feature | In the debit? | Interaction |
| --- | --- | --- |
| Rent generation and due day (dues.ts 348, 1429, 1488) | Yes | Autopay also raises rent for its month; duplicate protection not confirmed. #6829 due-day ruling not built. |
| Dues packages (packages, tenant_packages, packageSubscription; cron dues.ts 1110) | Only due type exactly "Rent" | Package rent under another name is never debited (one property already special-cased, dues.ts 137 to 139). #6989: property-wide package edits reprice tenants past the approved amount. |
| Late fine and grace (dues.ts 41, 116 to 125; property.ts 10640 to 10700; tenant.ts 1226 to 1232) | No | Setup delays her fine; cancel wipes 1000; retries continue past grace so fines land mid-retry; fine is its own due and needs a link. |
| Scheduled rent increase (#6765; services/cron/scheduledRentIncrease.ts 125 to 170) | Capped | Raises rent, ignores approved amount; no re-approval, no notice. |
| Renewal auto increase (PropertyService.ts 1884, 2124) | Capped | Same (increase code not confirmed). |
| Room change (v1/change-room/service.ts 52, 151, 1245) | Capped | Same; can change property without recalculating the window. |
| Food, mess, add-ons (property.ts 2295) | No | Separate due, needs a link; crosses ₹2,000 at typical prices. |
| Prepaid electricity (electricity_meter.ts 301; payment.ts 4839) | No | Separate small payment fits the plan. #6856 P0: anyone can recharge without login. |
| GST on packages (packagesFilterHelper.ts 343; invoiceMetaData.ts 14) | Yes if on rent | Rent plus GST exceeds the approved amount based on plain rent (autopayV2.ts 86 to 103); not confirmed. |
| Pro rata first and last month (dues.ts 1012) | Yes | Handled (lower of owed and cap). |
| Platform fee ₹30 (constants.ts 81 to 135; payment.ts 1904 to 1913) | No | FNF only; separate due keeps a monthly link alive; allocation order may be skipped (not confirmed). |
| Gateway charges (payment.ts 241 to 243, 1300, 1983; receipts invoices.ts 583 to 586, 872 to 875) | Link path | Taken from the request; web pay pages send 0 but the server has no guard forcing 0 on UPI. After 15 Oct, reads as MDR pass-through if used. |
| Autopay monthly fee (helpers 122 to 171; property.ts entity 962 to 976; controller 9282) | Yes | "RentOk pays" treated as tenant (#6880); web sends 3; Flutter fallback "RentOk"; setup payer RentOk only; no GST line or service name. |
| Advance adjust (helpers/invoices.ts 521 to 529; paymentService.ts 2498) | Reduces | Debit takes only what is unpaid. |
| Wallet, FlexiPe | n/a | Settlement side. |
| RentPass | No | A separate membership product (vouchers), not a dues discount; the dues discount is the credits system (payment.ts 2013 to 2035), which the Autopay path never applies (credit_obj not sent). |
| Discounts (owner discount) | Indirect | Lowers the rent invoice; debit follows. |
| Partial payments, allocation (constants.ts 37 to 78; payment.ts 1888 to 1913) | Yes | Capped leftover stays partial. |
| Cash with OTP (paymentService.ts 344 to 424) | Clashes | Recording cash never touches the schedule; if the charge is already queued, she is debited too. |
| Settlement (payment.ts 2313 to 2323, 2380 to 2392; settlementFlow.ts 538 to 541) | n/a | Settlement V2 ignores owner-paid fee (#6996). |
| Refunds (services/refunds/refunds.ts 273) | n/a | No Autopay refund path. |
| Deposit, cashless deposit (Eqaro) | No | Deposit above ₹2,000 by link carries MDR; no Autopay link. |
| Payment links (payment.ts 3914; short_link.ts 25) | Clashes | No check for a queued debit; #6821 "Amount" text. |
| Receipts, owner message (invoices.ts 337; payment.ts 2794) | n/a | Mode 205 prints "RentOk Bank Transfer"; no Autopay marker (#6835). |
| Legacy V1 engine (payment.ts 7447 to 7540, 8476) | Risk | Still routed; possible second debit (#6995). |
| Eviction, delete (evictionService.ts; autopayControllerV2.ts 98 to 109) | n/a | Mandate stays active; settlement ignores pending debits. |
| Multi-party, co-tenants (constants/checkinLinks.ts 80) | n/a | Parties have no billing, so no Autopay; no shared-rent split. |
| Parent app (sendReminderCore.ts 70) | n/a | Parents keep getting links; cannot own the mandate. |
| Bulk and automated reminders (sendReminderCore.ts 56 to 122; invoices.ts 7105, 7130) | n/a | No Autopay filter (#6830). |
| Autopay reminders (propertyDetails.ts 1495 to 1547) | n/a | Check-in link plus ignored flag; notice locked to a test record (tenant.ts 27986). |
| Hardcoded Autopay properties (tenant.ts 8171 to 8180) | n/a | Four forced on, one mandatory. |
| White label (waba_phone_map, #6884) | n/a | Cashfree still shows EAZYAPP. |
| Reports (v1/homepage/service.ts 212) | n/a | No Autopay report. |
| e-NACH (services/tenant/checkIn.ts 3829) | n/a | Only for the CirclePe journey. |
| Easebuzz virtual account (easebuzzQuickTransfer.ts 364) | n/a | One master payout account, not per tenant. |
| Tenant app banner (accounts_dues.dart 76 to 84) | n/a | Tap handler is a comment; status never saved. |

## Planned work and the push
- Release 36 (internal and beta 21 Sep; public 24 Sep; offsite 24 to 27 Sep; no staging, no feature flags; Linear has no Autopay item; REN-927 says never tested).
- Platform fee ₹30 for all: put it inside the same debit as its own line, same for every method; as a separate due it keeps a link alive.
- /p2: merged (#775, #892, #902), setup off, not routed; the biggest lever; needs #6816, #6825, marketplace #771.
- Onboarding revamp: new properties start with Autopay on and 7 days grace; rental options merging into packages means rent may not be due type "Rent"; fix the match first.
- WhatsApp split: owner messages only so far; tenant Autopay templates and number needed.
- BBPS with IDFC: discovery only; not a 1 Oct path.
- Multi-party signing: the place for the consent clause.

## 25 interaction pairs and fixes
1. Routes without login: #6816, #6861 first.
2. Link or cash payment after the debit is queued: any payment resolves the schedule; cancel the queued charge or refund automatically.
3. Reminder links for Autopay tenants: #6830 filter in sendReminderCore.ts and invoices.ts 7105.
4. Any rent rise above the approved amount: ask for a new approval, tell tenant and manager, flag.
5. Cancel wipes grace: save and restore, better split (#6817).
6. Setup delays late fine: split grace (#6817 A).
7. Retries and late fine: no fine while retries are live; after the last retry, fine from the original due day.
8. Chosen day vs due day: #6828 then #6829; interim 7-day window.
9. Check-in picker vs backend window: picker reads the backend window.
10. Eviction or delete: cancel the mandate; settlement shows pending debits.
11. Retries vs rule: 1 plus 3, notice before each, fallback day.
12. Notice locked: remove filter, daily job, template.
13. Fee payer bug: tenant default, management switch (#6880).
14. Fee vs MDR rule: named service fee, flat, GST line, shown before approval (see file 10 on the e-mandate charge rule).
15. Setup fee payer RentOk only: tenant default and management.
16. Platform fee: inside the debit, or suppress its link for Autopay tenants.
17. Other dues by link: phase 2 ceiling covers all monthly dues; small dues stay separate.
18. "Rent" name match: match on due category.
19. Above ₹15,000: mark, warn "approve in your UPI app", offer e-NACH.
20. Failed debit: #6817 reasons; tenant message with pay option; manager failed state.
21. Bulk reminder to step 1: direct link, single and chosen sends.
22. Tenant app status: save it; setup, manage, cancel.
23. Hardcoded properties: delete once default-on.
24. V1 engine: #6995.
25. Webhook status case: store lowercase; backfill (not confirmed).

## Missing for the ideal system
Separate grace; one "someone paid" hook; re-approval on rent change; Autopay refund path; pause; tenant self-service; tenant messages; manager tools on app and web; owner signal; direct link and payment-page tick; above-₹15,000 handling with e-NACH; per-tenant virtual account; service-fee invoice line; analytics and report; kill switch; default-on migration; consent in agreement and a real tick; recognisable merchant name; Linear tracking.

## Build order proposed by the agent (17 Sep to 1 Oct)
- 17 to 18 Sep: A security (#6816, #6861); B money bugs (#6880 and payer defaults, lowercase status, #6817 reasons, confirm V1 off, remove notice test filter).
- 18 to 20 Sep, after A: split grace; double-charge guard with #6830; cancel on eviction and delete; rent-rise guard; due-category match.
- 19 to 20 Sep: #6828 then 7-day window; picker fix and honest copy.
- 20 Sep: notice job and success and failure templates, retries 1 plus 3; kill switch; default-on migration script (not run).
- 21 Sep internal and beta release; first group of large operators on; on-call through the offsite.
- 28 to 30 Sep: #6825 then /p2 setup on and /p routed (analytics first); tenant app status, manager status column and single sends; #6829; run default-on migration; platform fee inside the debit and service fee with GST.
- After 1 Oct: re-approval, refunds, pause, e-NACH above ₹15,000, virtual accounts, all dues in one approval, owner messages and reports.
- Agent's note: the target depends on /p2 reaching the 209,000 link recipients; steps must merge by 21 Sep or switch-on moves to 28 Sep. (Release timing is Sanchay's call.)

Open checks: duplicate rent between Autopay and the monthly job; Settlement V2 fee (now #6996); Cashfree status casing; paying an already-paid invoice (file 08); gateway charge location (file 08); RentPass and refunds (file 08 and this file).

## Second pass (resumed agent, 17 Sep), new findings, checked by hand
1. A month with nothing to collect ends future debits: the two "no unpaid invoices" skip branches never book next month (autopayV2.ts 313 to 316, 341 to 344). Filed #6999 (P1).
2. Double charge path confirmed again (resolved_payment_id never set; payment call picks invoices without a paid check). Covered by file 08 and #6995 for the engine side.
3. GST on rent under-collected: approved amount sized on plain rent (autopayV2.ts 86 to 103; check-in plan_amount), invoice includes GST (dues.ts 855 to 858). Filed #7000 (P2).
4. The monthly fee is a hidden amount kept from settlement, not a named line with GST (helpers 141 to 201).
5. Tenant app banner shows only when she owes nothing and its button only pops a test message (accounts_dues.dart 73 to 84); profile row reads a saved value (whether it is ever saved not confirmed; the first tenant-app trace found no writer).
Other: 3, 6 and 12-month plans use other due-type names, so Autopay never collects them (dues.ts 1429); late fines can be moved onto the deposit monthly (adjustLateFine.ts); Autopay hard-codes the Asia/Kolkata time zone (helpers 8) while time zone work runs 28 Sep to 5 Oct; #6851 (payments confirmed without the gateway) belongs with the security lane.
The agent again recommended a first-group rollout for 1 Oct; that conflicts with R1 and is not adopted.
