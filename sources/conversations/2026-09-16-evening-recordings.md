---
date: 2026-09-16
window: 21:00 to 21:29
source: NeoSapien pendant, 3 recordings, summaries + MOM + raw transcripts read
tags: [neosapien, digest, autopay]
---

# NeoSapien, 16 Sep 2026, 9:00 PM to 9:29 PM

Three back-to-back recordings, one continuous sitting. Almost all of it is [[Auto Pay]].

## 1. Auto Pay rollout plan (9:00 to 9:10 PM)
Memory `f5327c86`. Sanchay plus a senior voice, probably [[Srijan]] (Sanchay says "Srijan" while replying to that speaker).

**Goal:** about 1.5 lakh tenants pay rent through RentOk. Move 70,000 to 75,000 of them onto Auto Pay (UPI), e-NACH, or a virtual bank account by **1 October**.

Where tenants get pushed to set it up:
- Tenant app: right after sign-up, and first thing on app open for anyone without it.
- Check-in: Auto Pay is a mandatory step.
- WhatsApp: a separate message after the rent agreement welcome message, with a button and steps.
- Nudge: tenants not on Auto Pay pay 0.4% of rent plus GST extra each month.
- Trust: tenants must be able to pause and delete their mandate.

Rent above the ₹15,000 UPI Auto Pay cap: split the debit (3 x 5,000 or 2 x 10,000).

Gateway cost, argued back and forth:
- [[Cashfree]]: about ₹5 per debit.
- [[PayU]], [[PhonePe]]: about ₹15 per quarter, unlimited debits.
- Sanchay's point: which is cheaper depends on how long the tenant stays and how many debits a month. Electricity is a separate debit from rent, so most tenants get several debits anyway. Today only rent is on Auto Pay.

Unified check-in, the blocker:
- A version is live for [[Millennial Living]]. A newer PR ([[Harsh]]'s work) is still pending review.
- Senior voice is frustrated: "no time" is why Auto Pay took two years and BBPS three. Will talk to [[Nimit]] and [[Jatin]].
- Landed on: park unified for now. Build a new **web check-in flow** on top of the revamped payment page (electricity already there), with login and Auto Pay. Same backend, new front end. Sanchay to check the underlying layers with Nimit.

Owner side:
- Property settings get a choice on platform charge and gateway charge. A bottom sheet tells every owner these charges start **15 October** ("government decision"), then asks them to act.
- A service agreement for payment cases goes into owner T&C, as a checkbox.

Tenant side legal:
- Tenant T&C at Auto Pay setup covers bounce charges and disputes.
- Rent agreement becomes an annexure, so chargebacks can be fought by sending the agreement.

Manager app:
- Show per tenant whether Auto Pay is live. Sanchay: settings and the colour status "done tomorrow" (17 Sep).
- Sending an Auto Pay link: today it only goes inside the check-in link (4 steps: renting terms, rental agreement, Auto Pay). There is a bulk "Auto Pay reminders" button. Whether a single-tenant send exists was left unconfirmed.

## 2. Live review of Auto Pay, heated (9:11 to 9:24 PM)
Memory `6dfe8017`. Several people testing on a phone. Names heard: Anurag / Rajkumar (a test tenant), Divakar.

Problems found live:
- **No separate Auto Pay link or button.** It hides inside the check-in link. Reviewer: "it will not get adopted", calls it a jugaad. He says he had asked for a separate button before. Sanchay apologised during this exchange.
- UI wastes a lot of screen space. PAN step confused people.
- **A setting does not save.** Reviewer: "QA nahi kara hua hai."
- No option to change the debit date.
- Late fine and grace period do not seem live. Features were cut in the rush to go live.
- UPI option did not appear, likely because rent plus a ₹50 charge crossed ₹15,000. Point raised again: above ₹15,000, do not force net banking if UPI can do multiple debits.
- Unclear if the Auto Pay fee is one time or monthly. Owner must be able to set the fee and choose who pays it (owner or tenant). "Need to sit on this."
- Past case: one tenant hit with repeated ₹200 bounce and debit charges.
- Cashless deposit still shows in one or two places. Remove everywhere.
- ₹1 is debited at setup today.

Decided: under ₹15,000, skip the extra screen and open the UPI app (PhonePe, Paytm) directly, "like micro drama apps". Going live from 1 October.

Side topic, bot for stores: a store (Allahabad mentioned) wants a full cart on the bot and on its official website, so coverage can reach all of Gurgaon. Marketing idea: printed carry bags, stickers, flyers, pamphlets in store.

## 3. Bot scope, debit notices, hiring (9:24 to 9:29 PM)
Memory `7ac09f93`. Sanchay with [[Diwakar]]. The pendant log ends here.

- Bot: budget ₹25,000 a month for adoption, heavy discounts on bot orders. Only worth building if **payments and order flow** both work.
- **No message goes to tenants before a debit today.** The 24 hour advance notice (transcript says "RDB", probably the pre-debit notification) is missing. Risk: a tenant reports the merchant.
- Mandate is on-demand: one authentication, then several debits, even the same or next day. So ₹20,000 rent can be two ₹10,000 debits.
- Sanchay to share an ID and password so someone can log in (with that person's phone number).
- Founder's Office JD is live on [[Wellfound]].
- December transactions being checked. Some show a "UGR" number (probably UTR, the bank reference).

## What needs a ticket or follow-up
1. Separate Auto Pay link and button, single tenant and bulk.
2. Setting-not-saving bug, and a QA pass on the whole Auto Pay flow.
3. Debit date change, late fine, grace period.
4. Direct UPI app handoff under ₹15,000 (1 Oct).
5. Split debits above ₹15,000 instead of forcing net banking.
6. Fee rules: one time vs monthly, owner sets it, owner or tenant pays.
7. Pre-debit notice 24 hours before each debit.
8. Remove cashless deposit leftovers.
9. Manager app Auto Pay status (promised 17 Sep).
10. Web check-in flow with Auto Pay; unblock with Nimit and Jatin.
11. Owner bottom sheet + T&C for 15 Oct charges; tenant T&C + agreement annexure.
12. Pause and delete mandate for tenants.

## Second pass: points missed the first time
Rollout plan (9:00):
- IDFC approval mentioned at the start, next to virtual account number.
- Payment link feature confirmed done.
- Manager app: Auto Pay settings on **by default for all properties**.
- **Bug:** payments were not going through at all on the senior person's own property.
- A small amount (₹2 here, ₹1 in the review) is debited at setup.
- "Paid by tenant / paid by owner" options visible; some amount already charged today.
- Rewards for moving to Auto Pay raised, never detailed. Open.
- Aside: an owner refused something and it was stopped. Unclear.

Live review (9:11):
- Test path: enabled Auto Pay on own property, added self as tenant, tenant profile, share check-in link. Only a bulk Auto Pay option is visible there.
- **Bug:** an already verified tenant is not landed straight on the Auto Pay step; has to click through.
- UPI should be the default option.
- Too much text; screen to be revamped like the pay.rentok.com payment page.
- Some UPI apps allow up to ₹1 lakh; add this to settings.
- A ₹26 charge showed during the test.
- Correction: "sector fees" was "setup fees". A setup charge is shown.
- The ₹1 setup debit seems to be reversed.
- Asked whether debit alerts go out; answer was notifications are not happening.
- Process: "don't ship like this in future"; someone waiting "for the next crisis".
- Bot pilot: stores hold cash; tried at 2 to 3 stores, landed at one. A walk-in issue to fix.

With Diwakar (9:24):
- A payment is found in our system only when there is a transaction ID.
- Bot can work in any category.
- Nobody is sure whether the pre-debit message goes via Cashfree. Verify.

Added follow-ups:
13. Land verified tenants directly on the Auto Pay step.
14. Payments failing on the senior person's own property.
15. UPI as default option; ₹1 lakh limit in settings.
16. Verify whether pre-debit notices are sent at all.

## Recording gaps (cannot be recovered)
| Recording | Length | Transcript ends | Missing |
|---|---|---|---|
| 9:00 rollout | 10:21 | 9:29 | about 50 s at end, about 30 s mid |
| 9:11 review | 12:55 | 9:47 | about 3 min at end, about 23 s mid |
| 9:24 Diwakar | 5:25 | 3:38 | about 1.8 min at end |

## Transcript caveats
- Speaker labels are unreliable. The same long passage is often tagged to both Sanchay and another speaker, so "who said it" above is best effort.
- Likely mis-hearings: "pay.rentokil.com" (pay.rentok.com), "unified life" / "life for all" (unified flow / live for all), "UGR" (UTR), "NDR" (unclear).
