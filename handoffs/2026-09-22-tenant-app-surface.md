# Handoff: the tenant app as one surface (22 Sep 2026)

## What I set out to do

The third surface document, same shape as the manager app and payment page ones: an engineer with
no product context opens any screen in the tenant app and knows what Autopay means on it, what is
broken there already, and what is still somebody's decision.

## What changed

- **`surfaces/tenant-app.md` is new**, 320 lines. A 22 row map, three flows, a pointer table, five
  things broken today, the ship order, what not to touch, a parity table against the payment page,
  and what is waiting on a person.
- **`decisions/open-questions.md` gained item 23**, the parent app that does not exist.
- No rulings added. R64 is still not in the decision log, three days running.

## The framing that changed the document

**There are two tenant apps in this plan, and only one exists before 1 October.** Nothing enters the
apps after the 18 September freeze, and `rentok_tenant_package` has had no commit since 26 August.
So for the push this surface can do exactly one thing: whatever the server can say through a screen
the app already draws (R56). Everything else in the tickets for this surface is post-launch by
definition, and planning it into 1 Oct is planning a release that cannot happen.

That is why the map's Ships column has one row marked "before 1 Oct" and twenty marked "next
release", rather than the usual mix.

## What I checked, and how

Code read on `rentok_tenant_package` origin/main `afea1abe` and `rentok-backend` origin/master
`1498fcd62`, 22 Sep. Issue states checked the same day with `gh`.

- **Three Autopay doors in the app are built and dark**, from two missing wires. The status and the
  link are parsed at `tenant_app_status_res.dart:25-26` and never saved; `PrefsUtils.getInt`
  returns 0 for an unwritten key (`prefs_utils.dart:104-109`), so the banner hides because 0 is not
  2 and the profile row hides because 0 is not different from 0. The dues chip reads
  `is_autopay_scheduled`, which no backend code sends. All three are rentok_tenant_package#42, open;
  its line numbers have drifted and the block is at `tenant.ts:16429` today.
- **The one live door goes to check-in.** The server mints a fresh check-in short link on every app
  open and returns it as her Autopay link (`tenant.ts:16429-16445`), against R52 and into a flow
  that opens at step 1 behind KYC (#7056).
- **The app can offer her rent that Autopay is about to take.** The payment page leaves that row out
  of Pay all; the app has no such idea. The backend half is #7002; the app half is specified
  nowhere, because B4 puts the guard on "the page".
- **There is no parent app**, while R24 and A6 both route the parent through one. The tenant app
  holds a local guardian as a contact field only (`edit_tenant_model.dart:27-29`).
- **A4's open engineering question is answered, and the answer is yes.** `ui_data` is built per
  tenant inside `getTenantAppStatus`, where her Autopay status is already in scope, and the app
  draws it as a home bottom sheet with a web button (`basepage.dart:352-375`). The constraint is
  that it is one slot with three claimants already (`tenant.ts:16364`, `:16398`, `:16455`) and the
  last assignment wins.
- **Not verified:** whether a check-in type short link expires the tenant's older payment links. The
  expiry helper is called on payment link creation; I did not trace the check-in path.

## The pattern worth carrying to the next surface

Three doors dark in the app, and the whole Autopay system dark on the payment page. **RentOk has
more Autopay interface built than it has wired.** A screen audit reports all of it as missing and
sizes a build; the real work is a payload, a flag and a saved value. It cuts both ways: wiring is
fast, and a wire turned on today would publish wording that three rulings have since replaced.

## What is now waiting

- **On Sanchay:** open question 23 (the parent app), and R64.
- **On engineering, dated:** her Autopay link must be the payment page before the announcement is
  worth sending, and the payment page link move is dated 25 Sep.
- **Unruled build decisions**, recorded in the document rather than as open questions: whether the
  app's first Autopay screens are a web view of the payment page settings, and where an Autopay
  announcement sits in the one slot it shares with the update-app and review sheets.

## The next step

Two surfaces left: **manager web** and **web check-in**. My recommendation is web check-in next,
because A3 is the only door with its own separate consent path (the agreement carries the terms)
and it is the one place a tenant can be blocked, which R21 forbids. Manager web is then mostly the
manager app document read against a different screen inventory.

## Traps carried forward

- A widget that exists is not a widget that renders. Two guards on the same unwritten value failed
  in opposite directions here. Trace the value from the server to the render, not the component.
- A ticket can name a repository that does not exist. A6 names a parent app; there is none.
- `rentok_tenant_package` has been frozen since 26 August, so every "what does the app do today"
  answer is stable, and every "when can we change it" answer is after 1 Oct.
