<!-- Captured 18 Sep 2026 from Cashfree's Subscriptions documentation (https://www.cashfree.com/docs/). Cashfree's live page is the authority. -->

> ## Documentation Index
> Fetch the complete documentation index at: https://www.cashfree.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# UPI One-Time Mandate

> Learn how to use UPI one-time mandates with Cashfree to block funds upfront from a customer account and capture payment later upon fulfilment.

UPI One-Time Mandate (OTM) is a secure, RBI-compliant payment workflow that allows you to block a specific amount from a customer's UPI-linked bank account upfront and debit it only after the order or service has been fulfilled.

This two-step block-then-capture model gives you confidence in fund availability before debiting, and gives customers a transparent authorisation trail in their UPI app.

## Key benefits

UPI OTM offers the following benefits:

* **Guaranteed fund availability**: You block funds at order time and capture only after fulfilment.
* **Customer trust and transparency**: Your customers approve the mandate in their UPI app and see the block in real time.
* **Flexible capture**: You can capture any amount up to the authorised order value.
* **Auto-release on void**: If the order is cancelled, funds are unblocked through a simple void request to the [Preauthorisation API](/docs/api-reference/payments/latest/payments/authorize).
* **UPI channel support**: You can use UPI Collect, UPI Intent, or UPI QR based on your checkout experience.

## Use cases

Use UPI OTM when you need to confirm payment availability before finalising an order.

Common scenarios include:

* **IPO applications**: Reserve funds for ASBA requests and debit only if the allotment succeeds.
* **Insurance approvals**: Block the premium amount until underwriting is completed.
* **Variable utility or charging services**: Hold funds when the final amount is not known at the time of booking.
* **Healthcare and hospital services**: Reserve a provisional amount while insurance coverage or treatment costs are confirmed.
* **Rental deposits**: Hold a refundable deposit and charge only for actual damages.
* **Travel and hospitality reservations**: Reserve funds for bookings while preserving flexibility for cancellations.
* **Limited-stock product launches**: Reserve funds for high-demand orders and collect payment only once the order is confirmed.

<Tip>Set `approve_by` to a short window to reduce abandoned mandates, and choose `start_time` and `end_time` based on your fulfilment SLA.</Tip>

## UPI OTM lifecycle

The UPI OTM lifecycle consists of four stages. Each stage maps to a Cashfree API call.

1. **[Create an order and payment session](#create-an-order)**: Create an order with the [Create Order API](/docs/api-reference/payments/latest/orders/create), then initiate a UPI mandate payment session with the [Order Pay API](/docs/api-reference/payments/latest/payments/pay) using `authorize_only: true` to block funds without immediately debiting the customer's account.
2. **[Get customer approval to block funds](#create-the-upi-mandate-session)**: Your customer approves the mandate in their UPI app. You receive a `SUCCESS` webhook, and the funds are blocked without immediate debit.
3. **[Capture the mandate on fulfilment](#capture-the-mandate)**: After you fulfil the order, call the [Preauthorisation API](/docs/api-reference/payments/latest/payments/authorize) with `action: CAPTURE` to debit the blocked amount.
4. **[Void the mandate or process a refund](#void-the-mandate)**: If the order is cancelled before capture, call the [Preauthorisation API](/docs/api-reference/payments/latest/payments/authorize) with `action: VOID` to release the block. If the order is already captured, create a refund with the [Create Refund API](/docs/api-reference/payments/latest/refunds/create) instead.

## Supported UPI channels

UPI OTM works across the following channels:

| `channel` value | Channel name | When to use                                                              |
| --------------- | ------------ | ------------------------------------------------------------------------ |
| `collect`       | UPI Collect  | Cashfree sends a collect request to the customer's UPI app.              |
| `link`          | UPI Intent   | A deep link opens the customer's UPI app directly on mobile.             |
| `qrcode`        | UPI QR       | A QR code is generated for the customer to scan and approve the mandate. |

## Integrate the UPI OTM flow

Use the following steps to create orders, start a UPI mandate session so customers can approve a block, capture or void the authorisation, and issue refunds after capture.

<Steps>
  <Step id="create-an-order" title="Create an order and payment session">
    Create an order with Cashfree using the [Create Order API](/docs/api-reference/payments/latest/orders/create) and your order and customer details.

    Use the following cURL example as a template when you call the API from your application.

    <Accordion title="Sample create order request">
      ```bash title="Request sample" theme={"dark"}
      curl --request POST \
          --url https://api.cashfree.com/pg/orders \
          --header 'x-client-id: <CLIENT_ID>' \
          --header 'x-client-secret: <CLIENT_SECRET>' \
          --header 'Accept: application/json' \
          --header 'Content-Type: application/json' \
          --header 'x-api-version: 2023-08-01' \
          --data '{
          "order_amount": 100.00,
          "order_currency": "INR",
          "order_id": "devstudio_4809486",
          "customer_details": {
              "customer_id": "devstudio_user",
              "customer_phone": "8474090589"
          },
          "order_meta": {
              "return_url": "https://www.cashfree.com/devstudio/preview/pg/web/checkout?order_id={order_id}"
          }
      }'
      ```
    </Accordion>
  </Step>

  <Step id="create-the-upi-mandate-session" title="Create UPI mandate session to block funds">
    Create the OTM transaction with Cashfree using the [Order Pay API](/docs/api-reference/payments/latest/payments/pay).

    The sample below uses UPI Collect; you can adapt the payload for your channel.

    <Accordion title="Sample UPI Collect mandate request">
      ```bash title="UPI Collect" theme={"dark"}
      curl --request POST \
          --url https://api.cashfree.com/pg/orders/sessions \
          --header 'x-client-id: <CLIENT_ID>' \
          --header 'x-client-secret: <CLIENT_SECRET>' \
          --header 'Accept: application/json' \
          --header 'Content-Type: application/json' \
          --header 'x-api-version: 2023-08-01' \
          --data '{
          "payment_method": {
              "upi": {
                  "channel": "collect",
                  "upi_id": "testsuccess@gocash",
                  "authorize_only": true,
                  "authorization": {
                      "approve_by": "2024-07-02T10:20:12+05:30",
                      "start_time": "2024-09-21T12:34:34Z",
                      "end_time": "2024-10-22T12:34:34Z"
                  }
              }
          },
          "payment_session_id": "sessionid"
      }'
      ```
    </Accordion>

    For UPI Intent or UPI QR, use the following `channel` values:

    * `link` for UPI Intent
    * `qrcode` for UPI QR

    Cashfree calls the acquiring bank to create an OTM transaction. If the customer approves the mandate, you receive a `SUCCESS` response and a webhook notification. The amount is blocked in the customer's account, but no amount is debited at this stage.

    <Note>The mandate blocks funds but does not debit them immediately. Capture the amount only when you are ready to complete the transaction.</Note>
  </Step>

  <Step id="capture-the-mandate" title="Capture the mandate">
    To capture the mandate, call the [Preauthorisation API](/docs/api-reference/payments/latest/payments/authorize) with the `CAPTURE` action.

    <Note>The captured amount must be less than or equal to the order amount.</Note>

    Use the following cURL example when you send a capture action for the order.

    <Accordion title="Sample capture request">
      ```bash title="Capture mandate" theme={"dark"}
      curl --request POST \
           --url https://api.cashfree.com/pg/orders/<ORDER_ID>/authorization \
           --header 'Accept: application/json' \
           --header 'x-client-id: <CLIENT_ID>' \
           --header 'x-client-secret: <CLIENT_SECRET>' \
           --header 'Content-Type: application/json' \
           --header 'x-api-version: 2023-08-01' \
           --data '{
        "action": "CAPTURE",
        "amount": 100
      }'
      ```
    </Accordion>

    Cashfree calls the acquiring bank to capture the mandate. If the capture succeeds, the payment amount is settled to you according to the settlement cycle.

    In most cases, capture succeeds immediately. For a small percentage of requests, you receive a failure response and the final outcome is confirmed later. For details on handling these cases, see [Capture error codes and handling](#capture-error-codes-and-handling).
  </Step>

  <Step id="void-the-mandate" title="Void the mandate or process a refund">
    Choose one path: void releases a block only before capture; refund applies only after capture. You do not run both for the same order.

    To void the mandate before capture, call the [Preauthorisation API](/docs/api-reference/payments/latest/payments/authorize) with the `VOID` action.

    Use the following cURL example when you void an authorisation.

    <Accordion title="Sample void request">
      ```bash title="Void mandate" theme={"dark"}
      curl --request POST \
           --url https://api.cashfree.com/pg/orders/<ORDER_ID>/authorization \
           --header 'Accept: application/json' \
           --header 'x-client-id: <CLIENT_ID>' \
           --header 'x-client-secret: <CLIENT_SECRET>' \
           --header 'Content-Type: application/json' \
           --header 'x-api-version: 2023-08-01' \
           --data '{
        "action": "VOID"
      }'
      ```
    </Accordion>

    Cashfree calls the acquiring bank to void the mandate. If the void succeeds, the blocked amount is released from the customer's account.

    <Note>If the bank returns a failure response, Cashfree automatically retries the void up to three times. If the void does not succeed, the blocked funds are released automatically at mandate expiry (`end_time`).</Note>

    <a id="process-a-refund" style={{ scrollMarginTop: '5rem' }} />

    To refund after capture, use the [Create Refund API](/docs/api-reference/payments/latest/refunds/create) instead of void. A refund can be initiated only after the transaction is captured. Use the following steps to process a refund:

    1. Call the [Create Refund API](/docs/api-reference/payments/latest/refunds/create) to initiate the refund.
    2. Cashfree submits the refund to the acquiring bank for processing.
    3. If processing succeeds, the amount is refunded to the customer.
    4. If the refund fails, Cashfree retries every six hours for up to five attempts.

    Use the following cURL example when you complete step 1 with the [Create Refund API](/docs/api-reference/payments/latest/refunds/create).

    <Accordion title="Sample create refund request">
      ```bash title="Create refund" theme={"dark"}
      curl --request POST \
          --url https://api.cashfree.com/pg/orders/<ORDER_ID>/refunds \
          --header 'x-client-id: <CLIENT_ID>' \
          --header 'x-client-secret: <CLIENT_SECRET>' \
          --header 'Accept: application/json' \
          --header 'Content-Type: application/json' \
          --header 'x-api-version: 2023-08-01' \
          --data '{
        "refund_amount": 100,
        "refund_id": "refund_001"
      }'
      ```
    </Accordion>

    <Note>If the refund remains unsuccessful after all retry attempts, Cashfree coordinates directly with the bank to process the refund offline.</Note>
  </Step>
</Steps>

## Capture error codes and handling

For a small percentage of captures from the [Preauthorisation API](/docs/api-reference/payments/latest/payments/authorize) that do not return an immediate success, Cashfree returns one of the following error codes. Each code has a defined resolution path.

| Error code | Meaning                        | What to expect                                                                                            |
| ---------- | ------------------------------ | --------------------------------------------------------------------------------------------------------- |
| `59`       | Processing delay at bank       | Cashfree escalates to NPCI. Delayed success can be delivered on T+5 business days.                        |
| `K1`       | Bank timeout or hold           | Cashfree escalates to NPCI. Delayed success can be delivered on T+5 business days.                        |
| `VH`       | Bank hold or verification hold | Cashfree escalates to NPCI. Delayed success can be delivered on T+5 business days.                        |
| `VO`       | Void override (not settable)   | The transaction is not settled. No further action is available through Cashfree for this capture attempt. |

<Note>Error codes `59`, `K1`, and `VH` are recoverable. Cashfree escalates these to NPCI and the settlement may arrive within T+5 business days. Error code `VO` is non-recoverable and has a very low occurrence rate.</Note>

## Integration checklist

Use the following checklist to validate a complete UPI OTM integration:

* Obtain `x-client-id` and `x-client-secret` from the [Merchant Dashboard](https://merchant.cashfree.com/auth/login).
* Create an order using the [Create Order API](/docs/api-reference/payments/latest/orders/create) and store the `payment_session_id`.
* Initiate the UPI OTM session with the [Order Pay API](/docs/api-reference/payments/latest/payments/pay) using `authorize_only: true` and the required `channel`.
* Call the [Preauthorisation API](/docs/api-reference/payments/latest/payments/authorize) with `action: CAPTURE` after fulfilment.
* Call the [Preauthorisation API](/docs/api-reference/payments/latest/payments/authorize) with `action: VOID` for cancellations before capture.
* Create a refund using the [Create Refund API](/docs/api-reference/payments/latest/refunds/create) only for orders already captured.
* Handle error codes `59`, `K1`, and `VH` by waiting up to T+5 business days for delayed settlement confirmation from NPCI.

<div class="hidden" data-table-of-contents="bottom">
  <p class="mt-4 font-medium flex items-center gap-2 related-docs-heading">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" class="w-4 h-4">
      <path d="M3 4h7a2 2 0 0 1 2 2v13a2 2 0 0 0-2-2H3z" />

      <path d="M21 4h-7a2 2 0 0 0-2 2v13a2 2 0 0 1 2-2h7z" />
    </svg>

    <span>Related topics</span>
  </p>

  <ul>
    <li><a href="/docs/api-reference/payments/latest/orders/create">Create Order API</a></li>
    <li><a href="/docs/api-reference/payments/latest/payments/pay">Order Pay API</a></li>
    <li><a href="/docs/api-reference/payments/latest/payments/authorize">Preauthorisation API</a></li>
    <li><a href="/docs/api-reference/payments/latest/refunds/create">Create Refund API</a></li>
    <li><a href="/docs/payments/webhooks">Payment Webhooks</a></li>
    <li><a href="/docs/payments/features/token-vault">Token Vault Overview</a></li>
  </ul>
</div>
