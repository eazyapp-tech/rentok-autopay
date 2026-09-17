# Code findings: two debit engines, open routes, links, receipts (17 Sep 2026)

From a helper agent under the finance walkthrough (backend origin/master, read-only); the engine query was re-read by hand.

## Two debit engines on the same table (check today)
- The older engine's bulk charge is still routed: `POST /payment/autopay/charge-subscription/bulk` (routes/payments.ts 389) calls `chargeSubscriptionBulk` (controllers/payment.ts 8470), which runs the older `AutoPayService.chargeSubscriptionBulk` (payment.ts 8476).
- Its query (services/autoPay/autopay.ts about 560 to 600) selects every row in the same `autopay` table with status active and an active tenant, on the tenant's rent day, excluding only five hardcoded properties. It does not look at the current engine's `autopay_debit_schedule`.
- The current engine creates a schedule for every tenant whose setup succeeds with a chosen day (autopayV2.ts handleAuthStatus), and its webhook now handles all properties (payment.ts 8282).
- **So if both scheduled jobs are running, a tenant outside those five properties can be debited by both engines.** Whether the older job still runs cannot be seen from the code (the trigger is an outside scheduler). A developer must confirm today, and the older route should be switched off before any push.

## Open Autopay routes (confirms #6816)
- `/v1/autopay/createSubscription`, `/chargeScheduledDebits`, `/webhook`, `/cancelSubscription`, `/details/:tenant_id`, `/editDetails` (routes/autopayV2.ts 6 to 17): no middleware at all.
- `/payment/autopay/webhook` (payments.ts 380): no auth. `/payment/autopay/charge-subscription` and `/bulk` (386, 389): only `HeaderValidator`.
- `/tenant/autopayDebitReminder` (tenant.ts 1067): no auth. `/property/send-autopay-reminders` (property.ts 1188): only `HeaderValidator`.
- The code's own comment (utils/commonFunctions.ts 1270 to 1273) says `HeaderValidator` never rejects anonymous callers; only `RequireAuth` does, and no Autopay route uses it. No webhook signature check found. Anyone can trigger debits, cancel, change dates, read details, or fake webhooks.

## Payment links and Autopay
- `generatePaymentLink` (payment.ts 3914) makes a `payment_page` short link, and expires the tenant's older ones (`expireOldShortLinks`, 4019). It returns a fake hardcoded `expires_at`.
- Nothing checks whether a bill is already scheduled for an Autopay debit (`autopay_debit_schedule_invoice` is never read by link code). A tenant or manager can pay by link a bill Autopay will also take (see file 08 for what happens then).

## Receipts and owner messages
- Receipts: `generateReceipt` (invoices.ts 337). Payment modes 203, 205, 206 and 210 all print as "RentOk Bank Transfer" (helpers/invoices.ts 1595 to 1598); Autopay is never named.
- Owner message `21_due_received` (payment.ts 2794, 3863; helpers/7510contants.ts 12212) has no Autopay marker.

## Cashless deposit (Eqaro)
- Separate product (eqaro entities, repositories, settlement routes); no shared path with Autopay.
