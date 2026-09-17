# Walkthrough: managers, owners, RentOk customer success (17 Sep 2026)

Agent walkthrough (opus), from the brief, files 01 to 03, Kamal's plan, the payment page ledger, the vault notes, and read-only code checks. Kept close to the agent's words; "Auto Pay" should read "Autopay" in the map.

## Code checks added by this walk (read-only, 17 Sep)
- Team permissions: about 90 keys in rentok-backend `src/services/teamMember/teamMember.ts`; none for Autopay. Closest: "View Dues, Collection & Send Reminders".
- Reports: no backend report mentions Autopay. Flutter dues list has a "Paid via Autopay" filter; tenant filter is Enabled or Disabled only.
- No dispute or chargeback handling in the Autopay service; no link to room change (searched, not found).
- Manager web has a bulk WhatsApp campaign permission (`wa_dashboard_campaign`), a home for a bulk Autopay send.

## Timeline pressure
- 17 to 23 Sep: fixes must land, starting with #6816.
- 24 Sep: Release 36; team offsite 24 to 27 Sep.
- 28 to 30 Sep: last setups before October rent; first big wave of 24-hour notices (today locked to one test record).
- 1 to 5 Oct: first big debit wave (59% fail today).
- 15 Oct: MDR on links. Late Oct: first MDR payout deductions; owners raise rent for November.

Scale: about 5,300 approvals a day; at 46% drop-off about 130,000 must start, roughly 2 of every 3 link recipients. Needs Autopay where tenants already pay (about 95,000 links a day) and large operators making it their rule. The CEO should see this math this week.

## M1 Manager, one 60-bed PG, Flutter app
- Learns: generic "Tenants to set up AutoPay" card. Fix: card in his numbers ("540 links last month; 38 tenants can stop getting them"); MDR explained as the owner's cost.
- Turns on: off by default in code (ruling says on); Flutter fallback payer RentOk; setup fee payer RentOk only; no grace field in Flutter. Fix: RentOk switches on centrally and tells him; sheet previews what the tenant sees; payer Tenant (default) or Property for both fees; grace field "Days after the rent date when Autopay can collect". Needs a switch-on script and backend setup-fee payer options.
- Bulk push: whole property only; link lands on check-in step 1. Fix: standalone one-screen Autopay link (day, amount, fee, next 3 dates, bank); bulk sheet with tick boxes and filters (not on Autopay, never opened, late last month). After #6816.
- One by one: no single send. Fix: "Send Autopay link" on tenant profile and dues row; "Show QR" for her phone.
- Tracks: Enabled or Disabled only. Fix: states per tenant: not sent, sent, opened, started not finished, active, failed; tap to call or WhatsApp.
- Refusals: not recorded. Fix: "Not now" asks why (auto-debit trust, salary timing, above ₹15,000, prefers cash); reason and reply script for the manager; one FAQ page (CRED's eight questions); "cash by choice" mark ends the chase.
- Failures: manager note only, "Unknown failure", tenant not told, 5 retries vs 1+3. Fix: real reason alert; tenant "keep ₹X ready", then virtual account and "Pay now"; no fine inside window; at most 3 retries aimed at salary day.
- Reconciles: dues row should read "Scheduled on Autopay for the 5th", not overdue; recording cash or a link payment within 24 hours of a scheduled debit warns and skips the debit (#6828, #6830).
- Rent, room, move-out: silent cap; no cancel on eviction or delete; cancel wipes grace incl. 1000. Fix: auto-cancel with tenant message; re-approval link before the first debit at a new rent; split grace (#6817 option A).
- Disputes: "Report a wrong debit" on the receipt opens a complaint with debit details; refund via existing refund permission.

## M2 Regional manager, 40 properties, 1,800 tenants, manager web, 15 managers
- Learns: portfolio sheet (1,800 tenants at about ₹12,000 assumed is roughly ₹1 lakh a month of link MDR with GST from 15 Oct).
- Turns on: per property only; web grace label describes late fine; web sends "RentOk pays" as a code backend reads as tenant (#6880). Fix: account-level Autopay settings with per-property override; fix #6880 first.
- Team: no Autopay permissions; change date unchecked; no-login routes (#6816, #6861). Fix: permission keys (table below); activity log of every Autopay action.
- Bulk push: web has no status, reminders, history; bulk WhatsApp has no Autopay template. Fix: status column, filter, cross-property send, campaign template.
- Tracks: Autopay board by property and manager: eligible, sent, opened, started, active, failed, % on Autopay, daily line to 1 Oct, export.
- Refusals rolled up per property; where "above ₹15,000" dominates, move to e-NACH (not built).
- Failures: failed-debit queue assigned to the property's manager, with reason, next retry and fallback status; 9 am digest.
- Reconciles: payment-method column in collection and settlement reports (Autopay, link, transfer, cash), Autopay fee lines, and from 15 Oct MDR deducted per link payment.
- Rent changes: scheduled rent increase says "112 tenants must re-approve Autopay" and sends it.
- Reports up: weekly one-page PDF for the founder.

## O1 Owner, 3 small PGs, WhatsApp only
- Learns: one WhatsApp before 25 Sep in his language with his own rupee figure: link rent costs you 0.4% from 15 Oct, Autopay costs you nothing. Needs Meta template approval (1 to 2 days) and the owner-category number.
- Decides from WhatsApp: buttons "Tenant pays the Autopay fee (recommended)" or "My property pays"; "Require Autopay for new tenants".
- Pushes: "Remind my tenants not on Autopay", sent in the property's name.
- Tracks: weekly "PG 1: 22 of 30 on Autopay (up 8). The 8 on links cost you ₹310 in October."
- Payouts: "Paid by Autopay" on payment messages; monthly statement with payment mix and MDR deducted; the 15 Oct owner sheet before the first deduction.
- Rent raise: offer "Autopay price" as a one-tap option (post ₹10,040, Autopay tenants pay ₹10,000), applied via scheduled rent increase with automatic re-approvals. Counsel on FAQ Q34.
- Risk: cash or personal UPI are free for him. Make RentOk's path the cheapest and the one with records.

## O2 Enterprise operator founder, white label
- 30-minute review with customer success: MDR exposure, links per tenant, late fines (platform-wide about 5% of ₹7.8 crore raised is paid), fee vs MDR.
- Policy: required at check-in for new tenants (283 properties use "mandatory"); track UPI-app cancellations.
- Fee payer: at ₹50 a month the fee exceeds link MDR on ₹10,000 (about ₹47), so an operator will not take it on. The agent proposes a fee near cost (about ₹20; Cashfree about ₹17.7 with GST), so operators paying it save about ₹27 a tenant a month. Needs a fee ruling.
- Brand: Cashfree page and UPI-app mandate list say EAZYAPP; white-label app shows no Autopay; messages from RentOk. Fix: "[Brand] Autopay, collected securely by RentOk (shown as EAZYAPP by your bank)"; ask Cashfree about per-brand display name; brand templates.
- Collections: debit success by property, bank and day; salary-day choice, balance nudge, virtual account fallback, e-NACH above ₹15,000; setup link to the parent who pays.
- Costs: monthly statement of link MDR, Autopay fees and payer, platform fee, MDR avoided.
- Control: permissions and exportable activity log. Disputes: written process with response time.

## S1 RentOk customer success, hundreds of accounts in 13 days
- Pick accounts by tenants receiving links (209,000 across 8,902 properties); measure concentration.
- Daily account tracker; admin bulk switch-on script with dry run and opt-out log.
- RentOk-side bulk send per account with the manager told first, only after #6816.
- Meta templates submitted by 19 to 20 Sep: owner explainer, tenant setup, 24-hour notice, success, failure.
- Daily call list of opened-not-finished tenants (human or AI voice); scripts and FAQ in Hindi and regional languages.
- On-call roster for the offsite and 1 to 5 Oct; failure-spike playbook; per-property kill switch (none exists).
- After 15 Oct: deduction questions, rent-raise requests, owner MDR sheet.
- Capacity estimate: 12 to 15 account calls a person a day; only top accounts get a human.

## What makes managers push
- Time saved in their own numbers (median tenant 9 links a month, p90 30).
- Leaderboard per manager; owner sees each property's rate weekly.
- Per-property targets and a daily line.
- Incentives: credits in RentOk products per activated tenant and recognition. Conflicts with R3 (RentOk absorbs nothing) unless funded otherwise; needs a ruling.
- One-tap tools: single send, QR, selected bulk send.

## What owners will do about link MDR
- Raise rent: approvals set at today's rent will be silently capped at the November rent. Fix: approve with headroom (for example rent plus 25%, at or under ₹15,000 where rent allows) and re-approve on rises.
- Push tenants to cash or personal UPI: make RentOk's Autopay the cheapest path.
- Add a link "convenience fee": banned. The existing per-property gateway fee charged to tenants on UPI link payments looks like MDR pass-through from 15 Oct; counsel, and probably block it on UPI payments.

## Permissions (none exist today)

| Action | Who | Guard |
| --- | --- | --- |
| See Autopay status and board | Anyone with "view tenants" | |
| Send setup link, single or bulk | Managers with "send reminders" | Frequency cap per tenant |
| Change a tenant's debit date | Property manager, at the tenant's request | Once a month, from next month; tenant told; logged |
| Cancel a mandate | Admin only; automatic at move-out or delete | Tenant told; reason; logged |
| Switch fee payer, on or off, mandatory, grace | Account owner or admin | Next cycle; switching fee to tenant raises the debit and needs re-approval; tenants told |
| Autopay reports and export | New "Autopay report" key | |

All behind #6816 and #6861.

## 15 problems ranked by impact on 70,000 by 1 Oct
1. No-login Autopay routes (#6816, #6861).
2. No Autopay where tenants already pay (/p, /p2 not routed, reminder messages).
3. Setup link lands on check-in step 1.
4. Large operators not activated (account-level settings, required for new tenants, customer success campaign).
5. No reason for tenants to switch (₹50 vs free link); fee near cost and Autopay price.
6. Managers cannot target or track (states, single send, QR, bulk select, web parity, board, permissions).
7. 46% of starters drop off (call list, resume link, screen text fixes).
8. One allowed day (grace default 0; set 7; split grace; any-day later).
9. Owners see nothing (weekly WhatsApp, "Paid by Autopay", 15 Oct sheet).
10. 24-hour notice locked to a test record; unlock before 28 Sep.
11. 59% failures, no reason, no tenant message.
12. Fee payer bugs (setup payer RentOk only; #6880; Flutter fallback RentOk).
13. Approved amount equals today's rent; approve with headroom.
14. Move-out and delete keep Autopay; cancel wipes grace.
15. Tenant-paid gateway fee on UPI links after 15 Oct, and owners moving tenants off RentOk.

## Open questions raised
- What counts toward 70,000 (answered: R8, approved mandates).
- The service fee level (operators take it on only below link MDR).
