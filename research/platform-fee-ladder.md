# The Platform fee suggested from average rent: what the numbers say (22 Sep 2026)

Sanchay, 22 September: the manager app suggests the Platform fee from the property's average rent.
**₹58 is a placeholder, not the price.** A property whose tenants pay ₹1,00,000 does not get the
same figure as one whose tenants pay ₹8,000.

Srijan said the same on 18 September, in his own words: "we will push every single owner to apply a
platform fee, based on whatever their average rent is". His method was to take 0.5% and round it.
Kamal's launch room parks the whole fee question, so it says nothing either way.

This file measures the portfolio so the ladder is built from what is there rather than invented,
and separates the part that is ordinary pricing from the one part that is not.

Checked against rulings R1 to R65. Figures from production on 22 September 2026.

---

## Answered, 22 September: R65

**The ladder runs from ₹58 to ₹399, and both ends are suggestions.** Management may set any amount
above ₹399 or below ₹58. R53's hard band of ₹58 to ₹118 is replaced.

The floor holds at ₹58, which was the recommendation, and the ceiling goes to the top rung rather
than R53's ₹118, which was also the recommendation. What Sanchay added is the part I had not
proposed: **neither end binds.** A property that wants to charge ₹30 and absorb the rest, or ₹1,200
on a ₹1,00,000 rent, may do so.

Two consequences, written out in R65: below ₹58 the property is absorbing part of RentOk's ₹49 plus
GST, which costs RentOk nothing and makes absorbing continuous instead of on or off; and above ₹399
the only requirement is the notice rule that applies to every change anyway (R13).

Everything below is the working that led there. The ladder table is the suggested ladder, not a
limit.

---

## What the portfolio actually looks like

Properties grouped by the average rent of their active and upcoming tenants.

| Average rent at the property | Properties | Tenants | Share of tenants | What 0.5% would give |
| --- | --- | --- | --- | --- |
| Under ₹6,000 | 9,603 | 84,227 | 24.1% | ₹19 |
| ₹6,000 to ₹9,999 | 8,177 | 117,306 | 33.5% | ₹38 |
| ₹10,000 to ₹14,999 | 4,490 | 85,456 | 24.4% | ₹60 |
| ₹15,000 to ₹24,999 | 2,508 | 42,510 | 12.2% | ₹91 |
| ₹25,000 to ₹49,999 | 1,086 | 11,635 | 3.3% | ₹164 |
| ₹50,000 to ₹99,999 | 334 | 3,234 | 0.9% | ₹332 |
| ₹1,00,000 and above | 226 | 5,292 | 1.5% | ₹933 |

Rents outside ₹500 to ₹5,00,000 were dropped as bad data; they are 1.3% of tenants and one band's
average was ₹3.3 crore without the filter.

## The ceiling is a real problem, and the floor is a bigger one

**R53 set the line between ₹58 and ₹118**, before R65 replaced it. Against the table above:

- **Above the ceiling: 5.7% of tenants**, about 20,000 people at 1,646 properties, sit at
  properties where 0.5% of average rent is more than ₹118. At the top band it is ₹933, eight times
  the ceiling. This is the case Sanchay raised, and R53 cannot express it.
- **Below the floor: 57.6% of tenants**, about 201,000 people, sit at properties where 0.5% of
  average rent is **less than ₹58**. At the largest band, 33.5% of tenants, it is ₹38.

So the flat fee is wrong at both ends, and **the end it is wrong at more often is the cheap one**.

**Why.** RentOk's own cost is flat: ₹49 plus GST per billed tenant, whatever the rent. The UPI
charge it replaces is not flat: 0.4% capped at ₹300, so it rises with rent. The two are equal at an
average rent of about **₹11,600**, which is close to the portfolio median of ₹8,500 and is why ₹58
feels about right in the middle and wrong everywhere else.

Below that crossing point, a tenant on the Platform fee pays more than the UPI charge would have
cost anyone. Above it, she pays less. That is a pricing fact, not a legal one, and it is Sanchay's
and Srijan's call.

## The part that is ordinary pricing, and the part that is not

**Scaling the fee with rent is ordinary pricing.** Every software product charges more to larger
customers. A fixed monthly price, identical on cash, bank transfer, link and Autopay, that happens
to be larger at an expensive property, is a price.

**Computing it from the payment is the problem**, and specifically computing it as 0.5% because
0.5% is the UPI charge plus tax. Then the fee is the UPI charge wearing another name, and the
arithmetic is the proof: a merchant may not pass that charge to the customer (Finance Ministry UPI
MDR FAQ, Q34), and no charge may be levied on a customer for using a mandate (RBI e-mandate
framework 2026, para 10(a)).

**The same suggested number can come from either route.** A property averaging ₹1,00,000 can be
suggested ₹499 from a published price list, or ₹500 from "0.5% of ₹1,00,000, rounded". The tenant
sees no difference. The difference is in our own manager app copy, our own pricing page and our own
code, which is exactly where anyone would look.

So the rule is narrow: **a ladder, never a rate.**

- The ladder is a price list RentOk publishes, with fixed rupee steps.
- It is set as a pricing decision, not computed from a percentage at run time.
- No screen, document or code comment derives it from the UPI charge or from a share of rent.
- The fee stays identical on every payment method including cash, which is what proves it is a
  price and not a payment charge (R63's first condition).

## The ladder

Built from the bands above, one step per band, round numbers, no arithmetic from rent. **Ruled as
R65 on 22 September; both ends are suggestions and management may set any amount outside them.**

| Average rent at the property | Suggested Platform fee | Share of tenants |
| --- | --- | --- |
| Under ₹6,000 | ₹29 | 24.1% |
| ₹6,000 to ₹9,999 | ₹49 | 33.5% |
| ₹10,000 to ₹14,999 | ₹69 | 24.4% |
| ₹15,000 to ₹24,999 | ₹99 | 12.2% |
| ₹25,000 to ₹49,999 | ₹149 | 3.3% |
| ₹50,000 to ₹99,999 | ₹249 | 0.9% |
| ₹1,00,000 and above | ₹399 | 1.5% |

The manager sees the step for his property, can move up or down the ladder, and can turn the line
off and absorb RentOk's charge instead. The rungs are round numbers a person would choose, and none
of them is 0.5% of anything.

**The two questions this answered**, kept for the record:

1. **Does the floor move below ₹58?** R53 set ₹58 so the line never suggests RentOk costs less than
   it does. The ladder above breaks that on the bottom two rungs, which is 57.6% of tenants. Holding
   the floor is defensible and simple; moving it prices the majority closer to what they are worth
   and costs revenue. Recommended: **hold ₹58 as the floor for now**, because the fee is the
   property's charge and RentOk's ₹49 is real, and revisit once the fee is live and owners react.
2. **Where does the ceiling go?** R53's ₹118 cannot serve 5.7% of tenants. The ladder proposes ₹399
   at the top. Recommended: **raise the ceiling to the top rung of whatever ladder is chosen**, and
   keep R53's rule that anything above it is really a rent rise and goes through the rent change
   flow.

## What this does not change

- **No ruling is overturned.** R35 still puts the fee on the property, R42 and R43 still set the
  default and the GST split, R63's other three conditions stand, and R15 still makes the fee
  identical on every payment method.
- **The tenant's experience is unchanged.** One line on her bill, the same amount every month,
  the same whether she pays by cash or Autopay.
- **Nothing about Autopay changes.** The mandate, the options, the day, the limit and the debit are
  untouched by which rung the property sits on.
- **The legal position is unchanged**, because the thing that carried the risk, the 0.5%
  arithmetic, is the one thing this does not do.

## Sources

Production figures through Metabase, 22 September 2026: `tenant`, active and upcoming, rent between
₹500 and ₹5,00,000, grouped by property. Srijan's instruction is in the 18 September transcript at
37:19 and 49:13, in the private repo. The legal position is in `legal-check.md` item 4 and
`discount-route.md`, both private, and rests on the Finance Ministry UPI MDR FAQ Q34 and RBI's
e-mandate framework 2026, para 10(a). Neither is legal advice.
