# UPI Autopay and e-NACH: what other payment providers' docs say (cross-check for the Cashfree email)

Research date: 18 Sep 2026. All URLs below were read on 18 Sep 2026 unless marked otherwise. Read-only research; nothing was posted anywhere.

Read first: `~/rentok-autopay/drafts/cashfree-email.md` (12 questions plus two regulation questions), `~/rentok-autopay/research/cashfree-docs-answers.md`, and `~/rentok-autopay/research/legal.md`. The RBI e-mandate framework text is **not** in `~/rentok-autopay/sources/`; `legal.md` quotes it from taxguru's copy, and I re-read that copy here.

**What could not be read.** NPCI's own site blocks automated reads (HTTP 403 on every page and circular). One circular, OC-223 of FY 2025-26, downloaded but is a scanned image PDF with no text layer and could not be OCR'd with the tools on this machine. So every "NPCI says" line below comes through a provider's doc, the RBI text, or press, and says so.

**Tags.** [official] a provider's or regulator's own docs. [archived] an official page that has since been taken down, read on the Internet Archive. [press] or [blog] a secondary source. Confidence: high, medium, low.

---

## The short version

1. **More than one debit a day on one UPI mandate: the sources disagree, and the weight of current docs says no.** Razorpay says NPCI allows one successful debit per billing cycle. Stripe said (April 2026) one charge per customer per day, then removed the line. PhonePe's old docs (2024, now taken down) allowed up to 20 debits in 24 hours on an on-demand mandate. That old PhonePe page is the most likely source of what your colleague heard. It predates NPCI's August 2025 limit of 4 attempts per mandate. Treat same-day parts as not allowed until Cashfree confirms in writing.
2. **Cancelling one scheduled debit while keeping the mandate exists at Cashfree.** Its docs describe a Manage Payment API that stops "a pending charge before it is debited". PayU has the same (a Delete action on the notice). Stripe says a debit cannot be cancelled once the notice is out. What Cashfree's docs do not say is whether the cancel works after the notice has gone out in the controlled flow.
3. **Pre-debit notice:** the tenant's bank or UPI app sends it, the merchant only triggers it. At least 24 hours before. The debit amount must equal the notified amount (Cashfree, PayU, Stripe agree). One open notice at a time: Cashfree and Stripe say so; PayU has a sequence number for several open notices.
4. **Retries:** NPCI allows 1 attempt plus 3 retries, only outside peak hours (PhonePe, Razorpay and PayU docs agree). PhonePe adds a 48-hour window. For e-NACH, NPCI advises at most 2 re-presentations, at least 3 days after a return.
5. **Blocked hours:** peak hours are 10:00 to 13:00 and 17:00 to 21:30. PhonePe's docs give the allowed windows to the minute. A first-debit exemption "within minutes of setup" is only supported by Stripe's 5-minute line; no official NPCI text found.
6. **Rent is not in any higher no-PIN category.** ₹15,000 per debit is the general limit. ₹1 lakh covers insurance, mutual funds and credit card bills (RBI), and Razorpay lists lending and investment category codes. Nothing names rent.
7. **Bounce charges:** Cashfree's own FAQ says a NACH debit that fails for low balance leads to a fine equal to the bank's cheque bounce charge. For UPI Autopay, no official source says banks charge for a failed debit.

---

## 1. More than one debit on one mandate in a day, and how many per cycle

| Source | What it supports | Verbatim (25 words or fewer) | URL | Conf. |
|---|---|---|---|---|
| Razorpay, UPI subsequent payments [official] | One successful debit per billing cycle, attributed to NPCI | "NPCI allows only one successful debit on a token per billing cycle." Also: "Do not create another subsequent payment until you get the status of the previous one." | https://razorpay.com/docs/payments/payment-gateway/s2s-integration/recurring-payments/upi/subsequent-payments/ | High that Razorpay says it; medium that it is NPCI's rule for "as presented" mandates (Razorpay's example is a monthly mandate) |
| Stripe, UPI AutoPay [archived, snapshot 21 Apr 2026] | One charge per customer per day; one open notice at a time | "Businesses can only have one pre-debit notification active per customer at a time. Raise a maximum of one charge per customer per day" | https://web.archive.org/web/20260421011051/https://docs.stripe.com/payments/upi/upi-autopay | Medium. The line is gone from the live page (checked 18 Sep 2026) and from the 8 Jul 2026 snapshot. Removal reason unknown |
| PhonePe, old Recurring Flow FAQ [archived, snapshot 21 Feb 2024; live page now returns 404] | Up to 20 debits in 24 hours on ON_DEMAND, up to ₹1 lakh total | "Merchants can debit maximum of 20 redemptions in rolling 24 hours until and unless cumulative redeemed sum is upto 1 lakh." | https://web.archive.org/web/20240221082108/https://developer.phonepe.com/v1/reference/faqs-2 | High that PhonePe said it in 2024. Low that it holds today: it predates NPCI's August 2025 rules, and the same page says for MONTHLY "within a month Merchants can debit only twice" |
| PhonePe, current Autopay docs (v2) [official] | Silent on a per-day or per-cycle count | Not found in the setup, notify, execute or sandbox pages | https://developer.phonepe.com/payment-gateway/autopay/api-integration/api-reference/subscription-setup | Nothing found |
| PayU, Recurring Payment Transaction API [official] | Several notices and debits can be open at once, tracked by a sequence number | "You may attempt multiple pre-debits and executions simultaneously in certain scenarios." | https://docs.payu.in/reference/recurring_payment_api | Medium. Does not say same day, and does not name the frequency |
| Cashfree, controlled flow [official, from our earlier file] | One open notice at a time (error "Prev_PDN_In_Progress") | See `research/cashfree-docs-answers.md` item 2 | https://www.cashfree.com/docs/api-reference/payments/latest/subscription/payment/controlled/overview | High |
| RBI e-mandate framework 2026, para 8 [official, taxguru copy] | Limit is per debit; heading names velocity checks; no clause on splitting | "All recurring transactions may be authorised without AFA up to ₹15,000/- per transaction." Heading: "Transaction limits and velocity check" | https://taxguru.in/rbi/rbi-issues-consolidated-directions-digital-payments-e-mandate-framework-2026.html | High |

**Where they disagree.** PhonePe (2024) says many a day. Stripe (2026) says one a day. Razorpay says one successful debit per billing cycle. Nothing official says what a "billing cycle" is for an "as presented" mandate. NPCI's own circular was not readable.

**Reading.** The colleague's PhonePe claim is real but old. The newer sources all point the other way, and Cashfree's one-open-notice rule means parts cannot overlap anyway. Parts on consecutive days are the best case; parts inside one "cycle" may be blocked outright if Razorpay's reading of NPCI applies to "as presented" mandates.

## 2. Cancelling one scheduled debit after the notice, keeping the mandate

| Source | What it supports | Verbatim | URL | Conf. |
|---|---|---|---|---|
| Cashfree, Manage Subscriptions [official] | A pending charge can be cancelled; mandate stays | "Cancel: Stop a pending charge before it is debited." | https://www.cashfree.com/docs/payments/subscription/manage | High that the action exists. Unknown whether it covers ON_DEMAND controlled-flow debits after the notice |
| Cashfree, Manage a Single Payment API [official] | The endpoint | "A payment can be cancelled or retried with this API." Path: `POST /subscriptions/{subscription_id}/payments/{payment_id}/manage` | https://www.cashfree.com/docs/api-reference/payments/latest/subscription/payment/manage | High |
| PayU, Pre-Debit Notification API [official] | The notice itself can be deleted | "pre-debit notification is triggered successfully for customer or deleted successfully in case of action delete." | https://docs.payu.in/reference/pre_debit_notification_api | Medium. Does not say the mandate is untouched, though nothing suggests otherwise |
| Stripe, India recurring payments [official] | Cannot cancel during the notice period | "The PaymentIntent transitions to a `processing` state for the entire duration of the pre-debit notification period (26 hours) and can't be cancelled." | https://docs.stripe.com/india-recurring-payments | High (Stripe only) |
| RBI framework para 6(c) [official] | The tenant can skip one debit and keep the mandate | "The issuer shall provider a customer with a facility to opt-out of any particular transaction or the e-mandate." | taxguru URL above | High |
| PhonePe v2 [official] | No cancel-a-notified-debit API found; a notified order fails on its own after `expireAt` (default 48 hours) | "after which the order will automatically fail or be skipped if it hasn't reached a terminal state." | https://developer.phonepe.com/payment-gateway/autopay/api-integration/api-reference/redemption-notify | Medium |

**Reading.** Cancelling a single debit is possible at scheme level (the tenant can do it, PayU lets the merchant delete the notice). At Cashfree the API exists. In the controlled flow, RentOk can also simply not call execute; whether the unexecuted notice then blocks the next notice ("Prev_PDN_In_Progress") until it expires is the real open point.

## 3. Pre-debit notice rules

| Rule | Source and verbatim | URL | Conf. |
|---|---|---|---|
| Who sends it: the tenant's bank or UPI app. The merchant triggers it | RBI 6(a): "An issuer shall send a pre-transaction notification to the customer, at least 24 hours prior to the actual charge / debit." Juspay: "This notification must be sent by the issuing PSP/Bank to the consumer at least 24 hours before the debit time." | taxguru URL; https://juspay.io/in/docs/upi-autopay/docs/how-to-integrate/troubleshooting--faqs | High |
| What it must contain | RBI 6(b): "merchant's name, transaction amount, date / time of debit, reference number of e-mandate, reason for debit" | taxguru URL | High |
| Minimum 24 hours; debit in the 25th hour | Razorpay: "Pre-debit notifications are delivered 24 hours before the debit and the actual debit is attempted in the 25th hour." Juspay: "Default execution happens at 25th hour of successful notification." | Razorpay subsequent payments URL; https://juspay.io/in/docs/upi-autopay/docs/how-to-integrate/mandate-execution-api | High |
| Latest: some providers set an upper bound | Juspay: "Notification should be sent between a window of 48–24 hours before the mandate execution time." Paytm (search summary only): 24 to 72 hours. Cashfree (our file): 1 to 7 days | Juspay FAQ URL | Medium |
| PayU asks for 48 hours on non-ad-hoc UPI frequencies | "For all frequencies (other than Daily and Adhoc), the merchant must send the notification 48 hours before the debit." | https://docs.payu.in/reference/pre_debit_notification_api | High (PayU only; looks like a PayU rule, not NPCI's) |
| Executed amount must equal notified amount | Cashfree FAQ: "If the executed debit amount differs from the amount notified in the PDN, the transaction is declined by the issuing bank". PayU: "should be same as the next execution amount." Stripe: "with the exact debit amount mentioned." | https://www.cashfree.com/docs/payments/subscription/faq ; PayU and Stripe URLs above | High |
| One open notice at a time | Cashfree (our file) and Stripe (archived April 2026) say yes. PayU's sequence numbers suggest several can be open | See item 1 | Medium: providers differ, so this may be a provider or bank rule, not an NPCI one |

## 4. Retries

**UPI Autopay**

| Source | Verbatim | URL | Conf. |
|---|---|---|---|
| PhonePe v2 notify page [official] | "You are limited to one initial attempt and three retries over a maximum of 48 hours." Merchant retries (CUSTOM) or PhonePe retries (STANDARD) | PhonePe notify URL | High |
| Razorpay blog [blog, Razorpay's own] | "one original attempt plus a maximum of three retries" | https://razorpay.com/blog/master-recurring-payments-upi-autopay-guide/ | Medium |
| Razorpay docs [official] | Razorpay retries by itself, except in the notify-first flow: "We will not attempt any retry if the debit fails for tokens with the notification object in the created order." | Razorpay subsequent payments URL | High |
| PayU [official] | "limiting the execution attempts to 4 will be applicable post 31st July, 2026." (The year is probably a typo for 2025, the NPCI date the press reports.) | https://docs.payu.in/reference/recurring_payment_api | High that PayU says 4; the date is suspect |
| Juspay FAQ [official, looks older] | "Failed mandates can be retried up to two times. If retries also fail, then mandate execution needs to be done again with pre-debit notification." | Juspay FAQ URL | Medium (older than the 1 plus 3 rule) |
| Cashfree (our file) | Its own retries: 3, an hour apart. Merchant retries: "A maximum of 3 retries are allowed per billing cycle." | https://www.cashfree.com/docs/payments/subscription/manage | High |
| Press (Ujjivan bank blog, Kiwi) | NPCI circular of 21 May 2025, in force 1 Aug 2025: 1 attempt plus 3 retries per mandate, non-peak hours only | https://www.ujjivansfb.bank.in/banking-blogs/banking-services/upi-rule-updates-npci-august | Medium |

**Useful detail:** after the 4 attempts on one notice, a new notice (and a new 24 hours) is needed. Juspay says this outright; PhonePe's 48-hour expiry implies it.

**e-NACH**

| Source | Verbatim | URL | Conf. |
|---|---|---|---|
| Juspay (LotusPay) summarising NPCI circular NPCI/2023-24/NACH/007 [official provider summary] | "Restrict the representation of the returned transactions to 2 times (1 presentation + 2 representations)." And: "only after 3 days from the date of a return." | https://docs.juspay.io/lotuspay/web/nach-debit-flow/ach-debit-penalty-charges-for-high-percentage-of-returns | High that NPCI advises it; the same page describes penalties on the merchant's sponsor bank for high return rates |
| Cashfree FAQ, NACH failure table [official] | "A total of 3 retries are allowed before the start of the next cycle." | https://www.cashfree.com/docs/help/subscriptions/faqs/faqs.md | High (Cashfree's own number; differs from NPCI's advice of 2) |
| Razorpay e-mandate FAQ [official] | "Wait at least 2 days before retrying a failed debit." (about new registrations not yet live at the bank) | https://razorpay.com/docs/build/llm-docs/payments/recurring-payments/emandate/faqs.md | High |

## 5. Execution time windows, and the first debit right after setup

| Source | Verbatim | URL | Conf. |
|---|---|---|---|
| PhonePe v2 [official] | "Retries must be executed only during the non peak periods – 9:31 PM to 9:59 AM and 1:01 PM to 4:59 PM" | PhonePe notify URL | High |
| PayU [official] | "NPCI recommends avoiding execution during peak hours, specifically between 10:00 AM to 1:00 PM and 5:00 PM to 9:30 PM." | PayU recurring API URL | High |
| Stripe [official] | "You can charge customers up to 5 minutes after the mandate is set up." | https://docs.stripe.com/payments/upi/upi-autopay | High that Stripe says it; says nothing about peak hours |
| Juspay FAQ [official] | PIN is needed for the first debit "in case no amount is debited within 1 min of mandate authentication" | Juspay FAQ URL | Medium |
| NPCI circular text | Not readable (403). The exemption of a first debit within 5 minutes from blocked hours is still only from TransactBridge (press), cited in our earlier file | none | Low |

## 6. Per-debit limit without the PIN, and whether rent qualifies

| Source | Verbatim | URL | Conf. |
|---|---|---|---|
| RBI 8(a) and 8(b) [official] | ₹15,000 general. "Payment of insurance premiums, subscription to mutual funds, and credit card bill payments may be made without AFA up to ₹1,00,000" | taxguru URL | High |
| Razorpay [official] | "For lending and investment categories (MCCs 6211, 6300, 7322, 6529, 5960), AFA is not required for debits up to ₹1,00,000." | https://razorpay.com/docs/payments/payment-gateway/s2s-integration/recurring-payments/upi/ | High |
| Stripe [official] | "UPI currently doesn't support recurring transactions of greater than 15,000 INR in value." | https://docs.stripe.com/india-recurring-payments | High (Stripe product limit, stricter than the rule) |
| PayU [official] | For e-NACH, "ADHOC" (as presented) with category "Loan EMI payment" "is not allowed as per NPCI guidelines" | PayU recurring API URL | High. Shows NPCI does restrict "as presented" by category, at least for e-NACH |
| Press summary of NPCI UPI/OC-151A (Dec 2023) | ₹1 lakh no-PIN limit for the category codes in its Annexure A | search-result summary only; circular not readable | Low |

**Rent (MCC 6513) appears in no higher-limit list found.** No NPCI circular limiting "as presented" UPI mandates by category was readable; the only category rule found (PayU) is for e-NACH loan EMIs.

## 7. First payment at mandate creation

| Source | Verbatim | URL | Conf. |
|---|---|---|---|
| RBI 5(a) [official] | "If the first transaction is processed along with registration of the e-mandate, then AFA validation may be combined." | taxguru URL | High |
| PhonePe v2 setup [official, via page summary] | TRANSACTION flow: amount at least ₹1 "or the first debit amount"; PENNY_DROP flow ₹2 | https://developer.phonepe.com/payment-gateway/autopay/api-integration/api-reference/subscription-setup | Medium (summary of the page, not a verbatim line) |
| PayU [official] | "When consent is taken, the first execution is carried out in real-time, and the execution sequence is set to 1." | PayU recurring API URL | High |
| Juspay FAQ [official] | The setup amount can be refunded and the mandate stays active | Juspay FAQ URL | High |

**Upper limit: not found anywhere.** Since the tenant enters her PIN at setup, the ₹15,000 no-PIN limit should not cap it; the general UPI per-transaction cap would. That is my inference, not a quote.

## 8. Merchant name shown to the tenant

| Source | Verbatim | URL | Conf. |
|---|---|---|---|
| RBI 6(b) [official] | The notice must carry the "merchant's name" | taxguru URL | High |
| Stripe [official] | `description`: "The description that your customers see in their UPI app when approving the e-mandate." | Stripe UPI AutoPay URL | High. This is a description line, not the merchant name |
| Press on NPCI OC-223 (7 Oct 2025) [press] | Mandate portability across UPI apps; merchants use unique Merchant Identifier Codes | https://www.teamleaseregtech.com/updates/article/47798/npci-issued-a-notification-regarding-the-enhancement-of-upi-autopay/ | Low |

**How the name is set, and whether a sub-merchant (property) name can appear: not found in any provider's docs.** It stays a Cashfree account-manager question.

## 9. Charges to the tenant for failed debits

| Source | Verbatim | URL | Conf. |
|---|---|---|---|
| Cashfree FAQ, NACH failure table [official] | "the end-customer will be asked to pay a fine of amount equivalent to the cheque bounce charges by the destination bank." | https://www.cashfree.com/docs/help/subscriptions/faqs/faqs.md | High for e-NACH |
| RBI 10(a) [official] | "No charges shall be levied to the customer for availing the e-mandate facility" (covers the facility, not failed debits; the framework covers cards, UPI and wallets, not NACH) | taxguru URL | High on what it says; it does not settle bounce fees |
| UPI Autopay | No official source found on bank charges for a failed UPI Autopay debit. A search summary claims none; not verified | none | Nothing found |

The tenant charged ₹200 several times fits the e-NACH pattern (one bounce fee per presentation), not anything documented for UPI.

## 10. Sandbox and testing

| Provider | What the docs say | URL | Conf. |
|---|---|---|---|
| Cashfree [official] | UPI Autopay is switched on by the account manager "on your production and sandbox accounts". ON_DEMAND charges can be raised straight away in sandbox; PERIODIC charges cannot be moved forward | https://www.cashfree.com/docs/payments/subscription/faq | High |
| PhonePe [official] | Full UAT sandbox: setup, notify, execute and failures chosen by templates, e.g. "Setup, notify & redemption success with merchant controlled retries" | https://developer.phonepe.com/payment-gateway/autopay/uat-sandbox | High |
| Stripe [official] | Sandbox exists; test cases shown are for cards, not UPI | https://docs.stripe.com/india-recurring-payments | High |
| Juspay, PayU, Paytm [official] | Sandbox or staging endpoints exist (api.sandbox.juspay.io, test.payu.in, securestage.paytmpayments.com); no UPI Autopay test scenarios found | Juspay execution, PayU recurring, Paytm pre-notify status pages | Medium |
| Razorpay | Nothing found on testing UPI Autopay | none | Nothing found |

---

## What this means for the Cashfree email

**Answered well enough to stop asking (or to ask only for a yes)**
- **Q3, sandbox:** Cashfree's own FAQ says the account manager enables UPI Autopay on sandbox, and ON_DEMAND charges can be tested there. Shorten to: "Please enable UPI Autopay on our sandbox account."
- **The retry and notice rules around Q1:** 1 attempt plus 3 retries, non-peak hours only, a new notice after that, amount must match. Consistent across PhonePe, Razorpay, PayU and Cashfree. No need to ask.

**Narrowed (still ask, but a sharper question)**
- **Q1, more than one debit a day:** current docs lean no, and Razorpay says one successful debit per billing cycle. Ask: "What counts as a billing cycle for an as-presented (ON_DEMAND) UPI mandate, and can two successful debits run on consecutive days within it?" Mention that PhonePe's 2024 docs allowed 20 a day, so Cashfree states the current rule.
- **Q2, cancelling one debit:** the Manage Payment API exists. Ask only whether it works on an ON_DEMAND controlled-flow debit after the notice is sent, and whether a notified but unexecuted debit blocks the next notice until it expires.
- **Q8, failed-attempt charges:** for e-NACH, Cashfree's FAQ already says the tenant is fined the bank's bounce charge. Still open: whether Cashfree bills RentOk for failed attempts, and anything on UPI bank charges.
- **Q10, blocked hours:** the windows are known to the minute (PhonePe). Still open: what Cashfree's standard flow does with a time inside a blocked window.
- **Q4, first payment at setup:** allowed by RBI and offered by PhonePe and PayU. Still open: Cashfree's upper limit, and whether it counts as a mandate transaction for the 15 Oct charge.
- **Regulation, "as presented" by category:** rent is in no higher-limit list, and NPCI does restrict "as presented" by category at least for e-NACH loan EMIs (PayU). Ask whether any such rule touches rent (MCC 6513) on UPI or e-NACH.

**Fully open (no other source helps)**
- **Q5, merchant name, and whether a property name can show.**
- **Q6, deep links on iOS and desktop** (not researched here).
- **Q7, whether a failed first debit cancels the mandate:** no provider says so either way.
- **Q9, routing different dues to different bank accounts.**
- **Q11, changing a PERIODIC mandate:** not researched here; Cashfree's docs already answered it in our earlier file, so it may not need asking.
- **Q12, which cancel endpoint to use.**
- **Settlement of each flow to owners as verified vendors.**

