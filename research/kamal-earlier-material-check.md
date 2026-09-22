# Kamal's three earlier documents, re-checked (22 Sep 2026)

The plan of 17 September in both versions, the context handoff of 17 September, and the flows page
of 18 September. All three were checked once before, on the day they arrived. This re-check exists
because that first check was made against **rulings R1 to R18**, and there are now 63 rulings with
R64 pending. A check is only as current as the rules it was made against.

Each finding below is followed by what it changes: the first thing that moves, what that causes, and
what that in turn causes. The last column of each is the one that matters, and the section at the
end says what none of this touches.

---

## The state of the three documents

| Document | Where it lives | State |
| --- | --- | --- |
| The plan, version 1 | `sources/2026-09-17-kamal-autopay-plan.md` | Superseded by version 2. Never separately reviewed, and does not need to be |
| The plan, version 2 | `sources/2026-09-17-kamal-plan-v2.md` | Reviewed 17 Sep in `research/kamal-plan-v2-review.md`, against R1 to R18 only |
| The context handoff | `sources/2026-09-17-kamal-session-handoff.md` | Reviewed in the same file. **Its sections 4 to 6 were never mined**, and they hold the most useful material of the three |
| The flows page, 9 figures | `sources/2026-09-18-kamal-flows-page.md` | Checked figure by figure in `research/kamal-artifacts-check.md`. That check holds |

**The saved copy of the flows page is a dead file.** The 478KB HTML in Downloads is a published
Notion shell whose content is fetched by script at run time: extracting it yields 170 characters of
chrome and no content. The 7,766-character text in `sources/` is the only record of that page, taken
from the live page on 18 September. **If Kamal edits that page, nothing here will notice.** Anything
that page is meant to settle should be copied into this repo, not linked.

---

## 1. Our own 17 September review is now a stale source

Five of its conclusions were correct then and are wrong now, because the ruling each rests on has
been replaced.

| The review says | Replaced by | What it now reads as |
| --- | --- | --- |
| "Day grid: any day of the month, which becomes her rent due date for fines (R9)" | **R41** | Wrong. Her day runs from her rent due day to the last grace day, and her late fine date does not move |
| "Under R18 the debit is variable, up to ₹{limit} per debit" | **R46** | Incomplete. She picks one of two options, and the limit is her own regular dues line by line |
| "Required by the property against R2, optional for tenants" listed as open | **R20, R21** | Settled. Required by default, and required means chase, never block |
| "The choice between a limit close to her dues and a ₹15,000 limit" listed as open | **R46** | Settled. Her own regular dues, for trust |
| "A ₹49 platform fee applies to every payment method" | **R35** | Wrong owner. RentOk charges management; the property decides whether a Platform fee line reaches the tenant |

**First order:** anyone quoting that review today gets four stale rules, and the first of them is the
exact line the built payment page prints to tenants.

**Second order:** the stale day rule is now in three places at once. It is in our review, in the
payment page code, and in Kamal's own prototype, which repeats it. Three artefacts agreeing with
each other looks like confirmation, and they agree only because they share one dead ancestor.

**Third order:** the next person to check any of the three against the other two concludes the
product is consistent and stops looking. The habit that catches this is not reading more carefully,
it is stamping every derived document with the ruling range it was checked against, which this file
now does and the others should.

---

## 2. The money the project is built on is about nine times larger than the plan says

Both Kamal's documents open with the same figure: about ₹150 crore of rent a year, 90 to 95% over
UPI, so about ₹75 lakh a year of exposure to the new charge. That sentence is the reason this
project exists and nobody had checked it.

Measured against production on 22 September, three consecutive months:

- **UPI is 94.8% of online money.** Kamal's 90 to 95% is exactly right.
- **August alone carried ₹140.7 crore of UPI rent**, growing about 9% a month since June.
- **The annual exposure is about ₹6.6 crore, not ₹75 lakh.**

The monthly volumes are in `2026-09-22-mdr-exposure-sizing.md` in the private repo, because they are
RentOk's payment volume.

**First order:** the prize is about nine times what every planning document assumes.

**Second order:** every cost line that reads as expensive stops being the constraint. Cashfree's
₹15 a debit across 70,000 tenants is roughly ₹1.26 crore a year against ₹6.6 crore saved. Kamal's
risk row, that per-hit pricing on a ₹45,000 rent split three ways costs about ₹45 against about ₹50
of billing, is real for that tenant and rounding error for the portfolio. **Paying more per mandate
to get a better rail is worth real money**, which is the opposite of how the provider negotiation
is currently framed.

**Third order:** it changes what "hold default-on rather than launch and patch" costs. A week's
delay is roughly ₹12 lakh of charge, which is cheap against one double-debit incident across 70,000
mandates, so Kamal's own launch gate is the right call and now has a number behind it.

**What it does not change:** the direction, the target, the 1 October date, or any ruling. Autopay
is still the answer; it is a larger answer than written down.

---

## 3. Half the charge sits in the segment the design serves worst

The ₹15,000 line is the pivot of Kamal's figure 02 and of R16. Nobody had sized it.

- **15.7% of billed tenants have regular dues above ₹15,000**, about 55,000 people.
- **Those payments carry 48.7% of the charge.** ₹104 a month each against ₹31 below the line.
- **The recurring packages barely matter to this.** Counting food, wifi, maintenance and the rest
  alongside rent moves the share from 15.2% to 15.7%, which is 1,843 tenants. Rent alone is a good
  enough test for who crosses the line.

**First order:** for those 55,000, a single silent debit is impossible. Option 2 takes their rent in
parts; Option 1 asks for a PIN every month.

**Second order:** parts depend on Cashfree allowing more than one debit per mandate per period,
which is Cashfree question 1 and is unanswered. The launch room records that Cashfree appears to
allow one per 24 hours while PhonePe has confirmed several with a short buffer. If Cashfree says one
per period, Option 2 cannot collect these rents in full, and the balance goes out as a link, which
carries the charge, on the very rents where the charge is largest.

**Third order:** the tail we automate worst is the tail that costs most, so the failure is
self-concentrating. That turns open question 24, whether e-NACH becomes the default rail above
₹15,000 instead of a small link under R44, from a matter of preference into roughly half the prize.
It is the highest-value product decision on the board and it is currently written as a link in a
corner of one screen.

**What it does not change:** the other 84%. Their dues are under the line, one silent debit
collects them, and none of the parts machinery, the PIN disclosure, the e-NACH question or the
Cashfree multi-debit answer touches them at all. **The ₹15,000 problem must not be allowed to hold
up the majority path**, which is the shape most launch delays take.

---

## 4. What the context handoff holds that nobody mined

Its sections 4 to 6 were never used. Four things in them carry real weight.

### The Figma file is the same system as the built payment page

Section 5.4 inventories a Design file, "Autopay, every state and surface", with sixteen named
frames: Offer on a bill, Offer with nothing to pay, Snoozed, Required, Started, On, Failed, the
moment sheet, the day grid, the dock above Pay all, after paying. **That is frame for frame the
system in the payment page code**, traced independently on 22 September for `surfaces/payment-page.md`.

The file's own annotation, written 14 September, says what that document found eight days later:
no tenant can see any of it, because no Autopay field is in the payload and the setup flag is false.

**First order:** the finding is confirmed from a second direction, and it is eight days old.

**Second order:** design, code and the check now agree, which means the work is real and the gap is
one payload and one flag, not a build.

**Third order:** and the same file specifies "the day grid, 31 days", so **the design file carries
the stale day rule too**. Wiring it on without fixing the copy publishes a promise R41 retired. The
order matters: the ruling fix ships before the wire, not after.

### The Payment Page Revamp Figma was never reviewed, and still has not been

Section 5.5: the node was never opened, because the Figma seat hit its limit first, and section 1.4
of the plan was written from first principles without it. That is still true today. It is the one
piece of design input on this surface that nobody has read.

### The high-rent tail is why CRED runs rent on cards

Section 4.2: the ₹1,00,000 no-PIN ceiling applies only to mutual funds, insurance premiums and
credit card bills, under RBI's December 2023 circular. Rent is not on the list, and Kamal's reading
is that this is why CRED built rent payment on the card rail instead of UPI Autopay.

**Second order:** a competitor solved the same ₹15,000 problem by changing rails. R44 rules out card
Autopay for us, so our two available answers are parts and e-NACH, which is section 3's point
arriving from a different direction.

### Autopay consent belongs after the agreement

Section 7 settled that during Kamal's own session, and the product agreed later: A3 makes Autopay
the step after the agreement. Today it is step 3 of 5 and the agreement is step 4, so a tenant
authorises a mandate before signing the document that governs it. Already ruled, still true in code.

---

## 5. What none of this changes

Worth stating plainly, because the instinct after a re-check is to reopen everything.

- **No ruling is overturned.** Nothing here contradicts R1 to R63, and nothing needs R64 rewritten.
- **The target, the date and the build order stand.** R1, R23 and R10 are untouched.
- **The 84% below ₹15,000 are unaffected** by every question section 3 raises.
- **The manager app and the tenant app surfaces are unaffected.** Both documents were written
  against the current rulings and neither depends on the sizing.
- **The flows page check of 18 September still holds.** All nine figures were read correctly against
  the rulings then, and the rulings that have landed since do not touch them.
- **Kamal's plan is not wrong in direction anywhere.** Its three real defects are a sizing figure
  that is too small, a day rule that a later ruling replaced, and a split-mandate idea that R16
  replaced with one mandate in parts. Everything else in it either became a ruling or is still good.

---

## What should move

1. **Take the corrected sizing to Srijan and Kamal.** Every planning number in both documents rests
   on the old one, and the provider negotiation is being run as though margin were the constraint.
2. **Rule open question 24**, e-NACH above ₹15,000, with section 3's numbers attached.
3. **Stamp every derived document with the ruling range it was checked against**, so a stale check
   announces itself. This file is checked against R1 to R63 with R64 pending.
4. **Copy anything the flows page is meant to settle into this repo.** The saved copy is a shell.
5. **Read the Payment Page Revamp Figma**, the one design input on this surface nobody has opened.

## Sources

`sources/2026-09-17-kamal-autopay-plan.md`, `sources/2026-09-17-kamal-plan-v2.md`,
`sources/2026-09-17-kamal-session-handoff.md`, `sources/2026-09-18-kamal-flows-page.md`, all four
confirmed identical to the copies Kamal sent. Earlier checks: `research/kamal-plan-v2-review.md`
(17 Sep, against R1 to R18) and `research/kamal-artifacts-check.md` (18 Sep, the 9 figures).
Production figures through Metabase on 22 September 2026, workings in the private repo at
`research/2026-09-22-mdr-exposure-sizing.md`. Checked against rulings R1 to R63, R64 pending.
