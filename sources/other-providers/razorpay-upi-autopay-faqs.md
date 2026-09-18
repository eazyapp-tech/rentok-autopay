# Razorpay: UPI Autopay FAQs

Captured 18 Sep 2026 as plain text for reference. Source: https://razorpay.com/docs/. The provider's page is the authority; check it before relying on a detail.

---

Frequently Asked Questions (FAQs) - Razorpay
Documentation Index
Fetch the complete documentation index at: /llms.txt
Use this file to discover all available pages before exploring further.
Skip to main content
Razorpay home pageIndia

Search...

⌘KAsk Assistant⌘I
Support
Blog
Dashboard
Dashboard

Search...

Navigation
About UPI Autopay
Frequently Asked Questions (FAQs)

Home
Payments
Engage
POS
Banking Plus
Payroll
Partners
API Reference
Developer Tools
Recurring Payments

Recurring Payments

Batch Operations

UPI Autopay Interoperability

Cards

Recurring Payments APIs for Cards

Frequently Asked Questions (FAQs)

Integrate Recurring Payments Using Cards

Supported Banks and Apps

Test Cards for Indian Recurring Payments - Card

Create a Recurring Payment

eMandate

Recurring Payments APIs for Emandate

Charge Customers During Registration - Use Cases and Payment Methods

Handle Errors

Frequently Asked Questions (FAQs)

Integrate Recurring Payments Using Emandate

Supported Banks

Glossary

Recurring Payments

Paper NACH

Recurring Payments APIs for Paper NACH

Frequently Asked Questions (FAQs)

Integrate Recurring Payments Using Paper NACH

Webhooks

About UPI Autopay

Recurring Payments APIs for UPI

Frequently Asked Questions (FAQs)

Integrate Recurring Payments Using UPI

QR Codes for Recurring Payments

Supported Banks and Apps

UPI Reserve Pay

Paper NACH Form

Wallets

Recurring Payments APIs for Wallets

Integrate Recurring Payments Using Wallets

About UPI Autopay
Frequently Asked Questions (FAQs)
Copy pageCopy page

Find answers to frequently asked questions about Recurring Payments using UPI.

Copy pageCopy page

Available in🇮🇳 India

What is the maximum amount I can charge per transaction?

The maximum transaction amount allowed is ₹15,000 when using UPI as a recurring payment method. Any auto debit above ₹15,000 undergoes an additional authorisation from the customer.

Which banks and apps support UPI Autopay?

Refer to the NPCI list of banks and apps supported for UPI Autopay.

Which are the intent-supported PSP apps?

The below table gives information about the frequently used intent-supported PSP apps on different platforms and checkout integrations. Standard Checkout Integration

 Custom Checkout Integration

 S2S Checkout Integration

PSP AppsmWebAndroid SDKiOS SDK
GPayx✓✓
PhonePe✓✓✓
Paytm✓✓✓
Amazon Payxxx
BHIMx✓x

PSP AppsmWebAndroid SDKiOS SDK
GPay✓✓x
PhonePe✓✓x
Paytm✓✓x
Amazon Payx✓x
BHIMx✓x

PSP AppsmWebAndroid SDKiOS SDK
GPay✓✓x
PhonePe✓✓x
Paytm✓✓x
Amazon Pay✓✓x
BHIM✓✓x

Watch Out!
You should contact our Support team to enable UPI Intent on standard checkout. Watch this video on how to get it enabled.

UPI Intent is not supported for @okaxis handle.

Which are the intent-supported PSP apps for TPV?

The below table gives information about the frequently used intent-supported PSP apps for TPV on different platforms and checkout integrations. Standard Checkout Integration

 Custom Checkout Integration

 S2S Checkout Integration

PSP AppsmWebAndroid SDKiOS SDK
GPay✓✓✓
PhonePe✓✓x
Paytm✓✓✓
Amazon Payx✓x
BHIMx✓x

PSP AppsmWebAndroid SDKiOS SDK
GPay✓✓✓
PhonePe✓✓x
Paytm✓✓✓
Amazon Payx✓x
BHIMx✓x

PSP AppsmWebAndroid SDKiOS SDK
GPay✓✓x
PhonePe✓✓x
Paytm✓✓x
Amazon Pay✓✓x
BHIM✓✓x

Watch Out!
You should contact our Support team to enable PSP apps other than PhonePe and Paytm on Standard Checkout for UPI TPV. Watch this video on how to get it enabled.

UPI Intent TPV is not supported for @okaxis handle.

How long does mandate registration take?

Mandate registrations occur in real time. Once the customer enters the MPIN, the mandate is authorised and a token is created on the customer. You can then use this token for subsequent debits on the customer’s account.

Can I charge customer payments in international currencies via a UPI mandate?

No, you cannot charge customer payments in international currencies. UPI mandates only support INR payments.

For UPI mandates, how long does it take for the token status to move from the `initiated` state to the `confirmed` state?

For UPI mandates, the token status is updated from initiated state to the confirmed state in real-time.MethodBankExpected Time to Complete
UPIAll supported banksReal-time.

For UPI mandates, how long does it take a subsequent charge to move from the `created` state to the `authorized` state?

For UPI mandates, subsequent charges are initiated 25 hours after the Pre Debit notification is sent to the customer. Once initiated,
For amount < ₹15,000: Authorisation is instant as the debit call is made directly to the customer’s bank.

For amount > ₹15,000: An additional authorisation is requested of the customer. Once received, the amount is debited from the customer’s bank.

What is pre-debit notification?

Pre-debit notifications are notifications sent to consumers 24 hours prior to the payment. These notices intimate the customer ahead of the actual debit, allowing them the option to pause or cancel the e-mandate.

Can I cancel a UPI mandate?

Yes, you can cancel a UPI mandate from the Dashboard.

Can I revoke a UPI mandate?

You can revoke a UPI mandate directly from the Dashboard. To do so, cancel the mandate first and then delete it.

Once registered, can I pause a UPI mandate?

No, you cannot pause a UPI mandate.

Once registered, can I modify a UPI mandate?

No, it is not possible to modify or update a UPI mandate. However, you can cancel the UPI mandate.

Once registered, can my customer cancel a UPI mandate?

Yes, your customers can cancel a UPI mandate from their UPI app.

Once registered, can my customer pause a UPI mandate?

Yes, your customers can pause a UPI mandate from their UPI app.

Once registered, can my customer modify a UPI mandate?

No, it is not possible to modify or update a UPI mandate. However, your customers can pause or cancel the UPI mandate from their UPI app.

What are some best practices I can follow when creating subsequent payments for UPI recurring payment?

For UPI, do not create subsequent payments on the last day of the cycle. This will cause the payment to fail.

What is the supported amount limit on PSP applications?

PSP appsMandate Maximum Amount < = ₹15,000Mandate Maximum Amount > ₹15,000
PhonePeYesNo
GooglePay - okhdfcbankYesYes
GooglePay - okaxisYesYes
GooglePay - okiciciYesYes
GooglePay - oksbiYesYes
BHIMYesNo
PaytmYesYes
Amazon PayYesYes

Is QR Code supported for UPI Autopay?

Yes, QR Code is supported on Standard Checkout to collect Recurring Paymennts. The customers can scan the QR using any PSP app and make the payment.

Can I restrict my customers from pausing and cancelling the mandate?

Yes, you can restrict your customers from pausing and cancelling the mandate by enabling OC125 functionality. After enabling, the Pause and Cancel mandate buttons are not available on PSP apps as shown in the image below.This functionality is supported only for lending businesses. Please contact our Support team for more information.

Was this page helpful?
YesNo

Recurring Payments APIs for UPI
Integrate Recurring Payments Using UPI

Razorpay home pagexlinkedingithubyoutube

Products
Payment GatewayPayment LinksRazorpayXPayroll

Resources
DocumentationAPI ReferenceSupportBlog

Company
About UsCareersPricing

xlinkedingithubyoutube

Assistant

Responses are generated using AI and may contain mistakes.