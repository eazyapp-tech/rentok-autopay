# How to work in this repo

This repo is shared by Sanchay (CPO) and Kamal (payments product manager). Both work here through Claude Code, in separate sessions, often on different days. These rules let either of them pick up where the other stopped. Claude Code reads this file automatically at the start of a session.

## Start of every session

1. Read `STATUS.md` first. It says where the work stands, what changed last, and what is waiting on whom.
2. Read the newest file in `handoffs/`.
3. Read `map/feature-map.md`, the only document to build from.
4. Skim `decisions/decision-log.md` for the rulings, and `decisions/open-questions.md` for what is unanswered.
5. Run `git pull` before changing anything. The other person's session may have pushed since.

## End of every session

Do all four, before the session ends:

1. Update `STATUS.md`: the date, who worked, what changed, what is now waiting, and the next step.
2. Write a handoff in `handoffs/YYYY-MM-DD-topic.md`, using `handoffs/TEMPLATE.md`.
3. Run `python3 scripts/check-writing.py .` and fix what it reports in the files you touched.
4. Commit and push. Never leave work only on a laptop.

## Access for now (18 Sep 2026)

- The repo is public for a short while, because Kamal does not have GitHub access yet.
- Until he does, he sends his changes and new work to Sanchay. Sanchay's session adds them here, with Kamal named in the commit message and in STATUS.md.
- Once Kamal has an account, he is added with write access and the repo goes private again. Until then, treat everything written here as public.

## Who decides what

- **Product rulings are Sanchay's.** Anything that changes what the product does goes into `decisions/decision-log.md` as a new R number, with its date and what it replaced. Never quietly edit an old ruling.
- **Kamal owns the payment provider side:** what Cashfree confirms, pricing, and the technical shape of mandates. Answers from Cashfree go into `research/cashfree-docs-answers.md`, with the date and the source.
- **Anything unruled is proposed, not decided.** Mark it "(proposed)" in the map and add it to `decisions/open-questions.md`. Do not build on it.

## The three markers used in the map

- **(agreed):** follows from a ruling, and Sanchay has confirmed it.
- **(proposed):** waiting for his yes.
- **[Cashfree]** a behaviour confirmed in Cashfree's documentation; **[ask Cashfree]** one their documentation does not answer.

## Rules for the documents

- **The map wins.** Older documents carry a banner naming what replaced them. Leave them as they are; they show the reasoning.
- **Every number carries its source and date.** If something is not verified, write that it is not verified.
- **Every code reference carries file and line,** and says which branch it was read on.
- **Plain English.** Short sentences, no jargon, no em dashes, and every reference explained where it sits, so a reader who was in no meeting can follow it. `scripts/check-writing.py` checks the mechanical part.
- **Bugs found in code become GitHub issues** in `eazyapp-tech/rentok-backend` or `eazyapp-tech/eazypg-marketplace`, linked on the Autopay epic #6846, and listed in the README table. This repo holds no code.

## Working at the same time

- Small changes go straight to `main`. Pull first, push as soon as the change is done.
- **Changes to `map/feature-map.md` go through a pull request,** because it is the document everything else points to. Say in the description which rulings changed.
- If both of you are working on the same day, say so in `STATUS.md` under "Working now", so neither of you edits the same file.

## What is sensitive

This repo is public. Before adding anything, check that it holds no personal financial details, no tenant personal information, and no credentials. Business numbers, pricing and the decision record are fine; the recording of a colleague's bank and card screens is not.

## Where things live outside this repo

- **Code:** `eazyapp-tech/rentok-backend`, `eazyapp-tech/eazypg-marketplace`, the manager app, manager web and the tenant app.
- **Issues:** the Autopay epic is rentok-backend#6846.
- **Designs:** the two Figma files linked in the README.
- **The published page** of the merged conversation timeline, linked in the README.
