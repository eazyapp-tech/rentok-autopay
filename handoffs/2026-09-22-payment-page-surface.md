# Handoff: the payment page as one surface (22 Sep 2026)

## What I set out to do

The second surface document, in the same shape as the manager app one: an engineer with no product
context opens any screen on the payment page and knows what to build, what not to build, what is
broken there already, and what is still somebody's decision.

Sanchay's added instruction for this one, from earlier in the week: take Kamal's prototype as
intent, extract and understand it first, and do not start on a redesign until we agree on the
objective. So this document is the extract, not the redesign.

## What changed

- **`surfaces/payment-page.md` is new**, 300 lines. A 22 row map, three flows that
  `map/diagrams.md` does not already draw, a pointer table, eight things broken today, the ship
  order, what not to touch, a section sorting Kamal's prototype into take, do not take and needs a
  ruling, and what is waiting on a person.
- **`decisions/open-questions.md` gained items 19 to 22**, all four from Kamal's PRD and prototype.
- No rulings added. R64 is still not in the decision log, same as yesterday.

## What I read first, because last time I did not

Every ticket that names this surface, found by counting the mentions rather than by trusting my own
list. It was nineteen tickets, not the eight I had named: A1 to A9, B1 to B4, C1, C2, C4, C5, D5,
E5, E2, S1. I read A1, A2, A4, A5, A8, A9, C1, C2, E5 in full and the state tables of B1, B3, B4,
D5. Also `map/feature-map.md` end to end, the whole decision log, `map/diagrams.md`, the repo's
CLAUDE.md, the tenant walkthrough, and both of Kamal's documents.

## What I checked, and how

Code read on `eazypg-marketplace` origin/main `66b49dd0` and `rentok-backend` origin/master
`1498fcd62`, 22 Sep. Issue states checked the same day with `gh`.

- **The Autopay system on the payment page is built and reaches no tenant.** Two independent
  reasons: `CAN_SET_UP = false` (`components/PayPage/autopay.js:24`) and the payload sends no
  Autopay object at all (`rentok-backend src/controllers/tenant.ts:15082`, backend #6825).
- **The page promises her rent date moves** (`AutopayCard.jsx:43`, `:80`, `:175`). That was R9.
  R41 replaced it on 17 Sep and says her late fine date does not move.
- **"Rent only"** in three places, against R46.
- **Non-monthly tenants refused** (`autopay.js:162-169`), against R28, filed as #7064.
- **The day grid offers all 31 days**, because the allowed window arrives in a payload field nobody
  sends.
- **The move of live links to the new page has not started.** No rewrite in `middleware.js` on
  origin/main, and all five blockers open on 22 Sep. R55 dates this 25 Sep.
- **91.5% of her links are dead** before she opens one (measured 13 Sep, 90 days, 8,025,999 links).
- **Not verified:** whether `PAY_P2_ENABLED` is actually on in production. That is a deployment
  question, not a code one.

## The one that matters most

Kamal's PRD and Sanchay's rulings disagree head on about whether this page tells the tenant that
UPI now carries a 0.4% charge. The PRD makes it the first thing she reads and then orders the
payment methods by what each costs her. R11, N2, N6 and R63's fourth condition of 22 Sep all
forbid exactly that. The prototype is built the PRD's way.

This is not mine to resolve, so it is open question 19, written as a disagreement between two
documents rather than as a recommendation. Open questions 20, 21 and 22 are the same shape: the
sub-₹2,000 split, the virtual account, and Rent Points with the Hubble store.

## What is now waiting

- **On Sanchay:** open questions 19 to 22, and 7 (link life), which now stands between a setup
  message and a tenant. And R64.
- **On engineering, dated:** the link move by 25 Sep, and the payload (#6825) before any screen.
- **On Kamal:** unchanged, the Cashfree list in `drafts/cashfree-email.md`.

## The next step

Sanchay picks the next surface. My recommendation is **the tenant app**, because C1, C2, B3 and B4
all land on it next and half the material is already loaded. Web check-in (A3) and manager web are
the two left after that.

Do not start a payment page redesign. His instruction was to extract and agree the objective first,
and this document is the extract.

## Traps carried forward

- Count the mentions before naming the tickets. My own list of "the eight tickets that touch this
  surface" was less than half of the nineteen that do.
- `origin/main` moved twice on 22 Sep while the tickets quote `ef0bcdd0` and `a147b316`. Re-read a
  line before quoting a ticket's line number as current.
- A finished design that reaches nobody looks identical to a missing feature in any audit that only
  reads the screen. Check the payload and the flag, not the component.
