# Friedland — Reserving for Reinsurance (2022)

Tasks: **A15, A16, A17**

Official: [Exam7_Study_Note_Friedland.pdf](https://www.casact.org/sites/default/files/2022-11/Exam7_Study_Note_Friedland.pdf)

This is the long one. Treat it as three exam chapters: what reinsurance is, why primary methods break, how to actually book ceded / assumed unpaid.

## A17 — Function and types

**Function:** insurance for insurers. Spread risk, protect surplus, stabilize results, increase capacity, support withdrawal from a line, provide expertise / capital relief.

**Forms you must be able to define and contrast**

| Form | How it attaches | Typical reserving headache |
|---|---|---|
| Quota share | Fixed % of every loss (and usually premium) | Cleanest. Ceded = % of gross if terms align. Watch ceding commission, sliding scale, loss corridors, caps. |
| Surplus share | % varies by policy limit vs a line | Mix: the ceded percentage is not one number. |
| Per-risk / per-occurrence excess | Pays above a retention on one risk or one occurrence | Thin data, long development, clash, definition of occurrence |
| Catastrophe excess | Pays above a retention on an event / aggregate of an event | Few points, demand surge, reinstatements, hours clause |
| Aggregate / stop-loss | Pays when the subject loss ratio or loss $ exceeds a threshold | Binary: IBNR in the layer depends on how close the subject is to the attachment |
| Facultative | Individual risk | Almost no triangle. Use exposure / BF / ground-up implied |
| Treaty | Book of business | You may have a triangle, but it is still not a primary triangle |
| Retrocession | Reinsurance of reinsurers | Even thinner; more clash and more contract complexity |

Also know: **admitted vs non-admitted**, **prospective vs retrospective** (loss portfolio transfer, ADC), **finite / structured** risk transfer (you still need a reserve; the accounting is not a free lunch), **multi-year** and **losses-occurring vs risks-attaching**.

## A15 — Why you cannot just run chain ladder on the ceded triangle

Primary methods assume a stable, high-volume, homogeneous triangle. Reinsurance data usually has:

- **Low frequency, high severity** — one claim owns a year
- **Reporting lag** that is longer (primary has to know, then report to the reinsurer, then the reinsurer opens a file)
- **Partial information** — bordereaux are late, incomplete, or at the wrong limit
- **Changing program structure** — last year’s 5 xs 5 is this year’s 10 xs 10; you cannot stack those years in one triangle without restating
- **Clash and cat** — dependence across “accident years” and across cedents
- **Inuring reinsurance** — the subject loss is already net of something else
- **Commutations, sunset clauses, aggregates, reinstatements** — the “ultimate” is contract-shaped, not ground-up-shaped
- **Premium that develops** (adjustable premium, reinstatement premium, sliding-scale commission) — Teng/Perkins logic on a treaty

**Adjustments before you steal a primary method**

1. Restate history onto the **current structure** (same attachment, limit, basis).
2. Separate attritional / working-layer from cat / clash.
3. Use **exposure** (on-level subject premium, limits profiles, ILFs) — this is Clark Cape Cod / BF territory, not CL.
4. Develop **reported counts and average severity** separately when dollars are unusable.
5. Apply **report-lag** factors from industry or from a large broker study when the triangle is empty.
6. Gross-up from ground-up primary indications with a size model (Sahasrabuddhe) when you are the cedent and you trust the primary ultimate.
7. Credibility-weight any thin treaty triangle toward the exposure method (Brosius / Benktander instinct).

## A16 — Calculating ceded (and assumed) unpaid

Pick the method from the data you actually have.

### If you are the **cedent** (primary company buying cover)

Often the best estimate is:

\[
\text{Ceded unpaid} = g(\text{gross unpaid}, \text{program terms})
\]

not an independent ceded chain ladder. Work policy-by-policy or segment-by-segment through the tower. Watch:

- Ground-up vs limited vs excess consistency (A4 papers)
- Whether ALAE is treated pro-rata or in addition
- Whether the gross ultimate already includes events that do not recover (below retention, excluded perils, exhausted limits)
- Reinstatement premium due if the layer is expected to burn (a premium *liability*, A5-adjacent)

Net unpaid = gross unpaid − ceded unpaid. If your ceded triangle method and your gross method disagree, **do not** book a net that is smaller than a plausible retention.

### If you are the **reinsurer** (assuming)

You usually do **not** have the primary’s full triangle. Toolkit:

- **Expected loss ratio / BF / Cape Cod** on on-level treaty premium, with a pattern that is slower than primary
- **Exposure rating** (limits profile × ILFs × ground-up rate) for the layer, then BF the IBNR
- **Experience rating** if there are enough years on a stable structure
- **Bornhuetter-Ferguson on reported-to-date** with a reinsurer lag pattern
- **Cape Cod** across a portfolio of similar treaties (Hürlimann collective prior)
- **Stochastic** only after you have a mean you believe; a Mack SE on 8 thin years is theater

For **excess** assumed: frequency of layer hits × severity-in-layer. Development of frequency (late reports into the layer) is often more important than severity development.

For **cat**: scenario / model residual + IBNER on known events. Do not average three cats in a triangle and call it a pattern.

### Commutations and aggregates

- A commutation is a settlement of unpaid; after it, those liabilities are gone and any triangle that still contains them must be restated.
- An aggregate deductible / corridor: ceded unpaid is near zero until the subject ultimate approaches the attachment, then it ramps fast. That is a nonlinear function of the primary ultimate — another reason not to develop ceded dollars independently.

## Reasonableness tests (A3 applied to A16)

- Ceded / gross ratio vs the program (quota share should sit near the cession %, after commission effects).
- Recoveries to date + ceded unpaid vs remaining limit.
- For a working excess: implied hit counts vs the size model.
- Year-by-year: a new AY with zero reported and a huge quota-share IBNR is fine; a new AY with zero reported and a huge *cat-layer* IBNR needs a scenario, not an LDF.

## Exam grab bag

- Define quota share, surplus, per-risk XS, cat XS, stop-loss, facultative vs treaty, losses-occurring vs risks-attaching.
- Give four reasons a primary CL on a ceded triangle is biased.
- Cedent: ceded unpaid from gross unpaid through the contract. Reinsurer: BF / exposure / Cape Cod, slower pattern.
- Reinstatement premium is part of the reinsurance cashflows; do not forget it when the layer is burning.
- Aggregate covers: ceded IBNR is an option on the primary ultimate, not a factor times reported.
