import os,re,json,subprocess
D=os.environ.get("TICKETS_DIR", "tickets")
F=json.load(open(f"{D}/_filed.json"))
IDRE=re.compile(r"\b(S[0-2]|A[1-9]|B[1-7]|C[1-6]|D[1-7]|E[1-5])\b")
titles={}
for tid in F:
    for l in open(f"{D}/{tid}.md"):
        if l.startswith("title:"): titles[tid]=l[6:].strip(); break
def fix_refs(body,repo):
    # full-name short forms
    body=re.sub(r"(?<![\w/])(?:eazypg-)?marketplace#(\d+)",r"eazyapp-tech/eazypg-marketplace#\1",body)
    body=re.sub(r"(?<![\w/])rentok-backend#(\d+)",r"eazyapp-tech/rentok-backend#\1",body)
    body=re.sub(r"(?<![\w/])rentok_tenant_package#(\d+)",r"eazyapp-tech/rentok_tenant_package#\1",body)
    body=re.sub(r"(?<![\w/])(?:rentok)?managerflutter#(\d+)",r"eazyapp-tech/rentokmanagerflutter#\1",body)
    body=re.sub(r"(?<![\w/])rentok-manager-web#(\d+)",r"eazyapp-tech/rentok-manager-web#\1",body)
    if repo!="rentok-backend":
        body=re.sub(r"(?<![\w/#])#((?:6[6-9]|7[0-1])\d\d)\b",r"eazyapp-tech/rentok-backend#\1",body)
    return body
for tid,v in F.items():
    repo,n=v["repo"],v["number"]
    body=subprocess.run(["gh","issue","view",str(n),"-R",f"eazyapp-tech/{repo}","--json","body","-q",".body"],capture_output=True,text=True).stdout
    if "## Ticket ids used above" in body: continue
    body=fix_refs(body,repo)
    ids=sorted({m for m in IDRE.findall(body) if m!=tid and m in F}, key=lambda x:(x[0],int(x[1:])))
    if ids:
        body+="\n\n## Ticket ids used above\n| Id | Ticket |\n| --- | --- |\n"+"\n".join(f"| {i} | [{titles[i]}]({F[i]['url']}) |" for i in ids)+"\n"
    r=subprocess.run(["gh","issue","edit",str(n),"-R",f"eazyapp-tech/{repo}","--body",body],capture_output=True,text=True)
    print(tid, "ok" if r.returncode==0 else r.stderr[:200], len(ids))
