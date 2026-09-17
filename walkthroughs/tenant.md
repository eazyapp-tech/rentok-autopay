# Walkthrough: eight tenants (17 Sep 2026)

Agent walkthrough (opus), from the brief and files 01 to 03, the two vault notes and the /p2 design ledger. Kept close to the agent's words; "Auto Pay" should read "Autopay" (the product's word) when this enters the map. Items marked (check) are general knowledge, not verified.

## T1 New PG tenant, ₹9,000, salary on the 7th, Android, new to UPI, booked by WhatsApp link

| Step | Today | Fix | Depends on | If missing |
| --- | --- | --- | --- | --- |
| Hears of it | Booking page never mentions Autopay | Line on token success: rent can be taken on your salary day; set up at check-in | Booking page | First mention comes behind KYC, when tired |
| Decides | Step 3 after repeated KYC and selfie errors; "1st - 1st"; fee "one-time" though monthly; "change anytime" false | Ask "when does your salary come?", open on the 8th; fee line "₹X every month, on every receipt"; next three dates; short voice explainer in her language | #6829 any-day with late-fine exemption; #6817 grace split; counsel wording | Picks the 1st, fails monthly, gets fined |
| Sets up | "Schedule Rent Payment"; terms tick forced; consent before agreement | "Set up Autopay"; real unticked terms; clause in agreement | Counsel terms; step order | Challengeable consent; cancels later |
| Confirms | UPI app shows EAZYAPP and ₹1, unexplained | Pre-handoff screen: EAZYAPP is RentOk's company; ₹1 returned; PIN once | Cashfree display name including RentOk | Drop-out (46% of starters) |
| After approval | App opens; no success; app never shows status | Success screen (day, next 3 dates, fee, where to cancel); WhatsApp confirmation; app status card | Save status in tenant app; template | Repeat attempts (one tried 38 times) |
| First debit | Notice locked to a test record | Notice: "₹9,050 on 8 Oct: rent ₹9,000 + Autopay fee. Keep it in your account." | Remove test filter; Cashfree trigger | Breaks the notice rule; debit at risk |
| Each month | Reminder links still arrive; receipt silent | Stop links while active (#6830); receipt "Paid by Autopay" with fee line and GST | #6830; receipt template | Pays twice, disputes |
| Rent change | Scheduled rise capped silently; rest unpaid, fined | Approve "up to" a ceiling with headroom; re-approve prompt before a rise above it | Cashfree ceiling rules; scheduled rent increase hook | Surprise fines for trusting tenants |
| Room change | Same silent cap | Room change triggers re-approve | Room change flow | Same |
| Failure | Only manager note; "Unknown failure"; 5 retries vs rule 1+3 | WhatsApp: couldn't collect, retry on 9th and 10th, or pay by bank transfer; no fine inside window | #6817; virtual account | Fine before she knows |
| Cancel or pause | No pause, no app entry; cancel wipes grace | Profile > Autopay: change day, skip a month, cancel; two taps; says fines apply again | Pause; login check (#6816) | Breaks cancel parity; she blocks in UPI app |
| Dispute | No path | "Report a problem" on receipt; refund in stated days | Support promise; Cashfree refund | Chargebacks |

## T2 Existing tenant, 14 months, ₹12,000, pays by link, never opened the app

- Bulk link lands on check-in step 1 (KYC again); live /p has no Autopay. Fix: direct one-screen setup link; single-tenant send; tick "Pay future rent with Autopay" on the pay screen, on by default. This pool (about 209,000 link recipients) is the only one big enough.
- Pays on about the 5th (median). Fix: pre-fill her usual day from receipts; reason on the tick: no more reminder links, never a late fine.
- Links keep coming until #6830. Her main reason disappears without it.
- After 15 Oct a link costs her ₹0; Autopay ₹50 a month. Fix: Autopay price discount larger than the fee, shown as "you save ₹X a month" (needs Q4 ruling and counsel).

## T3 Flat tenant, ₹28,000, iPhone, pays on the 1st

- Above ₹15,000 she enters a PIN monthly; code has no ₹15,000 rule. Fix: say it plainly; offer e-NACH first (silent, 1 to 5 days to activate); PIN-approved debit as second option (Cashfree and counsel to confirm it counts as Autopay). Without it, the owner pays about ₹132 a month in link MDR.
- iPhone handoff weaker (check). Fix: UPI app chooser plus net banking for e-NACH; test on iPhone.
- Unapproved PIN request counts as failure. Fix: WhatsApp nudge when sent, retry next morning, then bank transfer.

## T4 Often low on the debit day, irregular salary

- Fears bounce charges; e-NACH bounces usually carry bank charges, UPI Autopay usually not (check). Fix: UPI Autopay only for her; copy "if money is short, nothing is charged; we try again" (legal check).
- One fixed day; up to 5 retries at Cashfree ₹15 + GST each (about ₹106 for six). Fix: "Pay now with Autopay" button when money arrives; balance nudges; retries spread in window. Who pays for failed attempts is unruled.
- All retries fail, not told. Fix: same-day bank transfer account and link; fine only after final retry plus stated grace; manager sees "Failed: low balance".
- Fix: "skip this month" (pause).

## T5 Student whose parent pays

- Step 3 expects the student's own UPI. Fix: "ask someone to set this up" sends the approval to the parent (WhatsApp or parent app); step shows "waiting for parent" without blocking check-in. Cashfree payer-not-tenant (check); consent from the parent.
- Parent sees EAZYAPP. Fix: message names student, property and EAZYAPP.
- Notices and receipts go to the parent, copy to the student; payer contact stored separately.
- Move-out: parent's mandate keeps running. Fix: auto-cancel and tell the parent.

## T6 Co-tenant, rent split three ways

- One invoice to the lead tenant (₹28,000) means a PIN each month and the lead fronts all. Fix: per-share dues under the multi-party agreement; each sets up their own Autopay under ₹15,000 (counsel: real separate payers is not structuring).
- Fee per person (₹150 for one flat). Fix: state per person or split one fee.
- One share fails. Fix: per-share status and fines; tell only the one who failed.
- Flatmate leaves: re-split and re-approve.
- Growth: "invite flatmates" with a credit to her RentOk balance.

## T7 Moves out mid-month

- Notice months: part-month amount shown in the notice.
- Final bill: debit only the net after deposit and advance adjustments, only after she sees it; no debit if covered.
- Move-out does not cancel Autopay; setup says "until eviction". Fix: auto-cancel on confirmed move-out, message "Autopay stopped"; wording "until you move out". The worst trust breaker.
- Refund tracker; wrong-debit refund in stated days.

## T8 White-label property

- Payment page drops brand name. Fix: brand, then property, on every Autopay screen and message.
- EAZYAPP on a monthly permission looks like fraud. Fix: "[Brand] collects rent through EAZYAPP (RentOk)" before handoff, in notices and receipts. Check per-operator display name and merchant of record.
- Show "Paid by [Brand]" when the operator takes the fee.
- Operator-wide "Autopay compulsory at check-in" setting: fastest route to volume.

## As a tenant

- Yes because: no fines (16.7% of link payers fined in 90 days, median ₹600), my salary day, reminder links stop, and only if it is visibly cheaper.
- Stops me: ₹50 monthly fee vs ₹0 link; EAZYAPP; unexplained ₹1; KYC again; one-day window; PIN monthly above ₹15,000; bounce-charge fear.
- Cancel because: debit after move-out; double charge; fine while on Autopay; surprise amount; fee not on receipt; wrong day; no skip.
- Tell flatmates because: "saved ₹X, zero fines" on receipts; invite credit; one-tap setup from WhatsApp.

## 15 cross-cutting problems, ranked (target first, then trust)

1. Existing tenants have no one-tap setup path.
2. Autopay costs the tenant more than a link (₹50 vs ₹0); fix with an Autopay price discount larger than the fee, fee near cost.
3. No-login Autopay routes (#6816, #6861).
4. One allowed day, not tied to salary; fix with salary question, any-day plus late-fine exemption, grace split.
5. 59% failures and tenant never told.
6. Notice before each debit locked to a test record (legal requirement).
7. Move-out and deletion do not cancel Autopay.
8. EAZYAPP breaks trust at approval (worst for white label and parents).
9. Weak consent (forced tick, wrong fee wording, false "change anytime", button text, order).
10. Rent rises silently capped, then fined.
11. Cancel not as easy as setup (no app status, pause, change day).
12. Setup and cancel overwrite late-fine grace including 1000.
13. Above ₹15,000 not built (no e-NACH, no PIN path).
14. Who pays for failed attempts unruled.
15. Shared payers (parents, co-tenants) not modelled.

Under all: say Autopay covers rent only (41.5% owe more than one due type); receipts and owner messages say "Paid by Autopay".

To check with Cashfree and counsel: non-tenant payer; per-operator display name; PIN debit above ₹15,000 as Autopay; early debit on "pay now"; token as first debit given the 24-hour notice.
