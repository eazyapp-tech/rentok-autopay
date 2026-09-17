# Auto Pay push: MDR rules, costs, surfaces, and what we take from Kamal's plan

> Partly superseded. The fee model here predates R35 (the platform fee is the property's charge, not RentOk's) and R46. The rules on the new 0.4% UPI charge still hold.

17 Sep 2026. Target (CEO, fixed): 70,000 to 75,000 tenants on Auto Pay by 1 Oct. Live for every property, optional for tenants, charges borne by the tenant by default (Sanchay, 17 Sep).

## What the MDR rule actually says

Official sources: PIB release 2310586 and the Finance Ministry FAQ, both 15 Sep 2026 (copy in `sources/`).

| Point | Rule | Where |
| --- | --- | --- |
| Start date | 15 Oct 2026 | FAQ Q5 |
| Rate | 0.4% on merchant UPI payments above ₹2,000, capped at ₹300 (cap reached at ₹75,000) | PIB; FAQ Q35 |
| Free | Person to person; merchant payments up to ₹2,000; small merchants (QR into a personal account, up to ₹1 lakh a month) | FAQ Q23, Q24 |
| Auto Pay | "UPI Mandates or AutoPay do not carry prescribed MDR transaction charges" | FAQ Q22 |
| Passing it on | "merchants on-boarded cannot pass on MDR charges to customers" | FAQ Q34; PIB |
| Rent | Not named anywhere; standard 0.4% is the likely reading (inference) | none |
| GST | Not in official documents; press reports 18% with input credit; plan for about 0.472% | Business Standard headline, 16 Sep |
| Consumers | "UPI services will continue without any cost to consumers" | FAQ Q15 |

## UPI Auto Pay rules that shape the product

- No PIN needed per debit up to ₹15,000. Above that, the tenant approves each debit with her PIN. Rent has no exemption (exempt: insurance, mutual funds, credit card bills, up to ₹1 lakh). RBI e-mandate framework, 21 Apr 2026.
- Notice at least 24 hours before each debit, and an alert after it. The bank sends it on the merchant's or aggregator's trigger; many merchants also send their own.
- Tenant can pause, change or cancel any time; registration must be free.
- Debits only off peak (before 10 am, 1 to 5 pm, after 9:30 pm); at most one attempt plus three retries (secondary sources). Our code allows 5 retries.
- On-demand mandates allow more than one debit a month, each with its own notice (not confirmed in an NPCI document).
- Mandates can be seen and managed from any UPI app (NPCI circular OC-223, secondary source).

## Cost per ₹10,000 rent, from 15 Oct

| Path | Cost | Who can bear it |
| --- | --- | --- |
| Payment link (one-off UPI) | ₹40 MDR, about ₹47.2 with GST, plus any Cashfree margin (one-off UPI price unconfirmed) | Merchant only; not the tenant (Q34) |
| Auto Pay via Cashfree | ₹15 per debit attempt (₹1,000 and above) + ₹7.5 per mandate, plus 18% GST: about ₹17.7 a month, ₹8.85 once | Not MDR; a platform charge |
| e-NACH via Cashfree | ₹7.5 per mandate + ₹7.5 per debit, plus GST | Same |

Our code's default Auto Pay fee to the tenant is ₹50 a month. That is more than a link payment costs her (₹0 to her after 15 Oct), so as the code stands Auto Pay is the more expensive path for the tenant.

## Every surface, and the biggest levers

| Surface | Audience | Reach | Auto Pay today |
| --- | --- | --- | --- |
| Payment-link WhatsApp reminders (automated) | Tenants | About 2.87 million links in 30 days to about 209,000 tenants | No mention; the link opens the live page (/p) with no Auto Pay |
| Live payment page (/p) | Tenants | Every link | None |
| New payment page (/p2) | Tenants | None routed yet | Built, preview only, setup switched off |
| Rent-due WhatsApp bot flow (18_rent_reminder_*) | Tenants | Every due | No mention |
| Welcome WhatsApp on add tenant (tenant_add_wlcm_1_4) | New tenants | Every new tenant | No mention |
| Web check-in | New tenants | Every check-in link | The only working setup path; one-day window for most; picker disagrees with backend |
| Tenant app (Dues banner, Profile row) | App users | App users | Never shows (status not saved) |
| Pre-debit reminder (autopay_utility) | Auto Pay tenants | 1,226 | Locked to one test record |
| Setup, debit success, debit failure | Auto Pay tenants | 1,226 | Manager note only; tenant told nothing |
| Manager app: bulk reminder | Managers | Properties with Auto Pay on | Whole property only; link lands on check-in step 1 (autopay=true ignored) |
| Manager app: home card "Tenants to set up AutoPay" | Managers | Every manager | Live, generic card |
| Manager app: tenant filter, tenant profile row | Managers | Every manager | Enabled or disabled only; no failed state; no single send |
| Manager web: settings | Managers | Web users | Settings only; grace label wrong |
| Manager web: tenant list, dues, WhatsApp inbox, bulk WhatsApp | Managers | Web users | No Auto Pay at all |
| Owner WhatsApp per payment (21_due_received) | Owners | Every payment | Does not say whether Auto Pay paid it |
| Owner welcome email | New owners | Every new owner | Mentions Auto Pay |
| Rio assistant | Managers | Rio users | Answers about Auto Pay; can open the bulk reminder |
| Onboarding booking page (unified) | New tenants | Every booking | No Auto Pay |
| Sales Hub templates | Prospects | Sales | No Auto Pay |

## What we take from Kamal's plan (17 Sep)

Take:
- The "Choose a date between 1st and 1st" screenshot: confirms the one-day window in code.
- Button says "Set up Autopay", not "Schedule Rent Payment".
- A summary before the bank step: amount, "every month", next three debit dates.
- Success screen with a calendar and a cancel entry point.
- Consent clause inside the rental agreement; T&C clauses on cancellation, retries and failure.
- WhatsApp sequence: welcome, 7 days before due, 24 hours before debit, success, failure with "Pay now", monthly nudge for manual payers; frequency cap.
- Offer Auto Pay right after a successful link payment (already in the /p2 design).
- Manager app: status column (none, active, paused, failed), choose tenants for the bulk nudge, failure alerts, Auto Pay rate per property, date and pause overrides, fees-avoided figure.
- Manager incentives and co-tenant referral.
- Metrics list: activation, debit success, MDR avoided, tickets, cancellations with reason.

Do not take, or check first:
- Phases that move existing tenants in Nov to Jan: conflicts with the 1 Oct target.
- "Most rents are ₹15,000 to ₹50,000": RentOk is PG-heavy; measure the split before designing around it.
- Split one rent into 2 to 3 mandates: needs Cashfree and compliance confirmation; may look like structuring.
- "Pre-selecting the UPI app lifts completion 20 to 30%": unsourced; the Cashfree page controls this.
- "3 retries": code does 5; the rule is 1 plus 3.
- "Never mention MDR to tenants": fine, but the reason is stronger: tenants must not be charged it (Q34).
- "Waive Auto Pay fees permanently": needs Sanchay's ruling against "tenant bears charges by default".
- Misses: the no-login security hole (#6816), the 59% failure rate, the 11 Sep rulings, the /p2 design, the bulk link that lands on step 1.

## Ruling on Auto Pay charges (Sanchay, 17 Sep)

- The tenant pays the Auto Pay charges (setup and monthly) by default.
- Management can switch them to itself in property settings (two options: Management, Tenant).
- RentOk bears nothing, and management bears nothing unless it chooses to.
- My earlier recommendation (Auto Pay free to the tenant) is withdrawn.

Gaps against the ruling, in code today:
- Setup fee payer: backend offers only RentOk (`autopay_setup_bearers = [0]`, property.ts 9282), ₹50 default. RentOk is paying every setup today. Needs Tenant (default) and Management.
- Monthly fee payer: backend offers Owner or Tenant, default Tenant (property.ts 9283 to 9287). Matches.
- Flutter fallback default is "RentOk" for both (autopay_settings_bottom.dart 35 to 40). Needs Tenant.

## Charging the tenant without breaking the MDR rule (proposal, 17 Sep)

The rule bans passing MDR on to the customer (FAQ Q34). Auto Pay carries no prescribed MDR (FAQ Q22). So a fee for the Auto Pay service is not MDR, if it is built and named as a service fee:

1. **Name it for the service, never the payment.** "Auto Pay service fee": scheduling, the notice before each debit, retries, receipts, failure handling, rent records. Never "gateway fee", "convenience fee", "UPI charge", "transaction charge" or "MDR".
2. **Flat rupees, never a percentage of rent.** A percentage looks like MDR moved to the tenant.
3. **Billed by RentOk as its own invoice line with GST**, shown separately on every receipt; debited in the same Auto Pay debit as rent.
4. **Disclosed before the bank step and consented to**: on the setup screen, in the Auto Pay terms, and in the rental agreement clause.
5. **No fee for creating the mandate itself.** Collect the one-time setup fee as an "Auto Pay activation" line on the first debit, not at the ₹1 authorisation. (Legal to confirm whether e-mandate rules forbid a registration charge.)
6. **Management switch stays per property**, visible to the tenant as "Paid by your property" when switched.

Link payments (the path that does carry MDR from 15 Oct): the tenant cannot be charged MDR, and RentOk will not bear it. Options:
- **A. The property bears it**, deducted from settlement under owner terms (the 15 Oct owner sheet). Legal, since the property is the payee. Also the owner's reason to push Auto Pay.
- **B. A flat monthly platform fee for every tenant**, whatever the payment method (cash, link or Auto Pay), for the rent app and services, not linked to UPI or the amount. Legal only if truly method-neutral.
- **C. A free manual path with no UPI MDR**: bank transfer (IMPS or NEFT) to the property's virtual account.
- **D. Discount, never surcharge**: any Auto Pay benefit is framed as a reduction (for example RentPass cashback), never as a higher price for link payers.

Sanchay, 17 Sep: A and B make sense; C rejected (RentOk must keep payment control); D maybe. Owners will not absorb MDR; they will raise rent (₹10,000 becomes ₹10,040).

### Payment ladder that keeps collection with RentOk (proposal, 17 Sep)

| Rung | Rail | UPI MDR | RentOk control | Best for |
| --- | --- | --- | --- | --- |
| 1 | UPI Auto Pay (Cashfree mandate) | None (FAQ Q22) | Full | Default for every tenant, rent up to ₹15,000 without a PIN each month |
| 2 | e-NACH mandate from her bank account (Cashfree) | Not a UPI payment | Full | Rent above ₹15,000, or tenants whose UPI app fails; takes 1 to 5 days to activate |
| 3 | RentOk virtual bank account per tenant (Cashfree Auto Collect), paid by IMPS, NEFT or RTGS | Not a UPI payment | Full: money lands in RentOk's collection account, matched to her dues automatically | Manual payers who will not set up a mandate |
| 4 | UPI payment link or QR (one-off) | 0.4% above ₹2,000 | Full | Last resort; the property's MDR is deducted from its payout |
| 5 | Cash with OTP | None | Recorded | Exists today |

Watch-outs to confirm with Cashfree and counsel:
- A UPI payment to a virtual account's UPI ID is still a UPI merchant payment and likely carries MDR; only bank transfers into the virtual account avoid it. The virtual account page should show the account number and IFSC first, UPI last.
- Virtual account and e-NACH per-transaction fees are charges for those services, not MDR; charging them to the tenant follows the same service-fee rules as Auto Pay.
- Rejected: breaking rent into payments of ₹2,000 or less to stay under the MDR threshold. It would look like structuring.

### Pricing levers (all method-neutral or discount-shaped)

- **A. Property bears link MDR via payout deduction.** Owners recover it in their own rent pricing, which is their right.
- **B. Flat monthly platform fee for every tenant**, the same for cash, link, transfer or Auto Pay.
- **D, built as a product: "Auto Pay price".** The property posts one rent (for example ₹10,040, its own pricing). Tenants on Auto Pay get a standing discount (₹40 off). Nobody pays more than the posted price; Auto Pay tenants pay less. This is the owners' rent-raise behaviour turned into the strongest adoption reason there is: "Save ₹40 every month with Auto Pay". Counsel to confirm a method-based discount is acceptable under Q34's "posted price" wording.

Before 15 Oct: a written opinion from payments counsel, and Cashfree compliance confirmation of the fee structure. Also check who the merchant of record is: Cashfree shows EAZYAPP, which suggests RentOk collects on the property's behalf.
