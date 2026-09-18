# Brief: turn the Autopay feature map into build tickets (drafts only, do not file)

## Context
RentOk (Indian rental property management) must reach 70,000 to 75,000 tenants on an approved, active UPI Autopay or e-NACH mandate by end of 1 Oct 2026 (CEO target, fixed). A new 0.4% UPI charge on link payments starts 15 Oct and RentOk cannot bear it. Today is 18 Sep 2026; the tenant app and manager app froze for release today, so anything new in those apps ships in the next release after 1 Oct. By 1 Oct only the backend, the payment page (Next.js marketplace), web check-in, manager web and WhatsApp can change.

## Sources of truth (read before drafting; the map wins on conflict)
- `~/rentok-autopay/map/feature-map.md` (version 4): the requirements. Read all of it.
- `~/rentok-autopay/decisions/decision-log.md` (rulings R1 to R54, N1 to N6) and `decisions/open-questions.md` (what is still unruled).
- `~/rentok-autopay/research/code-check-18sep.md` (18 Sep code check summary) and the full reviewer reports in `~/Sanchay Personal Projects/rentok/autopay-push/code-check-18sep/` (check-*.md). They cite current code.
- `~/rentok-autopay/research/cashfree-docs-answers.md`, `research/systems-map.md`, `walkthroughs/*.md`, `data/growth-math.md`.
- Filed bugs: `gh issue list -R eazyapp-tech/rentok-backend --label autopay --state open --limit 100` and the same for eazypg-marketplace, rentok_tenant_package, rentokmanagerflutter. Also the security and money issues listed in code-check-18sep.md.

## Code (read-only; never check out, never edit)
`git fetch -q origin` then `git show <ref>:<path>` and `git grep -n <pat> <ref> -- <paths>`:
- backend `~/rentok-backend` origin/master (dc98a0d78 or newer)
- marketplace (payment page `/p` and rebuild `/p2`, web check-in) `~/RentOk Marketplace/eazypg-marketplace` origin/main
- manager web `~/RM Manager WebApp/rentok-manager-web` origin/main
- manager app `~/RentOk_Manager_App/rentokmanagerflutter` origin/main
- tenant app `~/rentok_tenant_package` origin/main
Cite every code fact as `repo path:line` at the commit you read. If you could not verify, write "not verified".

## What a ticket is
One ticket = one piece of work a person does from start to finish (a workflow), across every surface it touches. Not a screen, not a route. It covers what happens before, during and after the tool, including where she lands afterwards. Bugs already filed are linked, never re-described at length.

## Ticket file format (one markdown file per ticket)
Start with this header block exactly:
```
id: <group letter><number, e.g. A1>
title: <plain outcome, who and what, e.g. "Tenant sets up Autopay on one screen, from any link or card">
repo: <rentok-backend | eazypg-marketplace | rentok-manager-web | rentokmanagerflutter | rentok_tenant_package>  (where most of the work is; other repos named in the developer section)
labels: autopay, <P0|P1|P2>, <needs-decision if any part waits on a ruling>
lane: <By 1 Oct | Next app release | After 1 Oct>, and split per part if mixed
parent: <S0|S1|S2|epic>  (S0 testing, S1 security gate, S2 safe debits; everything else sits directly under the epic)
blocked_by: <issue numbers, with 3 to 6 words each>
waiting_on: <open question or Cashfree question, in words, or "none">
```
Then these sections, in this order, with these exact headings:

1. `## Who this is for, and why it matters` : who (tenant, parent, manager, owner, RentOk support), what she came to do, and why it matters for the target or for trust. 3 to 6 sentences.
2. `## The workflow, start to finish` : numbered steps in her words, from the moment she meets it to where she lands after it is done, including what the product does next without being asked (messages, status changes, what the manager sees). Name every surface at the step where it appears.
3. `## Every state she can see` : a table: state | what she sees (exact words where the map gives them) | what she can do next. Include loading, empty, success, partial, failure, not eligible, already done, and "waiting on someone else". No dead ends: every state has a next action.
4. `## Rules behind it` : each rule as a plain sentence followed by its ruling number, e.g. "Her approved limit is her own regular dues, never a round number (R46)." Mark anything unruled "(proposed, waiting on Sanchay)".
5. `## Done when` : checkable statements a tester can tick, including the counts/messages/manager view, and the guardrails that apply (no double charge, no wrong late fine, etc.).
6. `## Not in this ticket` : what is deliberately elsewhere, with the ticket id that covers it.
7. `## For the developer` : this is the only place for code. Per repo: what exists today (file:line at commit, 1 to 3 decisive lines quoted or described), what changes, data or API shape where helpful, and which filed issues must land first. Name the Cashfree API/flow and flag [ask Cashfree] items.
8. `## Related` : links as `eazyapp-tech/<repo>#<n>` with a few words each, plus the map section name.
9. `## Sources` : regulation (RBI e-mandate framework 2026 by paragraph, the Finance Ministry MDR FAQ by question, NPCI circulars), Cashfree documentation URLs (from `research/cashfree-docs-answers.md`), other providers' docs where they confirm the same NPCI rule (`research/psp-docs-crosscheck.md`), and research files in this repo, a few words each.

**Citing rules.** A rule that comes from regulation or Cashfree, not a ruling, carries its source in "Rules behind it". Every Cashfree behaviour in "For the developer" carries its doc URL, marked [Cashfree docs]; an unanswered one is marked [ask Cashfree] with its question number in `drafts/cashfree-email.md`.

## Writing rules (sections 1 to 6 are read by the CPO and non-native English speakers)
- Plain everyday words, short sentences. No em dashes anywhere (use commas, colons, full stops). No: robust, seamless, leverage, delve, moreover, notably, furthermore, canonical, downstream, cohort, reconcile.
- The tenant is "she". Use the map's words: mandate, approved limit, regular dues, grace days, Option 1, Option 2, platform fee line, e-NACH.
- No bare references: every R number, issue number or ticket id carries a few words of its meaning.
- No code, file names or API names in sections 1 to 6.
- Never invent a ruling. If the map is silent on something the workflow needs, write it as "(proposed)" and list it in your final report as a gap.

## Output
Write each ticket to `/private/tmp/claude-501/-Users-eazypg-Sanchay-Personal-Projects/d3f57ae7-2f17-4178-8e9c-d7d397c05614/scratchpad/tickets/<id>.md`. Do not file anything, do not comment on GitHub.
Your final message: a table of your tickets (id, title, lane, parent, blocked_by), then a list of GAPS (things the workflow needs that the map does not decide), then every map line in your scope that you did NOT cover and why.
