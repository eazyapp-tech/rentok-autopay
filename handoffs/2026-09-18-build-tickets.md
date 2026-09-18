# Handoff: 18 Sep 2026 night, the map turned into build tickets

**Objective.** Turn the feature map (version 4) into build tickets that engineering can work from, with the workflow thinking built in. File them, and make epic eazyapp-tech/rentok-backend#6846 the one place to track the push.

**Done**
- **36 build tickets filed**, listed in `map/build-tickets.md`, in the format in `drafts/ticket-format.md`.
  - Drafted by five reviewers working in parallel, each grounded in the code.
  - Checked three times: every map line has a ticket (10 gaps closed), the language is plain and matches the rulings, and the trimmed sections stay under 1,300 words.
- **The epic is rebuilt** with all 36 tickets as sub-issues and 56 bugs under the tickets they block. Every bug opens with two plain lines.
- **7 more bugs filed** (#7059 to #7064, marketplace#943), each checked twice against the code. Evidence added to #7005, #7039, #7048 and #7049.
- **Engineering's platform fee plan #7022** is answered with the rulings: the fee is a fixed bill line, not a percentage of online payments, and there is no charge for Autopay itself.
- **Rulings:**
  - R55 to R61: seven ticket conflicts, decided by Claude on Sanchay's instruction.
  - R62 (Sanchay): both options ship for 1 Oct, full scope, with a cut order (Option 1 and the full bulk rent change go first).
  - R30 now carries a note that its electricity sentence was replaced by R46 and R47.
- **Research:** other payment providers' docs cross-checked, in `research/psp-docs-crosscheck.md`.
  - Razorpay says NPCI allows one successful debit per billing cycle. If that holds for on-demand mandates, dues above ₹15,000 taken in parts, and "Request payment via Autopay", need a fallback.
  - The Cashfree email is sharpened to ask this first.
- **Sources saved:**
  - RBI's e-mandate framework text;
  - NPCI circular OC-223 (a scanned image);
  - 8 pages of Cashfree docs and its pricing page;
  - Razorpay and press captures.

**Where the sensitive material is.** This repo is public until Kamal has GitHub access. The material below is in the private companion repo eazyapp-tech/rentok-autopay-internal:
- the full code-check reports;
- the ticket texts as drafted, with the coverage table and cut order;
- the bug summaries;
- the frames and audio from Kamal's recording.

When this repo goes private, move them into `research/` and `map/`, and archive the companion repo.

**Next**
1. **Meta approval** for the 43 WhatsApp templates in [Autopay E1] (rentok-backend#7096). Start tomorrow; it takes days.
2. **Kamal sends the Cashfree email** (`drafts/cashfree-email.md`). Question 1, more than one debit per period, decides the parts and payment-request design.
3. **Sanchay speaks to Abhay** about #7022.
4. **Waiting on Sanchay:** open questions 1 to 9 in `decisions/open-questions.md`, including the five earlier points and the whitelabel brand.
5. **When Kamal has an account:** add him with write access, make this repo private, and merge in the companion repo.

**Not verified.**
- Clarity on the payment page (needs a browser check).
- The old debit engine's outside scheduler.
- Whether Cashfree can cancel a single debit after the notice.
- About 60 "(proposed)" product details inside the tickets, each listed in its ticket's "waiting on" line.

**Session:** d3f57ae7 (Claude Code, 17 to 18 Sep).
