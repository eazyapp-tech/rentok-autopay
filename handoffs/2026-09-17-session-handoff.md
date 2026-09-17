# Handoff: Auto Pay conversation review and rulebook (17 Sep 2026)

## Objective
Read every recorded Auto Pay conversation (NeoSapien pendant + Wispr Flow), merge them in date order, find the patterns, and propose one Auto Pay rulebook grounded in what the backend code does today.

## Where truth lives
- Published page (main output): https://claude.ai/code/artifact/001a1efe-871a-47fb-a9bb-97b46a642fee (doc id 001a1efe-871a-47fb-a9bb-97b46a642fee, prose node c299a6d3-9025, last rev 19). One open comment by Claude on the grace period row asks Sanchay to pick.
- Vault notes, `~/Documents/Obsidian Vault/RentOk/NeoSapien Digests/`:
  - 2026-09-16-evening.md (16 Sep, 3 NeoSapien recordings, second pass, gap table)
  - 2026-09-15-wispr-autopay-setup.md (15 Sep Wispr call)
  - 2026-09-16-autopay-merged-timeline.md (first merged version; the page is newer)
  - 2026-09-17-autopay-source-sweep.md (which sources have Auto Pay content, checked against full transcripts)

## Decisions, with reasons
- Chronological sections by date, later decisions marked "Changed later" / "Still conflicting": Sanchay asked for date division.
- Sources in scope: 19 May, 10 Aug, 7 Sep, 11 Sep (x2), 14 Sep, 15 Sep, 16 Sep (x3). Ten other recordings from 10 to 16 Sep were read in full and have no Auto Pay content. NeoSapien has nothing on 12 to 15 Sep.
- 7 Sep fee call covers platform and gateway fees only, not the Auto Pay fee.
- About 6 minutes at the end of the 16 Sep recordings were never transcribed; Sanchay does not remember them.
- Four patterns named on the page: no single rulebook (8 conflicts), on is not reachable, silent scope cuts, sequencing against fixed dates (24 Sep, 1 Oct, 15 Oct).
- Recommended next step: one written Auto Pay rulebook before more build. Recommended debit window: 11 Sep version (T-3 to T+12), because it does not depend on late fine settings the 16 Sep test says are not working. Not yet ruled by Sanchay.
- No Linear issues filed: standing rule to confirm before any Linear write.

## In progress at handoff
- Three read-only code traces on rentok-backend origin/master (b72e2490d, 17 Sep) in a scratchpad worktree: setup and money rules; lifecycle (pre-debit notice, failures, cancel, move-out, rent change); entry surfaces (check-in order, default on, manager status, reminders, pay page flag, unified check-in).
- A pending block "Proposed Auto Pay rulebook" is planted on the page above "Where things stand now".

## Update, same session
- Code traces done and key lines re-read by hand. Findings in vault note 2026-09-17-autopay-code-check.md and in the page section "Proposed Auto Pay rulebook" (rev 27). Work list now 42 items.
- Six money risks found in code: grace wipe on cancel, pre-debit reminder locked to a test record, no cancel on move-out, silent cap on rent increase, failures not told to tenant, legacy debit engine still reachable.
- Waiting on Sanchay: the debit window ruling, and permission to file Linear issues (standing confirm-first rule).

## Update 2, same session: full reconciliation
- Sanchay asked whether all apps, the payment page redesign and GitHub issues were checked. They were not; now they are. Summary in vault note 2026-09-17-autopay-reconciliation.md; page rev 34 replaces the "Proposed rulebook" with: joined-up picture, 11 Sep rulings vs team talk, every surface, blockers (filed and 10 new A to J), recommendation.
- Correction: the debit window was already ruled on 11 Sep (7-day grace default, any day later via #6829). My earlier pick contradicted it; removed.
- Key sources: marketplace worktree .claude/worktrees/rentoke-payment-redesign-ee444b/docs (LEDGER.md, handoffs/2026-09-11-autopay-design.md), epic rentok-backend #6846, Nimit plan in rentok/september-plan-audit.
- Next: Sanchay's answer on 1 Oct scope (first group recommended), then Linear mirroring (one Release 36 parent, 9 blockers + 10 new findings), only after his go. New findings A to J not yet filed on GitHub either.

## Update 3, same session: the push (feature-map gather stage)
- CEO target fixed (70-75k by 1 Oct); tenant pays Autopay charges by default, management can switch; RentOk and owners absorb nothing; RentOk keeps payment control; current code is not a limit. Saved to memory.
- Working folder: rentok/autopay-push/ (00 brief through 12, plus sources/ with the MDR FAQ and Kamal's plan). 05-inventory.md holds rulings R1 to R10, calls, exclusions, new information I1 to I8, open questions.
- Skills in use: feature-map (gather, sort, spar, write once), north-star-metric (04-success-metrics.md). R8: target counts approved active Autopay or e-NACH mandates.
- Five walkthroughs done (tenant, manager and owner, finance and ops, legal incl. TPAP, systems map) plus helper code findings.
- Issues filed on rentok-backend: #6995 (P0 double debit), #6996 (P1 V2 owner fee), #6998 (P1 RentOk charges split). New label: autopay.
- Open with Sanchay: RBI e-mandate para 10(a) vs R3 (asked once as new information); Q4 Autopay price (legal research says high risk); Q5 Autopay as the default way to collect; audio transcription; Linear mirroring after his go; Cashfree written question list.
- Next: state the complete picture, get rulings one by one, then write the map once on content-go.

## Next action (original list, steps 1 to 3 done)
1. Verify the three trace reports against the code (spot-check citations).
2. Fill the rulebook section: per disputed rule, what code does today (file:line), the conflicting meeting positions, recommended answer and reason.
3. Update conflicts and work list where code settles a question.
4. Ask Sanchay the one ruling needed; offer Linear filing after confirmation.

## Files touched
- The published page above (revs 1 to 19).
- The four vault notes above.
- This handoff file. Nothing committed.

## Session
- Claude Code desktop session in ~/Sanchay Personal Projects, 17 Sep 2026 (NeoSapien ids: f5327c86, 6dfe8017, 7ac09f93, ecea42ea, a17f21be, 59bf745d; Wispr ids: 4857d53b, a5db105c, c6464312).

## Update 4, same session (after compaction): fee model and debit rulings
- Rulings R11 to R18 are in rentok/autopay-push/05-inventory.md:
  - RentOk bears no payment cost, and the tenant never pays an Autopay charge as such.
  - Cost cover is a property setting: management, or the tenant through the ₹49 plus GST RentOk platform fee (the default), or the tenant through rent.
  - A rent or fee change starts on its start date for everyone.
  - Rent above ₹15,000 is taken in parts under one ₹15,000 mandate, with e-NACH only in the FAQ. The fee stays ₹49 for everyone.
  - "Autopay price" is dropped.
  - The monthly debit collects all monthly dues.
- New files:
  - 13-cost-cover-and-rent-change.md (bulk rent change workflow, and the Metabase rent spread with a median of ₹8,250);
  - 14-sorted-picture.md (spine, supporting, parked, cut).
  - The legal notes (10) have a split-debit addendum.
- Issues filed: #7002 (P1, a tenant who paid another way is still debited) and #7003 (P2, the debit record stores the wrong amount). Both are linked on #6846.
- Next: Sanchay reviews 14-sorted-picture.md and gives an explicit content-go. Then write the feature map once, run the bar checklist and md_lint, and update the published page.
- Nothing committed.

## Update 5: Kamal's plan v2, and rulings R19 to R21
- Kamal's plan v2 and his context file were reviewed in rentok/autopay-push/15-kamal-plan-v2-review.md. New Cashfree facts from their docs:
  - Cashfree sends the notice before each debit;
  - on-demand mandates cannot be paused or have their plan changed;
  - at most 3 retries per cycle;
  - setup can also take this month's payment (to confirm with Cashfree).
- Issue #7004 filed (P2, debit times sent to Cashfree in 12-hour format).
- R19: every mandate allows up to ₹15,000 per debit.
- R20: Autopay required by default for every property, which the property can turn off (existing `autopay_mandatory` setting).
- R21: "required" means chase, never block.
- Next: Sanchay's content-go on 14-sorted-picture.md, then write the feature map once and update the published page. Nothing committed.

## Update 6: feature map v2 written
- rentok/autopay-push/AUTOPAY-feature-map.md, version 2. It covers rulings R22 to R43, including Sanchay's corrections:
  - gateway charges are separate from the platform fee;
  - the platform fee is the property's charge (RentOk bills management ₹49 plus GST; the tenant line is ₹49 plus GST, or ₹58 where the property has no GST registration);
  - no confirm step and no waves;
  - a tenant-level "not required" switch;
  - managers request pause or stop;
  - allowed days run from the due day to the due day plus 7 (replaces #6829's any-day rule).
- Issues filed: #7005 and #7006 (backend), eazypg-marketplace#915.
- 14-sorted-picture.md is superseded by the map.
- Next: Sanchay's review of v2, then publish it as a page, mirror it to the vault, draft the Cashfree question list and the engineering tickets, and mirror to Linear after his go.
- Nothing committed.

## Update 7: Kamal's recording, second pass and audio
- The CRED part was re-read at one frame a second, including all 15 CRED Autopay FAQ answers. Notes are in 02. CRED automatically splits a bill above the mandate limit into several payments.
- The audio was transcribed locally with mlx-whisper (installed with pip --user): sources/2026-09-17-kamal-recording-transcript.md.
- New rulings:
  - R44: the approval runs on RentOk's own screen with UPI app links, and e-NACH goes through Cashfree's hosted page. Verified in Cashfree's docs.
  - R45: tenant self-service to change the day, pause and cancel, with management told each time. The pause limits are my calls.
- The map is now version 2.1.

## Update 8: team discussion rulings, R46 to R51 (map is now v2.2)
- **R46: two options at setup.** Option 1 is rent on her rent frequency (a fixed mandate). Option 2 is all dues on demand, recommended, with a limit equal to her itemised regular dues. This replaces the ₹15,000-for-everyone rule.
- **R47 and R51: Request payment via Autopay.** Covers any due except late fines, which the backend supports but keeps switched off. The debit runs 24 hours after the request; the tenant can approve or pay manually.
- **R48 and R50: pause is a tenant request.** The property approves it; no reply within 48 hours counts as approval. A pause can run up to the agreement end.
- **R49 and R50: the mandate ends at the agreement end date.** The renewal signing visit carries a new approval.
- **Research** on how other apps use UPI Autopay is in 18-discussion-17sep-night.md.

## Update 9: map version 3
- Cashfree research is in 19-cashfree-docs-answers.md. Findings that change the design:
  - on-demand retries need the controlled flow;
  - rent in parts is not confirmed;
  - Cashfree's split works by fixed percentage per mandate, not per due;
  - a mandate cannot be extended.
- Two cold reviews (about 60 findings in total) have been applied to AUTOPAY-feature-map.md, now version 3. Markers are now (agreed), (proposed), [Cashfree] and [ask Cashfree].
- Five items are marked "proposed" and need Sanchay's yes. After that, next steps are to publish, mirror to the vault, and draft the Cashfree questions and engineering tickets.
- Nothing committed.
