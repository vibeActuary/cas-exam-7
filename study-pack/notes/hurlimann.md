# Hürlimann — Credible Loss Ratio Claims Reserves (2009)

Tasks: **A1, A2, A3, A6, A11**  
**Not responsible for mathematical proofs.**

Official: [7_Hurlimann.pdf](https://www.casact.org/sites/default/files/2021-03/7_Hurlimann.pdf)

## What he adds on top of Mack 2000

Mack mixed CL and BF using an a priori ultimate \(U\) that different actuaries may pick differently. Hürlimann restates everything in **loss-ratio** language so that, given the same premiums, two actuaries get the same collective prior.

- **Individual loss-ratio reserve** = chain-ladder idea: gross up this origin period’s own latest claims with its own development. This is the “this year is special” estimate.
- **Collective loss-ratio reserve** = BF / burning-cost idea: apply an experience loss ratio (from premiums, or from a portfolio of years) to this origin period’s premium, then take the unreported piece.

A **credible loss-ratio reserve** is a weight \(Z\) on the individual reserve and \(1-Z\) on the collective reserve.

## The family of methods (memorize the weights, skip the proofs)

All of these are the same machine with different \(Z\):

| Method | Weight on individual / CL | Weight on collective / BF |
|---|---|---|
| Pure CL | 1 | 0 |
| Pure BF | 0 | 1 |
| Cape Cod | uses a portfolio-balanced expected LR; equivalent to a particular \(Z\) | |
| Benktander | \(Z = p\) (percent reported) | \(1-p\) |
| Neuhaus | a different closed-form \(Z\), still between 0 and 1 | |
| Hürlimann “optimal” | \(Z\) that minimizes MSE (and, with his parameter choice, also variance) | |

Cape Cod is the “we all used the same premiums and the same exposure-weighted LR” member of the family. That is Hürlimann’s advertised advantage over Mack’s BF prior: **same premiums ⇒ same collective reserve**.

## Optimal \(Z\) in words (A6)

You do not need the derivation. You need the comparative statics:

- More reported (\(p\) up) → more weight on the individual / CL piece.
- Noisier reporting (process variance up) → less weight on the individual piece.
- Stronger, more credible collective prior (smaller variance of the burning-cost LR) → less weight on the individual piece.
- His pragmatic parameter estimates are designed so you can compute \(Z\) and the MSE of the credible reserve from triangle quantities plus premiums, without a full Bayesian model.

If an item gives you the optimal \(Z\) formula already simplified, just plug in. If it asks you to *derive* the normal equations, that is outside the “not responsible for proofs” shield — do not go hunting through the appendix.

## Diagnostics (A1, A11)

Hürlimann is the paper to cite when the question is:

- “CL and BF disagree a lot. What weight is justified?”
- “Two actuaries used different ELRs in BF. How do we make the prior reproducible?” → use premiums and a collective loss ratio (Cape Cod / his collective reserve).
- “Is Cape Cod a credibility method?” → yes, it is a constrained credibility mix.

Red flags:

- \(Z\) outside \([0,1]\) means a parameter estimate went negative or you used \(p>1\).
- A collective LR that ignores a known regime change (law reform, COVID shutdown) is a precise-looking wrong answer.

## Exam grab bag

- Name the individual vs collective loss-ratio reserves in one sentence each.
- Place CL, BF, Cape Cod, Benktander, Neuhaus on the same credibility line.
- State the two advantages Hürlimann claims vs Mack 2000: (1) pragmatic parameter estimates, (2) collective reserve reproducible from premiums.
- Do **not** write a proof of optimality.
