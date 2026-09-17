# Who covers payment costs, and the rent change workflow (17 Sep 2026)

> Superseded in part: written before rulings R35 (the platform fee is the property's charge, not RentOk's) and R46 (two options; limit equals regular dues, no buffer). AUTOPAY-feature-map.md wins where they differ.

This note starts from ruling R11 and Sanchay's follow-up on 17 Sep:
- Owners get a choice of both routes.
- The setup cost must stop falling on RentOk.
- Managers need a bulk way to change rent.
- Editing an agreement makes it unsigned and sends it back to every party for signing.

## What the code does today (checked 17 Sep, backend origin/master, apps origin/main)

- **No bulk rent change for managers.**
  - `src/scripts/changeBulkRent.ts` is a one-off script with no route.
  - The tenant bulk import in manager web adds new tenants only.
  - The only bulk repricing is a side effect: editing a property package reprices tenants already on it (#6989, filed as a bug).
- **Single rent edit** (`POST /tenant/editTenantByUuid`, `tenant.ts:19881`) writes the new rent at once. It touches nothing else: no agreement change, no notice, no Autopay limit check. It needs the `edit_tenants_rental_details` permission.
- **Rent rise at renewal** (`agreementRenewal.ts:191-317`) first marks the agreement unsigned (action 2), then raises rent. Its invoice and activity-log lines are commented out (`:320-340`), so the tenant is not told.
- **Scheduled 2.5% rise** (`scheduledRentIncrease.ts`) is hard-coded to one account. It writes the new rent without any notice.
- **Agreement edit** (`POST /tenant/editTenantAgreement`, `tenant.ts:11539`) is one tenant at a time. It archives the signed copy, clears the agreement, and sends WhatsApp `agreement_edited` to the tenant and `agreement_edited_owner` to the owner. It does not change the terms itself.
- **Party re-issue** (`agreementParties.ts:318`) opens a new signing round for everyone.
- **The signing-only page** (`marketplace pages/esign/[shortId].js`) has no Autopay step. The full check-in page does (`pages/checkin/[checkinId].js:92-150`).
- **The ₹30 platform fee** is a recurring due type set on the property. It is billed under the property's name, not RentOk's. It is switched on by one hard-coded account ID (`constants.ts:81`), and there is no per-account setting.

## The setting: "Who covers payment costs" (property, with an account default)

Here, "costs" means three things:
- RentOk's Autopay setup and monthly fee;
- from 15 Oct, UPI charges on link payments;
- gateway charges.

RentOk never absorbs any of them. There are three choices:

1. **Management.** Taken from the payout, with a monthly RentOk tax invoice. This includes the setup fee, charged on the first successful debit.
2. **Tenants, through a RentOk platform fee.**
   - One flat monthly amount, the same for cash, link, bank transfer and Autopay.
   - Invoiced by RentOk under RentOk's GSTIN. Today's build bills it under the property, so that has to change.
   - Shown at check-in and in the agreement.
   - Collected inside the Autopay debit as well, which is lawful because it is not a charge for Autopay.
3. **Tenants, through rent.** The manager uses the rent change workflow below. The tenant sees one rent and no cost line.

**Until the start date, management pays.** From the start date the tenant side applies to every tenant, signed or not (ruled 17 Sep), once notice has been delivered.

## Rent change workflow (bulk, also used for one tenant)

1. **Choose.** Pick a property or properties and a set of tenants. The change is +₹, +% or a new amount. Also set the start date and a tenant-facing reason.
   - Guard: tenants cannot be picked by payment method. A rise only for link payers reads as passing on the UPI charge. A rise only for Autopay tenants reads as a charge for Autopay.
   - Guard: the reason cannot mention Autopay, UPI or payment charges.
2. **Preview.** Show each tenant's old and new rent, and flag these cases:
   - tenants whose Autopay limit is below the new rent;
   - tenants crossing ₹15,000, who then approve each debit with a PIN;
   - tenants crossing the ₹20,000 GST line;
   - tenants on the seven accounts with a ₹20,000 online cap;
   - tenants leaving or on notice before the start date (left out);
   - tenants whose agreement ends before the start date (handled at renewal);
   - tenants with another rent change already pending.
3. **Schedule.** Save a pending change. Rent is written only on the start date, so invoices for the current month stay as they are. Today's edit writes rent at once.
4. **Agreement.** Produce the updated agreement and open a new signing round for every party (tenant, co-tenants, parents, owner). This is a bulk version of the agreement edit plus party re-issue.
5. **One tenant visit** (a link on WhatsApp and in the tenant app):
   - She sees "Your rent changes from ₹X to ₹Y from 1 Nov".
   - She signs.
   - Then comes the Autopay step. If she is on Autopay and her limit is too low, she approves a higher limit. If she is not on Autopay, she is offered it with "no extra charge for Autopay".
   - **Every rent change becomes an Autopay sign-up moment.** The signing-only page needs the Autopay step added.
6. **Reminders and status.**
   - Reminders go out on day 0, day 3 and day 7.
   - The manager and owner see "N of M signed", who is pending, and who refused.
   - A refusal leads to the notice or move-out flow.
7. **Start date.** New rent applies to every tenant in the change, signed or not (ruled 17 Sep). Guard: the start date cannot be earlier than the notice delivered plus the agreement's notice period.
8. **Autopay.**
   - The notice before each debit shows the new amount.
   - If a debit is above her limit, prompt her to re-approve, and do not cut the debit short silently (see #7000).
   - New approvals get headroom above rent.
9. **Collisions** handled by the same pending-change record:
   - the renewal rise, which should get its tenant notice back;
   - the one-account 2.5% rise;
   - room change;
   - package edits (#6989).
10. **Audit.** Record who changed what and when, plus the reason and the signed copy.

## Setup cost

Today RentOk pays about ₹8.85 per mandate (setup payer is RentOk only, `property.ts:9274-9282`). The new rule:
- If management covers costs, charge the setup fee to management on the first successful debit.
- If tenants cover costs, the platform fee or the rent covers it.

Failed debit attempts may also be billed by Cashfree (about ₹17.70 each). Confirm with Cashfree, and price the management fee to cover them.

## Open questions

- Ruled 17 Sep: the new rent or fee starts on the start date for everyone, signed or not. Guardrails: notice delivered and recorded first; start date no earlier than the agreement's notice period; the tenant may decline by giving notice before it starts; the signing round still runs, for the record and the Autopay step.
- Ruled 17 Sep: default is tenant side through the RentOk platform fee.
- Ruled 17 Sep: ₹49 plus GST, covers Autopay costs; link UPI charges stay with management; replaces FNF's ₹30.

## Sizing the platform fee (Metabase, 17 Sep 2026)

Tenants with status 1 and rent above 0: 348,071. I assumed status 1 means active; that is not verified.
- Rent at the 25th percentile is ₹5,700, the median is ₹8,250, the 75th percentile is ₹13,000 and the 90th is ₹18,250.
- By band:
  - ₹2,000 or less: 3.9%
  - ₹2,001 to ₹10,000: 59.6%
  - ₹10,001 to ₹15,000: 20.6%
  - ₹15,001 to ₹25,000: 10.7%
  - above ₹25,000: 5.2%

Cost per tenant per month, GST included:
- A UPI link payment costs ₹38.94 at the median rent, ₹61.36 at the 75th percentile and ₹86.14 at the 90th.
- An Autopay debit costs ₹17.70 per attempt, which is about ₹42.50 at today's 2.4 attempts per success and about ₹26.55 at 1.5 attempts. The setup costs ₹8.85 once.

Autopay's cost does not grow with rent, but a link payment's does. So a flat fee can cover Autopay for every tenant, but it cannot cover link charges on higher rents.

Recommendation:
- A flat ₹49 plus GST covers Autopay costs, and RentOk keeps a margin even at today's failure rate.
- Link UPI charges stay with management and come out of the payout. That also keeps the owner's reason to push Autopay.

## Rent above ₹15,000 (ruled 17 Sep, R16)

- **The mandate:** one on-demand UPI Autopay mandate with a ₹15,000 limit. The number of parts is the rent divided by ₹15,000, rounded up: ₹20,000 is 2 debits, ₹40,000 is 3, ₹50,000 is 4.
- **Setup:** she sees "Your rent of ₹20,000 will be taken in 2 parts, ₹15,000 and ₹5,000, on your day" and approves once.
- **e-NACH:** only as a short FAQ answer ("Prefer your bank account? Set up e-NACH").
- **Design points that follow:**
  - Take both parts on the same day, in the allowed time windows.
  - Send one notice per part.
  - If one part fails, retry only that part, and never mark the rent paid until every part is in.
  - If she opts out of one part, the rest becomes a link for the balance only.
  - The preview in the rent change flow flags a new part count.
  - Receipts show one rent payment, made in parts.
- **Cost:** each part is a separate Cashfree debit fee (₹17.70). Ruled 17 Sep (R17): the fee stays ₹49 plus GST for everyone. Margin is checked on the whole tenant base, where cash and link payers pay ₹49 with no debit cost. Track it monthly in the fee-versus-Cashfree-cost report.
