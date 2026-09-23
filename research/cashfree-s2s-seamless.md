# Cashfree's S2S flow for Autopay, and how much of it we already use (23 Sep 2026)

**Cashfree calls it "Seamless"**, also "custom checkout" or "API-based integration". The opposite is
**"Hosted checkout"**, where Cashfree's own page collects the approval. Read through Context7
(`/websites/cashfree`), 23 September.

## The Seamless flow, step by step

| Step | Call | What happens |
| --- | --- | --- |
| 1. Create the mandate | `POST /pg/subscriptions` | Plan, customer, authorisation amount. Returns a `subscription_session_id`. Subscription is `INITIALISED` |
| 2. Raise the approval | `POST /pg/subscriptions/pay`, `payment_type: "AUTH"`, `payment_method.upi.channel` | Returns the UPI data for **our** screen: app links per UPI app (intent) or a `upi://mandate?...` string (QR). She approves in her UPI app |
| 3. Hear the result | Webhooks `SUBSCRIPTION_AUTH_STATUS`, `SUBSCRIPTION_STATUS_CHANGED` | `ACTIVE`, or `BANK_APPROVAL_PENDING`, `CUSTOMER_CANCELLED`, `CUSTOMER_PAUSED`, `LINK_EXPIRED` and others |
| 4. Send the notice (controlled flow) | `POST /pg/subscriptions/pay/controlled/notify-mandate` | The pre-debit notice for the exact amount, before the debit window |
| 5. Take the debit | `POST /pg/subscriptions/pay`, `payment_type: "CHARGE"` | Amount and schedule date. Result by `SUBSCRIPTION_PAYMENT_SUCCESS` or `SUBSCRIPTION_PAYMENT_FAILED` |
| 6. Check when a webhook is missed | `GET /pg/subscriptions/{id}` | Status and approval details |

**UPI Collect is being withdrawn** (NPCI, on Cashfree's own page). Seamless merchants must use
**intent on mobile and QR on desktop**, and pass the customer's device details.

## What RentOk uses today (`rentok-backend` origin/master, `eazypg-marketplace` origin/main)

| Step | Today | Where |
| --- | --- | --- |
| 1. Create | **Seamless** | `payment.ts:7463`, `utils/Cashfree/cashfree.ts:450` |
| 2. Approval | **Hosted**: Cashfree's page through the JS SDK, `cashfree.subscriptionsCheckout({ subsSessionId })` | check-in `components/autoPayDetails.js:83`; old payment page `[eazypgId]/checkout.js:224` |
| 4. Notice | **Not called anywhere** | no hit for `notify-mandate` in the backend |
| 5. Debit | **Seamless** | `payment.ts:7568` (`payment_type: "CHARGE"`), `cashfree.ts:537` |
| 6. Check | Seamless | `payment.ts:7614` |

## What this means for the build

- **R44 puts the approval on RentOk's own screen.** That is step 2 in Seamless mode: one more
  call on an endpoint we already use for debits, with `payment_type: "AUTH"`, and the setup sheet
  drawing the intent buttons or the QR itself. Kamal's forwardable QR is `channel: "qrcode"`.
- **Option 2 depends on step 4, and nothing calls it yet.** The feature map has RentOk sending the
  notice itself so the amount can vary each month. Until `notify-mandate` is built, the
  "all monthly dues" debit has no notice to rest on. This belongs to ticket B1 (`rentok-backend#7078`).
- **Every call is to `api.cashfree.com`, the live host**, which is the missing sandbox of
  `rentok-backend#6866`.
