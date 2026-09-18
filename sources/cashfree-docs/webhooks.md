<!-- Captured 18 Sep 2026 from Cashfree's Subscriptions documentation (https://www.cashfree.com/docs/). Cashfree's live page is the authority. -->

> ## Documentation Index
> Fetch the complete documentation index at: https://www.cashfree.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Events

> Receive Cashfree Subscriptions webhook events for mandate authorisation, charges, payment status changes, and subscription lifecycle updates on your endpoint.

Cashfree sends webhook notifications to your server whenever significant events occur during the lifecycle of a subscription, enabling you to track subscription status changes, payment outcomes, authorisation updates, and refund status in real-time without polling the API. By listening to these webhooks, you can automate your business workflows, update your database, and keep your customers informed about their subscription status.

Below are the various events that can be sent to your webhook endpoint. These webhooks will be triggered if you have integrated the Subscription API.

<Note>
  * If the merchant added the webhook under the 2025-01-01 version, they will receive the same version of the webhook for older subscriptions as well.
  * While filling the UPI payment methods, `upi_instrument` and `upi_instrument_number` will remain empty for webhook versions before 2025. This will be implemented in later versions.
  * While filling the UPI payment methods, `upi_payer_account_number` and `upi_payer_ifsc` will be applicable only for TPV customers who have passed TPV details while creating the subscription.
</Note>

* [`SUBSCRIPTION_STATUS_CHANGED`](/docs/api-reference/payments/latest/subscription/webhooks#subscription_status_changed)
* [`SUBSCRIPTION_AUTH_STATUS`](/docs/api-reference/payments/latest/subscription/webhooks#subscription_auth_status)
* [`SUBSCRIPTION_PAYMENT_NOTIFICATION_INITIATED`](/docs/api-reference/payments/latest/subscription/webhooks#subscription_payment_notification_initiated)
* [`SUBSCRIPTION_PAYMENT_SUCCESS`](/docs/api-reference/payments/latest/subscription/webhooks#subscription_payment_success)
* [`SUBSCRIPTION_PAYMENT_FAILED`](/docs/api-reference/payments/latest/subscription/webhooks#subscription_payment_failed)
* [`SUBSCRIPTION_PAYMENT_CANCELLED`](/docs/api-reference/payments/latest/subscription/webhooks#subscription_payment_cancelled)
* [`SUBSCRIPTION_REFUND_STATUS`](/docs/api-reference/payments/latest/subscription/webhooks#subscription_refund_status)
* [`SUBSCRIPTION_CARD_EXPIRY_REMINDER`](/docs/api-reference/payments/latest/subscription/webhooks#subscription_card_expiry_reminder)
* [`SUBSCRIPTION_CONTROLLED_NOTIFICATION_STATUS`](/docs/api-reference/payments/latest/subscription/webhooks#subscription_controlled_notification_status)
* [`SUBSCRIPTION_CONTROLLED_EXECUTION_STATUS`](/docs/api-reference/payments/latest/subscription/webhooks#subscription_controlled_execution_status)

Payment method object attributes:

<CodeGroup>
  ```javascript UPI theme={"dark"}
  "payment_method": {
        "upi": {
          "channel": "collect",
          "upi_id": "8709228804@ybl",
          "upi_instrument": "",
          "upi_instrument_number": "",
          "upi_payer_account_number": "",
          "upi_payer_ifsc": ""
        }
  },
  "payment_group": "upi"
  ```

  ```javascript ENACH theme={"dark"}
  "payment_method": {
      "enach": {
        "channel": "link",
        "auth_mode": "aadhar",
        "account_type": "",
        "account_number": "",
        "account_ifsc": "",
        "account_holder_name": "",
        "account_bank_code": ""
      }
  },
  "payment_group": "enach"
  ```

  ```javascript PNACH theme={"dark"}
  "payment_method": {
      "pnach": {
        "channel": "link",
        "mandate_creation_date": "",
        "mandate_start_date": "",
        "account_type": "",
        "account_number": "",
        "account_ifsc": "",
        "account_holder_name": "",
        "account_bank_code": ""
      }
  },
  "payment_group": "pnach"
  ```

  ```javascript Debit/Credit card theme={"dark"}
  {
    "payment_method": {
      "card": {
        "channel": null,
        "card_number": "XXXXXXXXXXXX2123",
        "card_network": "visa",
        "card_type": "debit_card",
        "card_sub_type": "R",
        "card_country": "IN",
        "card_bank_name": "KOTAK MAHINDRA BANK",
        "card_network_reference_id": null,
        "instrument_id": "8e9cc167-4fe2-4ece-be8d-c1b224e50a23"
      }
    },
    "payment_group": "debit_card"
  }
  ```
</CodeGroup>

## SUBSCRIPTION\_STATUS\_CHANGED

Whenever a subscription is created it goes to initialised state and customer is expected to authorise it. The list of statuses where this webhook will get triggered are:

* ACTIVE
* ON\_HOLD
* COMPLETED
* CUSTOMER\_CANCELLED
* CUSTOMER\_PAUSED
* EXPIRED
* LINK\_EXPIRED
* BANK\_APPROVAL\_PENDING
* CANCELLED
* CARD\_EXPIRED

<Tabs>
  <Tab title="Version (2025-01-01)">
    ```javascript theme={"dark"}
    {
    "data": {
    "subscription_details": {
      "cf_subscription_id": "23639356",
      "subscription_id": "mozuyYwUCbWEfJVVRLi",
      "subscription_status": "BANK_APPROVAL_PENDING",
      "subscription_expiry_time": "2055-08-07T10:30:46",
      "subscription_first_charge_time": null,
      "subscription_tags": null,
      "next_schedule_date": null
    },
    "customer_details": {
      "customer_name": null,
      "customer_email": "john@dummy.com",
      "customer_phone": "9900000000"
    },
    "plan_details": {
      "plan_id": "mozuyYwUCbWEfJVVRLi",
      "plan_name": "6Msuj2mttuf2F5P1FYVSet",
      "plan_type": "ON_DEMAND",
      "plan_max_cycles": 0,
      "plan_recurring_amount": null,
      "plan_max_amount": 399.00,
      "plan_interval_type": null,
      "plan_intervals": null,
      "plan_currency": "INR",
      "plan_note": null,
      "plan_status": null
    },
    "authorization_details": {
      "authorization_amount": 2.00,
      "authorization_amount_refund": false,
      "approve_by_time": "2025-09-06T10:30:47",
      "authorization_reference": "6ba74ac2b047424da95591xxxxx[at]xxxx",
      "authorization_time": "2025-08-07T10:31:36",
      "authorization_status": "PENDING",
      "payment_id": "49988270",
      "payment_method": {
        "upi": {
          "channel": "link",
          "upi_id": "9910000000@ybl",
          "upi_instrument": "",
          "upi_instrument_number": "",
          "upi_payer_account_number": "",
          "upi_payer_ifsc": ""
        }
      },
      "payment_group": "upi"
    },
    "payment_gateway_details": {
      "gateway_name": "CASHFREE",
      "gateway_subscription_id": "23639356",
      "gateway_plan_id": "mozuyYwUCbWEfJVVRLi",
      "gateway_auth_id": "6ba74ac2b047424da95591xxxxx[at]xxxx"
    }
    },
    "event_time": "2025-08-07T10:31:35+05:30",
    "type": "SUBSCRIPTION_STATUS_CHANGED"
    }
    ```
  </Tab>

  <Tab title="Version (2023-08-01)">
    ```javascript theme={"dark"}
    {
    "data": {
        "subscription_details": {
            "cf_subscription_id": "123456",
            "subscription_id": "Demo_Subscription",
            "subscription_status": "ACTIVE",
            "subscription_expiry_time": "2024-01-14T23:00:08+05:30",
            "subscription_first_charge_time": "2024-01-10T23:00:08+05:30"
        },
        "customer_details": {
            "customer_name": "john",
            "customer_email": "john@dummy.com",
            "customer_phone": "9900000000"
        },
        "plan_details": {
            "plan_id": "plan12345",
            "plan_name": "Plan Name",
            "plan_type": "ON_DEMAND",
            "plan_max_cycles": 10,
            "plan_recurring_amount": 100.00,
            "plan_max_amount": 1000.00,
            "plan_currency": "INR",
            "plan_note": "Note",
            "plan_status": "ACTIVE"
        },
        "authorization_details": {
            "authorizationAmount": 1.00,
            "authorizationAmountRefund": true,
            "approveByTime": "2025-09-06T16:44:48",
            "authorizationReference": "544edde057f34ce588627axxxxx[at]xxxx",
            "authorizationTime": "2025-08-07T16:46:06",
            "authorizationStatus": "PENDING",
            "paymentId": "50088288",
            "paymentMethod": "upi",
            "instrumentId": "xxxxx@xxxx"
        },
        "payment_gateway_details": {
            "gateway_name": "CASHFREE",
            "gateway_subscription_id": "Demo_Subscription",
            "gateway_plan_id": "plan12345",
            "gateway_auth_id": "6595231908096894505959"
        }
    },
    "event_time": "2023-01-03T11:16:10+05:30",
    "type": "SUBSCRIPTION_STATUS_CHANGED"
    }
    ```
  </Tab>
</Tabs>

## SUBSCRIPTION\_AUTH\_STATUS

The event is triggered when the checkout is completed by the customer for success and failed cases.

<Tabs>
  <Tab title="Version (2026-01-01)">
    ```javascript theme={"dark"}
    {
     "data": {
       "payment_id": "ab-SUBV2ODRFhdJuHlcQYyFw-1",
       "cf_payment_id": "49988825",
       "cf_txn_id": "4213159266",
       "cf_order_id": "4519691525",
       "subscription_id": "mozth7smWGCCqPRaSv7",
       "cf_subscription_id": "23639858",
       "payment_type": "AUTH",
       "subscription_details": {
         "cf_subscription_id": "23639858",
         "subscription_id": "mozth7smWGCCqPRaSv7",
         "subscription_status": "ACTIVE",
         "subscription_expiry_time": "2047-07-30T13:24:54",
         "subscription_first_charge_time": null,
         "subscription_tags": {
           "company": "Cashfree",
           "name": "Payment link"
         },
         "next_schedule_date": null
       },
       "authorization_details": {
         "authorization_amount": 2.00,
         "authorization_amount_refund": false,
         "approve_by_time": "",
         "authorization_reference": "cce92d335be0467693c020xxxxx[at]xxxx",
         "authorization_time": "2025-08-07T10:34:23+05:30",
         "authorization_status": "FAILED",
         "payment_id": "ab-SUBV2ODRFhdJuHlcQYyFw-1",
         "payment_method": {
           "upi": {
             "channel": "link",
             "upi_id": "9910000000@ybl",
             "upi_instrument": "",
             "upi_instrument_number": "",
             "upi_payer_account_number": "",
             "upi_payer_ifsc": ""
           }
         },
         "payment_group": "upi"
       },
       "payment_amount": 2.00,
       "payment_currency": "INR",
       "payment_schedule_date": "",
       "payment_initiated_date": "2025-08-07T10:33:56+05:30",
       "payment_remarks": "auth payment",
       "retry_attempts": 0,
       "failure_details": {
         "failure_reason": "DEBIT HAS BEEN FAILED"
       },
       "payment_status": "FAILED",
       "payment_gateway_details": {
         "gateway_name": "CASHFREE",
         "gateway_subscription_id": "23639858",
         "gateway_payment_id": "49988825"
       }
     },
     "event_time": "2025-08-07T10:34:23+05:30",
     "type": "SUBSCRIPTION_AUTH_STATUS"
    }
    ```
  </Tab>

  <Tab title="Version (2025-01-01)">
    ```javascript theme={"dark"}
    {
     "data": {
       "payment_id": "ab-SUBV2ODRFhdJuHlcQYyFw-1",
       "cf_payment_id": "49988825",
       "cf_txn_id": "4213159266",
       "cf_order_id": "4519691525",
       "subscription_id": "mozth7smWGCCqPRaSv7",
       "cf_subscription_id": "23639858",
       "payment_type": "AUTH",
       "authorization_details": {
         "authorization_amount": 2.00,
         "authorization_amount_refund": false,
         "approve_by_time": "",
         "authorization_reference": "cce92d335be0467693c020xxxxx[at]xxxx",
         "authorization_time": "2025-08-07T10:34:23+05:30",
         "authorization_status": "FAILED",
         "payment_id": "ab-SUBV2ODRFhdJuHlcQYyFw-1",
         "payment_method": {
           "upi": {
             "channel": "link",
             "upi_id": "9910000000@ybl",
             "upi_instrument": "",
             "upi_instrument_number": "",
             "upi_payer_account_number": "",
             "upi_payer_ifsc": ""
           }
         },
         "payment_group": "upi"
       },
       "payment_amount": 2.00,
       "payment_currency": "INR",
       "payment_schedule_date": "",
       "payment_initiated_date": "2025-08-07T10:33:56+05:30",
       "payment_remarks": "auth payment",
       "retry_attempts": 0,
       "failure_details": {
         "failure_reason": "DEBIT HAS BEEN FAILED"
       },
       "payment_status": "FAILED",
       "payment_gateway_details": {
         "gateway_name": "CASHFREE",
         "gateway_subscription_id": "23639858",
         "gateway_payment_id": "49988825"
       }
     },
     "event_time": "2025-08-07T10:34:23+05:30",
     "type": "SUBSCRIPTION_AUTH_STATUS"
    }
    ```
  </Tab>

  <Tab title="Version (2023-08-01)">
    ```javascript theme={"dark"}
    {
    "data": {
        "payment_id": "12345",
        "cf_payment_id": "67890",
        "cf_txn_id": "789012",
        "cf_order_id": "98765",
        "subscription_id": "sub12345",
        "cf_subscription_id": "sub67890",
        "payment_type": "DEBIT_CARD",
        "authorization_details": {
            "authorization_amount": 100,
            "authorization_amount_refund": true,
            "approve_by_time": "2024-07-20T16:09:50+05:30",
            "authorization_reference": "6595231908096894505959",
            "authorization_time": "2024-07-20T16:09:51",
            "authorization_status": "ACTIVE",
            "payment_id": "123",
            "payment_method": "DEBIT_CARD",
            "instrument_id": "hsdg9"
        },
        "payment_amount": 200.75,
        "payment_schedule_date": "2024-07-20",
        "payment_initiated_date": "2024-07-20",
        "payment_remarks": "auth payment",
        "retry_attempts": 0,
        "failureDetails": null,
        "payment_status": "SUCCESS",
        "payment_gateway_details": {
            "gateway_name": "CASHFREE",
            "gateway_subscription_id": "Demo_Subscription",
            "gateway_payment_id": "payment12345"
        }
    },
    "event_time": "2024-07-20T11:16:10+05:30",
    "type": "SUBSCRIPTION_AUTH_STATUS"
    }
    ```
  </Tab>
</Tabs>

## SUBSCRIPTION\_PAYMENT\_NOTIFICATION\_INITIATED

This webhook is used to inform the merchant that we have sent a notification of payment to the customer.

<Tabs>
  <Tab title="Version (2026-01-01)">
    ```javascript Version (2026-01-01) theme={"dark"}
    {
    "data": {
    "payment_id": "ab-SUBV2ODR683gV1CXF85ev-1",
    "cf_payment_id": "49970855",
    "cf_txn_id": null,
    "cf_order_id": "",
    "subscription_id": "moziva9hyjiLtCuGN74",
    "cf_subscription_id": "22390006",
    "payment_type": "CHARGE",
    "subscription_details": {
      "cf_subscription_id": "22390006",
      "subscription_id": "moziva9hyjiLtCuGN74",
      "subscription_status": "ACTIVE",
      "subscription_expiry_time": "2047-07-30T13:24:54",
      "subscription_first_charge_time": null,
      "subscription_tags": {
        "company": "Cashfree",
        "name": "Payment link"
      },
      "next_schedule_date": null
    },
    "authorization_details": {
      "authorization_amount": 399.00,
      "authorization_amount_refund": false,
      "approve_by_time": "",
      "authorization_reference": null,
      "authorization_time": "",
      "authorization_status": null,
      "payment_id": "ab-SUBV2ODR683gV1CXF85ev-1",
      "payment_method": null,
      "payment_group": null
    },
    "payment_amount": 399.00,
    "payment_currency": "INR",
    "payment_schedule_date": "2025-08-08T12:00:00+05:30",
    "payment_initiated_date": "2025-08-07T09:08:09+05:30",
    "payment_remarks": null,
    "retry_attempts": 0,
    "failure_details": {
      "failure_reason": null
    },
    "payment_status": "INITIALIZED",
    "payment_gateway_details": {
      "gateway_name": "CASHFREE",
      "gateway_subscription_id": "22390006",
      "gateway_payment_id": "49970855"
    }
    },
    "event_time": "2025-08-07T09:51:07+05:30",
    "type": "SUBSCRIPTION_PAYMENT_NOTIFICATION_INITIATED"
    }
    ```
  </Tab>

  <Tab title="Version (2025-01-01)">
    ```javascript Version (2025-01-01) theme={"dark"}
    {
    "data": {
    "payment_id": "ab-SUBV2ODR683gV1CXF85ev-1",
    "cf_payment_id": "49970855",
    "cf_txn_id": null,
    "cf_order_id": "",
    "subscription_id": "moziva9hyjiLtCuGN74",
    "cf_subscription_id": "22390006",
    "payment_type": "CHARGE",
    "authorization_details": {
      "authorization_amount": 399.00,
      "authorization_amount_refund": false,
      "approve_by_time": "",
      "authorization_reference": null,
      "authorization_time": "",
      "authorization_status": null,
      "payment_id": "ab-SUBV2ODR683gV1CXF85ev-1",
      "payment_method": null,
      "payment_group": null
    },
    "payment_amount": 399.00,
    "payment_currency": "INR",
    "payment_schedule_date": "2025-08-08T12:00:00+05:30",
    "payment_initiated_date": "2025-08-07T09:08:09+05:30",
    "payment_remarks": null,
    "retry_attempts": 0,
    "failure_details": {
      "failure_reason": null
    },
    "payment_status": "INITIALIZED",
    "payment_gateway_details": {
      "gateway_name": "CASHFREE",
      "gateway_subscription_id": "22390006",
      "gateway_payment_id": "49970855"
    }
    },
    "event_time": "2025-08-07T09:51:07+05:30",
    "type": "SUBSCRIPTION_PAYMENT_NOTIFICATION_INITIATED"
    }
    ```
  </Tab>

  <Tab title="Version (2023-08-01)">
    ```javascript theme={"dark"}
    {
    "data": {
        "payment_id": "12345",
        "cf_payment_id": "67890",
        "cf_txn_id": "789012",
        "cf_order_id": "98765",
        "subscription_id": "sub12345",
        "cf_subscription_id": "sub67890",
        "payment_type": "DEBIT_CARD",
        "authorization_details": {
            "authorization_amount": 100,
            "authorization_amount_refund": true,
            "approve_by_time": "2024-07-20T16:09:50+05:30",
            "authorization_reference": "6595231908096894505959",
            "authorization_time": "2024-07-20T16:09:51",
            "authorization_status": "PENDING",
            "payment_id": "123",
            "payment_method": "DEBIT_CARD",
            "instrument_id": "hsdg9"
        },
        "payment_amount": 200,
        "payment_schedule_date": "2024-07-20",
        "payment_initiated_date": "2024-07-20",
        "payment_remarks": "payment",
        "retry_attempts": 0,
        "failureDetails": null,
        "payment_status": "INITIALIZED",
        "payment_gateway_details": {
            "gateway_name": "CASHFREE",
            "gateway_subscription_id": "Demo_Subscription",
            "gateway_payment_id": "payment12345"
        }
    },
    "event_time": "2024-07-20T11:16:10+05:30",
    "type": "SUBSCRIPTION_PAYMENT_NOTIFICATION_INITIATED"
    }
    ```
  </Tab>
</Tabs>

## SUBSCRIPTION\_PAYMENT\_SUCCESS

This notification is sent whenever a successful payment is processed for an active subscription.

<Tabs>
  <Tab title="Version (2026-01-01)">
    ```javascript Version (2026-01-01) theme={"dark"}
    {
    "data": {
    "payment_id": "ab-SUBV2ODRc5Dl2meCr7Iui-1",
    "cf_payment_id": "49914526",
    "cf_txn_id": "4212435861",
    "cf_order_id": "4518936510",
    "subscription_id": "moznV33AssPd6vXsSm2",
    "cf_subscription_id": "23601811",
    "payment_type": "AUTH",
    "subscription_details": {
      "cf_subscription_id": "23601811",
      "subscription_id": "moznV33AssPd6vXsSm2",
      "subscription_status": "ACTIVE",
      "subscription_expiry_time": "2047-07-30T13:24:54",
      "subscription_first_charge_time": null,
      "subscription_tags": {
        "company": "Cashfree",
        "name": "Payment link"
      },
      "next_schedule_date": null
    },
    "authorization_details": {
      "authorization_amount": 2.00,
      "authorization_amount_refund": false,
      "approve_by_time": "",
      "authorization_reference": "427b608f83ad4cbdb6d472xxxxx[at]xxxx",
      "authorization_time": "2025-08-07T05:53:22+05:30",
      "authorization_status": "ACTIVE",
      "payment_id": "ab-SUBV2ODRc5Dl2meCr7Iui-1",
      "payment_method": {
        "upi": {
          "channel": "link",
          "upi_id": "8100000000@ybl",
          "upi_instrument": "",
          "upi_instrument_number": "",
          "upi_payer_account_number": "",
          "upi_payer_ifsc": ""
        }
      },
      "payment_group": "upi"
    },
    "payment_amount": 2.00,
    "payment_currency": "INR",
    "payment_schedule_date": "",
    "payment_initiated_date": "2025-08-07T05:52:21+05:30",
    "payment_remarks": "auth payment",
    "retry_attempts": 0,
    "failure_details": {
      "failure_reason": null
    },
    "payment_status": "SUCCESS",
    "payment_gateway_details": {
      "gateway_name": "CASHFREE",
      "gateway_subscription_id": "23601811",
      "gateway_payment_id": "49914526"
    }
    },
    "event_time": "2025-08-07T05:53:21+05:30",
    "type": "SUBSCRIPTION_PAYMENT_SUCCESS"
    }

    ```
  </Tab>

  <Tab title="Version (2025-01-01)">
    ```javascript Version (2025-01-01) theme={"dark"}
    {
    "data": {
    "payment_id": "ab-SUBV2ODRc5Dl2meCr7Iui-1",
    "cf_payment_id": "49914526",
    "cf_txn_id": "4212435861",
    "cf_order_id": "4518936510",
    "subscription_id": "moznV33AssPd6vXsSm2",
    "cf_subscription_id": "23601811",
    "payment_type": "AUTH",
    "authorization_details": {
      "authorization_amount": 2.00,
      "authorization_amount_refund": false,
      "approve_by_time": "",
      "authorization_reference": "427b608f83ad4cbdb6d472xxxxx[at]xxxx",
      "authorization_time": "2025-08-07T05:53:22+05:30",
      "authorization_status": "ACTIVE",
      "payment_id": "ab-SUBV2ODRc5Dl2meCr7Iui-1",
      "payment_method": {
        "upi": {
          "channel": "link",
          "upi_id": "8100000000@ybl",
          "upi_instrument": "",
          "upi_instrument_number": "",
          "upi_payer_account_number": "",
          "upi_payer_ifsc": ""
        }
      },
      "payment_group": "upi"
    },
    "payment_amount": 2.00,
    "payment_currency": "INR",
    "payment_schedule_date": "",
    "payment_initiated_date": "2025-08-07T05:52:21+05:30",
    "payment_remarks": "auth payment",
    "retry_attempts": 0,
    "failure_details": {
      "failure_reason": null
    },
    "payment_status": "SUCCESS",
    "payment_gateway_details": {
      "gateway_name": "CASHFREE",
      "gateway_subscription_id": "23601811",
      "gateway_payment_id": "49914526"
    }
    },
    "event_time": "2025-08-07T05:53:21+05:30",
    "type": "SUBSCRIPTION_PAYMENT_SUCCESS"
    }

    ```
  </Tab>

  <Tab title="Version (2023-08-01)">
    ```javascript theme={"dark"}
    {
    "data": {
        "payment_id": "12345",
        "cf_payment_id": "67890",
        "cf_txn_id": "789012",
        "cf_order_id": "98765",
        "subscription_id": "sub12345",
        "cf_subscription_id": "sub67890",
        "payment_type": "DEBIT_CARD",
        "authorization_details": {
            "authorization_amount": 100,
            "authorization_amount_refund": true,
            "approve_by_time": "2024-07-20T16:09:50+05:30",
            "authorization_reference": "6595231908096894505959",
            "authorization_time": "2024-07-20T16:09:51",
            "authorization_status": "ACTIVE",
            "payment_id": "123",
            "payment_method": "DEBIT_CARD",
            "instrument_id": "hsdg9"
        },
        "payment_amount": 200,
        "payment_schedule_date": "2024-07-20",
        "payment_initiated_date": "2024-07-20",
        "payment_remarks": "payment",
        "retry_attempts": 0,
        "failureDetails": null,
        "payment_status": "SUCCESS",
        "payment_gateway_details": {
            "gateway_name": "CASHFREE",
            "gateway_subscription_id": "Demo_Subscription",
            "gateway_payment_id": "payment12345"
        }
    },
    "event_time": "2024-07-20T11:16:10+05:30",
    "type": "SUBSCRIPTION_PAYMENT_SUCCESS"
    }
    ```
  </Tab>
</Tabs>

## SUBSCRIPTION\_PAYMENT\_FAILED

This notification is sent whenever payment processing fails for an active subscription.

<Tabs>
  <Tab title="Version (2026-01-01)">
    ```javascript theme={"dark"}
    {
    "data": {
    "payment_id": "ab-SUBV2ODRIeYlFEhMHfS0M-1",
    "cf_payment_id": "49585655",
    "cf_txn_id": "4212555720",
    "cf_order_id": "4519061918",
    "subscription_id": "mozh4iRHSsjre7GkDNz",
    "cf_subscription_id": "22393526",
    "payment_type": "CHARGE",
    "subscription_details": {
      "cf_subscription_id": "22393526",
      "subscription_id": "mozh4iRHSsjre7GkDNz",
      "subscription_status": "ACTIVE",
      "subscription_expiry_time": "2047-07-30T13:24:54",
      "subscription_first_charge_time": null,
      "subscription_tags": {
        "company": "Cashfree",
        "name": "Payment link"
      },
      "next_schedule_date": null
    },
    "authorization_details": {
      "authorization_amount": 399.00,
      "authorization_amount_refund": false,
      "approve_by_time": "",
      "authorization_reference": "a7d6101a7d9340269f070dxxxxx[at]xxxx",
      "authorization_time": "2025-07-25T22:37:53+05:30",
      "authorization_status": "ACTIVE",
      "payment_id": "ab-SUBV2ODRIeYlFEhMHfS0M-1",
      "payment_method": {
        "upi": {
          "channel": "link",
          "upi_id": "9910000000@ybl",
          "upi_instrument": "",
          "upi_instrument_number": "",
          "upi_payer_account_number": "",
          "upi_payer_ifsc": ""
        }
      },
      "payment_group": "upi"
    },
    "payment_amount": 399.00,
    "payment_currency": "INR",
    "payment_schedule_date": "2025-08-07T12:00:00+05:30",
    "payment_initiated_date": "2025-08-06T05:02:41+05:30",
    "payment_remarks": null,
    "retry_attempts": 0,
    "failure_details": {
      "failure_reason": "DEBIT FAILED | Insufficient Funds In Customer (Remitter) Account"
    },
    "payment_status": "FAILED",
    "payment_gateway_details": {
      "gateway_name": "CASHFREE",
      "gateway_subscription_id": "22393526",
      "gateway_payment_id": "49585655"
    }
    },
    "event_time": "2025-08-07T10:24:45+05:30",
    "type": "SUBSCRIPTION_PAYMENT_FAILED"
    }


    ```
  </Tab>

  <Tab title="Version (2025-01-01)">
    ```javascript theme={"dark"}
    {
    "data": {
    "payment_id": "ab-SUBV2ODRIeYlFEhMHfS0M-1",
    "cf_payment_id": "49585655",
    "cf_txn_id": "4212555720",
    "cf_order_id": "4519061918",
    "subscription_id": "mozh4iRHSsjre7GkDNz",
    "cf_subscription_id": "22393526",
    "payment_type": "CHARGE",
    "authorization_details": {
      "authorization_amount": 399.00,
      "authorization_amount_refund": false,
      "approve_by_time": "",
      "authorization_reference": "a7d6101a7d9340269f070dxxxxx[at]xxxx",
      "authorization_time": "2025-07-25T22:37:53+05:30",
      "authorization_status": "ACTIVE",
      "payment_id": "ab-SUBV2ODRIeYlFEhMHfS0M-1",
      "payment_method": {
        "upi": {
          "channel": "link",
          "upi_id": "9910000000@ybl",
          "upi_instrument": "",
          "upi_instrument_number": "",
          "upi_payer_account_number": "",
          "upi_payer_ifsc": ""
        }
      },
      "payment_group": "upi"
    },
    "payment_amount": 399.00,
    "payment_currency": "INR",
    "payment_schedule_date": "2025-08-07T12:00:00+05:30",
    "payment_initiated_date": "2025-08-06T05:02:41+05:30",
    "payment_remarks": null,
    "retry_attempts": 0,
    "failure_details": {
      "failure_reason": "DEBIT FAILED | Insufficient Funds In Customer (Remitter) Account"
    },
    "payment_status": "FAILED",
    "payment_gateway_details": {
      "gateway_name": "CASHFREE",
      "gateway_subscription_id": "22393526",
      "gateway_payment_id": "49585655"
    }
    },
    "event_time": "2025-08-07T10:24:45+05:30",
    "type": "SUBSCRIPTION_PAYMENT_FAILED"
    }


    ```
  </Tab>

  <Tab title="Version (2023-08-01)">
    ```javascript theme={"dark"}
    {
    "data": {
        "payment_id": "12345",
        "cf_payment_id": "67890",
        "cf_txn_id": "789012",
        "cf_order_id": "98765",
        "subscription_id": "sub12345",
        "cf_subscription_id": "sub67890",
        "payment_type": "DEBIT_CARD",
        "authorization_details": {
            "authorization_amount": 100,
            "authorization_amount_refund": true,
            "approve_by_time": "2024-07-18T16:09:50+05:30",
            "authorization_reference": "6595231908096894505959",
            "authorization_time": "2024-07-18T16:09:51",
            "authorization_status": "ACTIVE",
            "payment_id": "123",
            "payment_method": "DEBIT_CARD",
            "instrument_id": "hsdg9"
        },
        "payment_amount": 200,
        "payment_schedule_date": "2024-07-20",
        "payment_initiated_date": "2024-07-20",
        "payment_remarks": "payment",
        "retry_attempts": 0,
        "failureDetails": {
            "failureReason": "Insufficient balance"
        },
        "payment_status": "FAILED",
        "payment_gateway_details": {
            "gateway_name": "CASHFREE",
            "gateway_subscription_id": "Demo_Subscription",
            "gateway_payment_id": "payment12345"
        }
    },
    "event_time": "2024-07-20T11:16:10+05:30",
    "type": "SUBSCRIPTION_PAYMENT_FAILED"
    }
    ```
  </Tab>
</Tabs>

## SUBSCRIPTION\_PAYMENT\_CANCELLED

This notification is sent whenever payment processing is cancelled by user for an active subscription.

<Tabs>
  <Tab title="Version (2026-01-01)">
    ```javascript Version (2026-01-01) theme={"dark"}
    {
    "data": {
    "payment_id": "433563_33_1754492527395",
    "cf_payment_id": "2011332",
    "cf_txn_id": null,
    "cf_order_id": "",
    "subscription_id": "subTestIdOndemand_2025080615020470",
    "cf_subscription_id": "1220385",
    "payment_type": "CHARGE",
    "subscription_details": {
      "cf_subscription_id": "1220385",
      "subscription_id": "subTestIdOndemand_2025080615020470",
      "subscription_status": "ACTIVE",
      "subscription_expiry_time": "2047-07-30T13:24:54",
      "subscription_first_charge_time": null,
      "subscription_tags": {
        "company": "Cashfree",
        "name": "Payment link"
      },
      "next_schedule_date": null
    },
    "authorization_details": {
      "authorization_amount": 1.00,
      "authorization_amount_refund": false,
      "approve_by_time": "",
      "authorization_reference": null,
      "authorization_time": "",
      "authorization_status": null,
      "payment_id": "433563_33_1754492527395",
      "payment_method": null,
      "payment_group": null
    },
    "payment_amount": 1.00,
    "payment_currency": "INR",
    "payment_schedule_date": "2025-08-08T12:00:00+05:30",
    "payment_initiated_date": "2025-08-06T20:32:07+05:30",
    "payment_remarks": null,
    "retry_attempts": 0,
    "failure_details": {
      "failure_reason": null
    },
    "payment_status": "CANCELLED",
    "payment_gateway_details": {
      "gateway_name": "CASHFREE",
      "gateway_subscription_id": "1220385",
      "gateway_payment_id": "2011332"
    }
    },
    "event_time": "2025-08-06T20:32:07+05:30",
    "type": "SUBSCRIPTION_PAYMENT_CANCELLED"
    }
    ```
  </Tab>

  <Tab title="Version (2025-01-01)">
    ```javascript Version (2025-01-01) theme={"dark"}
    {
    "data": {
    "payment_id": "433563_33_1754492527395",
    "cf_payment_id": "2011332",
    "cf_txn_id": null,
    "cf_order_id": "",
    "subscription_id": "subTestIdOndemand_2025080615020470",
    "cf_subscription_id": "1220385",
    "payment_type": "CHARGE",
    "authorization_details": {
      "authorization_amount": 1.00,
      "authorization_amount_refund": false,
      "approve_by_time": "",
      "authorization_reference": null,
      "authorization_time": "",
      "authorization_status": null,
      "payment_id": "433563_33_1754492527395",
      "payment_method": null,
      "payment_group": null
    },
    "payment_amount": 1.00,
    "payment_currency": "INR",
    "payment_schedule_date": "2025-08-08T12:00:00+05:30",
    "payment_initiated_date": "2025-08-06T20:32:07+05:30",
    "payment_remarks": null,
    "retry_attempts": 0,
    "failure_details": {
      "failure_reason": null
    },
    "payment_status": "CANCELLED",
    "payment_gateway_details": {
      "gateway_name": "CASHFREE",
      "gateway_subscription_id": "1220385",
      "gateway_payment_id": "2011332"
    }
    },
    "event_time": "2025-08-06T20:32:07+05:30",
    "type": "SUBSCRIPTION_PAYMENT_CANCELLED"
    }
    ```
  </Tab>

  <Tab title="Version (2023-08-01)">
    ```javascript theme={"dark"}
    {
    "data": {
        "payment_id": "12345",
        "cf_payment_id": "67890",
        "cf_txn_id": "789012",
        "cf_order_id": "98765",
        "subscription_id": "sub12345",
        "cf_subscription_id": "sub67890",
        "payment_type": "DEBIT_CARD",
        "authorization_details": {
            "authorization_amount": 100,
            "authorization_amount_refund": true,
            "approve_by_time": "2024-07-18T16:09:50+05:30",
            "authorization_reference": "6595231908096894505959",
            "authorization_time": "2024-07-18T16:09:51",
            "authorization_status": "ACTIVE",
            "payment_id": "123",
            "payment_method": "DEBIT_CARD",
            "instrument_id": "hsdg9"
        },
        "payment_amount": 200,
        "payment_schedule_date": "2024-07-20",
        "payment_initiated_date": "2024-07-20",
        "payment_remarks": "payment",
        "retry_attempts": 0,
        "failureDetails": {
            "failureReason": "Subscription is not active"
        },
        "payment_status": "CANCELLED",
        "payment_gateway_details": {
            "gateway_name": "CASHFREE",
            "gateway_subscription_id": "Demo_Subscription",
            "gateway_payment_id": "payment12345"
        }
    },
    "event_time": "2024-07-20T11:16:10+05:30",
    "type": "SUBSCRIPTION_PAYMENT_CANCELLED"
    }
    ```
  </Tab>
</Tabs>

## SUBSCRIPTION\_REFUND\_STATUS

This event is triggered whenever a refund status of a transaction will be success, failed, or cancelled.

<Tabs>
  <Tab title="Version (2025-01-01)">
    ```javascript theme={"dark"}
    {
    "data": {
    "payment_id": "yCzJxeT2aXDqI",
    "cf_payment_id": "49778199",
    "refund_id": "WHOqiwy05P1l0",
    "cf_refund_id": "SUB_21ebb4bf-e84f-4afa-bb09-07aac433abe4",
    "refund_amount": 1000.00,
    "refund_speed": "STANDARD",
    "refund_note": "Tesg Refund",
    "refund_status": "SUCCESS",
    "failure_details": "",
    "refund_gateway_details": {
      "gateway_name": "CASHFREE",
      "gateway_payment_id": "49778199",
      "gateway_refund_id": "SUB_21ebb4bf-e84f-4afa-bb09-07aac433abe4"
    }
    },
    "event_time": "2025-08-06T17:20:02+05:30",
    "type": "SUBSCRIPTION_REFUND_STATUS"
    }
    ```
  </Tab>

  <Tab title="Version (2023-08-01)">
    ```javascript theme={"dark"}
    {
    "data": {
        "payment_id": "pay8643",
        "cf_payment_id": "863782648",
        "refund_id": "refund2",
        "cf_refund_id": "ref_212",
        "refund_amount": 100,
        "refund_note": "test",
        "refund_speed": "INSTANT",
        "refund_status": "SUCCESS",
        "failure_details": null,
        "payment_gateway_details": {
            "gateway_name": "CASHFREE",
            "gateway_payment_id": "pay8643",
            "gateway_refund_id": "refund2"
        }
    },
    "event_time": "2023-01-03T11:16:10+05:30",
    "type": "SUBSCRIPTION_REFUND_STATUS"
    }
    ```
  </Tab>
</Tabs>

## SUBSCRIPTION\_CARD\_EXPIRY\_REMINDER

This event is triggered 7 days prior to the card’s expiry date for active card subscriptions.

<Tabs>
  <Tab title="Version (2025-01-01)">
    ```javascript theme={"dark"}
    {
    "data": {
        "subscription_status_webhook": {
            "subscription_details": {
                "cf_subscription_id": "23661347",
                "subscription_id": "SUB_TEST_1754550382119",
                "subscription_status": "ACTIVE",
                "subscription_expiry_time": "2050-12-31T00:00:00",
                "subscription_first_charge_time": "2025-09-30T00:00:00",
                "subscription_tags": {
                    "next_schedule_date": "2025-09-30T00:10:00"
                }
            },
            "customer_details": {
                "customer_name": "John Doe",
                "customer_email": "john@cashfree.com",
                "customer_phone": "9090909090"
            },
            "plan_details": {
                "plan_id": "PLAN_1754550139964",
                "plan_name": "MY_PLAN",
                "plan_type": "PERIODIC",
                "plan_max_cycles": 2,
                "plan_recurring_amount": 5,
                "plan_max_amount": 1000,
                "plan_interval_type": "MONTH",
                "plan_intervals": 1,
                "plan_currency": null,
                "plan_note": null,
                "plan_status": null
            },
            "authorization_details": {
                "authorizationAmount": 1,
                "authorizationAmountRefund": false,
                "approveByTime": "2025-09-06T12:36:22",
                "authorizationReference": null,
                "authorizationTime": "2025-08-07T13:14:18",
                "authorizationStatus": "ACTIVE",
                "paymentId": "160594_178_1754552533131",
                "paymentMethod": "card",
                "instrumentId": null
            },
            "payment_gateway_details": {
                "gateway_name": "CASHFREE",
                "gateway_subscription_id": "23661347",
                "gateway_plan_id": "PLAN_1754550139964",
                "gateway_auth_id": null
            }
        },
        "card_expiry_date": "2025-09-30"
    },
    "event_time": "2025-09-24T02:00:09+05:30",
    "type": "SUBSCRIPTION_CARD_EXPIRY_REMINDER"
    }
    ```
  </Tab>
</Tabs>

<Note>
  The following webhooks are only relevant if you are using Controlled API endpoints for notification and charge.
</Note>

## SUBSCRIPTION\_CONTROLLED\_NOTIFICATION\_STATUS

Cashfree sends this webhook when the status of a merchant-controlled payment notification attempt changes (for example, SUCCESS or FAILED).

<Tabs>
  <Tab title="Version (2025-01-01)">
    ```javascript theme={"dark"}
    {
    "data": {
    "cf_notification_id": "3333",
    "cf_order_id": "123456",
    "cf_payment_id": "123456",
    "cf_subscription_id": "7891011",
    "cf_txn_id": "123456",
    "notification_attempted_time": "2025-06-01T22:14:59+05:30",
    "notification_completed_time": "2025-06-01T22:15:59+05:30",
    "notification_failure_details": {
      "failure_reason": "",
      "failure_error_code": "",
      "failure_sub_error_code": ""
    },
    "notification_id": "notification-001",
    "notification_initiated_time": "2025-06-01T22:14:58+05:30",
    "notification_status": "SUCCESS",
    "payment_amount": 1,
    "payment_id": "test-payment-id",
    "payment_remarks": "monthly charge",
    "payment_status": "INITIALIZED",
    "subscription_id": "test-subscription-id"
    },
    "event_time": "2025-06-01T22:15:59+05:30",
    "type": "SUBSCRIPTION_CONTROLLED_NOTIFICATION_STATUS"
    }
    ```
  </Tab>
</Tabs>

## SUBSCRIPTION\_CONTROLLED\_EXECUTION\_STATUS

Cashfree sends this webhook when the status of a merchant-controlled charge execution attempt changes (for example, SUCCESS or FAILED).

<Tabs>
  <Tab title="Version (2025-01-01)">
    ```javascript theme={"dark"}
    {
    "data": {
    "cf_execution_id": "3333",
    "cf_order_id": "123456",
    "cf_payment_id": "123456",
    "cf_subscription_id": "7891011",
    "cf_txn_id": "123456",
    "execution_attempted_time": "2025-06-01T22:14:59+05:30",
    "execution_completed_time": "2025-06-01T22:15:59+05:30",
    "execution_id": "execution-001",
    "execution_initiated_time": "2025-06-01T22:14:58+05:30",
    "execution_status": "SUCCESS",
    "failure_details": {
      "failure_reason": "",
      "failure_error_code": "",
      "failure_sub_error_code": ""
    },
    "payment_amount": 1,
    "payment_id": "test-payment-id",
    "payment_remarks": "",
    "payment_status": "SUCCESS",
    "subscription_id": "test-subscription-id"
    },
    "event_time": "2025-06-01T22:15:59+05:30",
    "type": "SUBSCRIPTION_CONTROLLED_EXECUTION_STATUS"
    }
    ```
  </Tab>
</Tabs>
