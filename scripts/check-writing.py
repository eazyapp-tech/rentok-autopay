#!/usr/bin/env python3
"""Writing rules: em dashes, banned words, bare references.

Two modes, one rule set:
  hook: PostToolUse on Write/Edit, warns and never blocks.
  gate: `python3 md_lint.py <file.md>` prints a success-only token and exits 1 on violations.
The gate mode checks any path you hand it, including handoffs, which the hook skips.
"""
import sys, re, glob; sys.path.insert(0, __file__.rsplit("/", 1)[0]); from _common import *

BANNED = r"\b(load-bearing|canonical|leverage|robust|seamless|delve|downstream|cohort|primitive|moreover|notably|furthermore|net-new|keystone|survivorship)\b"
BARE = r"\bper [A-Z]{1,4}-?\d+\b|\bsee above\b|\bas described earlier\b|\bas mentioned above\b"

# A line that declares the ban is not a line that breaks it. Without this the rule files,
# the stop lists and the skills that teach the rule all fail the gate they enforce, and a
# gate with false positives gets ignored, which is worse than no gate.
DECLARING = re.compile(r"\b(banned|ban|cut|stop.?list|never use|do not use|avoid|replace)\b[^.]{0,40}:", re.I)

def declares_the_ban(line):
    if DECLARING.search(line): return True
    return len(set(m.group(0).lower() for m in re.finditer(BANNED, line))) >= 3

CODE_SPAN = re.compile(r"`[^`]*`")

def violations(lines):
    hits = []
    for i, raw in enumerate(lines, 1):
        # a word inside a code span is a mention, not a use: `canonical` names the word
        l = CODE_SPAN.sub(" ", raw)
        if "—" in raw: hits.append((i, "em dash"))
        if declares_the_ban(l): continue
        if re.search(BANNED, l): hits.append((i, "banned word: " + re.search(BANNED, l).group(0)))
        if re.search(BARE, l) and "bare reference" not in l and 'never "per' not in l: hits.append((i, "bare reference: " + re.search(BARE, l).group(0)))
    return hits

def read_lines(fp):
    if os.path.getsize(fp) > 2_000_000: return None
    return open(fp, errors="ignore").read().split("\n")

# gate mode: one or more explicit paths. Sweep the whole folder a reader receives,
# never the main artifact alone: a cover note beside a clean sheet has carried a banned word.
if len(sys.argv) > 1:
    paths = [p for a in sys.argv[1:] for p in (sorted(glob.glob(os.path.join(a, "**/*.md"), recursive=True)) if os.path.isdir(a) else [a])]
    if not paths: print("no markdown files matched"); sys.exit(2)
    total = 0
    for fp in paths:
        try: lines = read_lines(fp)
        except Exception as e: print(f"cannot read {fp}: {e}"); sys.exit(2)
        if lines is None: print(f"{fp} is over 2MB, not checked"); sys.exit(2)
        hits = violations(lines)
        total += len(hits)
        for i, w in hits[:20]: print(f"{os.path.basename(fp)}:{i}: {w}")
    if total: print(f"WRITING-RULES: {total} violation(s) across {len(paths)} file(s)"); sys.exit(1)
    print(f"WRITING-RULES: CLEAN ({len(paths)} file(s))"); sys.exit(0)

# hook mode: warn, never block
d = read_input(); fp = (d.get("tool_input") or {}).get("file_path") or ""
if not fp.endswith(".md"): sys.exit(0)
if re.search(r"/(research|node_modules|skills-archive|tool-results|handoffs)/|/\.claude/projects/", fp): sys.exit(0)
try:
    lines = read_lines(fp)
    if lines is None: sys.exit(0)
except Exception: sys.exit(0)
hits = violations(lines)
if not hits: sys.exit(0)
ex = "; ".join(f"line {i}: {w}" for i, w in hits[:6])
print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": f"Writing check on {os.path.basename(fp)}: {len(hits)} issue(s). {ex}. Fix them now: replace em dashes with commas, colons, or full stops; swap banned words for plain ones; give every reference its meaning inline."}}))
