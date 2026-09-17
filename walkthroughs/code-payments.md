# Code findings on the payment path (17 Sep 2026)

From a helper agent under the finance walkthrough (backend origin/master, read-only), with one correction checked by hand.

## addPayment (shared by every payment source, including Autopay)
- `addPayment` (src/controllers/payment.ts 1293) reads `is_autopay` (1334). Its only use is an empty branch at 1576 to 1578; Autopay skips the gateway amount-mismatch check that other online payments run (`checkPaymentStatus`).
- Invoices named in `merge_invoice_ids` are fetched with no status filter (1850 to 1863), unlike the default path, which fetches only unpaid ones (1772 to 1776). If a rent bill is paid by link between scheduling and the Autopay debit, the debit still posts: the leftover becomes a new advance invoice (`createNewAdvanceInvoice`, version 2 branch 2100 to 2124), and the already-paid bill is re-touched (paid date overwritten, attached to a second payment). No "already paid, skip" guard. Reading: a double-processing bug; money becomes credit rather than being refused.
- Partial payments: allocation is due date ascending, amount descending, plus five hardcoded per-property sort overrides (1867 to 1908; services/payment/constants.ts). No check of the property's partial-payment setting before the partial branch (2040).

## Fees
- **Gateway charges exist and tenants pay them on online payments today.** `gateway_charges` comes from the request (payment.ts 1300) and is added to what the tenant pays (payment.ts 241 to 243, 1983); receipts show it as its own line (invoices.ts 583 to 586, 1005 to 1007, 872 to 875). The helper missed this because it searched for "gateway_fee". From 15 Oct, a tenant-paid gateway charge on a UPI payment above ₹2,000 reads as passing MDR to the customer (FAQ Q34). Counsel to review; likely block it on UPI and keep it only where lawful.
- The ₹30 "platform fee" is an allocation rule for one owner account (constants.ts 79 to 80, 113 to 131; used only when the property matches a hardcoded id), from commits 7f7d3ce95 and 96289174b (2 Sep 2026). Not a general fee, not on the Autopay path, no switch.
- Autopay code (autopayV2.ts, autopayV2Helpers.ts) has no fee logic beyond the monthly charge helpers already noted.

## Advance and credit
- "Adjust from Advance" and "Adjust from Deposit" are manual toggles on Record Payment. A property-level auto-adjust setting was only announced (rentokDocsIndex.ts 85, 25 Sep 2025); no code found.
- The Autopay debit never checks the tenant's advance, credit or wallet (no matches in autopayV2.ts, autopayV2Helpers.ts, autopayV2Repository.ts, autopayControllerV2.ts). A tenant whose credit already covers the rent is still debited in full.

## For the map
- Before debiting: re-check the bill is still unpaid and net off credit and advance; skip or reduce the debit.
- The tenant-paid gateway charge on UPI payments after 15 Oct is a compliance item, separate from the Autopay service fee.
