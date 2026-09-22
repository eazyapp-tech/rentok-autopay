# Handoff: checking Kamal's material, and the fee ladder (22 Sep 2026, late)

Covers the three passes after the tenant app surface document. Sessions
`048e5386-b13b-4a51-948b-53493979e3d9`, continuing `343ddfca-41cf-4c10-beff-09279ad57acf`.

## What I set out to do

Sanchay asked whether Kamal's material had actually been factored in, then asked for the three
earlier documents to be re-checked the same way, with the orders of effect of each finding and a
statement of what each one does not touch. He then corrected the fee model.

## What changed

- **`research/kamal-launch-room-check.md`** (new). All 23 sections of the launch room checked
  against the rulings. The payment page document had used six of them.
- **`research/kamal-earlier-material-check.md`** (new). The plan in both versions, the context
  handoff and the flows page, re-checked. Each finding carries its first, second and third order
  effects and what it does not change.
- **`research/platform-fee-ladder.md`** (new). The portfolio measured by property average rent, and
  a proposed ladder.
- **`research/2026-09-22-mdr-exposure-sizing.md` in the private repo** (new). Monthly payment
  volumes, kept out of the public repo.
- **`decisions/decision-log.md`:** R63's second condition **corrected, visibly and attributed to
  Claude, not rewritten**. No ruling added.
- **`decisions/open-questions.md`:** items 19 to 28.
- **`surfaces/manager-app.md`:** the charges section rewritten to match Sanchay's instruction.

## Decisions, with reasons

- **The correction to R63 is marked as mine, struck in place, not deleted.** The four conditions
  under R63 were research I appended on 22 Sep, and one of them said "no band that rises with rent".
  That over-reached: the source says a fee must not be sized to the UPI charge, which bans the
  formula, not the family. It was quoted in a surface document before the correction, so removing it
  silently would leave that quotation unexplained. The replacement is an open question because the
  numbers in it are Sanchay's.
- **The money sizing went to the private repo, the conclusion to the public one.** The repo's own
  rule allows business numbers in public, but RentOk's month-by-month payment volume is the most
  commercially sensitive figure the repo would carry while it is public for Kamal. Sanchay was told
  and can overrule.
- **Conflicts between Kamal's documents and the rulings were written as open questions with both
  positions, never resolved in the document.** Four of them, items 19 to 22.

## What I checked, and how

Production through Metabase on 22 September 2026, database 2.

- **UPI is 94.8% of online money**, matching Kamal's 90 to 95%. August carried **₹140.7 crore of
  UPI rent**, June and July ₹116.6 and ₹131.6 crore, growing about 9% a month. **Annual exposure to
  the new charge is about ₹6.6 crore, not the ₹75 lakh in both of Kamal's documents.**
- **15.7% of billed tenants have regular dues above ₹15,000**, about 55,000 people, and payments
  above ₹15,000 carry **48.7%** of the charge. Recurring packages move that share by 0.5 points, so
  rent alone is a fair test of who crosses the line.
- **Property average rent, banded:** 57.6% of tenants sit at properties where 0.5% of average rent
  is below R53's ₹58 floor, and 5.7% sit above its ₹118 ceiling. RentOk's ₹49 is flat and the charge
  it replaces rises with rent; they cross at about **₹11,600** of average rent.
- **The saved copy of the flows page holds no content.** It is a published Notion shell whose text
  is fetched by script; extracting it yields 170 characters of chrome. The text in `sources/` is the
  only record of that page.
- **Our own 17 Sep review of Kamal's plan was made against R1 to R18** and five of its conclusions
  have since inverted, including the day rule R41 replaced.
- **Not verified:** whether the ₹6.6 crore holds across a full year (three months checked for
  trend), and the exact semantics of `net_amount` after credits.

## What is now waiting

- **On Sanchay:** open questions 19 to 28. The two that block most work are 24, e-NACH above
  ₹15,000, which section 3 of the earlier-material check sizes at about half the prize, and 28, the
  two numbers in the fee ladder. **R64 is still not in the decision log, three days running.**
- **On Kamal:** whether his Cashfree list of fifteen really went out on 21 Sep. Our record says the
  email is drafted and unsent, his page says it was sent. Also the ₹15 mandate fee, quarterly or per
  execution, which changes the cost of every rent above ₹15,000.
- **On Srijan and Kamal together:** the corrected exposure figure, before the provider terms are
  settled. Every cost line reads differently at nine times the size.

## The next step

Take open question 27, the corrected sizing, to Srijan and Kamal, because the provider negotiation
is being run as though margin were the constraint and it is not. Two surfaces are still unwritten,
web check-in and manager web, and web check-in should go first because A3 is the only door where a
tenant can be blocked.

## Traps carried forward

- A check is only as current as the rules it was made against. Every derived document now ends with
  the ruling range it was checked against; the older ones do not, and cannot be dated by a reader.
- Three artefacts agreeing is evidence only if they were derived independently. The stale day rule
  sits in our review, the payment page code and Kamal's prototype, all from one ancestor.
- The sentence that starts "this is why we are doing this" is the one to verify first. It was one
  query, and it was wrong by about nine times.
