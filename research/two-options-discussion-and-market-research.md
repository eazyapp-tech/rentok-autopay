# Sanchay and team discussion, 17 Sep night: what it changes (analysis before rulings)

Source: Sanchay's pasted discussion notes, in Hindi and English, 17 Sep 2026.

## What the discussion says

1. **Pause at RentOk's end.**
   - Because the mandate is on-demand, RentOk can offer a pause on its own side: after an approved pause, RentOk simply raises no debits. The bank mandate itself is not paused.
   - When the pause ends, debits start again.
   - The owner or manager approves a tenant's pause request.
   - My earlier pause limits ("1. ये ठीक है") are accepted.
2. **"Request payment via Autopay" for managers.** When any due is raised (for example a ₹5,000 or ₹8,000 electricity bill), the manager gets a new option next to "Record payment" and "Remind to pay".
   - The tenant, and the parent, get WhatsApp and app messages: "Your owner has requested a payment of ₹X. It will be paid after 24 hours through your Autopay."
   - The buttons are "Approve (pay via Autopay)" and "Pay manually". There is no reject.
   - Owners stop sending reminders, and the payment actually gets collected.
3. **Mandate amount.** The team recalls deciding that the mandate should equal the rent, because in rentals and deposits a higher number lowers trust.
   - Dues within that amount are debited under the existing mandate, and no new mandate is made for a smaller due.
   - If a request is above it, approving the request raises the limit.
   - This replaces R19 (₹15,000 for everyone).
4. **Frequency.** A mandate can be monthly, which is fixed, or "as presented", which is on-demand.
   - Kamal was told to use "as presented".
   - RentOk's own screen can still say "Autopay every 1 month, cancel anytime".
   - **Conclusion of the discussion:** support both, default to on-demand, and switch a tenant or property to a fixed frequency (monthly, quarterly, half-yearly) where it helps.
   - The discussion also floated letting the tenant choose "monthly rent" or "total".
5. **The Autopay record.** Its start and end dates follow the tenancy. Pause, edit and delete are all needed.

## What Cashfree's documentation says (Context7, 17 Sep)

- **Two plan types:**
  - **PERIODIC:** a fixed recurring amount, charged automatically by Cashfree at fixed intervals of day, week, month or year, every N intervals.
  - **ON_DEMAND:** the merchant raises each charge with the amount it wants, up to `plan_max_amount`.
- **PAUSE and CHANGE_PLAN** are available for periodic plans and not for on-demand plans.
- **The maximum amount** is the most that can be charged under the mandate. The tenant sees it when she approves. A charge above it needs a new mandate.
- **Retries:** at most 3 per billing cycle.

## Consequences across the system

- **A limit equal to rent breaks every month when anything else is added.** The platform fee line (₹58 or ₹49 plus GST), a food package or GST on rent all push the regular debit above the limit.
  - **Fix:** the limit equals her regular monthly dues (rent plus fixed monthly dues plus the platform fee line), which is the number she recognises from her bill.
- **R18 splits in two.**
  - Fixed monthly dues are taken automatically each cycle.
  - Variable dues, such as electricity bills and one-off charges, go through "Request payment via Autopay", started by the manager.
  - This gives the tenant a clear notice for every non-regular debit, which fits "nothing moves without your say".
- **R19 is reversed.** A rent rise above her limit needs a new approval. The rent change flow already has a signing visit, and the approval can sit there, so the loss is contained.
- **Requests above her limit** cannot be debited under the current mandate.
  - "Approve" then opens her UPI app to approve a new, higher limit.
  - Otherwise she pays manually.
  - A new mandate replaces the old one; the old one is cancelled once the new one is active.
- **Rent above ₹15,000 (R16) still applies.** Any single debit above ₹15,000 needs a PIN, so regular dues above ₹15,000 are still taken in parts of up to ₹15,000, and her limit shows her full monthly amount.
- **Pause with approval.**
  - A tenant request goes to the manager.
  - After approval, no debits are raised until the resume month, and dues show "Pay now" for those cycles.
  - Debits restart on their own, with a message before the next one.
  - An unanswered request needs a rule, because she can always cancel in her UPI app if she feels stuck.
- **Fixed-frequency (periodic) mandates** give a real bank pause and plan change, but Cashfree debits them on its own schedule.
  - They cannot skip a cycle she already paid in cash unless RentOk cancels that charge first.
  - They cannot take variable dues.
  - Keep them as a switch RentOk can apply, not the default.
- **An end date equal to the agreement end** would make every renewal need a new mandate, and we would lose tenants at each renewal.
  - Better: the mandate stays valid until she moves out, and is cancelled automatically at move-out (#7005).
- **Count and messages.**
  - A pending or approved pause does not count, as before.
  - Request payment messages count toward the message limits.

## Questions for Sanchay (one at a time)

1. **The limit:** exactly her rent, or her regular monthly dues?
2. **A request with no response:** debit after 24 hours, or wait for her tap?
3. **Which dues can be requested?**
4. **An unanswered pause request:** what happens?
5. **Fixed frequency:** a tenant choice, or a RentOk or property switch?
6. **Mandate end date:** the tenancy end, or until move-out?

## Research on how other apps do it (web, 17 Sep; sourced facts only)

- **NPCI frequencies:** daily, weekly, fortnightly, monthly, bi-monthly, quarterly, half-yearly, yearly, and "as and when presented".
  - "As presented" allows several debits in any period, and it is the standard for variable bills such as electricity (KVB NACH page; Juspay LotusPay docs).
  - A fixed frequency is meant to be debited once per period.
  - NPCI limits "as presented" by payment category. RentOk already runs on-demand mandates, so rent is allowed, but this is still to confirm with Cashfree.
- **Kuku FM and STAGE:**
  - Both use ₹1 trials that turn into ₹199 to ₹699 debits, most of them quarterly.
  - RBI received complaints about them in 2025.
  - STAGE's defence rests on a clear payment page, a video, and WhatsApp plus SMS alerts before each debit (Outlook Money).
- **RBI asked NPCI to review UPI Autopay in Feb 2026** (Livemint, 20 Feb 2026). The complaints: unclear setup, no view of active mandates, hard cancelling, and users believing that uninstalling the app stops debits.
- **NPCI's circular of 7 Oct 2025:** every UPI app must show all of a user's mandates and let the user move a mandate to another app. Merchant-side moving between gateways is expected to follow (Medianama, 31 Aug 2026).
- **UPI Autopay has supported "fixed" or "up to a value" amounts since launch** (Moneycontrol, 2020).
  - SIPs, EMIs and insurance use a fixed amount on a fixed frequency.
  - Variable bills use "up to" with "as presented".
  - A debit above the limit fails, and the user pays manually.
- **Unverified:** a failed first debit cancels the mandate (Moneycontrol, 2020). The exact limit and price pairs for named apps, and the rent platforms' mandate setups, were also not confirmed.
- **Lessons:**
  - A shown maximum higher than what is charged, with no explanation, is exactly the pattern regulators are chasing.
  - A fixed option should be shown as a fixed amount.
  - A variable option should show its limit as itemised sums, not a round buffer.

## Design for the two options (R46)

**At setup, she picks one. Both are shown, and one must be chosen.**

**Option 1: "My rent, every {her rent frequency}"**
- A fixed-frequency mandate (periodic): monthly, quarterly, half-yearly or yearly, matching her rental frequency.
- **Fixed amount:** her regular bill for that period, meaning rent (with GST) plus fixed recurring dues plus the platform fee line. It is shown as one fixed amount with the parts listed.
- **What this option allows:**
  - Cashfree debits on its own schedule, and RentOk cancels a single debit if she has already paid.
  - A real pause at the bank.
  - A plan change when rent changes, which may need her approval.
- **What it cannot do:**
  - It cannot take extra bills, because a fixed frequency is debited once per period. Extra bills for these tenants arrive as a payment request with "Pay now", plus an offer to switch to Option 2.
  - It cannot take parts. If her amount is above ₹15,000, her bank asks for her PIN on every debit. Setup says so, and points her to Option 2, or to e-NACH through "Use bank account instead".

**Option 2: "All my dues, when they're due" (on-demand, "as presented")**
- This is the recommended option, and it is highlighted on the setup screen.
- **Limit:** her regular monthly dues, shown itemised: rent ₹10,000 + platform fee ₹58 = up to ₹10,058 per debit.
- **Debits:**
  - Regular dues are debited each cycle on her day.
  - Dues above ₹15,000 are taken in parts (R16).
- **Extra bills:** these come through "Request payment via Autopay".
  - The manager sends it, and she and her parent get: "{Property} has requested ₹X for {due}. It will be paid from your Autopay after 24 hours."
  - The buttons are "Approve now" and "Pay manually". There is no reject.
  - If she does nothing, the debit runs after 24 hours, and the bank notice still applies.
  - If the request is above her limit, "Approve" opens her UPI app to approve a new, higher limit; otherwise she pays manually.

**Both options:**
- The setup screen says "every {frequency}, cancel anytime".
- Tenant self-service, manager alerts, counting and move-out work as in the map.
- RentOk can switch a tenant between the two, with her consent, by asking for a new approval.

Rent above ₹15,000 is 16% of tenants.
