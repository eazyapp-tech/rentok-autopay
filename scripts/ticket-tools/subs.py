import os,json,subprocess
D=os.environ.get("TICKETS_DIR", "tickets")
F=json.load(open(f"{D}/_filed.json"))
B="rentok-backend"; M="eazypg-marketplace"
def gid(repo,n):
    r=subprocess.run(["gh","api",f"repos/eazyapp-tech/{repo}/issues/{n}","-q",".id"],capture_output=True,text=True); return r.stdout.strip()
def add(prepo,pn,crepo,cn):
    cid=gid(crepo,cn)
    r=subprocess.run(["gh","api","-X","POST",f"repos/eazyapp-tech/{prepo}/issues/{pn}/sub_issues","-F",f"sub_issue_id={cid}"],capture_output=True,text=True)
    return "ok" if r.returncode==0 else r.stdout[-160:].replace("\n"," ")+r.stderr[-120:]
res=[]
for tid in ["S0","S1","S2","A1","A2","A3","A4","A5","A6","A8","A9","B1","B2","B3","B4","B5","B6","B7","C1","C2","C3","C4","C5","C6","D1","D2","D3","D4","D5","D6","D7","E1","E2","E3","E4","E5"]:
    res.append((f"epic<-{tid}",add(B,6846,F[tid]["repo"],F[tid]["number"])))
BUGS={
 "S0":[(B,6866),(B,7044)],
 "S1":[(B,n) for n in [6816,6861,7018,7038,7039,7040,7019,7041,7042,7043,7051,7061,6851,7050]],
 "S2":[(B,n) for n in [6995,7002,6999,7045,7046,7047,7005,7004,7049,6817,7048,6996,6998,7000,7003,7059,7060,7063]],
 "A1":[(B,6825),(B,7054),(B,7064)],
 "A3":[(M,915),(M,935),(M,936),(M,937),(M,938),(M,943),(B,7056)],
 "A4":[("rentok_tenant_package",42)],
 "A8":[(B,6869)],
 "B1":[(B,6835)],
 "C1":[(B,6829)],
 "C6":[(B,7062)],
 "D2":[("rentokmanagerflutter",304)],
 "D4":[(B,7055),(B,6880),("rentokmanagerflutter",305)],
 "E1":[(B,6830)],
 "E2":[(B,7006)],
 "E5":[(M,939)],
}
for tid,lst in BUGS.items():
    for repo,n in lst:
        res.append((f"{tid}<-{repo}#{n}",add(F[tid]["repo"],F[tid]["number"],repo,n)))
bad=[r for r in res if r[1]!="ok"]
print(len(res),"links,",len(bad),"failed"); [print(b) for b in bad]
