<!-- Captured 18 Sep 2026 from Cashfree's Subscriptions documentation (https://www.cashfree.com/docs/). Cashfree's live page is the authority. -->

> ## Documentation Index
> Fetch the complete documentation index at: https://www.cashfree.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Subscription FAQs

> Browse Cashfree Subscriptions FAQs covering mandate authorisation, charges, supported methods like UPI mandates, retries, webhooks, and reconciliation.

export const posthog_0 = undefined

<AccordionGroup>
  <Accordion title="What is Subscription?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What are Subscriptions?" })}>
    Cashfree Subscriptions lets you set up and manage recurring payments for your customers.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-are-subscriptions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What are the payment methods supported by Cashfree Subscriptions?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What are the payment methods supported by Cashfree Subscriptions?" })}>
    | Payment methods supported | Banks or card networks or UPI handles                                                                                                                       | Maximum subscription amount allowed                 |
    | :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
    | eNACH                     | See the [list of NPCI-supported banks](https://www.npci.org.in/product/nach/all-members)                                                                    | ₹ 1,00,00,000                                       |
    | UPI autopay               | See the [list of banks and PSPs](https://www.npci.org.in/what-we-do/autopay/list-of-banks-and-apps-live-on-autopay)                                         | ₹ 15,000 (without AFA) or ₹ 1,00,000 (with AFA)     |
    | Card (Indian)             | Visa, Mastercard, RuPay                                                                                                                                     | ₹ 15,000 (without AFA) or ₹ 1,00,00,000  (with AFA) |
    | Card (International)      | Visa, Mastercard                                                                                                                                            | ₹ 1,00,00,000                                       |
    | Physical mandates         | See the [list of supported banks](https://gocashassets.s3.ap-south-1.amazonaws.com/subscriptions/List+of+Bank+Supported+for+Physical+NACH+-+Sheet1.pdf.zip) | ₹ 1,00,00,000                                       |

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-are-the-various-payment-methods-supported-by-cashfree-subscriptions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What frequencies are supported for all payment methods?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What frequencies are supported for all payment methods?" })}>
    | Payment method | Supported frequencies                  |
    | -------------- | -------------------------------------- |
    | eNACH          | Daily, weekly, monthly, yearly, ad-hoc |
    | UPI AutoPay    | Daily, weekly, monthly, ad-hoc         |
    | Card           | Weekly, monthly, yearly, ad-hoc        |
    | Physical NACH  | Daily, weekly, monthly, yearly, ad-hoc |

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-are-the-frequencies-supported-for-all-payment-modes-for-subscriptions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What are the different subscription states?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What are the different subscription states?" })}>
    * **INITIALIZED** – Subscription created, authorization pending.
    * **BANK APPROVAL PENDING** – Authorization successful, pending bank approval.
    * **ACTIVE** – Subscription registered across NPCI and destination bank.
    * **ON HOLD** – A charge has failed for the subscription.
    * **PAUSED** – Subscription is paused by the merchant.
    * **COMPLETED** – Subscription completed its scheduled duration.
    * **CUSTOMER CANCELLED** – Subscription cancelled by the customer.
    * **CUSTOMER PAUSED** – Subscription paused by the customer.
    * **EXPIRED** – In seamless subscriptions, authorization wasn't attempted before expiry.
    * **LINK EXPIRED** – In non-seamless subscriptions, authorization wasn't attempted before expiry.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-are-the-various-subscription-states" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can I retry a failed transaction and collect payments for that cycle?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can I retry a failed transaction and collect payments for that cycle?" })}>
    Yes. You can retry the last failed charge via the Merchant Dashboard or API.\
    [Refer to the retry subscription charge API](/docs/api-reference/payments/previous/subscriptionsv1/subscription/retry-subscription-charge) for details.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23can-i-retry-a-failed-transaction-and-collect-payments-for-that-cycle" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can I extend the expiry date of a subscription?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can I extend the expiry date of a subscription?" })}>
    No. You can’t extend the expiry date of a subscription. You can cancel the subscription and create a new one.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23can-i-extend-the-expiry-date-of-a-subscription" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can I test a subscription model before going live?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can I test a subscription model before going live?" })}>
    Yes. You can test any subscription model in the test environment before going live.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23can-i-test-a-subscription-model-before-going-live" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="How do I know if I have received payments?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "How do I know if I have received payments?" })}>
    You can use webhooks to receive notifications for all transactions.\
    [Follow these steps to configure webhooks](/docs/api-reference/payments/latest/subscription/webhooks).

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23how-do-i-know-if-i-have-received-payments" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Why aren't we receiving SUBSCRIPTION_PAYMENT_SUCCESS or SUBSCRIPTION_AUTHORIZED webhooks?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Why aren't we receiving SUBSCRIPTION_PAYMENT_SUCCESS or SUBSCRIPTION_AUTHORIZED webhooks?" })}>
    Subscription webhook events use a separate configuration from the main Payment Gateway webhooks. Log in to the [Merchant Dashboard](https://merchant.cashfree.com/auth/login), go to **Payment Gateway > Developers > Webhooks**, and select the **Subscriptions** tab. Add your endpoint there and select the subscription events you want to receive. An endpoint configured only under the main webhooks section does not receive subscription-specific events.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23why-are-we-not-receiving-subscription-webhooks" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can I replay or resend a missed subscription webhook?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can I replay or resend a missed subscription webhook?" })}>
    No. Cashfree does not currently support replaying or resending subscription webhooks, such as `SUBSCRIPTION_PAYMENT_SUCCESS`, after they trigger. To check the current status of a subscription payment instead, call the [Fetch Single Charge](/docs/api-reference/payments/latest/subscription/payment/fetch) API to poll the latest transaction state. As a fallback, configure webhook retry handling on your own server.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23can-i-replay-or-resend-a-missed-subscription-webhook" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Why do sandbox and production send different eNACH subscription webhook payload formats?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Why do sandbox and production send different eNACH subscription webhook payload formats?" })}>
    This happens when each environment uses a different webhook version. Select the same webhook version, `2026-01-01` (the current version), in both your sandbox and production subscription webhook settings. Older versions (`2022-09-01`, `2023-08-01`, `2025-01-01`) return a different payload structure, so mismatched versions across environments produce mismatched payloads for the same event.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23why-do-sandbox-and-production-send-different-webhook-payloads" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can I modify an existing subscription?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can I modify an existing subscription?" })}>
    Yes. You can update the recurring amount of an active subscription using the [Update Recurring Amount API](/docs/api-reference/payments/previous/subscriptionsv1/subscription/update-recurring-amount).

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23can-i-modify-an-existing-subscription" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can Subscriptions charge a variable amount each billing cycle instead of a fixed amount?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can Subscriptions charge a variable amount each billing cycle instead of a fixed amount?" })}>
    Yes. Use [On-Demand Subscriptions](/docs/payments/subscription/introduction). The customer authorises a maximum mandate amount once, at setup. You can then charge any amount up to that maximum for each billing cycle by calling `POST /pg/subscriptions/pay` with `payment_type: CHARGE`, without requiring re-authorisation. This approach suits usage-based or milestone billing, where the charge amount varies each cycle.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23can-subscriptions-charge-a-variable-amount-each-cycle" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What is the difference between 'Net Banking' and 'Debit Card' under the e-Mandate payment mode?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What is the difference between 'Net Banking' and 'Debit Card' under the e-Mandate payment mode?" })}>
    The customer is authenticated by their bank using either net banking or debit card credentials. Debit card credentials are used only for authentication. Therefore, the mandate remains valid even if the debit card expires.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-is-the-difference-between-auth-modes" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What is the maximum amount limit for each payment method?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What is the maximum amount limit for each payment method?" })}>
    | Payment method   | Supported networks or banks                                                                                                                 | Maximum subscription amount            |
    | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
    | eNACH            | See the [list of NPCI-supported banks](https://www.npci.org.in/product/nach/all-members)                                                    | ₹1,00,00,000                           |
    | UPI AutoPay      | [Live UPI apps and banks](https://www.npci.org.in/what-we-do/autopay/list-of-banks-and-apps-live-on-autopay)                                | ₹15,000 (no AFA), ₹1,00,000 (with AFA) |
    | Card             | Visa, Mastercard                                                                                                                            | ₹15,000 (no AFA), > ₹15,000 (with AFA) |
    | Physical Mandate | [Supported banks](https://gocashassets.s3.ap-south-1.amazonaws.com/subscriptions/List+of+Bank+Supported+for+Physical+NACH+-+Sheet1.pdf.zip) | ₹1,00,00,000                           |

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-is-the-maximum-amount-limit" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Which apps are supported for UPI Subscriptions?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Which apps are supported for UPI Subscriptions?" })}>
    View the [list of supported UPI apps and banks](https://www.npci.org.in/what-we-do/autopay/list-of-banks-and-apps-live-on-autopay).

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23which-apps-are-supported-for-upi-subscriptions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What is the cut-off time to raise a transaction?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What is the cut-off time to raise a transaction?" })}>
    | Charge raised on | Scheduled for | NACH            | UPI AutoPay       | SI on cards   |
    | ---------------- | ------------- | --------------- | ----------------- | ------------- |
    | 00:00–06:59 (T)  | null          | Raised on T     | Not Allowed       | Not Allowed   |
    | 07:00–11:59 (T)  | null          | Raised on T+1   | Not Allowed       | Not Allowed   |
    | 00:00–06:59 (T)  | T             | **Raised on T** | Not Allowed       | Not Allowed   |
    | 07:00–11:59 (T)  | T             | **Not Allowed** | Not Allowed       | Not Allowed   |
    | 00:00–20:59 (T)  | T+1           | Raised on T+1   | **Raised on T+1** | Not Allowed   |
    | 21:00–23:59 (T)  | T+1           | Raised on T+1   | **Not Allowed**   | Not Allowed   |
    | 00:00–23:59 (T)  | T+n (2–14)    | Raised on T+n   | Raised on T+n     | Raised on T+n |
    | 00:00–23:59 (T)  | T+15          | Not Allowed     | Not Allowed       | Not Allowed   |

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-is-the-cutoff-time-to-raise-a-transaction" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What are the common eNACH failure reasons?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What are the common eNACH failure reasons?" })}>
    Mandate creation and transactions may fail due to operational or customer-related issues. View the [common failure reasons](https://cashfreelogo.cashfree.com/website/docs/nach-errors.pdf).

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-are-the-various-enach-failure-reasons" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Which bank accounts are supported for eNACH mandates?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Which bank accounts are supported for eNACH mandates?" })}>
    Only savings accounts and individual (proprietor) current accounts are supported. Most destination banks do not support mandates for proprietor current accounts. For unsupported cases, consider using [Physical NACH](/docs/api-reference/payments/previous/subscriptionsv1/physical-mandates).

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-type-of-bank-accounts-are-supported" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Which intent apps are supported by Subscriptions?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Which intent apps are supported by Subscriptions?" })}>
    | App                              | Android intent | iOS intent |
    | -------------------------------- | -------------- | ---------- |
    | Paytm                            | ✔️             | ✔️         |
    | GPay (@okhdfc, @okicici, @oksbi) | ✔️             | ✔️         |
    | PhonePe                          | ✔️             | ✔️         |
    | AmazonPay                        | ✔️             | ✔️         |

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-are-the-intent-apps-supported" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can my customer pause or cancel a mandate from their end?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can my customer pause or cancel a mandate from their end?" })}>
    Yes. Customers can pause or cancel a mandate from their UPI app (Mandates > Active Mandates > Pause/Cancel > Submit).

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23can-customer-pause-cancel-mandate" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can I resume a mandate if my customer has paused it?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can I resume a mandate if my customer has paused it?" })}>
    No. Only the customer can resume a paused mandate from their UPI app.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23can-merchant-resume-customer-paused-mandate" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What is the maximum expiry period for eNACH mandates?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What is the maximum expiry period for eNACH mandates?" })}>
    The expiry period for an eNACH mandate can be set up to a maximum of 30 years.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-is-the-longest-expiry-time" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What happens if the card used for a subscription expires?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What happens if the card used for a subscription expires?" })}>
    If the card expires, the subscription is marked as <code>card\_expired</code>.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-happens-if-card-expires" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can the merchant receive advance notice of a card expiry?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can the merchant receive advance notice of a card expiry?" })}>
    Yes. The <code>subscription\_card\_expiry\_reminder</code> webhook is triggered 6 days before the card expiry.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23card-expiry-webhook-reminder" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What happens to an active subscription after the card expires?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What happens to an active subscription after the card expires?" })}>
    Once the card expires, the subscription moves to <code>card\_expired</code> status. Further charges cannot be processed.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23active-subscription-after-card-expires" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What should the merchant do if a subscription is marked as card_expired?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What should the merchant do if a subscription is marked as card_expired?" })}>
    The merchant must create a new mandate using the updated card details. The customer must then authorise the new mandate.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23subscription-marked-as-card-expired" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What are the different ways that I can use Cashfree to collect recurring payments or payments for subscriptions from my customers?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What are the different ways that I can use Cashfree to collect recurring payments or payments for subscriptions from my customers?" })}>
    Cashfree offers four different payment methods, each with specific limits on the allowed subscription amounts, as outlined below.

    * UPI AutoPay
    * Cards
    * eNach
    * Physical Mandate

    [Learn more about these payment modes](/docs/payments/subscription/payment-modes).

    {" "}

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-are-the-different-ways-that-i-can-use-cashfree-to-collect-recurring-payments-or-payments-for-subscriptions-from-my-customers" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Is the Cashfree Subscriptions solution compliant with the new Digital Lending Guidelines by RBI?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Is the Cashfree Subscriptions solution compliant with the new Digital Lending Guidelines by RBI?" })}>
    Yes, it is fully compliant with the new Digital Lending Guidelines by RBI. NBFCs and Fintechs can use Cashfree to collect repayments, disburse credit, and co-lend without a hassle.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23is-the-cashfree-subscriptions-solution-compliant-with-the-new-digital-lending-guidelines-by-rbi" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Who can benefit from using Cashfree Subscriptions?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Who can benefit from using Cashfree Subscriptions?" })}>
    Cashfree Subscriptions caters to various industries with diverse use cases. Some of the top ones include:

    * NBFCs and digital lending apps
    * OTT platforms
    * Ed-tech platforms
    * E-commerce companies
    * Investment firms
    * Insurance providers

          <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23who-can-benefit-from-using-cashfree-subscriptions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="How to create a subscriptions plan on Cashfree dashboard?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "How to create a subscriptions plan on Cashfree dashboard?" })}>
    1. Go to **Subscription Dashboard** > **All subscriptions** > **Create Subscriptions**

    2. Enter details – Add customer info, subscription ID, recurring amount, due date, and max debits.

           <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23how-to-create-a-subscriptions-plan-on-cashfree-payments-dashboard" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="How to create a UPI AutoPay plan?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "How to create a UPI AutoPay plan?" })}>
    To create a new subscription from the Merchant Dashboard, go to **Subscriptions Dashboard > All Subscriptions > Create Subscription**.

    You can also create multiple subscriptions at once using the Merchant Dashboard. Go to **Subscriptions Dashboard > Batch Subscriptions > Upload File** to upload a file that contains all the information required for multiple subscriptions.

    [Learn more](/docs/payments/subscription/create)

    {" "}

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23how-to-create-a-upi-autopay-plan" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="How do I activate UPI AutoPay for Subscriptions, and what does it cost?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "How do I activate UPI AutoPay for Subscriptions, and what does it cost?" })}>
    Cashfree does not offer UPI AutoPay activation as a self-serve feature. Contact your Cashfree account manager, or fill out the [Support Form](https://merchant.cashfree.com/merchants/landing?env=prod\&raise_issue=1), to request activation on your production and sandbox accounts. Charges depend on your pricing plan, so confirm the applicable rate with your account manager.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23how-do-i-activate-upi-autopay-for-subscriptions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What is the Bulk Payments tab on the Subscriptions dashboard?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What is the Bulk Payments tab on the Subscriptions dashboard?" })}>
    For On-Demand subscriptions, when you want to initiate a large number of payments for multiple subscriptions, you can use the Bulk Payments feature.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-is-the-bulk-payments-tab-on-the-subscriptions-dashboard" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can I migrate my mandate data from another payment aggregator to Cashfree?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can I migrate my mandate data from another payment aggregator to Cashfree?" })}>
    Cashfree supports importing mandate information for a subscription. You can move any historical mandate data to Cashfree and continue processing transactions in Cashfree. Cashfree ensures a smooth mandate porting experience.

    To initiate the porting process:

    1. **Contact Cashfree support**: Initiate the porting process by nominating Cashfree as your payment processing partner for your Utility Code or mandates.
    2. **Partner bank coordination**: Share the mandate list with your partner bank to update their systems. Our team will guide you through the process.
    3. **Import mandates**: Upload the updated mandate list into Cashfree’s system.
    4. **Start processing payments**: Once imported, you can begin processing payments seamlessly through Cashfree.
       [Learn more about importing mandates](/docs/payments/subscription/import).

           <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23can-i-migrate-my-mandate-data-from-another-payment-aggregator-to-cashfree" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What are the various eNACH transaction failure reasons?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What are the various eNACH transaction failure reasons?" })}>
    Once the eMandate is successfully created, the corresponding transactions can get declined due to the reasons listed below:

    | Transaction failure reason                                 | Detailed description                                                                                                                                                                                                                                           | Resolution                                                                                                                                                                                                 |
    | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Balance Insufficient                                       | This error is displayed when the end-customer does not have sufficient balance in their account. In this case, due to payment failure, the end-customer will be asked to pay a fine of amount equivalent to the cheque bounce charges by the destination bank. | The merchant can present the transaction again. It is recommended to contact the end-customer before retrying the failed transaction. A total of 3 retries are allowed before the start of the next cycle. |
    | Not Arranged For or Exceeds arrangement                    | This error is displayed when the end-customer does not have sufficient balance in their overdraft account.                                                                                                                                                     | The merchant can present the transaction again. It is recommended to contact the end-customer before retrying the failed transaction. A total of 3 retries are allowed before the start of the next cycle. |
    | Customer to refer to the branch                            | This error is displayed when the reason for the decline is unclear and the destination bank is expecting the end-customer to contact them for further clarification.                                                                                           | Merchant can contact the end-customer and recommend the end-customer to contact the bank and provide further clarification.                                                                                |
    | Account Closed                                             | This error is displayed when the account has been closed and thus all the associated mandates were deactivated.                                                                                                                                                | Further action cannot be taken in this scenario. The merchant can create another mandate for the end-customer to continue with the debit.                                                                  |
    | Invalid UMRN or Inactive Mandate                           | This error is displayed when the mandate has been de-activated by the NPCI's system. Usually when the mandate has not been debited over a prolonged period of time.                                                                                            | Further action cannot be taken in this scenario. The merchant can create another mandate for the end-customer to continue with the debit.                                                                  |
    | Mandate Cancelled                                          | This error is displayed when the mandate has been cancelled. This can be merchant initiated or end-customer initiated.                                                                                                                                         | Further action cannot be taken in this scenario. The merchant would have to create another mandate for the end-customer to continue with the debit.                                                        |
    | No Such Account                                            | This error is displayed when the account has been closed or no longer available. Thus all the associated mandates were deactivated.                                                                                                                            | Further action cannot be taken in this scenario. The merchant would have to create another mandate for the end-customer to continue with the debit.                                                        |
    | A/c Blocked or Frozen                                      | This error is displayed when all the withdrawals, purchases or transfers have been halted for this account. Hence, the presentation is not successful.                                                                                                         | The merchant must contact the end-customer to resolve this issue.                                                                                                                                          |
    | Payment Stopped by Drawer                                  | This error is displayed when the presentation has been stopped at the request of the end-customer.                                                                                                                                                             | The merchant must contact the end-customer to resolve this issue.                                                                                                                                          |
    | Payment Stopped under Court Order/Account Under Litigation | This error is displayed when the presentation has been stopped at a Court order.                                                                                                                                                                               | The merchant must contact the end-customer to resolve this issue.                                                                                                                                          |
    | Customer name mismatch                                     | This error is displayed when the account holder's name provided during mandate creation does not match the account holder's name at the time of presentation.                                                                                                  | Since the mandate cannot be edited, the merchant must create a new mandate with the end-customer.                                                                                                          |
    | Network Failure (CBS)                                      | This error is displayed when the Core Banking System(CBS) of the destination bank has a network failure. Generally, all the presentations for the affected bank would fail for the day.                                                                        | The merchant can try to present the transaction again. The transaction is expected to go through once the system is up.                                                                                    |
    | Returned as per customer request                           | This error is displayed when the presentation has been stopped at the request of the customer.                                                                                                                                                                 | The merchant must contact the end-customer to resolve this issue.                                                                                                                                          |
    | KYC Documents Pending                                      | Typically end-customer is expected to do a KYC for the bank account at least once in 3 years. On such cases, the presentation could be stopped by the bank, and this error message is displayed.                                                               | The end-customer must complete the KYC post which the merchant can try to present the transaction.                                                                                                         |
    | Documents Pending for Account Holder turning Major         | This error is displayed when the documentation is pending.                                                                                                                                                                                                     | End customer must complete the documentation process at the bank.                                                                                                                                          |
    | Account Inoperative                                        | This error is displayed when there are no transactions in an account for the last 3 months. All the associated mandates are deactivated.                                                                                                                       | Further action cannot be taken in this scenario. The merchant would have to create another mandate for the end-customer to continue with the debit.                                                        |
    | Dormant Account                                            | This error is displayed when there are no transactions in an account for the last 6 months. Account is dormant and all the associated mandates are deactivated.                                                                                                | Further action cannot be taken in this scenario. The merchant would have to create another mandate for the end-customer to continue with the debit.                                                        |
    | Small account, First Transaction to be from Base Branch    | For a bank account type - small account, the first transaction must happen at the home branch.                                                                                                                                                                 |                                                                                                                                                                                                            |
    | Account reached maximum Debit limit set on account by Bank | This error is displayed when the end-customer has sufficient balance in their account but the account has already reached the maximum limitation set for security reasons.                                                                                     | The merchant must contact the end-customer to increase the limit and then they try to do another presentation.                                                                                             |
    | Account Holder Expired                                     | This error message is displayed when the account holder has expired.                                                                                                                                                                                           | -                                                                                                                                                                                                          |
    | Account under litigation                                   | This error is displayed when an account is currently under legal action.                                                                                                                                                                                       | Further debits are not possible for this bank account. A new mandate must be created with a different bank account to take this forward.                                                                   |
    | Aadhaar number not mapped to the account number            | This error is displayed when the end customer Aadhaar number is not linked to the bank account.                                                                                                                                                                | The end-customer must link the Aadhaar number with the bank account post which the merchant can try to do another presentation.                                                                            |
    | Customer Insolvent / Insane                                | -                                                                                                                                                                                                                                                              | Further action cannot be taken for this error message. The merchant would have to create another mandate with a different bank account.                                                                    |
    | Item cancelled                                             | This error is displayed when the end-customer has cancelled the presentation.                                                                                                                                                                                  | The merchant must contact the end-customer to get this resolved post which the merchant can try to do another presentation.                                                                                |

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-are-the-various-enach-transaction-failure-reasons" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Multiple authorisations will be present if the customer has attempted the transaction multiple times?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Multiple authorisations will be present if the customer has attempted the transaction multiple times?" })}>
    Multiple auths will appear if the customer attempts the transaction more than once.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23multiple-authorizations-will-be-present-if-the-customer-has-attempted-the-transaction-multiple-times" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What causes a payment_mode_invalid_for_action error on the subscription pay endpoint?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What causes a payment_mode_invalid_for_action error on the subscription pay endpoint?" })}>
    The API returns this error when the requested payment mode is not valid for the action you are performing. Common causes include:

    * UPI AutoPay is not activated on your merchant account.
    * An `AUTH` action is being attempted on a subscription that is already authorised. Only one `AUTH` is allowed per mandate.
    * The plan or subscription type does not support the requested action. See [subscription payment modes](/docs/payments/subscription/payment-modes) for supported actions per mode.

    Use the [Fetch Subscription API](/docs/api-reference/payments/latest/subscription/fetch-subscription) to check the subscription's current status first. If UPI AutoPay activation is the cause, contact your account manager or fill out the [Support Form](https://merchant.cashfree.com/merchants/landing?env=prod\&raise_issue=1) — this requires commercial approval.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23what-causes-payment-mode-invalid-for-action-error" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="If a periodic subscription transaction is in the PENDING state and the subscription is then moved to the PAUSED state, will the transaction change to SUCCESS?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "If a periodic subscription transaction is in the PENDING state and the subscription is then moved to the PAUSED state, will the transaction change to SUCCESS?" })}>
    Yes, subscription may move to SUCCESS state or it may move to FAILED state based on bank’s confirmation. But the subscription state will move to terminal state.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23multiple-authorizations-will-be-present-if-the-customer-has-attempted-the-transaction-multiple-times" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="If a periodic subscription transaction is in the INITIALISED state and the subscription is then moved to the PAUSED state, will the transaction change to SUCCESS?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "If a periodic subscription transaction is in the INITIALISED state and the subscription is then moved to the PAUSED state, will the transaction change to SUCCESS?" })}>
    No, the subscription will move to SUCCESS.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23multiple-authorizations-will-be-present-if-the-customer-has-attempted-the-transaction-multiple-times" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can I force a PERIODIC subscription from INITIALIZED to PENDING in the sandbox environment?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can I force a PERIODIC subscription from INITIALIZED to PENDING in the sandbox environment?" })}>
    No. A PERIODIC subscription payment moves from `INITIALIZED` to `PENDING` only when its scheduled billing date arrives, and the sandbox environment does not support forcing this transition early. For `ON_DEMAND` subscriptions, trigger an immediate charge by calling `POST /pg/subscriptions/pay` with `subscription_id` and `payment_type: CHARGE` in the request body. Use this as the sandbox-friendly way to test a charge without waiting for a billing cycle.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23can-i-force-a-periodic-subscription-to-pending-in-sandbox" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Are offers supported with Subscriptions?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Are offers supported with Subscriptions?" })}>
    Offers are not currently supported with Subscriptions.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23are-offers-supported-with-subscriptions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Are the customer's email address and mobile number both required for a UPI AutoPay mandate?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Are the customer's email address and mobile number both required for a UPI AutoPay mandate?" })}>
    Yes. The Subscriptions API requires both `customer_email` and the customer's mobile number to create a UPI AutoPay mandate, and neither field is optional. The API rejects the subscription creation request if either field is missing. If collecting an email address upfront is difficult, capture a valid address during customer onboarding, before you initiate mandate creation.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23are-email-and-mobile-number-required-for-upi-autopay-mandate" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Where does Cashfree use the customer’s phone number (India and International)?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Where does Cashfree use the customer’s phone number (India and International)?" })}>
    The customer’s phone number is primarily used for sending payment links to customers and sending subscription mandate notifications for recurring payments. It may also be used for transaction-related communication where applicable. This applies to both domestic and international transactions wherever relevant.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23are-offers-supported-with-subscriptions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Is it mandatory for the merchant to validate the phone number?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Is it mandatory for the merchant to validate the phone number?" })}>
    It is not mandatory for the merchant to perform OTP validation at their end. However, since the customer’s phone number is used to send payment links and important mandate notifications, we expect the number to be accurate. If an incorrect number is provided, the customer may not receive the communication.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23are-offers-supported-with-subscriptions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Does Cashfree validate the phone number?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Does Cashfree validate the phone number?" })}>
    Yes, Cashfree performs a basic validation check to ensure the phone number is in the correct format. For Indian transactions, this includes verifying that it is a valid 10-digit mobile number. This is only a format-level validation and does not include OTP-based verification.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23are-offers-supported-with-subscriptions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="When will a subscription be moved to the EXPIRED state?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Does Cashfree validate the phone number?" })}>
    If a subscription remains in the INITIALIZED state and the configured expiry time is reached, and there is no successful authorization/payment against the subscription (or the authorization attempt fails), the subscription will continue to remain in the INITIALIZED state. Once the subscription crosses its expiry time, it will be moved to the EXPIRED state.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23are-offers-supported-with-subscriptions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can I debit a lower amount than what was sent in the pre-debit notification (PDN)?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can I debit a lower amount than what was sent in the pre-debit notification (PDN)?" })}>
    No. The debit amount cannot change after the PDN is initiated. If the executed debit amount differs from the amount notified in the PDN, the transaction is declined by the issuing bank due to the amount-match logic enforced at the issuing bank.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23lower-debit-amount-vs-pdn-notified-amount" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="When will a subscription be moved to the COMPLETED state?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Does Cashfree validate the phone number?" })}>
    Once the authorization payment is successfully completed and the subscription moves to the ACTIVE state, the behaviour is different. Even if the merchant has not specified the number of cycles (max\_cycles), when the subscription reaches its configured expiry time (expires\_on), the subscription will be moved to the COMPLETED state and not the EXPIRED state.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23are-offers-supported-with-subscriptions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What does the Maximum Amount field represent in a subscription plan?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What does the Maximum Amount field represent in a subscription plan?" })}>
    The **Maximum Amount** is the upper limit you can charge under a mandate, set through the `plan_max_amount` parameter in the [Create Plan API](/docs/api-reference/payments/latest/subscription/create-a-plan) or the [Create Subscription API](/docs/api-reference/payments/latest/subscription/create-subscription). The customer sees this limit during the authorisation process. If a future charge exceeds this authorised limit, you need a new authorisation or mandate from the customer.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23maximum-amount-field" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Why are the Card and UPI payment options not visible even though both payment modes are enabled at the account level?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Why are the Card and UPI payment options not visible even though both payment modes are enabled at the account level?" })}>
    If Cards are enabled at the account level but the Card payment option is not displayed during the subscription flow, check the following:

    1. Plan Maximum Amount:
       In both Sandbox and Production, if the `plan_max_amount` configured for the subscription is greater than ₹15,000, Card and UPI payment modes may not be displayed by default due to the applicable mandate limits. Ensure that the `plan_max_amount` is within the supported limit. If you need to support amounts above ₹15,000, the AFA (Additional Factor Authentication) configuration must be enabled. Once AFA is enabled, customers must authenticate each recurring charge using UPI PIN for UPI Autopay, or OTP/2FA for Cards.
    2. Customer Phone Number:
       If the `plan_max_amount` is less than ₹15,000 and Cards are still not visible, ensure that a valid customer phone number is passed while creating the subscription. Dummy phone numbers are blacklisted for Card payment mode and may result in Cards not being displayed.

           <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23card-and-upi-payment-options-not-visible" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What is the Max. No. of Debits field in a subscription plan?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What is the Max. No. of Debits field in a subscription plan?" })}>
    The Max. No. of Debits defines the maximum number of times you can charge a customer under a specific subscription or mandate, set via the `plan_max_cycles` parameter in the [Create Plan API](/docs/api-reference/payments/latest/subscription/create-a-plan) or the [Create Subscription API](/docs/api-reference/payments/latest/subscription/create-subscription). If you leave it blank, the subscription remains active until its configured expiry date or cancellation.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23max-debits-field" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What does the On Hold status mean for a subscription and how can it be resolved?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What does the On Hold status mean for a subscription and how can it be resolved?" })}>
    The On Hold status occurs for NACH and Card standing instructions when a recurring payment fails. To reactivate it, you can retry the failed charge (up to 3 retries per billing cycle) via the Merchant Dashboard or the Manage Payment API. Once the payment succeeds, the subscription resumes.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23on-hold-status" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can I offer multiple subscription plans on one Payment Form?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can I offer multiple subscription plans on one Payment Form?" })}>
    Yes. A Subscription Payment Form can have a single plan or multiple plans. Add more plans to the same form when you want customers to choose an option at checkout. Customers select one plan and complete mandate registration for that plan only. See [Subscription Payment Form](/docs/payments/no-code/payment-forms/subscription-payment-form).

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23can-i-offer-multiple-subscription-plans-on-one-payment-form" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What is the default session ID expiry for the Create Subscription API?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What is the default session ID expiry for the Create Subscription API?" })}>
    The default expiry value for the subscription session ID is 2 hours. If the session ID expires, the subscription remains in INITIALISED status. You must generate a new session ID using the [Fetch Subscription API](/docs/api-reference/payments/latest/subscription/fetch-subscription) to open the checkout page again.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23session-id-expiry" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Why am I unable to find an old subscription in the Merchant Dashboard even if it was recently updated?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Why am I unable to find an old subscription in the Merchant Dashboard even if it was recently updated?" })}>
    When searching for subscriptions in the Merchant Dashboard using date filters, you must use the original creation date of the subscription rather than the last updated date. If a subscription was created in the past but updated recently, set your Merchant Dashboard date range filter to include that original creation period to locate the record.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23why-am-i-unable-to-find-old-subscription" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Where can I find the API documentation for UPI AutoPay integration?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Where can I find the API documentation for UPI AutoPay integration?" })}>
    You can refer to the following API documentation for UPI AutoPay integration:

    * [Create Subscription](/docs/api-reference/payments/latest/subscription/create-subscription)
    * [Get Subscription](/docs/api-reference/payments/latest/subscription/fetch-subscription)
    * [Manage Subscription](/docs/api-reference/payments/latest/subscription/manage-subscription)
    * [Create Plan](/docs/api-reference/payments/latest/subscription/create-a-plan)
    * [Raise a Charge](/docs/api-reference/payments/latest/subscription/raise-a-charge-or-create-an-auth)

          <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23upi-autopay-api-docs" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="How does the charge flow work for merchant-controlled UPI subscriptions compared to Cashfree-controlled ones?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "How does the charge flow work for merchant-controlled UPI subscriptions compared to Cashfree-controlled ones?" })}>
    In the Merchant-Controlled flow, the `payment_type` field is not used. Instead, the merchant handles notification and execution separately using specific APIs (`notify-mandate` and `execute-mandate`). The `payment_type` field is only applicable to Cashfree-controlled flows, where a single API call triggers both the pre-debit notification and the charge.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23merchant-controlled-charge-flow" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="What is the minimum gap required between a successful pre-debit notification and execution for UPI mandates?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "What is the minimum gap required between a successful pre-debit notification and execution for UPI mandates?" })}>
    A 25-hour window is required between a successful pre-debit notification and the execution of the charge. This logic and restriction apply to both the Sandbox and Production environments.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23pre-debit-notification-window" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Is there an enablement process or lead time required to start using merchant-controlled UPI mandate APIs in production?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Is there an enablement process or lead time required to start using merchant-controlled UPI mandate APIs in production?" })}>
    No separate enablement process or lead time is required. You can start using the merchant-controlled APIs directly in Production and migrate subscriptions gradually.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23merchant-controlled-enablement" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="How do I cancel or revoke a mandate if I am integrated with Cashfree through Juspay?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "How do I cancel or revoke a mandate if I am integrated with Cashfree through Juspay?" })}>
    If you are using Juspay as a payment orchestrator for Cashfree subscriptions, you should not call Cashfree's Cancel Subscription API directly. Instead, use [Juspay's Revoke Mandate API](https://juspay.io/in/docs/api-reference/docs/express-checkout/revoke-mandate-api). Juspay internally maps their `mandateId` to Cashfree's `subscription_id` and handles the underlying cancellation with Cashfree and the NPCI.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23how-to-cancel-mandate-via-juspay" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Can I set the authorization amount to zero for UPI or Card subscriptions?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Can I set the authorization amount to zero for UPI or Card subscriptions?" })}>
    No. For UPI and Card payment methods, the authorization amount cannot be set to ₹0. A ₹0 authorization amount is supported only for eNACH (Netbanking). If you attempt to set it to ₹0 for UPI, a ₹1 authorization amount will be deducted from the customer's account.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23can-i-set-the-authorization-amount-to-zero-for-upi-or-card-subscriptions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="How do I resolve the 'Split creation failed' error when using subscription_payment_splits?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "How do I resolve the 'Split creation failed' error when using subscription_payment_splits?" })}>
    The `Split creation failed` error typically occurs if Easy Split is not enabled for your account or if the vendors are not correctly configured. Ensure that:

    * Easy Split is enabled at the account level. Contact your account manager, or fill out the [Support Form](https://merchant.cashfree.com/merchants/landing?env=prod\&raise_issue=1), to enable this for your sandbox and production accounts.
    * The `vendor_id` used in the request already exists in your account.
    * The vendor is in an `ACTIVE` state before using it in a subscription request.

          <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23split-creation-failed" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="How can I implement a subscription with a trial period and an initial authorization charge?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "How can I implement a subscription with a trial period and an initial authorization charge?" })}>
    To set up a subscription with a trial period (for example, 3 days) and an initial authorization fee, follow these steps:

    1. **Create a Plan**: Use the [Create Plan API](/docs/api-reference/payments/latest/subscription/create-a-plan) with `plan_type: PERIODIC`, `plan_interval_type: MONTH`, and the recurring amount in `plan_recurring_amount`.

    2. **Create the Subscription**: Use the [Create Subscription API](/docs/api-reference/payments/latest/subscription/create-subscription) with the following parameters:

       * `authorization_details.authorization_amount`: Set to `1` to charge ₹1 instantly for mandate setup.
       * `authorization_details.authorization_amount_refund`: Set to `false` to keep the ₹1 as a trial fee, or `true` to refund it after authorization.
       * `subscription_first_charge_time`: Set this to the date when the trial ends (for example, 3 days from the authorization date). The first recurring charge will trigger on this date.

           <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23how-can-i-implement-a-subscription-with-a-trial-period-and-an-initial-authorization-charge" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Why am I not receiving webhooks for refunds on subscription authorization transactions?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Why am I not receiving webhooks for refunds on subscription authorization transactions?" })}>
    For subscription authorization transactions, the refund behavior is determined by the `authorization_amount_refund` parameter set during subscription creation. If you initiate a refund through the Payment Gateway dashboard, Cashfree triggers the `REFUND_STATUS` webhook event. If this event is not enabled in your webhook configuration, no notification is sent. Ensure that `REFUND_STATUS` is enabled under your Payment Gateway webhook settings.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23why-am-i-not-receiving-webhooks-for-refunds-on-subscription-authorization-transactions" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>

  <Accordion title="Are there specific validations for percentage values in subscription payment splits?" onClick={() => posthog_0.capture('Accordion Clicked', { title: "Are there specific validations for percentage values in subscription payment splits?" })}>
    Percentage values in `subscription_payment_splits` follow Easy Split rules. Keep the following in mind:

    * Each vendor `percentage` must be greater than `0`.
    * The total of all vendor percentages cannot exceed `100`.
    * Any remaining percentage stays with you as the merchant.

    You can pass decimal values, for example, `12.05`.

    <iframe src="https://www.cashfree.com/devstudio/preview/pg/embed/faqFeedback?section=subscriptions%2Ffaqs%23split-percentage-validations" style={{ width: "100%", height: "65px", border: "none" }} title="FAQs feedback component" />
  </Accordion>
</AccordionGroup>
