<!-- Captured 18 Sep 2026 from Cashfree's Subscriptions documentation (https://www.cashfree.com/docs/). Cashfree's live page is the authority. -->

> ## Documentation Index
> Fetch the complete documentation index at: https://www.cashfree.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Raise a Charge or Create an Auth

> Use this API to create an auth or to raise a charge.

<Warning>In the sandbox environment, authorisation-related responses for eNACH, card, and UPI differ from those in production.</Warning>

<Warning>UPI AutoPay Collect flow for recurring mandates is being deprecated across desktop and Android as per NPCI guidelines. To ensure uninterrupted payment acceptance, merchants are advised to migrate to UPI AutoPay Intent and UPI AutoPay QR flows. For integration changes and more details, refer to the [UPI AutoPay Collect Deprecation](/docs/payments/manage/payment-methods/upi-collect) document.</Warning>

You must generate the URL in production by concatenating it with the payload data in JSON format. The following are example responses for all Seamless Auth modes in the production environment.

<AccordionGroup>
  <Accordion title="Card method">
    ```
    {
      "action": "custom",
      "cf_payment_id": "39394805",
      "channel": "link",
      "data": {
        "url": "https://centinelapi.cardinalcommerce.com/V2/Cruise/StepUp",
        "payload": {
          "JWT": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI4MjcxZmJlMS1mOTU5LTQwMTgtOTc1OC01MzZkMWRkNzM2NjIiLCJpYXQiOjE3NDc2NDI4NjIsImlzcyI6IjYxNDIwNjg4OTMzODI1Njc1MDg0ZGI2ZiIsImV4cCI6MTc0NzY0NjQ2MiwiT3JnVW5pdElkIjoiNjRkNjA3ZGFmZjUzNDk2MWYxNjk0YWZjIiwiUGF5bG9hZCI6eyJBQ1NVcmwiOiJodHRwczovL3NlY3VyZWljaWNpLWNyMS5pY2ljaWJhbmsuY29tL3YxL2Fjcy9zZXJ2aWNlcy9icm93c2VyL2NyZXEvTC84MTEyLzMzNzAxNTBlLTM0OGEtMTFmMC05NTliLTJiYjZmODk2ZjIzOCIsIlBheWxvYWQiOiJleUp0WlhOellXZGxWSGx3WlNJNklrTlNaWEVpTENKdFpYTnpZV2RsVm1WeWMybHZiaUk2SWpJdU1pNHdJaXdpZEdoeVpXVkVVMU5sY25abGNsUnlZVzV6U1VRaU9pSTRZV1ZtT1RCaU15MW1ZakU0TFRRME5qa3RPREF3TVMwMk1tVm1ZakEwWW1RMk56TWlMQ0poWTNOVWNtRnVjMGxFSWpvaU16TTNNREUxTUdVdE16UTRZUzB4TVdZd0xUazFPV0l0TW1KaU5tWTRPVFptTWpNNElpd2lZMmhoYkd4bGJtZGxWMmx1Wkc5M1UybDZaU0k2SWpBeUluMCIsIlRyYW5zYWN0aW9uSWQiOiJUNGVtNEdidnBubGwzQWViakNKMSJ9LCJPYmplY3RpZnlQYXlsb2FkIjp0cnVlLCJSZXR1cm5VcmwiOiJodHRwczovL3d3dy5jYXNoZnJlZS5jb20vc3Vic2NyaXB0aW9uL2NhcmRfcmV0dXJuLzE1MTk5NzA3P3NiY2RhdGE9bHM5SmlOMUl6VUlKaU9pY0diaEpDTGlRMVZLSmlPaUFYZTBKeWUualY5MTNOd2NUTzVFVE54b2pJa2xFYTBWWFlpc25PaXdrVVY5bFRTVkZWRkoxWEhCMVhJUlZWQkp5ZS5CM2txOWhMeXdvY2hlV1U3QV9yT2tmQ2tTVl9TUEw3NzZxcl9mVHY2RG85MmwifQ.BeWYE8vslkOLZVWJd4mJ4MU1eu682fpp2Va7IvzdL9U",
          "MD": "3881717951"
        },
        "content_type": "application/json",
        "method": "post"
      },
      "payment_amount": 1,
      "payment_currency": "INR",
      "payment_id": "test12343234887",
      "payment_method": "card",
      "payment_status": "PENDING",
      "payment_type": "AUTH",
      "subscription_id": "jd-rupay-test106"
    }
    ```
  </Accordion>

  <Accordion title="Enach Seamless Auth">
    ```
    {
      "action": "custom",
      "cf_payment_id": "39394843",
      "channel": "link",
      "data": {
        "url": "https://enach.npci.org.in/onmags/sendRequest",
        "payload": {
          "AuthMode": "NetBanking",
          "BankID": "ICIC",
          "CheckSumVal": "Ril5otPjBl/Y44z3a0HAsSce2NlDqO1iEpP3pIBuKGYJplXVLuIQ1azxNB2aSJkx7...",
          "MandateReqDoc": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Document xmlns=\"http://npci.org/onmags/schema\">...</Document>"
        },
        "content_type": "application/json",
        "method": "post"
      },
      "payment_amount": 1,
      "payment_currency": "INR",
      "payment_id": "test12343234888",
      "payment_method": "enach",
      "payment_status": "PENDING",
      "payment_type": "AUTH",
      "subscription_id": "jd-enach-test107"
    }
    ```
  </Accordion>

  <Accordion title="UPI Link">
    ```
    {
      "action": "custom",
      "cf_payment_id": "40756575",
      "channel": "link",
      "data": {
        "url": "https://payments.cashfree.com/subscriptions/checkout/timer",
        "payload": {
          "paymentType": "UPI",
          "upiIntentData": {
            "androidAuthAppLinks": {
              "AMAZONPAY": "intent://mandate?pa=branchautopay.cf@icici&pn=Branch&tr=EZM2025060413545205666653&am=10.00&cu=INR&orgid=400011&mc=7322&purpose=14&tn=Cashfree%20Payments&validitystart=04062025&validityend=04062055&amrule=MAX&recur=ASPRESENTED&rev=N&share=Y&block=N&txnType=CREATE&mode=13&fam=10.00#Intent;scheme=upi;package=in.amazon.mShop.android.shopping;end",
              "BHIM": "intent://mandate?pa=branchautopay.cf@icici&pn=Branch&tr=EZM2025060413545205666653&am=10.00&cu=INR&orgid=400011&mc=7322&purpose=14&tn=Cashfree%20Payments&validitystart=04062025&validityend=04062055&amrule=MAX&recur=ASPRESENTED&rev=N&share=Y&block=N&txnType=CREATE&mode=13&fam=10.00#Intent;scheme=upi;package=in.org.npci.upiapp;end",
              "DEFAULT": "upi://mandate?pa=branchautopay.cf@icici&pn=Branch&tr=EZM2025060413545205666653&am=10.00&cu=INR&orgid=400011&mc=7322&purpose=14&tn=Cashfree%20Payments&validitystart=04062025&validityend=04062055&amrule=MAX&recur=ASPRESENTED&rev=N&share=Y&block=N&txnType=CREATE&mode=13&fam=10.00",
              "GPAY": "gpay://upi/mandate?pa=branchautopay.cf@icici&pn=Branch&tr=EZM2025060413545205666653&am=10.00&cu=INR&orgid=400011&mc=7322&purpose=14&tn=Cashfree%20Payments&validitystart=04062025&validityend=04062055&amrule=MAX&recur=ASPRESENTED&rev=N&share=Y&block=N&txnType=CREATE&mode=13&fam=10.00#Intent;scheme=upi;package=com.google.android.apps.nbu.paisa.user;end",
              "PAYTM": "paytmmp://mandate?pa=branchautopay.cf@icici&pn=Branch&tr=EZM2025060413545205666653&am=10.00&cu=INR&orgid=400011&mc=7322&purpose=14&tn=Cashfree%20Payments&validitystart=04062025&validityend=04062055&amrule=MAX&recur=ASPRESENTED&rev=N&share=Y&block=N&txnType=CREATE&mode=13&fam=10.00#Intent;scheme=upi;package=net.one97.paytm;end",
              "PHONEPE": "phonepe://mandate?pa=branchautopay.cf@icici&pn=Branch&tr=EZM2025060413545205666653&am=10.00&cu=INR&orgid=400011&mc=7322&purpose=14&tn=Cashfree%20Payments&validitystart=04062025&validityend=04062055&amrule=MAX&recur=ASPRESENTED&rev=N&share=Y&block=N&txnType=CREATE&mode=13&fam=10.00#Intent;scheme=upi;package=com.phonepe.app;end"
            },
            "iosAuthAppLinks": {
              "BHIM": "bhim://upi://mandate?pa=branchautopay.cf@icici&pn=Branch&tr=EZM2025060413545205666653&am=10.00&cu=INR&orgid=400011&mc=7322&purpose=14&tn=Cashfree%20Payments&validitystart=04062025&validityend=04062055&amrule=MAX&recur=ASPRESENTED&rev=N&share=Y&block=N&txnType=CREATE&mode=13&fam=10.00",
              "GPAY": "tez://upi/mandate?pa=branchautopay.cf@icici&pn=Branch&tr=EZM2025060413545205666653&am=10.00&cu=INR&orgid=400011&mc=7322&purpose=14&tn=Cashfree%20Payments&validitystart=04062025&validityend=04062055&amrule=MAX&recur=ASPRESENTED&rev=N&share=Y&block=N&txnType=CREATE&mode=13&fam=10.00",
              "PAYTM": "paytmmp://mandate?pa=branchautopay.cf@icici&pn=Branch&tr=EZM2025060413545205666653&am=10.00&cu=INR&orgid=400011&mc=7322&purpose=14&tn=Cashfree%20Payments&validitystart=04062025&validityend=04062055&amrule=MAX&recur=ASPRESENTED&rev=N&share=Y&block=N&txnType=CREATE&mode=13&fam=10.00",
              "PHONEPE": "phonepe://mandate?pa=branchautopay.cf@icici&pn=Branch&tr=EZM2025060413545205666653&am=10.00&cu=INR&orgid=400011&mc=7322&purpose=14&tn=Cashfree%20Payments&validitystart=04062025&validityend=04062055&amrule=MAX&recur=ASPRESENTED&rev=N&share=Y&block=N&txnType=CREATE&mode=13&fam=10.00"
            }
          }
        },
        "content_type": "application/json",
        "method": "post"
      },
      "payment_amount": 10,
      "payment_id": "PAY-1749025491584-4289ae9a",
      "payment_method": "upi",
      "payment_status": "PENDING",
      "payment_type": "AUTH",
      "subscription_id": "SUB_TEST_1749025465390"
    }

    ```
  </Accordion>

  <Accordion title="UPI Collect">
    ```
    {
      "action": "custom",
      "cf_payment_id": "40756761",
      "channel": "collect",
      "data": {
        "url": "https://payments.cashfree.com/subscriptions/checkout/timer",
        "payload": {
          "paymentType": "UPI"
        },
        "content_type": "application/json",
        "method": ""
      },
      "payment_amount": 10,
      "payment_id": "PAY-1749025606422-791be52e",
      "payment_method": "upi",
      "payment_status": "PENDING",
      "payment_type": "AUTH",
      "subscription_id": "SUB_TEST_1749025465390"
    }

    ```
  </Accordion>

  <Accordion title="UPI QR code">
    ```
    {
      "action": "custom",
      "cf_payment_id": "40757018",
      "channel": "qrcode",
      "data": {
        "url": "",
        "payload": {
          "paymentType": "UPI",
          "qrData": "upi://mandate?pa=branchautopay.cf@icici&pn=Branch&tr=EZM2025060413592105685824&am=10.00&cu=INR&orgid=400011&mc=7322&purpose=14&tn=Cashfree%20Payments&validitystart=04062025&validityend=04062055&amrule=MAX&recur=ASPRESENTED&rev=N&share=Y&block=N&txnType=CREATE&mode=13&fam=10.00"
        },
        "content_type": "application/json",
        "method": "post"
      },
      "payment_amount": 10,
      "payment_id": "PAY-1749025760541-4c158190",
      "payment_method": "upi",
      "payment_status": "PENDING",
      "payment_type": "AUTH",
      "subscription_id": "SUB_TEST_1749025465390"
    }
    ```
  </Accordion>

  <Accordion title="Physical Nach Auth">
    ```
    {
    	"action": "post",
    	"cf_payment_id": "47720375",
    	"channel": "post",
    	"data": {
    		"url": "https://api.cashfree.com/pg/view/gateway/subscriptions/testkriti12upi12ANUG5689TFVNB357123",
    		"payload": null,
    		"content_type": "",
    		"method": null
    	},
    	"payment_amount": 0,
    	"payment_currency": "INR",
    	"payment_id": "PAY-1749025760541-4c158190",
    	"payment_method": "pnach",
    	"payment_status": "PENDING",
    	"payment_tags": null,
    	"payment_type": "AUTH",
    	"subscription_id": "SUB_TEST_1749025465390"
    }
    ```
  </Accordion>
</AccordionGroup>


## OpenAPI

````yaml openapi/payments/v2026-01-01.yaml post /subscriptions/pay
openapi: 3.0.0
info:
  version: '2026-01-01'
  title: Cashfree Payment Gateway APIs
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html
  contact:
    email: developers@cashfree.com
    name: API Support
    url: https://discord.com/invite/QdZkNSxXsB
  description: >-
    Cashfree's Payment Gateway APIs provide developers with a streamlined
    pathway to integrate advanced payment processing capabilities into their
    applications, platforms and websites.
servers:
  - url: https://sandbox.cashfree.com/pg
    description: Sandbox server.
  - url: https://api.cashfree.com/pg
    description: Production server.
security: []
tags:
  - name: Orders
    description: Collection of APIs to handle orders.
  - name: Payments
    description: Collection of APIs to handle payments.
  - name: Refunds
    description: Collection of APIs to handle refunds.
  - name: Settlements
    description: Collection of APIs to handle settlements.
  - name: Payment Links
    description: Collection of APIs to handle payment links.
  - name: Token Vault
    description: >-
      Collection of APIs to use Cashfree's token Vault. This helps you save
      cards and tokenize them in a PCI complaint manner. We support creation of
      network tokens which can be used across acquiring banks.
  - name: softPOS
    description: Collection of APIs to manage softPOS' agent and order.
  - name: Offers
    description: Collection of APIs to handle offers.
  - name: Eligibility
    description: >-
      Collection of APIs to check eligibile entities - payment methods, offer,
      affordibility.
  - name: Settlement Reconciliation
    description: Collection of APIs to handle settlements.
  - name: PG Reconciliation
    description: Collection of APIs to handle reconciliation.
  - name: Customers
    description: Collection of APIs to handle customers.
  - name: Easy-Split
    description: Collection of APIs to handle Easy-Split.
  - name: Simulation
    description: Collection of APIs to handle simulation.
  - name: Disputes
    description: Collection of APIs to handle disputes.
  - name: Utilities
    description: Collection of APIs for utility requirement.
  - name: Downtimes
    description: Collection of APIs for managing downtimes.
externalDocs:
  url: https://api.cashfree.com/pg
  description: This url will have the information of all the APIs.
paths:
  /subscriptions/pay:
    post:
      tags:
        - Subscription
      summary: Raise a Charge or Create an Auth
      description: Use this API to create an auth or to raise a charge.
      operationId: SubsCreatePayment
      parameters:
        - $ref: '#/components/parameters/apiVersionHeader'
        - $ref: '#/components/parameters/xRequestIDHeader'
        - $ref: '#/components/parameters/xIdempotencyKeyHeader'
        - $ref: '#/components/parameters/xClientDeviceHeader'
        - $ref: '#/components/parameters/xClientOsHeader'
        - $ref: '#/components/parameters/xClientRenderingTypeHeader'
        - $ref: '#/components/parameters/xClientBrowserHeader'
      requestBody:
        $ref: '#/components/requestBodies/CreateSubscriptionPaymentRequest'
      responses:
        '200':
          description: response of created payment.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateSubscriptionPaymentResponse'
              examples:
                Sandbox_UPI_QRCode:
                  value:
                    action: custom
                    cf_payment_id: '123456'
                    channel: qrcode
                    data:
                      url: https://dummy-url.com/upi/qrcode
                      payload:
                        paymentType: UPI
                        upiIntentData:
                          androidAuthAppLinks:
                            GPAY: https://dummy-url.com/upi/gpay
                            PHONEPE: https://dummy-url.com/upi/phonepe
                          iosAuthAppLinks:
                            GPAY: https://dummy-url.com/upi/gpay
                            PHONEPE: https://dummy-url.com/upi/phonepe
                      content_type: application/json
                      method: post
                    payment_amount: 1
                    payment_id: PAY-123456
                    payment_method: upi
                    payment_status: PENDING
                    payment_type: AUTH
                    subscription_id: SUBSCRIPTION-123
                Sandbox_UPI_Link:
                  value:
                    action: custom
                    cf_payment_id: '123457'
                    channel: link
                    data:
                      url: https://dummy-url.com/upi/link
                      payload:
                        paymentType: UPI
                        upiIntentData:
                          androidAuthAppLinks:
                            GPAY: https://dummy-url.com/upi/gpay
                            PHONEPE: https://dummy-url.com/upi/phonepe
                          iosAuthAppLinks:
                            GPAY: https://dummy-url.com/upi/gpay
                            PHONEPE: https://dummy-url.com/upi/phonepe
                      content_type: application/json
                      method: post
                    payment_amount: 1
                    payment_id: PAY-123457
                    payment_method: upi
                    payment_status: PENDING
                    payment_type: AUTH
                    subscription_id: SUBSCRIPTION-124
                Sandbox_UPI_Collect:
                  value:
                    action: custom
                    cf_payment_id: '123458'
                    channel: collect
                    data:
                      url: https://dummy-url.com/upi/collect
                      payload:
                        paymentType: UPI
                        upiIntentData:
                          androidAuthAppLinks:
                            GPAY: https://dummy-url.com/upi/gpay
                            PHONEPE: https://dummy-url.com/upi/phonepe
                          iosAuthAppLinks:
                            GPAY: https://dummy-url.com/upi/gpay
                            PHONEPE: https://dummy-url.com/upi/phonepe
                      content_type: application/json
                      method: post
                    payment_amount: 1
                    payment_id: PAY-123458
                    payment_method: upi
                    payment_status: PENDING
                    payment_type: AUTH
                    subscription_id: SUBSCRIPTION-125
                Sandbox_Card:
                  value:
                    action: custom
                    cf_payment_id: '123459'
                    channel: link
                    data:
                      url: https://dummy-url.com/card/checkout
                      payload:
                        amount: '1.00'
                        orderCurrency: INR
                        paymentMode: SBC_CREDIT_CARD
                        returnUrl: https://dummy-url.com/card/return
                        signature: dummy-signature
                        transactionId: TXN-123
                      content_type: application/json
                      method: post
                    payment_amount: 1
                    payment_id: PAY-123459
                    payment_method: card
                    payment_status: PENDING
                    payment_type: AUTH
                    subscription_id: SUBSCRIPTION-126
                Sandbox_ENach:
                  value:
                    action: custom
                    cf_payment_id: '123460'
                    channel: link
                    data:
                      url: https://dummy-url.com/enach/checkout
                      payload:
                        AuthMode: dummyAuthMode
                        BankID: dummyBankId
                        CheckSumVal: dummyCheckSum
                        MandateReqDoc: dummyMandateDocument
                        MerchantID: dummyMerchantId
                        signature: dummy-signature
                      content_type: application/json
                      method: post
                    payment_amount: 0
                    payment_id: PAY-123460
                    payment_method: enach
                    payment_status: PENDING
                    payment_type: AUTH
                    subscription_id: SUBSCRIPTION-127
                Sandbox_Pnach:
                  value:
                    action: post
                    cf_payment_id: '2463045'
                    channel: post
                    data:
                      url: https://dummy-url.com/pnach/checkout
                      payload: null
                      content_type: application/x-www-form-urlencoded
                      method: post
                    payment_amount: 0
                    payment_currency: INR
                    payment_id: test_pnach_payment_id_2
                    payment_method: pnach
                    payment_status: PENDING
                    payment_tags: null
                    payment_type: AUTH
                    subscription_id: Test_Pnach_4
          headers:
            x-api-version:
              $ref: '#/components/headers/x-api-version'
            x-ratelimit-limit:
              $ref: '#/components/headers/x-ratelimit-limit'
            x-ratelimit-remaining:
              $ref: '#/components/headers/x-ratelimit-remaining'
            x-ratelimit-retry:
              $ref: '#/components/headers/x-ratelimit-retry'
            x-ratelimit-type:
              $ref: '#/components/headers/x-ratelimit-type'
            x-request-id:
              $ref: '#/components/headers/x-request-id'
            x-idempotency-key:
              $ref: '#/components/headers/x-idempotency-key'
            x-idempotency-replayed:
              $ref: '#/components/headers/x-idempotency-replayed'
        '400':
          $ref: '#/components/responses/Response400'
        '401':
          $ref: '#/components/responses/Response401'
        '404':
          $ref: '#/components/responses/Response404'
        '422':
          $ref: '#/components/responses/Response422'
        '429':
          $ref: '#/components/responses/Response429'
        '500':
          $ref: '#/components/responses/Response500'
      deprecated: false
      security:
        - XClientID: []
          XClientSecret: []
        - XClientID: []
          XPartnerAPIKey: []
        - XClientID: []
          XClientSignatureHeader: []
        - XPartnerMerchantID: []
          XPartnerAPIKey: []
      x-codeSamples:
        - lang: bash
          label: create_subscription_charge
          source: |-
            curl --request POST \
              --url https://sandbox.cashfree.com/pg/subscriptions/pay \
              --header 'Content-Type: application/json' \
              --header 'x-api-version: <x-api-version>' \
              --header 'x-client-id: <api-key>' \
              --header 'x-client-secret: <api-key>' \
              --data '{
              "subscription_id": "test-subscription-id",
              "payment_id": "test-payment-id",
              "payment_amount": 10,
              "payment_schedule_date": "2025-06-01T16:40:00",
              "payment_remarks": "2nd EMI payment",
              "payment_type": "CHARGE",
              "payment_method": {
                "upi": {
                  "upi_id": "john@upi",
                  "channel": "collect"
                }
              }
            }'
        - lang: bash
          label: create_subscription_auth_upi_link
          source: |-
            curl --request POST \
              --url https://sandbox.cashfree.com/pg/subscriptions/pay \
              --header 'Content-Type: application/json' \
              --header 'x-api-version: <x-api-version>' \
              --header 'x-client-id: <api-key>' \
              --header 'x-client-secret: <api-key>' \
              --data '{
              "subscription_id": "test-subscription-id",
              "subscription_session_id": "sub_session_Vf5ZOcJTbGkcw4kcpayment",
              "payment_id": "test-payment-id",
              "payment_type": "AUTH",
              "payment_method": {
                "upi": {
                  "channel": "link",
                  "upi_id": "john.doe@okbank"
                }
              }
            }'
        - lang: bash
          label: create_subscription_auth_upi_collect
          source: |-
            curl --request POST \
              --url https://sandbox.cashfree.com/pg/subscriptions/pay \
              --header 'Content-Type: application/json' \
              --header 'x-api-version: <x-api-version>' \
              --header 'x-client-id: <api-key>' \
              --header 'x-client-secret: <api-key>' \
              --header 'x-client-device: mobile' \
              --header 'x-client-os: ios' \
              --header 'x-client-rendering-type: mweb' \
              --header 'x-client-browser: safari' \
              --data '{
              "subscription_id": "test-subscription-id",
              "subscription_session_id": "sub_session_Vf5ZOcJTbGkcw4kcpayment",
              "payment_id": "test-payment-id",
              "payment_type": "AUTH",
              "payment_method": {
                "upi": {
                  "channel": "collect",
                  "upi_id": "john.doe@okbank"
                }
              }
            }'
        - lang: bash
          label: create_subscription_auth_upi_qrcode
          source: |-
            curl --request POST \
              --url https://sandbox.cashfree.com/pg/subscriptions/pay \
              --header 'Content-Type: application/json' \
              --header 'x-api-version: <x-api-version>' \
              --header 'x-client-id: <api-key>' \
              --header 'x-client-secret: <api-key>' \
              --data '{
              "subscription_id": "test-subscription-id",
              "subscription_session_id": "sub_session_Vf5ZOcJTbGkcw4kcpayment",
              "payment_id": "test-payment-id",
              "payment_type": "AUTH",
              "payment_method": {
                "upi": {
                  "channel": "qrcode"
                }
              }
            }'
        - lang: bash
          label: create_subscription_auth_card
          source: |-
            curl --request POST \
              --url https://sandbox.cashfree.com/pg/subscriptions/pay \
              --header 'Content-Type: application/json' \
              --header 'x-api-version: <x-api-version>' \
              --header 'x-client-id: <api-key>' \
              --header 'x-client-secret: <api-key>' \
              --data '{
              "subscription_id": "test-subscription-id",
              "subscription_session_id": "sub_session_Vf5ZOcJTbGkcw4kcpayment",
              "payment_id": "test-payment-id",
              "payment_type": "AUTH",
              "payment_method": {
                "card": {
                  "channel": "link",
                  "card_number": "4111111111111111",
                  "card_holder_name": "John Doe",
                  "card_expiry_mm": "12",
                  "card_expiry_yy": "25",
                  "card_cvv": "123",
                  "card_network": "VISA",
                  "card_type": "CREDIT"
                }
              }
            }'
        - lang: bash
          label: create_subscription_auth_enach
          source: |-
            curl --request POST \
              --url https://sandbox.cashfree.com/pg/subscriptions/pay \
              --header 'Content-Type: application/json' \
              --header 'x-api-version: <x-api-version>' \
              --header 'x-client-id: <api-key>' \
              --header 'x-client-secret: <api-key>' \
              --data '{
              "subscription_id": "test-subscription-id",
              "subscription_session_id": "sub_session_Vf5ZOcJTbGkcw4kcpayment",
              "payment_id": "test-payment-id",
              "payment_type": "AUTH",
              "payment_method": {
                "enach": {
                  "channel": "link",
                  "auth_mode": "net_banking",
                  "account_holder_name": "John Doe",
                  "account_number": "1518121112",
                  "account_type": "SAVINGS",
                  "account_bank_code": "ICIC"
                }
              }
            }'
        - lang: bash
          label: create_subscription_auth_pnach
          source: |-
            curl --request POST \
              --url https://sandbox.cashfree.com/pg/subscriptions/pay \
              --header 'Content-Type: application/json' \
              --header 'x-api-version: <x-api-version>' \
              --header 'x-client-id: <api-key>' \
              --header 'x-client-secret: <api-key>' \
              --data '{
              "subscription_id": "test-subscription-id",
              "subscription_session_id": "sub_session_Vf5ZOcJTbGkcw4kcpayment",
              "payment_id": "test-payment-id",
              "payment_type": "AUTH",
              "payment_method": {
                "pnach": {
                  "channel": "post",
                  "account_holder_name": "John Doe",
                  "account_number": "1518121112",
                  "account_type": "SAVINGS",
                  "account_bank_code": "ICIC",
                  "account_ifsc": "ICIC0000123",
                  "mandate_creation_date": "2025-06-01",
                  "mandate_start_date": "2025-06-05"
                }
              }
            }'
components:
  parameters:
    apiVersionHeader:
      in: header
      name: x-api-version
      required: true
      description: API version to be used. Format is in YYYY-MM-DD.
      schema:
        type: string
        description: API version to be used.
        default: '2026-01-01'
      example: '2026-01-01'
      x-ignore: true
    xRequestIDHeader:
      in: header
      name: x-request-id
      description: >-
        Request ID for the API call. Can be used to resolve tech issues.
        Communicate this in your tech related queries to Cashfree.
      required: false
      schema:
        type: string
      example: 4dfb9780-46fe-11ee-be56-0242ac120002
    xIdempotencyKeyHeader:
      in: header
      name: x-idempotency-key
      required: false
      description: >
        An idempotency key is a unique identifier you include with your API
        call.

        If the request fails or times out, you can safely retry it using the
        same key to avoid duplicate actions.
      schema:
        type: string
        format: UUID
      example: 47bf8872-46fe-11ee-be56-0242ac120002
    xClientDeviceHeader:
      in: header
      name: x-client-device
      required: false
      description: >-
        Accepted values are `mobile`, `desktop`, and `tablet`. Required for UPI
        Collect requests.
      schema:
        type: string
        enum:
          - mobile
          - desktop
          - tablet
      example: mobile
    xClientOsHeader:
      in: header
      name: x-client-os
      required: false
      description: >-
        The client device's operating system. This header is required for UPI
        Collect requests. The only accepted value is `ios`.
      schema:
        type: string
        enum:
          - ios
      example: ios
    xClientRenderingTypeHeader:
      in: header
      name: x-client-rendering-type
      required: false
      description: >-
        Accepted values are `mweb`, `webview`, and `native`. Required for UPI
        Collect requests when `x-client-device` is `mobile`. `mweb` renders the
        payment in a mobile browser, `webview` renders it inside an in-app
        browser, and `native` renders it natively inside a mobile app using
        SDKs.
      schema:
        type: string
        enum:
          - mweb
          - webview
          - native
      example: mweb
    xClientBrowserHeader:
      in: header
      name: x-client-browser
      required: false
      description: >-
        Accepted values are `safari`, `chrome`, `firefox`, and `edge`. Required
        for UPI Collect requests.
      schema:
        type: string
        enum:
          - safari
          - chrome
          - firefox
          - edge
      example: safari
  requestBodies:
    CreateSubscriptionPaymentRequest:
      description: Request body to create a subscription payment.
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/CreateSubscriptionPaymentRequest'
          examples:
            create_subscription_charge:
              $ref: '#/components/examples/create_subscription_charge'
            create_subscription_auth_upi_link:
              $ref: '#/components/examples/create_subscription_auth_upi_link'
            create_subscription_auth_upi_collect:
              $ref: '#/components/examples/create_subscription_auth_upi_collect'
            create_subscription_auth_upi_qrcode:
              $ref: '#/components/examples/create_subscription_auth_upi_qrcode'
            create_subscription_auth_card:
              $ref: '#/components/examples/create_subscription_auth_card'
            create_subscription_auth_enach:
              $ref: '#/components/examples/create_subscription_auth_enach'
            create_subscription_auth_pnach:
              $ref: '#/components/examples/create_subscription_auth_pnach'
  schemas:
    CreateSubscriptionPaymentResponse:
      title: CreateSubscriptionPaymentResponse
      description: The response returned is Create Subscription Auth or Charge APIs.
      type: object
      example:
        payment_id: test-paymey
        subscription_id: Demo_Subscription
        payment_amount: 1
        cf_payment_id: '12345'
        payment_method: upi
        payment_status: SUCCESS
        payment_type: AUTH
        action: custom
        channel: link
        data:
          url: >-
            https://api.cashfree.com/pg/view/gateway/tuOssT3fNV8soG97VSeHca034555-8a65-4aaf-9e67-c9893471af23
          payload: null
          content_type: null
          method: null
      properties:
        cf_payment_id:
          type: string
          description: Cashfree subscription payment reference number.
        failure_details:
          type: object
          properties:
            failure_reason:
              type: string
              description: Failure reason of the payment if the payment_status is failed.
        payment_amount:
          type: number
          format: float64
          description: The charge amount of the payment.
        payment_id:
          type: string
          description: A unique ID passed by merchant for identifying the transaction.
        payment_initiated_date:
          type: string
          description: >-
            The date on which the payment was initiated. We store timestamps in
            IST.
          format: ISO8601
          example: '2025-06-01T10:20:12+05:30'
        payment_status:
          type: string
          description: Status of the payment.
        payment_type:
          type: string
          description: Payment type. Can be AUTH or CHARGE.
          example: CHARGE
        subscription_id:
          type: string
          description: A unique ID passed by merchant for identifying the subscription.
        data:
          type: object
          description: >-
            Contains a payload for auth app links in case of AUTH. For charge,
            the payload is empty.
        payment_method:
          type: string
          description: Payment method used for the authorisation.
    CreateSubscriptionPaymentRequest:
      title: CreateSubscriptionPaymentRequest
      description: The request to be passed for the create subscription payment API.
      properties:
        subscription_id:
          type: string
          description: A unique ID passed by merchant for identifying the subscription.
        subscription_session_id:
          type: string
          description: Session ID for the subscription. Required only for Auth.
        payment_id:
          type: string
          description: >-
            A unique ID passed by merchant for identifying the subscription
            payment.
        payment_amount:
          type: number
          format: float64
          description: The charge amount of the payment. Required in case of charge.
        payment_schedule_date:
          type: string
          description: >-
            The date on which the payment is scheduled to be processed. This
            field is required for UPI and CARD payment modes. Cashfree stores
            timestamps in IST, but you can provide them in a valid ISO 8601 time
            format.

            For IST this `2025-06-01T10:20:12+05:30` translates to `2025-06-01
            10:20:12`.

            For UTC this `2025-06-01T10:20:12Z` translates to `2025-06-01
            15:50:12+05:30`.



            Please note that only the date component is considered. Any time
            value provided will be ignored.
        payment_remarks:
          type: string
          description: Payment remarks.
        payment_type:
          type: string
          description: Payment type. Can be AUTH or CHARGE.
        payment_method:
          type: object
          description: >-
            Payment method. Can be one of ["upi", "enach", "pnach", "card"].
            This field is not required when raising a charge. It is only
            mandatory when raising an authorisation. In the case of a charge,
            this field is ignored, and the charge will be created using the same
            payment method that was used for the original authorisation.
          oneOf:
            - $ref: '#/components/schemas/CreateSubscriptionPaymentRequestUpi'
            - $ref: '#/components/schemas/CreateSubscriptionPaymentRequestEnach'
            - $ref: '#/components/schemas/CreateSubscriptionPaymentRequestPnach'
            - $ref: '#/components/schemas/CreateSubscriptionPaymentRequestCard'
      required:
        - subscription_id
        - payment_id
        - payment_type
    BadRequestError:
      title: BadRequestError
      description: Invalid request received from client.
      example:
        message: bad URL, please check API documentation
        help: >-
          Check latest errors and resolution from Merchant Dashboard API logs:
          https://bit.ly/4glEd0W Help Document: https://bit.ly/4eeZYO9
        code: request_failed
        type: invalid_request_error
      type: object
      properties:
        message:
          type: string
        code:
          type: string
        help:
          type: string
        type:
          type: string
          enum:
            - invalid_request_error
    AuthenticationError:
      title: AuthenticationError
      description: Error if api keys are wrong.
      example:
        message: authentication Failed
        code: request_failed
        type: authentication_error
      type: object
      properties:
        message:
          type: string
        code:
          type: string
        type:
          type: string
          description: authentication_error.
    ApiError404:
      title: ApiError404
      description: Error when resource requested is not found.
      example:
        message: something is not found
        help: >-
          Check latest errors and resolution from Merchant Dashboard API logs:
          https://bit.ly/4glEd0W Help Document: https://bit.ly/4eeZYO9
        code: something_not_found
        type: invalid_request_error
      type: object
      properties:
        message:
          type: string
        code:
          type: string
        help:
          type: string
        type:
          type: string
          enum:
            - invalid_request_error
          description: invalid_request_error.
    IdempotencyError:
      title: IdempotencyError
      description: >-
        Error when idempotency fails. Different request body with the same
        idempotent key.
      example:
        message: something is not found
        help: >-
          Check latest errors and resolution from Merchant Dashboard API logs:
          https://bit.ly/4glEd0W Help Document: https://bit.ly/4eeZYO9
        code: request_invalid
        type: idempotency_error
      type: object
      properties:
        message:
          type: string
        help:
          type: string
        code:
          type: string
        type:
          type: string
          enum:
            - idempotency_error
          description: idempotency_error.
    RateLimitError:
      title: RateLimitError
      description: Error when rate limit is breached for your api.
      example:
        message: Too many requests from IP. Check headers
        code: request_failed
        type: rate_limit_error
      type: object
      properties:
        message:
          type: string
        code:
          type: string
        type:
          type: string
          enum:
            - rate_limit_error
          description: rate_limit_error.
    ApiError:
      title: ApiError
      description: Error at Cashfree's server.
      example:
        message: internal Server Error
        help: >-
          Check latest errors and resolution from Merchant Dashboard API logs:
          https://bit.ly/4glEd0W Help Document: https://bit.ly/4eeZYO9
        code: internal_error
        type: api_error
      type: object
      properties:
        message:
          type: string
        code:
          type: string
        help:
          type: string
        type:
          type: string
          enum:
            - api_error
          description: api_error.
    CreateSubscriptionPaymentRequestUpi:
      title: CreateSubscriptionPaymentRequestUpi
      description: payment method upi.
      type: object
      properties:
        upi:
          type: object
          properties:
            channel:
              description: Channel. can be link or qrcode.
              type: string
            upi_id:
              type: string
    CreateSubscriptionPaymentRequestEnach:
      title: CreateSubscriptionPaymentRequestEnach
      type: object
      description: payment method enach.
      properties:
        enach:
          type: object
          properties:
            account_bank_code:
              description: >-
                Account bank code (mandatory). Consists of the first four
                alphabetic characters of the IFSC.
              type: string
            account_holder_name:
              description: Account holder name.
              type: string
            account_ifsc:
              description: >-
                Account IFSC (optional). Complete 11-character alphanumeric
                code.
              type: string
            account_number:
              description: Account number.
              type: string
            account_type:
              enum:
                - SAVINGS
                - CURRENT
              description: Account type.
              type: string
            auth_mode:
              description: >-
                Authentication mode. can be `debit_card`, `aadhaar`, or
                `net_banking`.
              type: string
            channel:
              description: Channel. can be link.
              type: string
    CreateSubscriptionPaymentRequestPnach:
      title: CreateSubscriptionPaymentRequestPnach
      type: object
      description: payment method pnach.
      properties:
        pnach:
          type: object
          properties:
            account_bank_code:
              description: >-
                Account bank code. Consists of the first four alphabetic
                characters of the IFSC.
              type: string
            account_holder_name:
              description: Account holder name.
              type: string
            account_ifsc:
              description: Account IFSC. Complete 11-character alphanumeric code.
              type: string
            account_number:
              description: Account number.
              type: string
            account_type:
              description: Account type.
              type: string
            channel:
              description: Channel. can be post.
              type: string
            mandate_creation_date:
              description: Mandate creation date.
              type: string
            mandate_start_date:
              description: Mandate start date.
              type: string
    CreateSubscriptionPaymentRequestCard:
      title: CreateSubscriptionPaymentRequestCard
      type: object
      description: payment method card.
      properties:
        card:
          type: object
          properties:
            card_cvv:
              description: Card CVV.
              type: string
            card_expiry_mm:
              type: string
              description: Card expiry month.
            card_expiry_yy:
              type: string
              description: Card expiry year.
            card_holder_name:
              description: Card holder name.
              type: string
            card_network:
              description: Card network.
              type: string
            card_number:
              description: Card number.
              type: string
            card_type:
              description: Card type.
              type: string
            channel:
              description: Channel. can be link.
              type: string
  headers:
    x-api-version:
      schema:
        type: string
        format: YYYY-MM-DD
        enum:
          - '2026-01-01'
      description: >-
        This header has the version of the API. The current version is
        `2026-01-01`.
    x-ratelimit-limit:
      schema:
        type: integer
      example: 200
      description: Ratelimit set for your account for this API per minute.
    x-ratelimit-remaining:
      schema:
        type: integer
      example: 2
      description: >-
        Rate limit remaning for your account for this API in the next minute.
        Uses sliding window.
    x-ratelimit-retry:
      schema:
        type: integer
      example: 4
      description: |
        Contains number of seconds to wait if rate limit is breached
        - Is 0 if withing the limit
        - Is between 1 and 59 if breached
    x-ratelimit-type:
      schema:
        type: string
        enum:
          - app_id
          - ip
      example: ip
      description: >
        either ip or app_id

        - `ip` if making a call from the browser. True for api where you don't
        need `x-client-id` and `x-client-secret`

        - `app_id` for authenticated api calls i.e using `x-client-id` and
        `x-client-secret`
    x-request-id:
      schema:
        type: string
      example: some-req-id
      description: >-
        Request id for your api call. Is blank or null if no `x-request-id` is
        sent during the request.
    x-idempotency-key:
      schema:
        type: string
      example: some-idem-id
      description: >-
        An idempotency key is a unique identifier you include with your API
        call. If the request fails or times out, you can safely retry it using
        the same key to avoid duplicate actions.
    x-idempotency-replayed:
      schema:
        type: string
        format: boolean
      example: 'true'
      description: |-
        In conjunction with `x-idempotency-key` this means
        - `true` if the response was replayed
        - `false` if the response has not been replayed.
  responses:
    Response400:
      description: Bad request error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/BadRequestError'
      headers:
        x-api-version:
          $ref: '#/components/headers/x-api-version'
        x-ratelimit-limit:
          $ref: '#/components/headers/x-ratelimit-limit'
        x-ratelimit-remaining:
          $ref: '#/components/headers/x-ratelimit-remaining'
        x-ratelimit-retry:
          $ref: '#/components/headers/x-ratelimit-retry'
        x-ratelimit-type:
          $ref: '#/components/headers/x-ratelimit-type'
        x-request-id:
          $ref: '#/components/headers/x-request-id'
        x-idempotency-key:
          $ref: '#/components/headers/x-idempotency-key'
        x-idempotency-replayed:
          $ref: '#/components/headers/x-idempotency-replayed'
    Response401:
      description: Authentication Error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/AuthenticationError'
      headers:
        x-api-version:
          $ref: '#/components/headers/x-api-version'
        x-ratelimit-limit:
          $ref: '#/components/headers/x-ratelimit-limit'
        x-ratelimit-remaining:
          $ref: '#/components/headers/x-ratelimit-remaining'
        x-ratelimit-retry:
          $ref: '#/components/headers/x-ratelimit-retry'
        x-ratelimit-type:
          $ref: '#/components/headers/x-ratelimit-type'
        x-request-id:
          $ref: '#/components/headers/x-request-id'
        x-idempotency-key:
          $ref: '#/components/headers/x-idempotency-key'
        x-idempotency-replayed:
          $ref: '#/components/headers/x-idempotency-replayed'
    Response404:
      description: Resource Not found.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError404'
      headers:
        x-api-version:
          $ref: '#/components/headers/x-api-version'
        x-ratelimit-limit:
          $ref: '#/components/headers/x-ratelimit-limit'
        x-ratelimit-remaining:
          $ref: '#/components/headers/x-ratelimit-remaining'
        x-ratelimit-retry:
          $ref: '#/components/headers/x-ratelimit-retry'
        x-ratelimit-type:
          $ref: '#/components/headers/x-ratelimit-type'
        x-request-id:
          $ref: '#/components/headers/x-request-id'
        x-idempotency-key:
          $ref: '#/components/headers/x-idempotency-key'
        x-idempotency-replayed:
          $ref: '#/components/headers/x-idempotency-replayed'
    Response422:
      description: Idempotency error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/IdempotencyError'
      headers:
        x-api-version:
          $ref: '#/components/headers/x-api-version'
        x-ratelimit-limit:
          $ref: '#/components/headers/x-ratelimit-limit'
        x-ratelimit-remaining:
          $ref: '#/components/headers/x-ratelimit-remaining'
        x-ratelimit-retry:
          $ref: '#/components/headers/x-ratelimit-retry'
        x-ratelimit-type:
          $ref: '#/components/headers/x-ratelimit-type'
        x-request-id:
          $ref: '#/components/headers/x-request-id'
        x-idempotency-key:
          $ref: '#/components/headers/x-idempotency-key'
        x-idempotency-replayed:
          $ref: '#/components/headers/x-idempotency-replayed'
    Response429:
      description: Rate Limit Error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/RateLimitError'
      headers:
        x-api-version:
          $ref: '#/components/headers/x-api-version'
        x-ratelimit-limit:
          $ref: '#/components/headers/x-ratelimit-limit'
        x-ratelimit-remaining:
          $ref: '#/components/headers/x-ratelimit-remaining'
        x-ratelimit-retry:
          $ref: '#/components/headers/x-ratelimit-retry'
        x-ratelimit-type:
          $ref: '#/components/headers/x-ratelimit-type'
        x-request-id:
          $ref: '#/components/headers/x-request-id'
        x-idempotency-key:
          $ref: '#/components/headers/x-idempotency-key'
        x-idempotency-replayed:
          $ref: '#/components/headers/x-idempotency-replayed'
    Response500:
      description: API related Error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ApiError'
      headers:
        x-api-version:
          $ref: '#/components/headers/x-api-version'
        x-ratelimit-limit:
          $ref: '#/components/headers/x-ratelimit-limit'
        x-ratelimit-remaining:
          $ref: '#/components/headers/x-ratelimit-remaining'
        x-ratelimit-retry:
          $ref: '#/components/headers/x-ratelimit-retry'
        x-ratelimit-type:
          $ref: '#/components/headers/x-ratelimit-type'
        x-request-id:
          $ref: '#/components/headers/x-request-id'
        x-idempotency-key:
          $ref: '#/components/headers/x-idempotency-key'
        x-idempotency-replayed:
          $ref: '#/components/headers/x-idempotency-replayed'
  examples:
    create_subscription_charge:
      description: Create Payment. Charge Subscription.
      summary: Create Payment
      value:
        subscription_id: test-subscription-id
        payment_id: test-payment-id
        payment_amount: 10
        payment_schedule_date: '2025-06-01T16:40:00'
        payment_remarks: 2nd EMI payment
        payment_type: CHARGE
        payment_method:
          upi:
            upi_id: john@upi
            channel: collect
    create_subscription_auth_upi_link:
      description: Create Auth using UPI Link.
      summary: Create Auth - UPI Link
      value:
        subscription_id: test-subscription-id
        subscription_session_id: sub_session_Vf5ZOcJTbGkcw4kcpayment
        payment_id: test-payment-id
        payment_type: AUTH
        payment_method:
          upi:
            channel: link
            upi_id: john.doe@okbank
    create_subscription_auth_upi_collect:
      description: Create Auth using UPI Collect.
      summary: Create Auth - UPI Collect
      value:
        subscription_id: test-subscription-id
        subscription_session_id: sub_session_Vf5ZOcJTbGkcw4kcpayment
        payment_id: test-payment-id
        payment_type: AUTH
        payment_method:
          upi:
            channel: collect
            upi_id: john.doe@okbank
    create_subscription_auth_upi_qrcode:
      description: Create Auth using UPI QR Code.
      summary: Create Auth - UPI QR Code
      value:
        subscription_id: test-subscription-id
        subscription_session_id: sub_session_Vf5ZOcJTbGkcw4kcpayment
        payment_id: test-payment-id
        payment_type: AUTH
        payment_method:
          upi:
            channel: qrcode
    create_subscription_auth_card:
      description: Create Auth using Card.
      summary: Create Auth - Card
      value:
        subscription_id: test-subscription-id
        subscription_session_id: sub_session_Vf5ZOcJTbGkcw4kcpayment
        payment_id: test-payment-id
        payment_type: AUTH
        payment_method:
          card:
            channel: link
            card_number: '4111111111111111'
            card_holder_name: John Doe
            card_expiry_mm: '12'
            card_expiry_yy: '25'
            card_cvv: '123'
            card_network: VISA
            card_type: CREDIT
    create_subscription_auth_enach:
      description: Create Auth using eNACH.
      summary: Create Auth - eNACH
      value:
        subscription_id: test-subscription-id
        subscription_session_id: sub_session_Vf5ZOcJTbGkcw4kcpayment
        payment_id: test-payment-id
        payment_type: AUTH
        payment_method:
          enach:
            channel: link
            auth_mode: net_banking
            account_holder_name: John Doe
            account_number: '1518121112'
            account_type: SAVINGS
            account_bank_code: ICIC
    create_subscription_auth_pnach:
      description: Create Auth using Physical NACH.
      summary: Create Auth - Physical NACH
      value:
        subscription_id: test-subscription-id
        subscription_session_id: sub_session_Vf5ZOcJTbGkcw4kcpayment
        payment_id: test-payment-id
        payment_type: AUTH
        payment_method:
          pnach:
            channel: post
            account_holder_name: John Doe
            account_number: '1518121112'
            account_type: SAVINGS
            account_bank_code: ICIC
            account_ifsc: ICIC0000123
            mandate_creation_date: '2025-06-01'
            mandate_start_date: '2025-06-05'
  securitySchemes:
    XClientID:
      type: apiKey
      in: header
      name: x-client-id
      description: >-
        Client app ID. You can find your app id in the [Merchant
        Dashboard](https://merchant.cashfree.com/auth/login/pg/developers/api-keys?env=prod).
    XClientSecret:
      type: apiKey
      in: header
      name: x-client-secret
      description: >-
        Client secret key. You can find your secret key in the [Merchant
        Dashboard](https://merchant.cashfree.com/auth/login/pg/developers/api-keys?env=prod).
    XPartnerAPIKey:
      type: apiKey
      in: header
      name: x-partner-apikey
      description: >-
        If you are partner and you are making an api call on behalf of a
        merchant.
    XClientSignatureHeader:
      type: apiKey
      in: header
      name: x-client-signature
      description: >-
        Use this if you do not want to pass the secret key and instead want to
        use signature.
    XPartnerMerchantID:
      type: apiKey
      in: header
      name: x-partner-merchantid
      description: >-
        If you are partner use this to specify the merchant ID if you don't have
        the merchant client app ID.

````