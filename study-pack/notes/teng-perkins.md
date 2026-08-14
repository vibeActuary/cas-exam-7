# Teng & Perkins — Estimating the Premium Asset on Retrospectively Rated Policies (1996)

Plus Feldblum discussion (1998), **Sections 1–2 only**.  
**Exclude Teng/Perkins Section 5. Not responsible for Annual Statement notation.**

Tasks: **A5**

Official paper: [proceed96/96611.pdf](https://www.casact.org/pubs/proceed/proceed96/96611.pdf)  
Feldblum: [proceed98/980274.pdf](https://www.casact.org/pubs/proceed/proceed98/980274.pdf)

## What the “premium asset” is

On a retrospectively rated policy, premium is a function of losses. After the policy period you book **additional / return premium** as losses develop. If you have booked an unpaid-loss reserve but have **not** booked the extra retro premium those losses will generate, your balance sheet is missing an asset (or, for return premium, missing a liability).

A5 is: forecast that premium reserve / premium asset, consistent with the loss reserve.

## Retro premium in one formula

A standard linear retro:

\[
P = (BP + CF\times L)\times TM
\]

subject to a minimum and maximum premium.

- \(BP\) = basic premium (expense + net insurance charge, etc.)
- \(CF\) = conversion factor (loss conversion / expense multiplier on losses)
- \(L\) = losses in the retro calculation (often limited, sometimes including ALAE)
- \(TM\) = tax multiplier
- Min / max bind some policies

The **incremental premium** created by an incremental loss \(dL\) is, if the policy is **not** at the min or max:

\[
dP = CF\times TM\times dL
\]

If the policy is already at the **maximum**, \(dP=0\).  
If the policy is at the **minimum**, additional losses may still produce no premium until you climb off the min — or, depending on the plan, the first dollars of development just eat the minimum cushion.

That is the whole exam: **leverage of losses into premium depends on where the policy sits relative to the corridor.**

## Teng/Perkins approach (the part you need)

They estimate the premium asset by looking at how booked retro premium has historically moved as losses have developed, using development-style triangles of:

- losses entering the retro calculation
- booked retro premium
- implied additional-premium-to-loss ratios

and then applying those ratios to **current unpaid losses**, with adjustments for:

- the fraction of the book expected to be at max (no more premium)
- the fraction at min (dampened premium response)
- changes in plan parameters (CF, TM, loss limits)

You can also do it **policy-by-policy** (or cell-by-cell): take the actuary’s selected ultimate loss for that policy, run it through the retro formula, subtract premium already booked. That is the most accurate and the most expensive. Teng/Perkins give a triangle / aggregate approximation when you cannot price every account.

## Feldblum Sections 1–2 (this is the conceptual gold)

Feldblum restates the economics without Annual Statement choreography:

1. The premium asset is the **expected additional premium arising from loss development and from the retro formula**, not a plug to make the combined ratio look nice.
2. It must be **consistent with the loss reserve**. If you raise the loss reserve by $10M and the book is fully open (no one at max), you must also raise the premium asset by about \(CF\times TM\times 10M\). If you do one and not the other, the P&L and the surplus move the wrong way.
3. Min/max, loss limitations, and the insurance charge mean the incremental ratio \(dP/dL\) is **between 0 and \(CF\times TM\)**, not equal to it for the whole book.
4. You also owe a premium asset (or liability) for **future additional/return premium on known booked losses** if the last adjustment has not been issued — not only for IBNR.

## What they will not ask

- Line numbers on the Annual Statement, Schedule P mapping, or statutory blank citations (explicitly out).
- Teng/Perkins Section 5.

## Exam grab bag

- Define the premium asset in one sentence: expected future additional (minus return) retro premium.
- Compute \(dP=CF\times TM\times dL\) and then haircut for the probability of being at max.
- “We increased the loss reserve $5M. What happens to the premium asset?” — answer with the min/max split, not a single number.
- Consistency: loss reserve and premium asset must use the same loss ultimate and the same definition of “loss” (limited? ALAE in?).
- If all policies are at the maximum, the premium asset on *future* loss development is zero. That is a common trick ending.
