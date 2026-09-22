# Handoff: the manager app as one surface (22 Sep 2026)

## What I set out to do

Sanchay asked for one document per surface, so an engineer with no product context can open any
screen and know what to build and what not to build. His reason: the team cannot tell what is in
scope, what the workflows are, or how to visualise them. Manager app first, then the rest.

## What changed

- **`surfaces/manager-app.md` is new**, then rewritten once. First version restated D1 to D7 badly
  and was 558 lines. It is now 295 lines and points at each ticket instead: the map, four flows, a
  pointer table, what breaks today, the ship order, and the do-not-touch list.
- **`decisions/open-questions.md` gained items 10 to 18**, nine proposals that were sitting inside
  D1, D2 and D3 where Sanchay would never have found them.
- No rulings added. No issues filed. The only product change recorded is **R64**, which is Sanchay's
  22 Sep ruling on charges, written up in the document's section 7 and not yet in the decision log.
  **The next session should add R64 properly**, or confirm that R35 and R63 already cover it.

## What I checked, and how

- **Code**, read on `rentok-backend` origin/master, `rentokmanagerflutter` origin/main and
  `rentok-manager-web` origin/main, 21 and 22 Sep 2026. Five traces: every rent and agreement path
  against the mandate ceiling, grace period precedence across three columns, the manager app screen
  inventory, the app versus web parity diff, and the MDR meeting record.
- **`autopay.plan_amount` is written at insert and updated by no code path.** Nine update call
  sites, none touches it. The debit truncates with `Math.min` and records the truncated figure, so
  the shortfall is invisible.
- **`autopay.end_date` is never written anywhere.** Every mandate is unbounded.
- **`cancelSubscription` has no caller outside the Autopay module.** Move-out does not cancel.
- **Grace is three columns, not four.** The property late fine grace and the Automatic Late Fine due
  type grace are the same row with two front doors.
- **Disproved one scare.** The Flutter app posts the whole property config with nulls; the backend
  guards every field with `NotNullUndef`, which returns false for null. It is safe.
- **Not verified:** whether the legacy V1 debit engine still runs in production. That is a deployment
  question, not a code one.

## What is now waiting

- **On Sanchay:** open questions 10 to 18, newly added. The three that block a manager screen are
  which status wins when two apply, how the Autopay rate is counted, and alert timing. Also whether
  R64 is a new ruling or is already covered by R35 and R63.
- **On Kamal:** unchanged, the Cashfree list in `drafts/cashfree-email.md`.
- **On an adviser:** unchanged. A payments lawyer on the Platform fee wording and its place in the
  tenancy agreement, per `legal-check.md` item 4.

## The next step

Write `surfaces/payment-page.md` in the same pointer shape, from A1, A2, A8, A9, B1, B3, B4, C1 and
Kamal's PRD and prototype, having read all of them first.

## What went wrong here, so it does not repeat

I wrote the document before reading the sources that specify it, three times, and Sanchay caught it
three times. The tickets D1, D2, D3 and D7 each specify a section I had written from a one-page
summary. `map/diagrams.md` already held a pause diagram I had drawn again. The repo's own CLAUDE.md,
which I had not read, says to start from STATUS.md, the newest handoff and the feature map.

**The rule: read every source that names the surface before writing a line about it.**
