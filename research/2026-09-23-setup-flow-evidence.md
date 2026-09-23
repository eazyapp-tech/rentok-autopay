# The autopay setup flow: what the evidence says before it is designed (23 Sep 2026)

Sanchay proposed splitting the setup sheet into steps: why, what it pays, the day, a review of every
term, then approval through our own payment-mode screen. Before building it, three things were
checked: where tenants actually drop today, how the best products do this exact flow, and whether
approval on our own screen works from a phone browser.

## 1. Where tenants drop today: at the bank step

The `autopay` table, all time (Metabase, database 2, 23 Sep):

| Status | Tenants | Rows | Last 60 days (rows) |
| --- | --- | --- | --- |
| initialized (reached the bank step, never approved) | 1,369 | 3,657 | 449 |
| active | 1,280 | 1,308 | 318 |
| customer_cancelled (approved, then cancelled in the UPI app) | 437 | 448 | 2 |
| cancelled | 162 | 171 | 0 |
| bank_approval_pending | 78 | 120 | 32 |
| customer_paused | 66 | 66 | 0 |
| link_expired | 6 | 9 | 0 |

**More tenants stall at the bank step than get through it**, and each stalled tenant tried about
2.7 times. That step is Cashfree's hosted page today. The steps before it (what it pays, the day,
the review) happen before a row exists, so this table cannot see drop-off there. The design effort
therefore goes first to the approval and to what she sees after it.

## 2. How the best products do it

Read on Mobbin, 23 Sep, iOS.

- **Apple Wallet, setting up Apple Card autopay** ([flow](https://mobbin.com/flows/f9571d52-cc73-41a9-901a-f00a9668e128)).
  Amount first (monthly balance, minimum, other), each choice with a one-line consequence ("stop or
  avoid new interest charges"). Then the date. Then a compact sheet: bank, "repeats once a month,
  from 28 Feb", change bank account, confirmed with Face ID. **No benefits screen**: the reason sits
  on the card before she starts. **No agreement tick**: authentication is the consent.
- **ANZ Plus, "Ready to pay?"** ([flow](https://mobbin.com/flows/58ae4fb9-9382-4ea8-a2c6-5bae06c192dc)).
  Payee, amount, from-account, then a three-part strip, "Pay on · Recurs · Ends", with one Edit link.
  One full-width button at the foot.
- **Cash App, "Review your plan"** ([screen](https://mobbin.com/screens/c8ddc72e-ce0b-40b9-978c-89c71fb89337)).
  Plan and price with "cancel anytime in the app", **due today** as its own line, payment method,
  next payment. Above the button that carries the amount: by tapping, you authorise us to charge
  on each due date **and to retry failed payments on days 1, 3 and 5**. No tick.
- **Cash App auto reload** ([flow](https://mobbin.com/flows/f87028e9-6820-49b9-8cbf-dc3f525f3ecc)).
  The date as a short horizontal row of day cards, not a month grid.
- **Klarna** ([screen](https://mobbin.com/screens/129a0cc2-758b-4e61-8246-0f70bc2922f3)) and **Meta
  Quest** ([screen](https://mobbin.com/screens/d9f3c37c-8fd1-417a-a5e7-e7adcae6599d)). "From today,
  per month" separate from "due today", and consent written beside the button.
- **N26** ([screen](https://mobbin.com/screens/d5e2fdfd-c697-464a-bbeb-ed118f21586d)). "Fee: €0 ·
  Free" as its own row, and "you can cancel your plan at any time" above Confirm.
- **What not to copy.** foodpanda greys out Confirm until an agreement box is ticked
  ([screen](https://mobbin.com/screens/2e1fc9d9-e70a-4654-a60c-1787455ccede)); Shopee's agreement box
  arrives **already ticked** ([screen](https://mobbin.com/screens/355503df-4a10-4c3e-b4a4-08e6851d7178)),
  which is the pattern our legal notes record CCPA fining in 2026.

CRED, from Kamal's recording of 17 Sep (`research/kamal-recording-and-screens.md`): autopay as an
unticked row on its pay sheet, "cancel, pause and edit anytime", a 15-question FAQ, and bills above
the mandate limit split automatically.

## 3. Approval on our own screen works on both phones

Cashfree's `POST /pg/subscriptions/pay` with `payment_type: "AUTH"` and `upi.channel: "link"`
returns ready app links (Context7, `/websites/cashfree`, 23 Sep):

- **Android:** GPay, PhonePe, Paytm, BHIM, Amazon Pay, and a `DEFAULT` `upi://mandate` link that
  opens the phone's own app chooser.
- **iPhone:** GPay (`tez://`), PhonePe, Paytm and BHIM. **No Amazon Pay and no "any UPI app"
  option**, because iOS has no system chooser for UPI.
- **A web page cannot list the apps she has installed.** Cashfree's guidance is to show the common
  ones. So the screen shows a fixed set and needs a way out when her app is not there: a QR code
  (`channel: "qrcode"`) to scan from another phone, or the bank-account mandate.
- The same response carries the payee name her app will show (`pn`) and the mandate's end date
  (`validityend`). **The review screen must print those exact values**, not its own copy of them.

## What this changes in the proposal

1. The approval and its outcome get the most craft, because that is where the measured loss is.
2. The "why" lives on the way in (the card and the moment, with her own numbers), not as a screen
   she must tap through.
3. The day is a short row of only the days she may pick (at most eight under R41), not a 31-day grid
   with most of it greyed.
4. Each option says its consequence in one line.
5. The review is a compact ledger with one Edit link; "due today" is its own line; the autopay fee
   shows as ₹0; retries are stated beside the button; the button is the consent, with no tick.

Checked against rulings R1 to R70.
