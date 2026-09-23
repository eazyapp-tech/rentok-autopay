# The 23 September workflow and UI call, cleaned and checked

Sanchay, Kamal and the tech team, in one room, on the afternoon of 23 September. Nimit is addressed by
name; an engineer who knows the Cashfree integration speaks throughout. The recording runs about 133
minutes, of which roughly the first 100 are Autopay. NeoSapien memory `a3adbea1`, "Auto-Pay
Integration — Workflow and UI Consensus".

Read in full on 23 September, not from the summary. The cleaned transcript is in the private repo,
`rentok-autopay-internal/meetings/2026-09-23-autopay-workflow-and-ui-call.md`. Times below are minutes
into that recording. Speaker labels in the recording are unreliable, so positions are attributed only
where the recorder's own voice (Sanchay's) or the content makes it certain.

**NeoSapien's summary gets two things wrong.** It gives the length as 78 minutes, and it lists "AI
tools (Runway ML, image generation, MCP)" as a meeting topic. Those two passages (108:04 and 111:00)
are Sanchay dictating instructions to an AI agent for the brand-site work, picked up by the recorder.
They are not something the room discussed.

---

## In one paragraph

The room agreed to go live first with the Autopay that is already built, offered on the new payment
page, and to leave the question of who bears which charge for later. Setting up Autopay starts from an
**unticked checkbox** in the pay flow, with a "Know more" link. Behind it sits a short two-step
flow: step one is the benefits and what it pays, step two is the day and a preview of the next
debits. Approval goes through **Cashfree's hosted page for launch**, and our own screen follows as soon
as the server-to-server flow is ready. After setup she sees a confirmation, then a management screen
with the next three debits and three actions: change the date, pause, cancel. Pause is RentOk's own
(we stop debiting), runs to a date she picks, and takes effect **from the next cycle**. The Pay button
is never blocked. The working method was argued for most of an hour; it ended with Sanchay building
the UI mocks and the room sitting on them that evening at 8:30, with the backend contract following
the mocks.

---

## What the call was for

Kamal set it out at 16:38. Two days earlier they had agreed three things; the first is to **make the
Autopay that already exists easy to set up from the payment page**, for anyone who lands there. What
it will not get into: who bears which charge. The first release runs on whatever charge settings are
live today ("jaise abhi set up hua hua hai"). The reason to go first with exposure: the more tenants
see it, the more set it up, whether or not RentOk pushes it.

Timeline, as said: "live in two days" (04:16), later relaxed to "not tonight, then tomorrow, live the
day after" (60:12), which is 25 September.

## How the work gets done

The first twenty minutes and much of the middle were about method, not the product.

- **Kamal** wanted the changes closed on the HTML prototype first, then built. His worry (02:26): build
  it tonight, discover at 2 a.m. that it was never thought through, and do it twice.
- **Sanchay** said the prototype is a 512 KB single file ("monolith") and slow to change, the
  prototype stays the reference, and he was reading the live code to see where things go. He would not
  change things live in the room for three hours (20:32). He wants the changes gathered, then built,
  then shown to Kamal on the Ishika property, then demoed.
- **Kamal** (60:32): "the right way of building is to get consensus first". He wants a rough workflow
  locked and shared in front of everyone, not sent later by one person (63:36).
- **Resolved** (64:58 and 104:48): Sanchay builds the UI mocks, everyone sits on them at 8:30 p.m., and
  the backend contract is written from the mocks. Kamal expects only small backend changes, because
  nothing wholly new is being built.

## The flow, as the room left it

### 1. Where she starts

- A **checkbox in the pay flow, "Set up autopay", unticked by default** (Sanchay, 07:42; agreed 19:08).
- Where exactly: on the screen after she taps Pay, where the amount and the final Pay key are.
  That screen appears only where the property allows part payment; Kamal pointed out that properties
  without it are few (13:59).
- Kamal's refinement (14:29): extend the existing bottom sheet with the checkbox and share its footer
  and state, so it works whichever screen she is on.
- The benefits must be reachable: a **"Know more"** link beside the checkbox (15:51; the transcript
  hears it as "no more").
- Two ways in, both kept (57:51, 70:43): a **quick** one, the checkbox; and a **promotional or
  informational card** that opens the full flow.

### 2. What happens after she ticks it

- Untouched, the pay flow is exactly as today. Cash and every other method stay available (28:03).
- **The full flow is two steps** (71:48 to 72:23). Step one: the benefits, and what it pays. Step two:
  the day, with a preview of the next debits, their start and end, and any charges.
- **Both options stay: rent only, and all monthly dues.** An engineer argued for dropping a screen and
  going straight to Cashfree with her due date pre-picked, changeable later (53:03). **Kamal argued
  against it and the room kept the steps:** "autopay ka game hi pura trust ka game hai", Autopay is a
  game of trust, and a tenant who cannot see which date the money leaves on will not tick at all
  (50:27, 53:34, 55:16).
- **Sanchay called the current bottom sheet too crowded** and does not want that design (59:11). Kamal
  agreed on the principle, one screen that shows what is included and takes her input.

### 3. Approving with her bank

- **Wanted:** her UPI apps shown on our screen, and a tap opening that app directly, with no Cashfree
  page ("native", Sanchay, 29:19 to 29:47).
- **Not possible today** (the engineer, 29:48 to 30:43): the server-to-server flow is several steps,
  each with its own token. Estimated at one to two days on its own (62:24).
- **Agreed for launch** (Kamal, 47:00): tapping opens **Cashfree's hosted page**. The
  server-to-server flow is found and built in parallel, and it replaces the hosted page in one switch.
  With the hosted page, there is no point showing app icons on our screen first (31:05).
- iPhone: Sanchay read that the apps can be shown on iOS as well (34:08).
- PhonePe's documentation was opened for comparison (44:34 to 46:53): web integration, a token from
  client credentials that expires in 60 minutes, a sandbox, and targeting a specific app. Someone
  thought PhonePe might be easier (62:52).
- **e-NACH is not on the quick path.** It sits on the next or detail screen, and Cashfree's hosted page
  shows it at the end anyway (75:03 to 75:49).

### 4. How much she approves

- **"All monthly dues": ₹15,000 by default for now; "Rent only": her rent** (73:13 to 73:42), "until
  Cashfree's part comes".
- Kamal asked why not approve ₹21,000 and take ₹15,000 at a time (81:41). Sanchay: above ₹15,000 every
  debit needs her PIN. Kamal added a practical limit: with the mandate set above ₹15,000, Cashfree's
  page does not even offer UPI (82:22).
- **Above ₹15,000, split into parts:** a ₹40,000 rent shows as ₹15,000, ₹15,000 and the rest (80:15).
  Whether it can run on the same day depends on Cashfree switching something on "tonight", which
  someone had already asked for (32:10). If they do not, launch keeps the hosted page and the backend
  adjusts; the UI is built either way (32:46).
- **Paying today and setting up in one approval** (Kamal, 74:19): her pending dues go in as the
  approval amount and are taken there and then, and the mandate is set up in the same step; the
  callback carries both. The ₹1 to ₹2 mandate charge is RentOk's, not hers (74:45).

### 5. After she approves

- **Confirmation** (77:59): your dues are cleared, autopay is set up, it goes on this date every month,
  you are in control and can change it at any time.
- **Back on the payment page's home:** "Autopay is set up, next payment on…", which opens a **detail
  screen** (82:49): the schedule, what the mandate covers and in whose name, and the actions.
- **The schedule shows the next three debits** (79:34), no further than her agreement end or move-out
  date (79:51). Sanchay first said five or six. Kamal worried that a long list frightens a tenant who
  may leave in two months. The list is kept for transparency, because the person whose call it is
  asked for it (79:20 to 80:05).
- **Three actions: change the date, pause, cancel** (80:37). These were already agreed with Abhay the
  day before.
- **Editing needs her to log in** by phone, and every change sends her a WhatsApp message (83:38).
- **States the screens must also show**, listed by Kamal (85:17): a new debit amount with a Pay
  option; after a cancellation, a way to set it up again; an interrupted setup that resumes where she
  left off (87:30); after a pause, a large "Resume" card (87:38).
- **A cancellation is told to the manager too**, on screen and by message (85:53).

### 6. Pause, change date, and the Pay button

- **Pause is RentOk's own.** We stop taking debits; the mandate stays live at Cashfree, and her UPI app
  will still show it active. Our screen says we will not debit until she resumes (88:39 to 89:15).
  The engineer suggested pausing it in the UPI app's records too (89:16).
- **Pause runs to a date she picks** on a calendar, not a number of months (90:23).
- **Pause takes effect from the next cycle, never the current one** (Sanchay, 90:38). Otherwise a
  tenant pauses the day before every debit. To stop this cycle, she uses her own UPI app.
- **Changing the date:** two or three days before each debit she gets a message: it goes on the 5th,
  your grace runs to the 7th, you can move it until then (Kamal, 92:26).
- **The Pay button is never blocked** (Sanchay, 92:51). While Autopay is on it stays, as a secondary
  button; after a pause it becomes the main one. Kamal: if she then pays by UPI, the UPI charge
  applies instead (93:12).
- **A debit already sent can still be stopped**: RentOk cancels the one it raised (94:35, 96:06).

---

## Where the call disagrees with what is already ruled

| The call says | Already ruled or recorded | What has to happen |
| --- | --- | --- |
| "All monthly dues" approves **₹15,000 by default** for everyone, for now (73:13) | **R68**, logged at 15:09 the same afternoon: her fixed dues plus ₹2,000, rounded up to the next ₹5,000, never above ₹15,000, so a ₹6,000 tenant approves ₹10,000 | Sanchay's call. Either the flat ₹15,000 is a launch shortcut, which is simple because R68's numbers are backend settings and can start at ₹15,000, or R68 stands from day one. The page already reads the ceiling from the backend, so either works without a page change |
| Approval through **Cashfree's hosted page** for launch, our own screen later (47:00) | **R44**: the approval step lives on RentOk's own screen | R44 stays the goal; launch runs hosted. Worth recording, because the 2.7 attempts per stalled tenant measured today (`research/2026-09-23-setup-flow-evidence.md`) happen on that hosted page |
| The tenant **pauses herself**, from the next cycle, to a date she picks (88:39 to 91:21) | **R48**: a pause is a request the property approves, with silence counting as yes after 48 hours. Open question 30 asks exactly this | The call treats pause as hers, with no approval mentioned. Open question 30 now has his spoken lean, and still needs his word |
| Pause **only from the next cycle** | Nothing ruled | A refinement worth putting to him: allow a pause for this cycle **until the bank's notice goes out** (about 25 hours before the debit), and from the next cycle after that. The loophole is pausing after the amount is locked; before the notice, a pause costs nothing, and forcing her into her UPI app instead can mean a failed debit and a bounce charge from her bank |
| The first release runs on **today's charge settings** ("as currently set up") | **R64**: one Platform fee on the tenant by default; the Autopay setup and monthly fees are deleted | Needs a yes from him: does launch deliberately ship before R64, or should the charge settings change before 25 Sep? |
| Pay today **inside the same approval**, dues as the approval amount (74:19) | **R70**: until Cashfree answers question 2, she pays today first, then sets up | Cashfree's own API has a switch for it: creating a subscription takes `authorization_amount_refund` (their example sets it to `true`). So keeping the approval amount as her payment is a documented setting. What is still unknown is the largest amount allowed, and above ₹15,000 the PIN rule applies |
| Manage actions "invoked from the manager app" (81:19) | **R39**: a manager may ask, see or request, never do | Probably means the manager app shows the same schedule. If it means the manager can pause or cancel her mandate, it contradicts R39 |

## What the call confirms

- **Cashfree's cancellations are being missed** (the engineer, 86:20): Cashfree sends the status under a
  different word ("changed"), our code reads another, and "kisi ka cancellation hume pata hi nahi
  chalta", we never learn that anyone cancelled. This is `rentok-backend#7124` (P0).
- **The notice before a debit is not being sent** (94:52 to 95:27): Kamal described two calls, the
  notice and the debit. The engineer said only one is made today, and that the server-to-server flow
  needs two. This is the `notify-mandate` gap recorded on `rentok-backend#7078`.
- **Above ₹15,000 is blocked at our own account**, consistent with Cashfree question 11 (AFA and 2FA not
  enabled). Kamal saw it on the hosted page: UPI does not appear when the mandate is above ₹15,000.
- The unticked checkbox matches the evidence gathered the same afternoon: CRED shows Autopay as an
  unticked row, and a pre-ticked agreement box is the pattern our legal notes record as fined.

## Feedback on the setup sheet built earlier the same day

Two remarks were made while the team looked at the payment page, most likely at the branch opened in
the browser pane just before the call:

- "all monthly… this should not come like this, it looks completely broken" (10:01)
- "I don't want this design; look, the bottom sheet is completely full" (59:11)

Both point the same way as the two-step flow the room agreed: one sheet holding the option, the day
grid, the benefits and the terms is too much at once.

## Other threads in the same recording

- **The association event** (34:20 to 37:50, 40:24 to 42:11, 67:53 to 70:40): about 170 payments (159
  after removing two), 200 to 250 contacts, 200 demos expected to give 200 to 300 registrations, ₹1
  lakh of direct sponsorship, travel and marketing budget, five volunteers. Point made: without
  registrations and a verified OTP, there is no demo to give.
- **Tenants told to pay by bank transfer to avoid the UPI charge** (96:53 to 104:21). Some owners are
  telling tenants, on WhatsApp groups, to add the property's current account as a payee. The room
  debated P2P and P2M: a UPI transfer to a personal account is person to person and free; to a current
  account's QR it is person to merchant and the bank charges 0.4%, even with no gateway (said to be
  confirmed, and IDFC said the same). IMPS costs about ₹5. Sanchay: 99% sure, and 15 October will show.
  This supports the "do not pay this by UPI" warning planned for the virtual account.
- **Property access** (105:47): an owner who gave someone two or three properties finds the web home
  dashboard showing all of them, while the app shows the right ones. Account level against property
  level. A ticket was raised with Ankit.
- **Login screen** (117:13): Nitish reviewed and changed it, and it has gone back to how it was before.
  The WhatsApp and Gmail icons used to sit at the bottom.
- **Leads from the microsites** (126:53): use Karan's document, the format already used for JustDial
  and MagicBricks: the URL `/microsite/<easyId>`, with the property's easyId appended, sending JSON.

## What needs Sanchay

1. **The ceiling at launch:** a flat ₹15,000 for "all monthly dues", as said in the room, or R68's rule
   from day one. Recommended: **R68 from day one.** It is already built on both sides of the page,
   costs nothing extra, and a ₹6,000 tenant approving ₹10,000 rather than ₹15,000 is exactly the trust
   Kamal argued for.
2. **Pause:** whether the tenant pauses herself (open question 30), and whether "next cycle only" should
   become "until the notice goes out". Recommended: **hers to pause, allowed until the notice.**
3. **Charges at launch:** today's live settings, or R64's Platform fee, before 25 September.
4. **Hosted approval for launch**, recorded as a step on the way to R44 rather than a change to it.

Checked against rulings R1 to R70.
