# Legal and regulatory research (17 Sep 2026)

Agent research (opus) with sources opened on 17 Sep 2026; facts and readings kept separate. Not legal advice; a payments counsel opinion is still needed.

## Three findings the plan had not accounted for
1. RBI's e-mandate framework (April 2026), para 10(a): "No charges shall be levied to the customer for availing the e-mandate facility for recurring transactions." Para 10(c): the acquirer (Cashfree) must make its merchants comply. A tenant-paid Autopay setup or monthly fee is high risk. (Verified by hand, see below.)
2. Money landing in RentOk's (EAZYAPP's) own bank account and then paid to owners is likely unlicensed payment aggregation under RBI's Payment Aggregator directions (15 Sep 2025). These rules made PhonePe, CRED and Paytm stop credit card rent payments.
3. Splitting one rent into two or three mandates under ₹15,000 is likely to be read as avoiding the PIN rule. Drop it.

## 1. Is RentOk a payment aggregator?
- Facts: an aggregator collects for merchants and settles to them; non-banks need RBI authorisation (₹15 crore net worth at application, ₹25 crore within three years). A gateway that never handles funds is outside. Escrow may pay a third party on the merchant's instruction only if the merchant's turnover is above ₹40 lakh and the third party is the real payee (Razorpay Route enforced this from 31 Dec 2025). BBPS directions: operating a bill payment system outside BBPS needs authorisation. Cashfree Easy Split settles directly to each KYC-checked vendor's bank account.
- Reading: Setup A (money in Cashfree escrow, Cashfree pays owners through Easy Split, owners as KYC-checked vendors) keeps RentOk on the safe side. Setup B (money in EAZYAPP's own account, RentOk pays owners) is the activity that needs authorisation. "RentOk keeps control" can be met through Setup A: control means running the flow and the ledger, not holding the money.
- Risks: unauthorised payment system exposure; Cashfree switching service off; "EAZYAPP" as merchant name on notices invites disputes.
- Recommend: Cashfree to confirm in writing how every flow settles today (links, Autopay, instant settlement, virtual accounts); move all flows to Easy Split with owners as vendors; file Cashfree's use-case declaration; ask for a merchant name including the property. Do not apply for RentOk's own licence now.

## 2. TPAP, UPI plugin, own licence
- Facts: a TPAP is a UPI app (like PhonePe) through a sponsor bank, with NPCI approval, audits and in-app complaints (Rediff approved 30 Dec 2025 with Axis Bank). Vendor claim: 8 to 12 weeks. UPI app providers cannot charge any platform fee on UPI payments (FAQ Q17). The UPI plugin lets a merchant take UPI inside its own app without being a TPAP (the bank's SDK is the licensed party); it needs one-time phone binding, where PhonePe reports 40 to 50% drop-off. MDR is charged to the merchant whichever app the tenant uses.
- Reading: becoming a TPAP removes no MDR, allows no fee, adds liability, cannot happen before 15 Oct. Mandates are still created by the merchant through Cashfree. The plugin helps repeat payers only.
- Recommend: no TPAP application now; keep Cashfree's hosted flow for 15 Oct; pilot a UPI plugin in the tenant app in early 2027; own PA licence only if Easy Split becomes a hard limit (2027 or later).

## 3. BBPS
- Facts: a "Housing Societies and Rentals" category exists; since NPCI's notice of 21 Aug 2025 only registered entities (not individuals or sole proprietors) qualify. Customer convenience fee belongs to the app or agent the customer pays through, capped. From 15 Oct UPI apps cannot charge platform fees on BBPS bills. The ₹5 flat MDR covers named utilities; rent is not named.
- Reading: RentOk cannot be the biller for rent it does not own; most owners are individuals and excluded; rent via BBPS most likely carries 0.4%; money passes through the biller operating unit's escrow.
- Recommend: no BBPS for 15 Oct; later, for registered operators only, ask Cashfree or Setu in writing about category, MDR and settlement. A reach channel, not an MDR saving.

## 4. Charging tenants
- Facts: FAQ Q34 (no MDR pass-through; consumers pay only the posted price). E-mandate framework para 10(a) and 10(c). PA directions: any charge beyond the price must be displayed before the transaction. CCPA fined platforms in 2026 for late-revealed checkout fees and probed payment-method fees. Debit card MDR cannot be passed on; credit card surcharges must be disclosed and follow the acquirer's contract. Cashfree cost to merchant: ₹7.5 per mandate, ₹15 per debit of ₹1,000 or more, ₹20 per virtual account credit, plus 18% GST.
- Reading: setup fee, do not charge (collecting it on the first debit does not change what it pays for). Monthly tenant-paid Autopay fee: high risk (a charge for using the mandate). A flat platform fee for every tenant is defensible if the same for every method, not tied to rent or MDR, shown upfront and agreed. "Autopay price" discount: high risk (link payers pay the MDR amount in another form; CCPA payment-method fee scrutiny). Owners raising rent for everyone is lawful. RentOk's platform fee carries 18% GST on its own line.
- Recommend: stop designing tenant-paid Autopay setup and monthly fees (default to management or drop); if revenue is needed, one method-neutral platform fee; no Autopay discount; Cashfree compliance sign-off on any fee.

## 5. Mandates for monthly collection
- Facts (e-mandate framework): no PIN up to ₹15,000 per debit; only insurance, mutual funds and credit card bills get ₹1 lakh; first debit always needs the PIN; notice at least 24 hours before each debit with merchant name, amount, date, reference and reason, with opt-out of one debit or the mandate; tenant sets the maximum on variable mandates and can cancel any time. Q22: no prescribed MDR on Autopay. NPCI from 1 Aug 2025 (secondary source): debits only before 10:00, 13:00 to 17:00, after 21:30; one attempt plus three retries.
- Reading: one on-demand debit per rent cycle, PIN above ₹15,000, is lawful and should be MDR-free (confirm with Cashfree). Splitting rent, several debits on one obligation, or mandates for one-off dues look like avoiding MDR or the PIN rule.
- Recommend by 15 Oct: at most 3 retries; off-peak debits; our own pre-debit notice fixed; re-approval on rent rises; drop the split-mandate idea. Later: ask NPCI through Cashfree and the industry body to add rent to the higher limit.

## 6. Virtual accounts
- Facts: Cashfree Auto Collect creates per-customer virtual accounts and UPI IDs; ₹20 per credit to the merchant. MDR applies to UPI merchant payments; bank transfers are not UPI. Aggregator money must sit in escrow at a scheduled commercial bank.
- Reading: Cashfree virtual accounts settling through Easy Split need no RentOk licence; virtual accounts straight into EAZYAPP's current account are Setup B (high risk); UPI to the virtual UPI ID likely carries MDR; charging the tenant the ₹20 is a method-based fee.
- Recommend: Cashfree virtual accounts only, through Easy Split; show account number and IFSC first; absorb the ₹20 (note: conflicts with the ruling that RentOk absorbs nothing; needs a decision).

## 7. Owners
- Facts: Model Tenancy Act model asks three months' written notice before a revision (states differ; not checked). MDR is the merchant's cost; 18% GST on MDR with input credit (reported). Tenant-side TDS on rent above ₹50,000 a month (2% individuals, 10% companies), now section 393 of the Income-tax Act 2025 (search results). E-commerce operator TDS (0.1%) continues under section 393 (search result). GST exemption for hostels and PGs up to ₹20,000 per person per month for stays of 90 days or more (search result).
- Reading: owners may reprice at renewal or where the agreement allows; a mid-term ₹40 rise without a clause or notice is open to challenge (PG licences more flexible). RentOk's fee to the owner (including MDR recovery) is RentOk's taxable service at 18%; call it a payment processing fee. RentOk may be an e-commerce operator liable to 0.1% TDS on payouts, and GST collection at source may apply for GST-registered taxable PGs; past exposure possible. Owners must disclose payee, rent, fees, GST and that RentOk collects on their behalf.
- Recommend: tax opinion now on e-commerce operator status; owner agreement addendum (fees, deductions, GST invoices, collection mandate); rent-rise template with notice.

## 8. Consent and cancellation
- Facts: registration with PIN, validity shown, change or cancel any time and told so at registration; notices before and after each debit (after-debit notice includes how to complain); single-debit opt-out; no facility fee; customer-liability rules apply; CCPA fines forced subscriptions and manipulative renewal prompts.
- Reading: today's forced tick, mandate before agreement, false "one-time" fee, false "change date anytime", "until eviction" with no tenant cancel, and no cancel on eviction each break a rule or invite a CCPA complaint.
- Clause guidance: optional authorisation of monthly UPI Autopay or e-NACH to EAZYAPP (RentOk) on the owner's behalf; maximum amount and day; 24-hour notice; PIN above ₹15,000; pause a debit or cancel any time in the UPI app or RentOk app; cancelling does not end the tenancy; other methods at the same rent; ends automatically at move-out; complaint contact.
- Recommend by 15 Oct: agreement before mandate; unticked consent; correct copy; cancel in the tenant app; auto-cancel on eviction or deletion; Autopay never a condition of tenancy.

## Ten biggest legal risks
1. Unlicensed payment aggregation (money in EAZYAPP's own account). Fix: Easy Split, owners as vendors, declaration to Cashfree.
2. Tenant-paid Autopay setup and monthly fees vs para 10(a). Fix: drop or management pays; method-neutral platform fee only.
3. MDR passed on in another form (Autopay discount, link fees). Fix: same price for every method.
4. Split mandates or payments. Fix: one mandate, one debit per cycle.
5. Consent defects. Fix: section 8 changes before the push.
6. Security gap (#6816, #6861). Fix before /p2 or any bulk push.
7. NPCI operating rules (5 retries, peak-hour debits, silent cap, no cancel on eviction).
8. Tax exposure (e-commerce TDS, GST collection, GST on fees). Fix: tax opinion; GST invoices.
9. Merchant identity (EAZYAPP). Fix: property-level merchant name; "RentOk for <property>".
10. Relying on an FAQ rather than NPCI's circular for Q22 and PIN debits. Fix: Cashfree written confirmation and counsel opinion before 15 Oct.

Next step recommended: one written question list to Cashfree today (settlement per flow; charging of PIN debits above ₹15,000 and of UPI to a virtual account; whether any tenant-paid fee is allowed).

## Sources
- S1 Finance Ministry MDR FAQ, 15 Sep 2026 (copy in sources/)
- S2 RBI Payment Aggregator directions, 15 Sep 2025: https://www.fidcindia.org.in/wp-content/uploads/2025/09/RBI-PAYMENT-AGGREGATORS-DIRECTIONS-15-09-25.pdf
- S3 Khaitan note, 3 Oct 2025: https://www.khaitanco.com/sites/default/files/2025-10/ERGO%20-%20PA%20Master%20Directions%20-%203%20Oct%202025_0.pdf
- S4 Cyril Amarchand note, 23 Sep 2025: https://www.cyrilshroff.com/wp-content/uploads/2025/10/Client-Alert-RBI-Introduces-Consolidated-Framework-for-Payment-Aggregators-3.pdf
- S5 RBI e-mandate framework 2026: https://taxguru.in/rbi/rbi-issues-consolidated-directions-digital-payments-e-mandate-framework-2026.html
- S6 CA Jatin Karda, 16 Sep 2026: https://cajatinkarda.in/articles/upi-mdr-charges-october-2026
- S7 ThePrint/PTI, 17 Sep 2026: https://theprint.in/economy/no-us-pressure-in-upi-mdr-decision-npci-circular-offers-no-advantage-to-foreign-credit-cards-finmin/3045344/
- S8 Business Standard, 16 Sep 2026: https://www.business-standard.com/industry/banking/payments-apps-flag-losses-on-bill-payments-via-upi-as-platform-fees-banned-126091601232_1.html
- S10 NPCI BBPS biller categories notice, 21 Aug 2025: https://www.teamleaseregtech.com/updates/article/46742/npci-issued-a-notification-regarding-the-review-of-biller-categories-o/
- S11 RBI BBPS directions 2024: https://taxguru.in/rbi/master-direction-reserve-bank-india-bharat-bill-payment-system-directions-2024.html
- S14 Cashfree Easy Split FAQ: https://www.cashfree.com/docs/help/easy-split/faqs/faqs
- S15 Cashfree pricing: https://www.cashfree.com/payment-gateway-charges/
- S16 Cashfree Auto Collect: https://www.cashfree.com/auto-e-collect/
- S17 Razorpay Route: https://razorpay.com/docs/payments/route/
- S18 Razorpay Turbo UPI FAQ: https://razorpay.com/docs/payments/payment-gateway/flutter-integration/custom/payment-methods/turbo-upi/faqs/
- S19 PhonePe on the UPI plugin: https://www.phonepe.com/blog/milestones/merchant-upi-plugin-marketing-hype-versus-reality/
- S20 Razorpay TPAP guide: https://razorpay.com/blog/tpap-integration-go-ahead-requirements-process-benefits-guide/
- S21 Rediff TPAP approval: https://www.electronicpaymentsinternational.com/news/rediff-com-india-final-approval/
- S22 IDFC FIRST Bank on TPAP roles: https://www.idfcfirst.bank.in/personal-banking/payments/upi-payments/list-TPAPs-roles-responsibilities
- S23 Medianama on rent payments halted: https://www.medianama.com/2025/09/223-rbi-pa-rules-phonepe-paytm-cred-credit-card-rent-payments/
- S24 Kiwi on NPCI Autopay changes: https://gokiwi.in/blog/major-changes-by-npci-on-upi-in-2025/
- S25 Outlook Business on CCPA fines: https://www.outlookbusiness.com/corporate/ccpa-fines-9-digital-platforms-including-zepto-indigo-over-dark-patterns
- S26 RetailIntel on card surcharges: https://retailintel.in/signal/rbi-rules-bar-debit-card-surcharges-while-credit-card-fees-r-592d1ad5

## Addendum 17 Sep: one mandate, rent above ₹15,000 split into several debits (Sanchay's proposal)

Proposal: one UPI Autopay mandate with a ₹15,000 limit. Rent of ₹20,000 would be taken as a ₹15,000 debit plus a ₹5,000 debit within about 24 to 48 hours, with e-NACH also offered.

**What the RBI text says** (E-mandate Framework 2026, read on taxguru's copy, 17 Sep):
- Para 8(a): recurring debits need no PIN "up to ₹15,000/- per transaction". The limit is per debit, and the text has no clause against splitting. The paragraph's heading is "Transaction limits and velocity check", which means issuers are expected to watch how often a mandate is debited.
- Para 4(c): on a variable mandate, the tenant sets the maximum for any one debit.
- Para 6: every debit needs its own notice at least 24 hours before, and she can opt out of any one debit.
- Para 10(c): Cashfree must make sure its merchants comply.

**NPCI** (press report of the 1 Aug 2025 rule): at most one attempt plus three retries "per mandate", and debits only outside peak hours. The report does not say whether the retry budget is per debit or per cycle.

**MDR:** Autopay has no prescribed MDR (FAQ Q22), so splitting changes nothing on MDR. It only matters for the PIN.

**Reading:**
- The text does not forbid it. But the only purpose of the split is to avoid the PIN step RBI set for debits above ₹15,000, and bank velocity checks exist to catch exactly that pattern.
- If Cashfree or a bank treats it as avoiding the rule, the risk is declines, or Cashfree acting on all RentOk mandates, not only the split ones.
- Practical costs:
  - two notices a month;
  - she can opt out of one part, leaving rent part-paid;
  - two debit fees (₹17.70 each), which a ₹49 fee does not cover at today's failure rate;
  - the second debit may fail after the first succeeds;
  - retries may be shared across both debits.

**Recommend:**
- e-NACH as the default for rent above ₹15,000.
- Split debits only after Cashfree confirms in writing that its bank partners and NPCI allow the pattern for rent (added to the Cashfree question list).
- If Cashfree says yes: disclose both debits at setup, collect them on the same day, and keep one notice that names both amounts if the issuer allows it.
