# Siewert — Reserving Workers Compensation High Deductibles (1996)

Tasks: **A4**

Official: [7_Siewert.pdf](https://www.casact.org/sites/default/files/2021-03/7_Siewert.pdf)

## Why WC deductibles are a different A4 problem

A high-deductible WC policy is not “primary minus a number.” The deductible is per-occurrence (sometimes with an aggregate), the excess is often unlimited medical, development is extremely long, and the **mix of small medical vs large indemnity/occupational-disease claims** changes the deductible layer vs the excess layer over time.

Siewert builds a model that splits the claim into:

- **Limited (deductible) layer** — what the insured retains
- **Excess layer** — what the insurer / excess writer pays

and lets each layer have its own development, leveraging the relationship between limited and unlimited severity.

## Model structure (the exam skeleton)

1. Start from a **ground-up** or **limited** severity distribution and a claim-count / reported-count process.
2. The expected cost in the deductible layer is a limited expected value; the excess is the tail expectation.
3. Development happens because:
   - counts continue to be reported (IBNR counts),
   - known claims continue to develop in severity,
   - a claim that looked small can **pierce** the deductible later (the WC version of Sahasrabuddhe’s connector).
4. Therefore you **cannot** take a ground-up LDF and apply it to both layers. The excess LDF is larger and longer-tailed.

Typical objects to compute:

- Limited severity \(E[X \wedge D]\)
- Excess severity \(E[(X-D)_+]\)
- Layer relativity \(E[(X-D)_+]/E[X]\) or vs \(E[X\wedge D]\)
- Development of each layer as the severity distribution “ages” (medical inflation, indemnity lags, reopenings)

## Practical reserving methods he discusses

You should be able to describe, not just name:

- **Direct excess triangle** — if you have excess-only data. Often thin and noisy. High process variance. Credibility-weight toward a severity-model excess pattern (Brosius instinct).
- **Ground-up minus deductible layer** — build a ground-up ultimate, subtract a modeled deductible-layer ultimate. Consistent if both pieces use the same size model.
- **Increased-limit / excess-ratio method** — apply an excess ratio that itself develops with age.
- **Report-lag + severity-lag** — especially for occupational disease and lifetime medical.

WC-specific landmines:

- **Medical-only vs lost-time mix.** A shift toward medical-only cheapens the deductible layer and can starve the excess — or the opposite if large medical claims are the excess.
- **Deductible erosion by inflation.** A fixed $500k deductible in a 10-year-old year is a different layer than $500k today. Trend the attachment (Sahasrabuddhe again).
- **Aggregate deductibles and corridors.** Per-occurrence model is not enough; you need a frequency overlay.
- **ALAEs** inside or outside the deductible. The paper and the exam will punish you if you apply a loss LDF to a loss+ALAE layer without saying so.

## Diagnostics (A4 reasonableness)

- Excess unpaid / ground-up unpaid should rise as you look at more recent years (less mature ⇒ more of the remaining development is excess).
- If the insured’s retention triangle is developing *up* while your excess is developing *down*, check claim coding (deductible recoveries, reimbursements).
- Compare implied excess ratios to an ILF table from pricing. Persistent disagreement is a model problem, not a “pick the midpoint” problem.

## Exam grab bag

- Why ground-up LDFs understate excess unpaid on high-deductible WC.
- Sketch: limited LEV vs excess tail, then apply separate development.
- Name two WC-specific reasons the layer mix changes with age (lost-time emergence, medical inflation, reopenings, OD).
- “Data is thin in the excess triangle” → credibility to a severity-based excess pattern, not a 5-year weighted excess LDF of 4.00.
