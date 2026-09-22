# Kamal's launch room, all 23 sections, checked against our rulings (22 Sep 2026)

The launch room is one HTML page Kamal wrote, "RentOk Autopay: the launch room", figures as of
21 September. It has **23 sections**, counted from the page itself. This checks every one, the same
way `research/kamal-artifacts-check.md` checked the 9 figures of his flows page on 18 September.

**Why this file exists.** The payment page surface document used six of the 23 sections. The other
seventeen were read but never checked line by line against the decision log, and several of them
carry facts we do not have.

Kamal's material so far, all of it: his plan version 1 and 2 (17 Sep), a context handoff (17 Sep),
the Notion copy and the flows page with 9 figures (18 Sep), the screen recording and transcript
(17 Sep), this launch room (21 Sep figures, read 22 Sep), and the payment page prototype with
sixteen screens (22 Sep).

---

## The seven things that should move today

1. **The Cashfree list is sent, and our repo says it is not.** Section "pending" says it went out on
   **21 September to a named person at Cashfree**, fifteen items, with three marked blocking and one
   answer wanted 22 Sep. `STATUS.md` says "drafted for Kamal, not sent", and
   `decisions/open-questions.md` lists ten questions as unsent. **Our record is a day behind on the
   single largest external dependency.** Fix the record, then compare his fifteen against our ten.
2. **AFA and 2FA are not enabled on our Cashfree account at all,** so nothing above ₹15,000 reaches
   Autopay there today (section "broken"). That is not in the feature map, and it sits under R16,
   which is how every rent above ₹15,000 is meant to work.
3. **Mandates do not port between providers.** Section "migration" says to plan on every tenant
   re-authorising if we move rails, and that nobody migrates between 25 Sep and 2 Oct. The feature
   map has no migration position at all.
4. **Two tickets on the critical path are not among the 36:** a provider-adapter interface and the
   Rent Coins ledger (section "build"). His words: without the first, moving to PhonePe becomes a
   rewrite in November.
5. **Open question 6, the whitelabel brand, has an answer that needs nobody.** Section "brand": name
   the payee she is about to see, in her property's own words, in the same sentence as the amount
   and the date, on our screen and in the messages. One day of work, no provider dependency. It does
   not replace the ruling, it removes the blocker while the ruling waits.
6. **Open question 23, the parent with no app, has an answer in the same page.** Section "setup"
   offers a **QR she can forward to whoever actually pays her rent**, who scans and approves from
   their own UPI app. His words: the easiest version of R24. A6 can drop its dependency on an app
   that does not exist.
7. **The ₹15 mandate fee is either quarterly or per execution, and both are written down.** Section
   "enach" says the 21 Sep call read it as quarterly and PhonePe's own sheet says per execution.
   That one answer changes the cost of every rent above ₹15,000.

---

## All 23 sections

| # | Section | What it adds | Status against our rulings |
| --- | --- | --- | --- |
| 1 | Why now | ₹150 crore of rent a year, 90 to 95% over UPI, about ₹75 lakh a year of exposure. Mandate cost ₹5 a debit or ₹15 a quarter against ₹15 charged per debit, about ₹10 a tenant a month on about ₹50 billing | Agrees on the reason. **The cost numbers differ from ours** (Cashfree's list price, about ₹7.5 a mandate plus ₹15 a debit). Both are in the repo; neither is confirmed in writing. Its closing line, that the platform fee is parked, is overtaken by R35, R53, R63 |
| 2 | Goals and metrics | R1 and R8 restated, plus a guardrail that online rent collected must not drop month on month, and a new input: managers actively pushing, not measured, to be instrumented before 25 Sep | Agrees. Correctly names N1, N2, N3, N4 and N6 as ruled out. The "no month-on-month drop" guardrail is not in `decisions/success-metrics.md` and should be |
| 3 | What is broken | Our own code check, restated accurately, with the sequencing rule R10 | Agrees, **except two facts we do not have:** AFA and 2FA are not enabled on our account, and Cashfree appears to allow one debit per 24 hours while PhonePe has confirmed several with a 1 to 5 minute buffer |
| 4 | The payment page | The charge notice first, then six routes in cost order | **Conflicts.** Open question 19 and 20. R11, N2, N6 and R63's fourth condition |
| 5 | Split under ₹2,000 | A 10 to 30 minute session, a live paid and remaining and time-left display, no refund path, money held and settled, balance still carries late fine, partial state visible to manager and owner | **Conflicts with N1**, and the page answers the objection. Open question 20. If it ever ships, the four rules here are the product rules it needs, and none of them is in any ticket |
| 6 | Virtual account | One permanent account number per tenant through Cashfree's VAN API, oldest dues cleared first, a beneficiary walkthrough, and a warning not to send money to it over UPI. **The challan product comes off the website in the same release** | Open question 21. **The challan removal is a product change nobody has ruled**, and his reason is sound: two account numbers for one tenant loses a rent payment |
| 7 | RuPay and net banking | RuPay debit carries zero MDR, so detect the card type from the BIN as she types. Net banking is a flat charge, stated in rupees | R34 keeps gateway charges unchanged, so the facts are right. **Saying them on screen still prices one method against another**, which is the open question 19 argument in a second place |
| 8 | Autopay setup | One PIN: her real due is the authorisation, with no separate ₹1 debit. Above the cap, the full amount is authorised and only collection splits. A **forwardable QR** as the parent-payer route. A mandate can return pending and confirm the next day, so check-in must not read pending as failure | **Agrees with R46, R52, R41, R50, R60, R56, R59, R62.** Two things we do not have: the forwardable QR, which answers open question 23, and the pending-then-confirmed state, which A1 and A3 do not name |
| 9 | The debit engine | Two pre-debit notices, one per part. Part two five minutes after part one. Retries 1 plus 1 plus 3. NPCI caps attempts at 4 a mandate, per debit or per period unconfirmed. Webhooks as the source of truth with polling as backup. A global debit stop and a success-rate floor | Agrees with R36 and our retry shape, **except the count:** our map says up to 3 retries, his says 1 plus 1 plus 3. The global stop is our open question 9, so it is now proposed in two places |
| 10 | e-NACH | **The right rail above ₹15,000, not a backup.** One presentment instead of three parts, about twenty times cheaper on PayU's rates, no exposure to the ₹1,00,000 daily ceiling, and a mandate she cannot casually switch off | **A real difference.** R44 makes e-NACH a small "Use bank account instead" link. He would route high rent to it by default. Needs a ruling. Also carries the ₹15 quarterly or per execution contradiction |
| 11 | Providers | Cashfree for 1 Oct, PhonePe as fast follower on server-to-server with our own screens, agreement unsigned. PayU commercials in. Easebuzz parked. Build a provider-agnostic mandate interface with adapters | New. The feature map names only Cashfree. **The adapter interface is unfiled and he puts it on the critical path** |
| 12 | Migration | Mandates do not port. Assume every tenant re-authorises if we move rails. No migration between 25 Sep and 2 Oct. Inside Cashfree, mandates made on the newer endpoints may not cancel through the older path, so cancellations fail silently | New, and large. The inside-Cashfree half is **already our Cashfree question 12 and is flagged in C1**; the cross-provider half is not anywhere |
| 13 | Settlement | Our two P1 payout defects, restated. One rent, one payout, however many parts. Split pieces settle on the normal cycle even when the rent is short. Per-due routing falls back to separate debits per recipient | Agrees, and the per-due fallback is the same conclusion the feature map reaches. The "multiplies per-hit cost and needs a decision" line is new |
| 14 | Branding | 19.5% of tenants on whitelabelled properties. Cashfree asked about brand whitelisting. **The mitigation we control: name the payee before she leaves our screen** | **Answers open question 6 in practice.** One day of work, no provider dependency. It does not replace the ruling |
| 15 | Hubble and Rent Coins | ₹10,000 of rent earns 10,000 coins, a one-time grant of about 1,000 for setting up Autopay, a deliberately flat rate with **no different rates by payment method**, spent on gift cards through a white-label SDK inside our own app | Open question 22. Worth noting: the flat, method-neutral rate is the one thing about it that is already R63-shaped |
| 16 | Notifications and ops | R27, R57 and the message limits, restated correctly. The manager's four things. **Four counters alarmed at zero every day:** double charges, wrong late fines, post-move-out debits, security incidents | Agrees with E1, E2, D3 and our guardrails. The alarmed counters are sharper than our wording and should be taken |
| 17 | Engineering plan | Workstreams mapped to our filed tickets, naming this repository as the specification of record | Agrees. Names the two missing tickets |
| 18 | Timeline | Ten days, dated, in engineer-days, marked as proposals for engineering to confirm. **If the security gate or the double-debit fix slips past 24 Sep, hold default-on rather than launch and patch** | New. That last line is a launch-gate recommendation nobody has ruled on, and it is the right shape: it protects money rather than the date |
| 19 | Risks and rollback | Nine risks with likelihood and response. Rollback has three levers: exempt one tenant (R38), turn off "required" for a property (R61), and the global debit stop | Agrees, and the three levers are exactly our rulings. Useful as written |
| 20 | Task list | Everything outstanding by owner, including eight decisions marked for Sanchay and three for Srijan | Overlaps our open questions 1 to 9 and adds several: split session length, operator payout for part-paid rents, scope of a version 2 auto-refund of short payments |
| 21 | Open questions | Twenty questions with an owner and a "needed by" date | **Ours have no dates.** His list is the same work with a clock on it. Several are the same question in different words, and the two lists should be reconciled rather than kept apart |
| 22 | Waiting on providers | Cashfree 15 items sent 21 Sep, PhonePe 7 from a call the same day, PayU drafted, Hubble to request, Easebuzz parked | **Contradicts `STATUS.md`,** which says the Cashfree email is drafted and not sent. Item 1 above |
| 23 | Charges, parked | The platform fee, GST, pass-through, the discount and who absorbs the 0.4% are all parked as a separate discussion. RBI para 10(a) and 10(c) quoted correctly, so Autopay itself is never charged to a tenant | **Overtaken.** R35, R42, R43, R53 and R63 decide the fee, and R63's four conditions of 22 Sep decide how it may be described. The RBI half agrees with us exactly |

---

## What does not need a ruling, and should just be taken

- The payee-name framing (section 14).
- The forwardable QR as the parent route (section 8), which makes A6 buildable without a parent app.
- The four counters alarmed at zero (section 16), sharper than our guardrail wording.
- The three rollback levers as one list (section 19), all of them already our rulings.
- The "hold default-on rather than launch and patch" gate (section 18), which is a recommendation to
  Sanchay rather than a decision, and belongs next to R10's build order.

## What needs a ruling, in the order it blocks work

1. The charge notice and the cost-ordered routes (open question 19).
2. The sub-₹2,000 split (open question 20).
3. e-NACH as the default rail above ₹15,000, against R44's small link (new, section 10).
4. The virtual account, and with it the challan removal (open question 21, and the challan is new).
5. Rent Coins and Hubble (open question 22).
6. Whether the provider-adapter interface and the Rent Coins ledger are filed now (new, section 17).

## Sources

The launch room HTML, 23 sections, read in full on 22 September 2026, figures as of 21 September.
Checked against `map/feature-map.md` version 4, `decisions/decision-log.md` R1 to R63 with R64
pending, and `decisions/open-questions.md` items 1 to 23. Earlier checks of Kamal's material:
`research/kamal-artifacts-check.md` (the 9 figures), `research/kamal-plan-v2-review.md` (the plan),
`research/kamal-recording-and-screens.md` (the recording).
