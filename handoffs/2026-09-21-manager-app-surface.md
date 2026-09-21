# Handoff: the manager app surface document

Session `55738a51-000b-4c09-90dc-b5739dd57649`, continuing `41975625-dbe3-4afd-b72b-f315a0961389`.
Written 21 Sep 2026, after the document was delivered and before the next surface is picked.

## Objective

Sanchay asked for one document per surface that lets a developer with no product context open any
screen in the manager app and know what Autopay means on it: what it shows, what the manager can do,
what happens next, and what must not be touched. Manager app first, closed out completely, then the
next surface.

The reason is not documentation for its own sake. In his words, the team cannot currently tell what
is in scope, what is out, or how the workflows join up.

## The thing that changed the job

The product was already decided. `map/feature-map.md` v4, `decisions/decision-log.md` with 63
rulings, and the D1 to D7 ticket drafts already specify the manager's line in detail. I found them
two turns in, after starting as though this were a design exercise.

**So the job is mapping, not deciding.** Anything that looks like a new product decision in
`surfaces/manager-app.md` is either a mistake or is marked open. The feature map wins every
disagreement.

## Decisions taken in this session, with reasons

**R64, his ruling, recorded here because it is not yet in the decision log.** Tenants bear the setup
charge, the monthly charge and the platform charge by default. Management can take any one of the
three onto itself. The switch lives in Autopay settings in the manager app.

This reopens **R11**, which retired tenant-borne Autopay charges on the ground that the RBI
e-mandate framework 2026 para 10(a) forbids charging a customer for the mandate. I raised that twice.
He ruled. It is filed as open question 2 in the document, pointed at Srijan and a payments lawyer,
and explicitly marked as blocking nothing in the build. **Do not re-raise it.** If the lawyer comes
back against it, that is new information and the conversation reopens on its own.

**Manager can never set up, pause or stop a tenant's Autopay.** His ruling, and it became section 1
of the document because it removes a whole class of wrong screens in one sentence.

**Request payment via Autopay is deferred.** His call, on provider feasibility and bandwidth. Nothing
else in the document depends on it, so it is the clean first cut.

**The charges bottom sheet is dismissible**, three screens, returning until the property sets or
declines. His confirmation. My pick on placement, which he has not overturned: manager web for
1 Oct, app at the next release.

**Team permissions: ten actions, recommended as four groups** (see, chase, change money, change
tenancy). He confirmed permissions are needed and was explicitly unsure about ten. Left open.

## What the five traces found, in one line each

- **Rent change.** `autopay.plan_amount` is written at insert and updated by no code path anywhere.
  The invoice is regenerated from current rent minutes before each debit, so the bill moves and the
  ceiling does not. The debit truncates silently and the truncated figure is written to the schedule,
  so the shortfall is invisible. A cron raises rent 10% for a fixed property list with its
  notification block commented out.
- **Agreement.** `autopay.end_date` is never written. Every mandate is unbounded. Renewal does not
  touch the mandate, and a mandate cannot be extended at the provider.
- **Move-out.** Nothing cancels. The only reason charging stops is that no unpaid rent invoice is
  found, which is an accident and not a guard.
- **Grace.** Three columns, not four: the property late fine grace and the "Automatic Late Fine" due
  type grace are the same row with two front doors. `tenant.grace_period` alone carries five
  meanings, including the 1000 sentinel and the Autopay debit day window.
- **Parity.** Gaps run both ways. Autopay grace is web only; per-tenant grace and per-tenant Autopay
  status are app only.

## One finding I disproved, worth keeping

The parity trace flagged that the Flutter app posts the whole property config with `null` for every
untouched field, including on the twenty-property copy. It looked like a P0. It is safe:
`updatePropertyConfig` guards every field with `NotNullUndef`, which returns false for `null`. The
neighbouring one is real: the Enable Autopay toggle is hardcoded on, sends `autopay_status: 1`, and
one Save from the promo banner turns Autopay on for the property.

## Files touched

- `surfaces/manager-app.md` **(new, 528 lines, uncommitted)**. The deliverable.
- `handoffs/2026-09-21-manager-app-surface.md` (this file).

Outside this repo, earlier in the same session: the Autopay API contract on
`rentok-backend` PR #7138 gained a navigation header and three corrections (commit `3147a1c5c`,
pushed), and `~/rentok-autopay-internal/drafts/2026-09-21-message-to-kamal-cashfree.md` holds the
five Cashfree questions, drafted and not sent.

## Next action

He picks the next surface. My recommendation is **manager web**, while the same material is loaded,
because half of it is the same decisions on a different screen and the parity gaps run both ways.
The remaining surfaces after that: tenant app, payment page, web check-in.

Do not start the next surface without his word. He runs this as gather, state back, then write once.

## Traps carried forward

- A timed-out Linear save may still have succeeded. Verify with a read, never a retry.
- Verify a scripted edit with the shortest distinctive token. A pattern longer than a few words
  straddles line breaks in hard-wrapped markdown and the grep reports a clean miss.
- The 18 Sep MDR meeting record describes itself as uncertain: missing audio, medium-confidence
  attributions, fifteen unresolved reader disagreements. Use it for the shape of screens, not as
  proof of who decided what.
