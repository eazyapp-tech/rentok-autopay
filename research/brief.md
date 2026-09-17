# Brief: RentOk Auto Pay push (for every walkthrough)

> The brief the walkthroughs were run from, on 17 Sep morning. Superseded by map/feature-map.md, kept to show what each walkthrough was asked.

Date: 17 Sep 2026. RentOk is an Indian rent-management SaaS (PG, co-living, flats). Managers use a Flutter manager app and a Next.js manager web app; tenants use a Flutter tenant app, web check-in links (rentok.com/checkin), payment links (pay.rentok.com, live page /p and a redesigned page /p2), and WhatsApp. Payments go through Cashfree; the Cashfree page shows the merchant as EAZYAPP (RentOk's company), and RentOk settles money to properties.

## Fixed rulings (do not argue with these)
- CEO target: 70,000 to 75,000 tenants on Auto Pay, e-NACH or virtual account by 1 Oct 2026. Base today: 1,226 active Auto Pay tenants of about 413,000 active tenants; about 1.5 lakh pay rent through RentOk; about 209,000 receive payment links (about 2.87 million links in 30 days).
- Reason: the government's new MDR on UPI merchant payments from 15 Oct 2026: 0.4% above ₹2,000, capped at ₹300. UPI Auto Pay carries no prescribed MDR (Finance Ministry FAQ Q22). Merchants cannot pass MDR to customers (FAQ Q34). GST on MDR is reported at 18%.
- Auto Pay goes live for every property; optional for tenants; pushed hard by RentOk, management and owners.
- The tenant pays Auto Pay charges (setup and monthly) by default; management can switch them to itself. RentOk absorbs nothing. Owners will not absorb costs either; they raise rent instead (₹10,000 becomes ₹10,040).
- RentOk must keep control of the payment flow. Owner-direct payments are rejected.
- Current code and data are today's reality to change, not a limit. Real limits: law and regulation, the ₹15,000 no-PIN limit on UPI Auto Pay for rent, the notice at least 24 hours before each debit, cancel as easy as setup, and the dates.
- Earlier rulings (11 Sep): Auto Pay on by default for every property; default Auto Pay grace 7 days; tenant may pick any day of the month and that day becomes her rent due date for late fines; day change once a month from next month; reminder links stop for tenants on active Auto Pay; Auto Pay offered on the payment page by default; rent only for now.

## What exists today (checked in code, 17 Sep)
- Backend Auto Pay V2: Cashfree on-demand mandate; ₹1 refundable authorisation; one debit per month capped at the approved amount; allowed day = due day to due day + Auto Pay grace (default 0, so most tenants get one day); monthly fee ₹50 default, payer Owner or Tenant (default Tenant); setup fee ₹50 with only RentOk as payer; retries up to 5; cancel exists, no pause; change date exists with no permission check.
- Security: Auto Pay routes need no login (P0, rentok-backend #6816); shared permission check says yes to logged-out callers (#6861).
- Failures: 59% of real rent debits fail, mostly low balance; reasons saved as "Unknown failure" (#6817). 46% of tenants who start setup never finish (eazypg-marketplace #859).
- Setting up Auto Pay overwrites the tenant's grace period, which late fines also use; cancelling empties it, wiping manager-set grace including "late fine off" (1000).
- Eviction and tenant deletion do not cancel Auto Pay. A rent rise above the approved amount is silently capped. Failures reach only a manager note. The notice before each debit is locked to one test record. An older debit engine route is still reachable.
- Web check-in: Auto Pay is step 3 of 5 (after KYC and selfie, before the rental agreement); date picker shows "1st - 1st"; copy says fees are one-time (the monthly fee is monthly); "change the date anytime from settings" is false; terms tick hard-set to accepted; after approval the tenant app opens without a success confirmation.
- Live payment page /p: no Auto Pay. Redesigned /p2: full Auto Pay design, preview only; setup switched off until #6816; not routed.
- Tenant app: Auto Pay banner and profile row never show (status not saved); no prompt; no management.
- Manager Flutter app: settings (on, mandatory, eligible since, fee payers); tenant profile shows set up or not; bulk reminder to a whole property only, whose link lands on check-in step 1 because "autopay=true" is ignored; no single send; no failed state; no cancel or history. Home card "Tenants to set up AutoPay" exists.
- Manager web: settings plus Auto Pay grace field (label wrongly describes late fine); no tenant status, reminders or history.
- WhatsApp: rent reminder links, payment receipts, welcome and rent bot do not mention Auto Pay. Owners get a message per payment that does not say whether Auto Pay paid it.
- Other money features that exist: dues packages and grouped packages; platform fee and gateway fee settable per property and per package (7 Sep); late fine with grace; advance and "adjust from advance"; RentPass cashback; cashless deposit (Eqaro); instant settlement; partial payments with a fixed allocation order; discounts; prepaid electricity; cash with OTP; receipts and invoices; bulk dues reminders; multi-party agreements; eviction and move-out; room change; scheduled rent increase (new); white label; parent app.
- Planned: Release 36 public release 24 Sep (platform fee ₹30, Auto Pay "held ready for MDR"), /p2 switch-on, property onboarding revamp, WhatsApp number split by category, team offsite 24 to 27 Sep.

## Proposals already on the table (17 Sep, not yet ruled)
- Auto Pay service fee: flat, named for the service, billed as its own line with GST, consented; setup fee collected on the first debit rather than at authorisation.
- Link-payment MDR borne by the property through payout deduction (A); optional flat platform fee for all tenants (B); "Auto Pay price" standing discount off a posted rent (D).
- Payment ladder under RentOk control: UPI Auto Pay; e-NACH; RentOk virtual account per tenant (bank transfer); UPI link as fallback; cash with OTP. Also to check: card mandates, BBPS biller, UPI credit.
- Core shift: Auto Pay becomes the way every monthly payment is collected; above ₹15,000 the tenant approves each debit with her PIN; link only as fallback.

## Files with more detail
- /Users/eazypg/Sanchay Personal Projects/rentok/autopay-push/01-mdr-rules-and-surfaces.md
- /Users/eazypg/Sanchay Personal Projects/rentok/autopay-push/02-kamal-recording-and-screens.md
- /Users/eazypg/Sanchay Personal Projects/rentok/autopay-push/03-workflows.md
- /Users/eazypg/Documents/Obsidian Vault/RentOk/NeoSapien Digests/2026-09-17-autopay-reconciliation.md
- /Users/eazypg/Documents/Obsidian Vault/RentOk/NeoSapien Digests/2026-09-17-autopay-code-check.md
- /Users/eazypg/RentOk Marketplace/eazypg-marketplace/.claude/worktrees/rentoke-payment-redesign-ee444b/docs/payment-page-redesign/LEDGER.md
- /Users/eazypg/Sanchay Personal Projects/rentok/autopay-push/sources/2026-09-15-dfs-upi-mdr-faq.txt
