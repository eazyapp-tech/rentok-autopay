# Autopay in pictures

These diagrams draw `feature-map.md`. If a diagram and the map disagree, the map wins: fix the diagram in the same pull request as the map change. GitHub draws them on its own. The published interactive page uses the same diagrams, copied from this file.

Rule numbers such as R46 point to `decisions/decision-log.md`.

## 1. A tenant's journey

```mermaid
flowchart TD
    subgraph Doors["Where she meets it"]
        A1["Check-in, after the agreement"]
        A2["WhatsApp from RentOk or her manager"]
        A3["Card on the tenant app home"]
        A4["Tick above Pay: pay now and turn on Autopay"]
        A5["Signing step after a rent change or renewal"]
        A6["Link sent to her parent"]
    end
    Doors --> S["One setup screen, opened at the approval step"]
    S --> C{"She picks one option (R46)"}
    C -->|"Option 1"| O1["My rent, every rent period: a fixed amount"]
    C -->|"Option 2, recommended"| O2["All my dues, when they're due: up to her regular dues"]
    O1 --> AP["Approve on RentOk's screen: UPI app, QR code or UPI ID, bank account through Cashfree"]
    O2 --> AP
    AP --> OK["Autopay is on: next three dates, change day, pause, cancel"]
    OK --> M["Every period: heads-up, bank notice, debit, receipt"]
    M --> M
    M --> CH{"Something changes"}
    CH -->|"Rent or fee change"| RC["Rent change flow, new approval if above her limit"]
    CH -->|"She asks to pause"| P["Manager or owner approves, 48 hours of silence counts as yes"]
    CH -->|"She cancels"| X["Dues show Pay now, chased again, never blocked"]
    CH -->|"Agreement ends"| R["Renewal asks for a new approval 15 days before"]
    RC --> M
    P --> M
    R --> M
    M --> OUT["Moves out: last debit, then the mandate is cancelled"]
```

## 2. Every state an Autopay can be in

```mermaid
stateDiagram-v2
    [*] --> NotSetUp
    NotSetUp --> Started: opens setup
    Started --> NotSetUp: leaves halfway
    Started --> WaitingBank: chooses bank account (e-NACH)
    WaitingBank --> On: bank approves, 24 to 48 hours
    Started --> On: approves in her UPI app
    On --> PauseRequested: she asks to pause
    PauseRequested --> Paused: property approves, or 48 hours pass
    PauseRequested --> On: property declines
    On --> Paused: she pauses in her UPI app
    Paused --> On: pause ends or she resumes
    On --> Failed: debit fails
    Failed --> On: a retry succeeds
    Failed --> On: next period, dues sent as a link this time
    On --> NeedsApproval: her regular dues rise above her limit
    NeedsApproval --> On: she approves the new amount
    On --> EndingSoon: agreement ends within 15 days
    EndingSoon --> On: she renews
    EndingSoon --> Ended: agreement end date passes
    On --> Cancelled: she cancels, or RentOk stops it on request
    Cancelled --> Started: set up again
    Ended --> Started: set up again
    On --> [*]: she moves out
    NotSetUp: Not set up
    WaitingBank: Waiting for bank approval
    PauseRequested: Pause requested
    NeedsApproval: Needs new approval
    EndingSoon: Ending soon
```

Counts toward the target: On, Pause requested, Failed (still active), Needs new approval, Ending soon. Does not count: Paused, Ended, Cancelled, Not set up, Started, Waiting for bank approval.

## 3a. One debit, Option 2 (all dues, on demand)

```mermaid
sequenceDiagram
    autonumber
    participant T as Tenant
    participant R as RentOk
    participant C as Cashfree
    participant B as Her bank
    participant M as Manager
    R->>R: Bill ready, advance and credits used first
    R->>T: WhatsApp 2 days before: amount, breakdown, check balance
    R->>C: Send notice for the exact amount (controlled flow)
    C->>B: Pre-debit notice
    B->>T: Bank notice, at least 24 hours ahead
    Note over R,C: Wait at least 25 hours. The amount is now fixed.
    R->>C: Take the debit, in NPCI's allowed hours
    C->>B: Debit up to 15,000 per part
    alt Paid
        B-->>C: Success
        C-->>R: Payment success
        R->>T: Receipt: Paid by Autopay
        R->>M: Shows as paid
    else Failed
        B-->>C: Failed, with a reason
        C-->>R: Payment failed
        R->>T: Same day: reason, Pay now, next retry
        R->>M: Alert with the reason
        R->>C: Up to 3 retries, timed near salary day
    end
    Note over R,C: Dues above 15,000: the next part starts after the last one, one notice at a time
```

## 3b. One debit, Option 1 (rent on a fixed schedule)

```mermaid
sequenceDiagram
    autonumber
    participant T as Tenant
    participant R as RentOk
    participant C as Cashfree
    participant B as Her bank
    R->>T: WhatsApp 2 days before: amount and check balance
    C->>B: Cashfree sends the notice on its schedule
    B->>T: Bank notice, at least 24 hours ahead
    alt She already paid another way
        R->>C: Cancel this period's debit
        R->>T: Link for anything left
    else Normal period
        C->>B: Debit the fixed amount
        alt Paid
            B-->>C: Success
            C-->>R: Payment success
            R->>T: Receipt: Paid by Autopay
        else Failed
            C->>B: Cashfree retries up to 3 times, an hour apart
            R->>T: Reason, Pay now link
        end
    end
    Note over T,B: Above 15,000 her bank asks for her UPI PIN on every debit
```

## 3c. A payment request for an extra bill (R47)

```mermaid
sequenceDiagram
    autonumber
    participant M as Manager
    participant R as RentOk
    participant T as Tenant and parent
    participant C as Cashfree
    M->>R: Request payment via Autopay on a due
    alt Option 2 and Autopay is on
        R->>T: Requested 5,000 for electricity, paid from Autopay after 24 hours
        alt She taps Approve now, or does nothing
            R->>C: Notice, then debit after the waiting period
            C-->>R: Paid
            R->>M: Paid by Autopay
        else She taps Pay manually
            R->>T: Pay now link
        else Above her limit
            R->>T: Approve a new limit in her UPI app, or pay manually
        end
    else Option 1, paused, cancelled or not set up
        R->>T: Normal Pay now request
    end
```

## 4. The three charges, and where money goes

```mermaid
flowchart LR
    T["Tenant"] -->|"Rent and bills"| P["Payment via Autopay, link, card or cash"]
    T -->|"Platform fee line: 58, or 49 plus GST if the property is GST-registered. On by default, the property decides"| P
    T -->|"Gateway charge, only on card, net banking and similar methods, as today"| GW["Payment gateway"]
    P --> CF["Cashfree"]
    CF -->|"Owner's share"| O["Property or owner"]
    O -->|"RentOk service charge: 49 plus GST per billed tenant a month, taken from the payout"| RO["RentOk"]
    O -->|"New 0.4% UPI charge on link payments above 2,000, from 15 Oct"| CF
    X["Autopay debit: no 0.4% UPI charge"] -.-> CF
```

## 5. A pause request (R48, R50)

```mermaid
flowchart TD
    A["Tenant asks: skip next debit, or pause until a month"] --> B["Manager and owner alerted, status Pause requested"]
    B --> H{"Decision within 48 hours?"}
    H -->|"Approve"| Y["Paused until the chosen month"]
    H -->|"No reply in 48 hours"| Y
    H -->|"Decline"| N["Autopay continues, she is told"]
    Y --> O1["Option 1: RentOk pauses the mandate at her bank"]
    Y --> O2["Option 2: RentOk raises no debits"]
    O1 --> D["Paused periods show Pay now"]
    O2 --> D
    D --> E["Pause ends on its own, with a message before the next debit"]
    U["She pauses in her UPI app"] --> Z["Takes effect at once, the manager is told, only she can resume"]
```

## 6. The push to 1 Oct

```mermaid
flowchart LR
    S0["0. Test with real money on staff tenants, no sandbox"] --> S1["1. Login and fake-payment fixes"] --> S2["2. Safe debits: double charge, paid elsewhere, debits never queued plus backfill, move-out, debit time, allowed days"]
    S2 --> S3["3. Check-in: set up later, per-tenant switch, fee payer fix, honest success, terms"]
    S3 --> S4["4. One setup screen with two options"]
    S4 --> ON["Autopay on and required for everyone"]
    S2 --> MF["Money fixes before the first October debit: payouts, GST, saved amounts"]
    ON --> W["Messages to every tenant not on Autopay, biggest push 30 Sep evening and 1 Oct morning"]
    W --> T["Target counted at the end of 1 Oct: 70,000 to 75,000"]
```

```mermaid
timeline
    title Fixed dates
    18 Sep : App release freeze
    24 Sep : Release 36 goes public : Team offsite starts
    27 Sep : Team offsite ends
    30 Sep : Biggest push, evening
    1 Oct : Platform fee starts, after notice : Target counted at end of day
    15 Oct : New 0.4% UPI charge begins
```
