# Handoff: all five surface documents are written (22 Sep 2026, session close)

Closes the session. Covers web check-in and manager web, which have no handoff of their own, and
sets out where the whole surface set now stands. Sessions `048e5386-b13b-4a51-948b-53493979e3d9`,
continuing `343ddfca-41cf-4c10-beff-09279ad57acf`, `55738a51-000b-4c09-90dc-b5739dd57649` and
`41975625-dbe3-4afd-b72b-f315a0961389`.

Earlier handoffs from the same run: `2026-09-21-manager-app-surface.md`,
`2026-09-22-manager-app-surface.md`, `2026-09-22-payment-page-surface.md`,
`2026-09-22-tenant-app-surface.md`, `2026-09-22-kamal-material-and-the-fee.md`.

## What I set out to do

One document per surface, so a developer with no product context can open any screen and know what
Autopay means on it, what is broken there already, and what is still somebody's decision. Sanchay's
reason: the team could not tell what was in scope, what the workflows were, or how they joined up.

## What changed

**All five surfaces are written**, 1,654 lines in total, each pointing at the tickets rather than
restating them.

| Document | Lines | Its one rule |
| --- | --- | --- |
| `surfaces/manager-app.md` | 305 | A manager may ask, see or request. Never do |
| `surfaces/payment-page.md` | 369 | Outside check-in, this page **is** her Autopay |
| `surfaces/tenant-app.md` | 320 | Two tenant apps, and only one exists before 1 Oct |
| `surfaces/web-check-in.md` | 316 | The only surface where a tenant can be blocked, and it blocks |
| `surfaces/manager-web.md` | 344 | The only manager surface that can ship before 1 Oct, and the one with the least Autopay in it |

Also this session: `research/kamal-launch-room-check.md`, `research/kamal-earlier-material-check.md`,
`research/platform-fee-ladder.md`, and `research/2026-09-22-mdr-exposure-sizing.md` in the private
repo. Open questions 19 to 29. One correction inside R63, marked as mine.

## Decisions, with reasons

- **Point at the tickets, never restate them.** A second document that summarises a first disagrees
  with it the moment either changes. The first manager draft was 558 lines and became 295.
- **Every derived document now ends with the ruling range it was checked against.** All five say
  "checked against R1 to R63, R64 pending". A check made on 17 September against R1 to R18 was still
  being quoted this week with five of its conclusions inverted; this is what stops that repeating.
- **Conflicts between two owners are surfaced, never resolved quietly.** Four of Kamal's designs
  disagree with a ruling; they went in as open questions 19 to 22 with both positions and no
  recommendation.
- **The R63 correction was struck in place, dated and attributed to me**, not edited away, because
  the wrong clause had already been quoted in a surface document.

## What I checked, and how

Code read 21 and 22 September on `rentok-backend` origin/master `1498fcd62`, `eazypg-marketplace`
origin/main `66b49dd0`, `rentok-manager-web` origin/main `5311f662`, `rentok_tenant_package`
origin/main `afea1abe`, `rentokmanagerflutter` origin/main. Production through Metabase, 22
September. Issue states through `gh`, same day.

**Web check-in.** The forward gate passes only on an active mandate
(`pages/checkin/[checkinId].js:158`), against R21. The Autopay tab is pushed at `:110` and the
agreement at `:131`, so the mandate is authorised before the document that governs it. `termsAccepted`
starts `true` with the checkbox commented out (`components/autoPayDetails.js:22`). The Cashfree
result is fetched into a variable and never read (`:1044`), and the success dialog opens on the
address alone. **The Autopay step reaches 0.51% of properties today, 438 of 85,591**, and August ran
at **1,774 new tenants a day**. Nine blocking issues, all open.

**Manager web.** Two files in the whole repository mention Autopay. The tenant profile has none. The
old fee model is still on screen with **RentOk as the unset default payer**
(`PaymentSettings.tsx:828`), and those same bearer fields are what refuse setup under #7054. An
Autopay debit renders as "RentOk Bank Transfer" (`utils/commonUtils.ts:44-56`), so no screen on web
can tell it from a link payment. **"Eligible for tenants joined since" saves a date and writes an
activity log line, and no Autopay path reads it** (every `eligibility_date` hit in the backend is in
the settings save path or the entity).

**Not verified:** whether `PAY_P2_ENABLED` is on in production; whether the old debit engine's job
is disabled; how many managers only ever open the app, which decides how much of the manager line
reaches anyone before the app release.

## What is now waiting

**On Sanchay.** Open questions 1 to 29 in `decisions/open-questions.md`. In the order they block
work:

1. **R64**, still not in the decision log, four days running. It is written into all five surface
   documents.
2. **Open question 24**, whether e-NACH becomes the default rail above ₹15,000. The numbers put it
   at roughly half the prize: 15.7% of tenants carry 48.7% of the charge.
3. **Open question 28**, the two Platform fee ladder numbers, the floor and the ceiling.
4. **Open question 19**, whether the payment page names the UPI charge at all, where Kamal's PRD and
   four rulings disagree head on.
5. **Open questions 10 to 18**, which decide what the Autopay list and its alerts do. Three of them
   block the list itself.
6. **Open question 29**, the inert "eligible since" control: rule it in or take it off the screen.

**On Kamal:** whether the Cashfree list of fifteen really went out on 21 September, since our record
says it is drafted and unsent; and whether the ₹15 mandate fee is quarterly or per execution, which
changes the cost of every rent above ₹15,000.

**On Srijan and Kamal together:** the corrected exposure figure, about ₹6.6 crore a year rather than
₹75 lakh, before the provider terms are settled.

**On an adviser:** the Autopay clause in the agreement, with a payments lawyer. Check-in is the only
surface where the wording has a signature attached to it.

## The next step

The five surfaces are a map, not a build. The next session's first act should be **taking the
corrected sizing to Srijan and Kamal**, because the provider negotiation is being run as though
margin were the constraint and it is not.

After that, the work that is dated rather than optional: the payment page link move by 25 September
(R55), and the six web check-in fixes **before** D4 turns Autopay on by default, because that switch
takes them from a handful of tenants a day to every check-in at once.

## Traps carried forward

- A check is only as current as the rules it was made against. Stamp the range; four of the five
  documents needed it added at close-out, and the gap was invisible until it was checked.
- **Grep a hard-wrapped document with a short token.** The stamp check reported four documents
  unstamped and one stamped; the real answer was three, because the phrase straddled a line break in
  two of them. This is the second time that trap has cost a wrong answer in this repo.
- A widget that exists is not a widget that renders, and a control that saves is not a control that
  does anything. Trace the value from the server to the render, and from the screen to the reader.
- Three artefacts agreeing is evidence only when they were derived independently.
