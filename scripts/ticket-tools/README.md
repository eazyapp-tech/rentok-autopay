# Ticket tools

Scripts used on 18 Sep 2026 to file the 36 Autopay build tickets. Each ticket is one markdown file in the format in `drafts/ticket-format.md`, with a header block (`id`, `title`, `repo`, `labels`, `lane`, `cut_order`, `parent`, `blocked_by`, `waiting_on`).

Set `TICKETS_DIR` to the folder holding the ticket files. The default is `tickets`.

1. **`create.py`** files each ticket in its repo, with the title "[Autopay <id>] ...". The header block becomes a table at the top of the issue. It writes `_filed.json` (id to issue number and URL) and skips tickets already filed, so it is safe to run again.
2. **`links.py`** fixes references between repos, so a bare "#7002" in a marketplace issue points to the backend issue. It also adds a "Ticket ids used above" table linking every ticket a body mentions.
3. **`subs.py`** nests each ticket under the epic (rentok-backend#6846), and each bug under the ticket it blocks. The bug-to-ticket list inside it is the 18 Sep assignment; edit it for new bugs.

GitHub sub-issues need the child's database id, not its number: `gh api repos/eazyapp-tech/<repo>/issues/<n> -q .id`. Sub-issues work across repos in the organisation. An issue has only one parent.
