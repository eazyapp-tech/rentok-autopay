# Auto Pay push: workflows, not features (draft, 17 Sep 2026)

> Superseded. Written on 17 Sep before rulings R16 and R46 (two setup options, dues taken in parts). Kept for the reasoning. map/feature-map.md wins where they differ.

Constraints that are real: the MDR rule (no pass-through to tenants, Auto Pay exempt), the ₹15,000 no-PIN limit, a notice before each debit, easy cancel, RentOk keeps payment control, tenant bears charges by default (management can switch), RentOk and owners absorb nothing, 70,000 to 75,000 on Auto Pay by 1 Oct. Current code and data are the starting point, not a limit.

## The core shift

Today the monthly workflow is: rent is raised, a payment link goes out, the tenant pays a one-off UPI payment. From 15 Oct every such payment above ₹2,000 costs 0.4%.

The redesign: **the Auto Pay approval becomes the way RentOk collects every monthly payment.** A one-off link becomes the fallback, not the default.

- Rent up to ₹15,000: collected silently on her day.
- Rent above ₹15,000: still collected through her Auto Pay approval, but her UPI app asks for her PIN each month. For her it feels like paying a link; for RentOk it is an Auto Pay debit, with no MDR and full control. Counsel and Cashfree to confirm the PIN debit on an on-demand mandate is treated as Auto Pay.
- Everything is collected by RentOk and settled to the property by RentOk. Nothing goes owner-direct.

## Workflow 1: getting a tenant onto Auto Pay (every lifecycle moment)

| Moment | What happens | Why it converts |
| --- | --- | --- |
| Booking or token payment | The token is paid through the Auto Pay approval itself (the first debit), not a separate link | Highest intent; she is already paying |
| Web check-in | Auto Pay is the payment step, with her day, the fee line, the next three dates and one approval; mandatory where the property says so | Every new tenant passes through it |
| Every payment she makes by link | One tick on the pay screen, "Pay future rent with Auto Pay", on by default where the property uses Auto Pay | The CRED pattern; she is already in her UPI app |
| After any payment | A sheet: "That was the last time you do this by hand" | Moment of relief (11 Sep design) |
| Rent revision, room change, agreement renewal | The new rent needs a new approval, so the flow asks for it | Natural re-consent moment; fixes rent rising past the approved amount |
| Tenant app open | A full-screen Auto Pay prompt until she sets it up or says not now; status and manage in the app | The app is her home for rent |
| WhatsApp | A setup message with one button that opens the approval directly (no check-in steps in front); WhatsApp Flow form where possible | Where tenants already read rent messages |
| Manager push | Manager app and manager web: list of tenants not on Auto Pay, send to one or many, see who opened and who finished | Managers know their tenants personally |
| Owner or operator decision | Large operators make Auto Pay the rule for their properties | Fastest path to volume: a few accounts hold many tenants |
| Call, human or AI voice | Tenants who opened but did not finish get a call that walks them through it | 46% of starters never finish today |

## Workflow 2: collecting every month (RentOk in control, no MDR)

1. Dues are raised for the month (rent and, optionally, every other due in one approval with a ceiling that covers them).
2. 24 hours before: the notice, with the amount, the day and "keep ₹X in your account".
3. Her day: the debit runs. Silent up to ₹15,000; PIN approval in her UPI app above it.
4. Success: receipt to her, "paid by Auto Pay" to the manager and owner, settled to the property.
5. Small separate dues of ₹2,000 or less (for example an electricity top-up) stay as their own natural payments, which carry no MDR. Rent is never broken up to stay under ₹2,000.

## Workflow 3: when a debit fails (59% today)

1. Balance nudge a day before and on the morning of the debit.
2. Retry on her salary day, not just the next day (her day is chosen around salary; the 11 Sep any-day ruling).
3. If all retries fail: the same day she gets her RentOk virtual account number to pay by bank transfer, and a payment link only as the last option. Both land with RentOk.
4. No late fine while she is inside her Auto Pay window.
5. The manager sees "failed, reason: low balance" and can call.

## Workflow 4: money and incentives (nobody absorbs the cost)

- **Auto Pay service fee**, flat, paid by the tenant by default, switchable to management; billed as its own line with GST.
- **Auto Pay price**: the property posts one rent; Auto Pay tenants get a standing discount. Owners were going to raise rent anyway; this turns it into the adoption reason.
- **RentOk balance**: discounts and cashback land in her RentOk balance and pay her next dues, so every benefit stays inside RentOk's flow.
- **Deposit benefit**: cashless or lower deposits offered only with Auto Pay, because rent risk falls.
- **Owner payout**: rent collected by Auto Pay settles to the owner faster than link payments. Owners see "MDR your tenants' link payments cost you this month" beside "tenants not on Auto Pay".
- **Platform fee**: optional, flat and the same for every payment method.

## Workflow 5: rails RentOk controls, to add or check

| Rail | What it gives | To check |
| --- | --- | --- |
| UPI Auto Pay, on-demand | No MDR; silent to ₹15,000; PIN above | PIN debits treated as Auto Pay |
| e-NACH from bank account | Not UPI; high limits; bank-to-RentOk | Cashfree fee; activation time |
| Card mandates (credit or debit card) | High-rent tenants who want card rewards | Card rules on surcharges; who pays card MDR |
| RentOk virtual account per tenant | Bank transfers land with RentOk and match automatically | UPI into the virtual account still carries MDR; show account number first |
| BBPS biller (RentOk as the biller) | Tenants pay or set Auto Pay for rent inside PhonePe or GPay "bill pay", with the bill fetched from RentOk | Whether rent or housing fits a BBPS category; fees; the team has wanted BBPS for three years (16 Sep call) |
| UPI credit (RuPay credit card or credit line on UPI) | Pay rent on credit inside the UPI app | Charges fall under card rules |

## Rejected, with reasons

- Owner-direct UPI or bank payments: RentOk loses control (Sanchay, 17 Sep).
- Splitting rent into pieces of ₹2,000 or less: looks like structuring.
- Charging tenants any fee named or sized like MDR: banned (FAQ Q34).
