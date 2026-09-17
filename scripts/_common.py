import json, sys, os, re, time
from pathlib import Path
HOME = Path.home()
STATE = HOME / ".claude" / "state"; LOGS = HOME / ".claude" / "logs"
STATE.mkdir(parents=True, exist_ok=True); LOGS.mkdir(parents=True, exist_ok=True)

def read_input():
    try: return json.loads(sys.stdin.read() or "{}")
    except Exception: return {}

def state_file(name, sid):
    d = STATE / name; d.mkdir(parents=True, exist_ok=True); return d / f"{(sid or 'unknown')[:16]}.json"

def load(p):
    try: return json.loads(p.read_text())
    except Exception: return {}

def save(p, obj): p.write_text(json.dumps(obj))

def transcript_turns(path):
    """Returns (user_prompts:list[str], last_assistant_text:str, written_paths:list[str]) for Claude Code or Codex transcripts. Fail open."""
    users, last_text, paths = [], "", []
    try:
        for line in open(path, errors="ignore"):
            try: o = json.loads(line)
            except Exception: continue
            t = o.get("type"); m = o.get("message") or {}
            if t == "user" and isinstance(m.get("content"), str) and not o.get("isSidechain"):
                c = m["content"].strip()
                if c and not c.startswith("<"): users.append(c)
            elif t == "assistant" and isinstance(m.get("content"), list):
                txt = " ".join(b.get("text", "") for b in m["content"] if b.get("type") == "text").strip()
                if txt: last_text = txt
                for b in m["content"]:
                    if b.get("type") == "tool_use" and isinstance(b.get("input"), dict):
                        fp = b["input"].get("file_path");
                        if fp: paths.append(fp)
            elif t == "response_item":
                p = o.get("payload") or {}
                if p.get("type") == "message":
                    parts = p.get("content") or []
                    txt = " ".join((x.get("text") or "") for x in parts if isinstance(x, dict)).strip()
                    if p.get("role") == "user" and txt and not txt.startswith("<"): users.append(txt)
                    elif p.get("role") == "assistant" and txt: last_text = txt
    except Exception: pass
    return users, last_text, paths

def log_event(name, **kv):
    """One line per hook run in ~/.claude/logs/hooks.log, so a silent hook can be audited later. Fail open."""
    try:
        with open(LOGS / "hooks.log", "a") as f: f.write(time.strftime("%Y-%m-%dT%H:%M:%S") + "\t" + name + "\t" + json.dumps(kv, default=str) + "\n")
    except Exception: pass

def context_tokens(path):
    """Current context size from the newest assistant usage block in a Claude Code transcript (0 if unknown). Fail open."""
    n = 0
    try:
        for line in open(path, errors="ignore"):
            if '"usage"' not in line: continue
            try: o = json.loads(line)
            except Exception: continue
            u = ((o.get("message") or {}).get("usage")) if o.get("type") == "assistant" else None
            if u: n = int(u.get("input_tokens", 0) or 0) + int(u.get("cache_creation_input_tokens", 0) or 0) + int(u.get("cache_read_input_tokens", 0) or 0)
    except Exception: pass
    return n

def handoff_files(cwd):
    """Every handoff file a session could have written: the repo's docs/handoffs, plus the two global folders."""
    import glob, subprocess
    pats = [str(HOME / ".claude/handoffs/*.md"), str(HOME / ".claude/docs/handoffs/*.md")]
    try:
        root = subprocess.run(["git", "-C", cwd or ".", "rev-parse", "--show-toplevel"], capture_output=True, text=True, timeout=5).stdout.strip()
        if root: pats.append(root + "/docs/handoffs/*.md")
    except Exception: pass
    out = []
    for p in pats: out += glob.glob(p)
    return out
