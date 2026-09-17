# Kamal's recording and screenshots (17 Sep 2026)

Source: `~/Downloads/WhatsApp Video 2026-09-17 at 6.19.41 PM.mp4` (4 min 23 s, screen recording with sound) and two screenshots of the web check-in Auto Pay step. Read as 66 scene frames. The sound was not transcribed. The recording shows a personal card and bank accounts, so frames are not published anywhere.

## What the recording shows, in order

1. **Web check-in, a real phone (Kamal Test, ₹12,000 rent):** KYC with an Aadhaar upload; the "Please complete your KYC" and "Selfie required" errors show several times; a live selfie; the guardian and food preference form; then Setup Payment (step 3 of 5).
2. **Setup Payment:** Autopay details, then the date sheet, then "Schedule Rent Payment". Cashfree's page shows the merchant as **EAZYAPP**, ₹1, and UPI or Bank Account.
3. **After approval:** the phone opens the Smart Tenant App (notification permission prompt, then home). No success screen for Auto Pay is seen.
4. **Tenant app:** home (Total dues ₹79,755, Express Check-in banner, menu, profile status: KYC, selfie, police verification), Pay Now (GPay, PhonePe, Paytm, RentPass cashback), profile and "My Renting Info". **Auto Pay appears nowhere:** not on home, not on dues, not at payment, not in profile.
5. **CRED, as the benchmark (credit card bill):**
   - Bill payment screen: pay total due, minimum due or another amount.
   - An FAQ page: what if payment fails; notified before and after; not enough balance; cancel or edit anytime; change bank account; set a cap; only specific billers; bill higher than the mandate limit.
   - The CRED Pay sheet: recommended bank accounts over UPI with "new enhanced limit"; a row "**pay future bills with autopay** · cancel, pause & edit anytime · know more" with a tick box, **unticked by default**; ticking it keeps the same "Pay now" button.

## What the RentOk screens get wrong (each checked against code)

| Screen detail | Problem | Why, in code |
| --- | --- | --- |
| "Choose a date between 1st - 1st", only the 1st selectable | Looks broken; no choice | Backend window is due day to due day + Auto Pay grace, grace defaults to 0 (autopayV2Helpers.ts 38 to 69) |
| Details say "Starting from 17 Sep'26"; the date sheet says "Starting from 1st October 2026" | Two different start dates on one screen | Details use the valid-from date; the sheet uses the next chosen day |
| "Autopay Fee ₹50 ₹0/one-time" | The backend fee is monthly, not one-time | autopay_monthly_charge is added to every monthly debit |
| Both fees struck to ₹0 | Reads as a temporary offer | The fee payer on this property is not the tenant |
| "Valid till: Until eviction" | Harsh word; and eviction does not actually cancel Auto Pay | Eviction and delete never call cancel (finding A) |
| "Schedule Rent Payment" | Does not say Auto Pay or "every month" | Consent wording |
| "You can change this date anytime from settings" | False: no such setting in the tenant app or check-in | No tenant-facing change-date entry exists |
| Cashfree page says EAZYAPP | Tenant does not recognise the name; trust drops at the approval moment | Merchant display name on the Cashfree account |
| After approval the app opens, no Auto Pay success | The win is not confirmed; she may think it failed | Return goes to /api/cashfree-return, then the flow |
| Auto Pay step before the agreement | Consent is not tied to the signed document | Step order in pages/checkin/[checkinId].js |
| KYC and selfie errors before reaching Auto Pay | Auto Pay sits behind the hardest step | Existing tenants sent the bulk reminder hit this too |

## What the tenant app confirms

The app shows no Auto Pay status, offer or management anywhere. This matches the code: the Auto Pay status it receives is never saved, so the Dues banner and Profile row never show.

## What to take from CRED

1. **Auto Pay as a tick on the payment screen, at the moment of paying.** Same idea as the 15 Sep call's tick on the final payment screen, and the 11 Sep design's "offer at the moment of relief". CRED leaves it unticked; for our push, recommend ticked by default where the property is on Auto Pay, with the reason on the row. (Decision for Sanchay.)
2. **One line under the tick: "cancel, pause & edit anytime", with "know more".**
3. **A plain FAQ page** answering the eight questions CRED answers, in our words; every surface links to it.
4. **Bank accounts listed with the UPI mark**, so the tenant sees which account pays.
5. **CRED uses UPI Auto Pay here, not only cards**: credit card bills are in the ₹1 lakh category. Rent is not, so the ₹15,000 limit still applies to us.

## Correction to Kamal's written plan

His plan says CRED built rent on the card rail to avoid the ₹15,000 limit. This recording is CRED's credit card bill flow, which uses UPI Auto Pay under the exempt category. It does not show CRED's rent flow.

## Second pass, 17 Sep evening (CRED part at one frame a second, FAQ answers read in full)

**CRED's Autopay page** ("introducing autopay", reached from "know more"):
- **Headline:** "automate your bills. never miss a due date." The line under it: "set it once, stay protected always."
- **Five benefit cards:**
  - manage all your bills effortlessly;
  - never miss a due, never face a fine;
  - support that doesn't keep you waiting;
  - you stay in control, always (edit, pause or cancel; "nothing moves without your say");
  - built for safety, trusted by millions.

**CRED's 15 FAQ questions, with their answers (paraphrased):**
1. **What is Autopay?** It pays your bills on the date you pick, from your linked bank account.
2. **How do I set it up?** Choose a bill, turn on Autopay, pick a bank account, verify with ₹1. It takes under a minute.
3. **Which bills?** Credit cards, electricity, gas, water, broadband, postpaid mobile, insurance and more.
4. **Is it safe?** Bank-grade encryption, layered authentication and risk checks.
5. **What if a payment fails?** You are told at once, the payment is retried automatically, and you can pay manually before the due date.
6. **Will I be notified?** Yes: a reminder 24 hours before the debit and a confirmation after it.
7. **What if my balance is too low?** You are alerted 24 hours ahead. If the bank declines, CRED retries or helps you pay manually.
8. **Can I cancel or edit?** Yes, you can pause, cancel or change it at any time, in the app.
9. **Can I change the bank account?** Yes: edit the settings and link the new account.
10. **Can I set a cap?** Yes. If a bill is above the cap, CRED tells you and helps you pay it manually. The cap can be changed in "Manage Autopay".
11. **Can I choose which bills?** Yes, Autopay is set per biller.
12. **What if the bill is above my mandate limit?** **CRED automatically splits it into several payments so the bill is paid.** This is a live precedent for R16.
13. **Is there a charge?** No, Autopay is free, with no setup or service charge.
14. **When does it happen?** On the date you choose, with a notice 24 hours before, and you can pause or cancel before it runs.
15. **Receipt?** A confirmation in the app and on WhatsApp, with details and documents in your transaction history.

It also lists a 16th question with no visible answer: what happens during bank or biller downtime.

**The bill payment sheet:**
- Choices: pay total due (tagged "100% late fee protection"), pay minimum due, or pay another amount.
- A "Check bank balance" link.

**The CRED Pay sheet:**
- A saving from CRED balance is applied on its own, with a "remove" link.
- Bank accounts are listed with the UPI mark, a "check balance" link and a green "new enhanced limit" tag (₹2 lakh, ₹5 lakh).
- The Autopay row is unticked. Once ticked, its "know more" link becomes "edit". The "Pay now" button stays the same.

**CRED home:**
- An "Upcoming bills" list with "due in 6 days" and a Pay button on each.
- "Pay all cards together".
- A "secure your card, as per RBI guidelines, enable now" nudge on the card page.

**RentOk Payment Options (same recording):**
- "I am paying ₹79,755" with "Edit Amount".
- A "RentPass Cashback EDIT" line.
- Wallet, EMI and Pay later options.
- **"Share Payment link on WhatsApp"**, which is the existing pattern for letting someone else pay.

**Taken into the feature map (version 2.1):**
- an Autopay page with benefits and an FAQ in our words;
- the tick changing to "edit" once ticked;
- "check balance" links;
- showing which of her accounts can do Autopay;
- credits applied before the notice;
- a rule for when her own limit in the UPI app is below the bill;
- a "taken in N days" card;
- "share setup link on WhatsApp";
- handling for bank or Cashfree downtime;
- a confirmation in the app and on WhatsApp.

**Not taken:** choosing which bills Autopay covers. R18 ruled that Autopay collects all monthly dues.

**The sound is still not transcribed.**

## What Kamal says in the recording (transcribed 17 Sep; full text in sources/2026-09-17-kamal-recording-transcript.md)

**Covered by the map already:**
1. **Verification comes before Autopay.** Tenants have to finish verification before they can set up Autopay, which he calls "highly broken". A separate link should open Autopay directly. The map has the one-screen setup.
2. **Better copy** about on-time payment and avoiding penalties, with an FAQ section. It should say that rent above ₹15,000 is taken in two or three debits, and that tenants can pause or refuse. The map has the Autopay page and FAQ.
3. **Tenants choose their own date:** from the due date plus a set period (his example: due date 10th, plus 5 or 3 days). The map has R41, due day to due day plus 7.
4. **Set up Autopay while paying rent,** with no separate ₹1 verification. The map has "pay and turn on", pending Cashfree.
5. **A dedicated Autopay page in the tenant app,** plus a toggle at payment. The map has both.

**New, and needing a ruling:**
6. **Replace the Cashfree page.** It is a two-step process. Our own screen should offer UPI, bank, card or e-NACH, and choosing UPI should open the UPI apps directly, without the Cashfree page.
7. **A settings section in the tenant app** to change the date, pause and edit Autopay. The map has change date and cancel; pause is currently only possible in the UPI app.
