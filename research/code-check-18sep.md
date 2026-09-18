# Every Autopay and payment issue, checked against the code (18 Sep 2026)

**What was checked.**
- Every issue on the two older lists Sanchay shared, the claims Nimit made on the 18 Sep call, and twelve claims about the apps.
- Code read on 18 Sep: backend `dc98a0d78`, marketplace `66f9394f`, tenant app `afea1abe`, manager app `2e91d8ceb`, manager web `58583ff3`.
- Five reviewers read the code, split into security, money and links, Autopay, page data and electricity, and the apps. The most serious findings were then checked a second time by hand. Some counts come from read-only queries on RentOk's data tool.

**Why the details are not here.** This repo is public until Kamal has GitHub access. Several findings describe how money can be taken through holes that are still open. The full reports sit with Sanchay and go into this folder once the repo is private. The issues themselves are in private repos.

## The headline
- **Every older issue is still true.** None has been fixed.
- **33 new issues were filed**, 3 of them P0. Seven came from a second check while the build tickets were being written.
- **473 of the 781 current tenants with an active mandate have no debit queued.** Only 249 do. Without a backfill, those 473 are not debited in October while everyone believes Autopay is on. Causes:
  - #6999: an empty month ends Autopay;
  - #7045: a cancelled debit gets stuck;
  - #7046: a day change leaves nothing queued;
  - #7047: a pause is never rebooked.
- **Default-on Autopay would fail at setup for most properties** (#7054). Check-in and the backend read an unset fee payer differently; 81,319 properties have it unset.
- **Autopay cannot be tested in sandbox.** Every Autopay call to Cashfree is hardcoded to live. Testing before 1 Oct uses real money.

## New issues filed on 18 Sep
| Issue | Pri | In plain words |
| --- | --- | --- |
| rentok-backend#7038 | P0 | A payment can be recorded as online without Cashfree confirming it |
| rentok-backend#7039 | P0 | Old Autopay charge routes need no login |
| rentok-backend#7040 | P0 | Discounts are not checked when a payment is recorded |
| rentok-backend#7041 | P1 | A new short link can replace an old one |
| rentok-backend#7042 | P1 | A payment whose first check fails is never recorded |
| rentok-backend#7043 | P1 | The payment link generator needs no login |
| rentok-backend#7044 | P1 | A Cashfree verification secret is in the source |
| rentok-backend#7045 | P1 | A debit cancelled at Cashfree stops Autopay for good |
| rentok-backend#7046 | P1 | Changing the debit day leaves no debit queued |
| rentok-backend#7047 | P1 | A paused Autopay never restarts |
| rentok-backend#7048 | P1 | RentOk's own pre-debit WhatsApp only goes to one test schedule |
| rentok-backend#7049 | P2 | Cancelling Autopay wipes the tenant's grace days |
| rentok-backend#7050 | P1 | The Aliste webhook forwards a payment that failed its check |
| rentok-backend#7051 | P1 | Payout routes need no login |
| rentok-backend#7052 | P2 | Expired tenant logins keep working in some cases |
| rentok-backend#7053 | P2 | An Aliste recharge can silently do nothing |
| rentok-backend#7054 | P1 | Setup is refused wherever the fee payer was never set |
| rentok-backend#7055 | P2, needs decision | Turning Autopay off for a property does not stop debits |
| rentok-backend#7056 | P2 | Autopay links open check-in at step 1 |
| eazypg-marketplace#935 | P1 | Check-in never shows the Autopay terms |
| eazypg-marketplace#936 | P1 | A refused setup leaves the button spinning, with no message |
| eazypg-marketplace#937 | P1 | Check-in says "complete" without checking she approved |
| eazypg-marketplace#938 | P2 | A monthly fee is labelled "one-time" |
| eazypg-marketplace#939 | P2 | Session recording probably runs on the payment page |
| rentok_tenant_package#42 | P1 | The app's Autopay entry never shows |
| rentokmanagerflutter#304 | P2 | "Remind Tenant" says a message went out when none did |
| rentokmanagerflutter#305 | P2 | The Autopay settings sheet starts and saves as on |
| rentok-backend#7059 | P1 | Mandates have no end date, so they outlive the agreement |
| rentok-backend#7060 | P1 | Cancelling leaves a debit already sent to Cashfree running |
| rentok-backend#7061 | P1 | The setup reminder route needs no login |
| rentok-backend#7062 | P1 | A rent rise above her approved amount is taken partly, and nobody is told |
| rentok-backend#7063 | P2 | A debit with no matching record is mistaken for the ₹1 setup payment |
| rentok-backend#7064 | P2 | Only monthly rent can use Autopay, but other billing periods must too |
| eazypg-marketplace#943 | P2 | Check-in asks for Autopay before the agreement |

Comments with new evidence were added to #7005, #7039 (two marketplace pages still call the old routes), #7048, #7049, #7022 (engineering's fee plan, answered with the rulings), #6816, #6817, #6825, #6829, #6835, #6861, #6866, #6880, #6995, #6999, #7002, #7018, #7019 and to the epic #6846, which now lists what to fix before 30 Sep.

## Where Nimit's answers on the call were checked
| What Nimit said | What the code shows |
| --- | --- |
| Web check-in already looks up Autopay status; extract it into a shared function for the payment page | Right. The lookup is in `getCheckIn` and two app calls; the payment page's call has none yet, so the extraction is the fix (#6825) |
| The payment mode shows which payments Autopay made | Partly. Mode 205 is shared with the payment page, bookings and the app; only the order id prefix tells them apart (#6835) |
| An empty month does not end Autopay | That month takes no debit, but the next month is never booked (#6999) |
| "There is a cron, we need to review" | No scheduler in the code; both debit jobs are web routes called from outside, and the old one's routes are open (#7039) |
| The Pay button is not blocked | True today |
| A separate Autopay grace setting exists | At property level, on manager web only. At tenant level, one number drives both the debit window and the late fine |
| Not sure a queued debit is cancelled when she pays by hand; it needs to be | Right that it is not done: only whole mandates can be cancelled today, so a single-charge cancel needs Cashfree's confirmation (#7002) |
| The terms workflow exists and needs showing on screen (he was not sure) | The checkbox exists but is commented out, and the tick is never sent to the backend. Showing it is half the fix; saving it is the other half (#935) |
| The fee payer setting fails because no default is set | The monthly-fee dropdown never enables Save (rentokmanagerflutter#305) |

## What this changes in the plan (proposed, for the map pull request)
1. **Step 1 of the order** adds #7038, #7039 and #7040 to the login fix. It also adds #7018, with the warning that Autopay's own call must move inside the server first.
2. **Safe debits** add the backfill for the 473, plus #7045, #7046, #7047, #7048 and #7054.
3. **Check-in** adds #935, #936, #937 and #7056.
4. **Testing:** agree now how the fixes are tested with real money before 30 Sep, since there is no sandbox. For example, a few staff tenants on small amounts.
5. **Counting:** a mandate counts toward the target only if a debit is queued for it, or it is waiting for its first due. Otherwise the count includes Autopays that will never take money.
