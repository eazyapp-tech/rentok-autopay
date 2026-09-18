import os,re,json,subprocess,glob
D=os.environ.get("TICKETS_DIR", "tickets")
OUT=os.path.join(D,"_filed.json")
filed=json.load(open(OUT)) if os.path.exists(OUT) else {}
order=["S0","S1","S2","A1","A2","A3","A4","A5","A6","A8","A9","B1","B2","B3","B4","B5","B6","B7","C1","C2","C3","C4","C5","C6","D1","D2","D3","D4","D5","D6","D7","E1","E2","E3","E4","E5"]
CUT={"1":"cut: 1 keep","2":"cut: 2 second","3":"cut: 3 first"}
def parse(tid):
    txt=open(f"{D}/{tid}.md").read()
    head,_,rest=txt.partition("\n## ")
    h={}
    for line in head.splitlines():
        m=re.match(r"^([a-z_]+):\s*(.*)$",line)
        if m: h[m.group(1)]=m.group(2).strip()
    return h,"## "+rest
for tid in order:
    if tid in filed: continue
    h,body=parse(tid)
    repo=h["repo"].split()[0]
    rows=[("Lane",h.get("lane","")),("Cut order (R62)",h.get("cut_order",""))]
    if h.get("cut_order_split"): rows.append(("Cut order split",h["cut_order_split"]))
    rows+= [("Parent",h.get("parent","epic")+" (under Autopay epic eazyapp-tech/rentok-backend#6846)"),("Blocked by",h.get("blocked_by","")),("Waiting on",h.get("waiting_on","")),("Repos",h.get("repo",""))]
    table="| | |\n| --- | --- |\n"+"\n".join(f"| **{k}** | {v.replace('|','/')} |" for k,v in rows)
    intro=f"Autopay build ticket **{tid}**, written from the Autopay feature map (https://github.com/eazyapp-tech/rentok-autopay/blob/main/map/feature-map.md, version 4) on 18 Sep 2026. Plain requirements first; code is only in \"For the developer\".\n\n"
    full=intro+table+"\n\n"+body
    labels=[l.strip() for l in h["labels"].split(",")]
    c=h.get("cut_order","")[:1]
    if c in CUT: labels.append(CUT[c])
    args=["gh","issue","create","-R",f"eazyapp-tech/{repo}","--title",f"[Autopay {tid}] {h['title']}","--body",full]
    for l in labels: args+=["--label",l]
    r=subprocess.run(args,capture_output=True,text=True)
    url=r.stdout.strip()
    if not url.startswith("http"): print("FAIL",tid,r.stderr[:300]); break
    filed[tid]={"url":url,"repo":repo,"number":int(url.rsplit("/",1)[1])}
    json.dump(filed,open(OUT,"w"),indent=1)
    print(tid,url)
