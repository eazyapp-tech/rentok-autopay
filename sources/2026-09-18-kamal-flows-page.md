# Kamal's flows page: text of the 9 figures (captured 18 Sep 2026)

Saved from the HTML copy Kamal shared on 18 Sep ("RentOk Autopay Flows"). Text only; the drawings are summarised in research/kamal-artifacts-check.md.

    RentOk Autopay Flows (Copy)
    Product · Payments
    UPI Autopay, drawn end to end
    Every flow behind the autopay redesign — the money case, the regulatory ceiling, the split-mandate fix, and the four surfaces a mandate is born on.
    As of 17 Sep 2026
    28 days to MDR
    PSP · Cashfree
    9 figures
    01
    The same rent, two rails
    From 15 October, collecting rent by hand costs 0.4%. Collecting it by mandate costs nothing.
    One month's rent
    ₹12,000
    Payment link · QR · Collect
    tenant pays by hand, every month
    0.4% MDR
    capped at ₹300
    ₹48
    per tenant, per month
    UPI Autopay mandate
    authorised once, debits itself
    Zero MDR
    NPCI-exempt
    ₹0
    forever, at any rent
    NPCI's MDR framework charges merchants 0.4% on person-to-merchant UPI above ₹2,000 and cannot be passed to the payer — but 
    recurring mandates are explicitly zero-MDR
    . At 10,000 tenants on ₹12,000 rent, the manual rail is roughly ₹48 lakh a year that autopay simply doesn't incur.
    02
    Where the silent-debit line falls
    Autopay debits without a PIN only up to ₹15,000. Above it, RBI requires the tenant to authenticate every single month.
    RBI additional-factor threshold
    ₹15,000
    PG bed · ₹12,000
    debits silently
    Independent flat · ₹30,000
    PIN tap every month
    silent — no PIN, ever
    UPI PIN required on every single debit
    ₹0
    ₹15,000
    ₹30,000
    ₹50,000
    monthly rent →
    The ₹1,00,000 ceiling everyone quotes applies only to NPCI's exempt categories — mutual funds, insurance premiums, credit-card bills. 
    Rent is not on that list.
     This one line is why CRED runs RentPay on the card rail instead, and it decides the shape of every flow that follows.
    03
    Split the mandate, not the debit
    One ₹30,000 mandate breaks the line every month. Three smaller mandates all stay under it — and all stay silent.
    Today · one mandate
    Proposed · three mandates
    ₹15,000 silent-debit line
    ₹30,000
    PIN tap, every month
    autopay that isn't automatic
    ₹12,000
    ₹12,000
    ₹6,000
    all three debit silently
    needs Cashfree sign-off before we commit
    The threshold applies 
    per mandate execution
    , not to a payer's total monthly debits to one merchant — which is how fintechs handled high-ticket SIPs and insurance premiums before those categories got their own exemption. Nothing published permits or forbids it for rent, so this needs a technical spike with Cashfree before it becomes the default path.
    04
    Setting it up at check-in
    The redesigned post-signup flow: the word "autopay" before the commitment, a real date grid, and a cancel button on the success screen.
    Check-in complete
    “Set up Autopay” — full screen
    never blocks check-in
    skip
    WhatsApp nudge
    3 days before next rent due
    ≤ ₹15,000
    one mandate, silent forever
    > ₹15,000
    2–3 split mandates, or a 1-tap approval
    Mandate summary
    ₹12,000 on 1 Oct, 1 Nov, 1 Dec
    Pick the debit date
    all 31 days live, not just the 1st
    Authorise in the UPI app
    their primary app pre-selected
    Autopay on
    12-month calendar + Pause / Cancel
    Three fixes carry most of the weight: the CTA says 
    autopay
     instead of “Schedule Rent Payment”, the summary spells out the next three debit dates rather than “starting from”, and cancelling is one tap from the screen that confirms setup — the parity RBI expects between starting and stopping.
    05
    Turning a payment link into a mandate
    The tenant who just paid by hand is the easiest autopay conversion there is — and the one most exposed to MDR.
    Link opened
    WhatsApp / SMS
    Pays this month
    one-time, ₹12,000
    Success screen
    + autopay checkbox
    “never pay manually again”
    Phone → UPI Intent
    authorised in 2 taps
    Desktop → UPI Collect
    enter VPA, approve in app
    Mandate live
    no app install needed
    Two details decide whether this works: the offer lands 
    after
     the payment succeeds, not before it, and the page reads the device — an Intent button silently fails on desktop, where the Collect flow is the only one that completes.
    06
    What CRED does that we don't
    CRED's entire autopay opt-in is one checkbox above the Pay button. The same slot on RentOk's pay-dues screen is empty.
    RentOk · pay dues, today
    UPI — GPay · PhonePe · Paytm
    Pay with cash (OTP)
    Enter UPI ID / VPA
    Pay with cards
    nothing here
    no autopay offer on this screen
    Pay ₹12,000
    the whole gap
    CRED · pay a bill
    Total due ₹8,013.88 · due in 6 days
    Pay total / minimum / other
    RBL Bank ••2711 · check balance
    saving ₹4 from CRED balance
    pay future bills with autopay
    cancel, pause & edit anytime
    Pay now
    It costs CRED one row and it asks nothing of a tenant who is already mid-payment. Add the same checkbox to the pay-dues screen and to the payment link — 
    alongside
     the dedicated setup flow, not instead of it — and every manual payment becomes a conversion surface.
    07
    Every state a mandate can be in
    The lifecycle Design has already drawn — each state maps to a numbered frame in the Figma spec.
    Snoozed
    tenant said not now
    03
    Offer
    on a bill, or on nothing
    01 · 02
    Required
    property insists
    04
    Started
    one approval left
    05
    On
    pays itself on the 5th
    06
    Failed
    didn't go through
    07
    Cancelled
    tenant or manager
    not now
    next bill
    approves
    property requires it
    approval done
    debit declines
    retry succeeds
    cancelled
    retries exhausted · re-offered later
    Numbered tags are the frames in 
    Autopay — every state and surface
    . Design has the states; none of it is live yet — the payload carries no autopay fields and the approve key is gated behind 
    rentok-backend#6829
     and 
    #6816
    .
    08
    What WhatsApp sends, and when
    Six messages around one debit. Only one of them is a legal requirement.
    Welcome
    set up in 30 seconds
    Day 0
    T−7d
    Rent due
    still no mandate
    Heads up
    keep the balance ready
    T−48h
    T−24h
    Pre-debit notice
    required by NPCI
    Receipt — or failure
    retry in 24 hrs, pay now
    debit day
    +7d
    Paid by hand again
    nudge to set up autopay
    The 
    T−24h pre-debit notice is an NPCI requirement
    , not a growth message — it ships in Phase 0 regardless of the rest. Everything else is capped deliberately: one welcome, one pre-due reminder, the two debit-day messages, and a monthly nudge. More than that buys opt-outs.
    09
    Four phases against one deadline
    Phase 0 has to land before 15 October — and it can't start until two backend tickets do.
    blocked until rentok-backend #6829 and #6816 ship
    OCT
    NOV
    DEC
    JAN
    FEB
    MAR
    15 Oct · MDR live
    Phase 0 · fix & comply
    new flow, pre-debit notice, T&C
    Phase 1 · default-on
    every new tenant sees the prompt
    Phase 2 · migrate the base
    50% of manual payers in 90 days
    Phase 3 · sustain
    85% portfolio-wide by mid-2027
    Phase 0 is the only phase with a hard external date. Everything in it — the redesigned setup flow, the mandatory pre-debit notice, the agreement clauses — is compliance or cost, not growth; the growth phases can slip, this one can't.
    Drawn from the RentOk UPI AutoPay product plan · 17 Sep 2026
    Full written plan →
