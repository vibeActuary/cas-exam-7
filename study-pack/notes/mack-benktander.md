# Mack — Credible Claims Reserves: The Benktander Method (2000)

Tasks: **A1, A2, A3, A9, A11, A12**

Official: [7_Mack_2000.pdf](https://www.casact.org/sites/default/files/2021-03/7_Mack_2000.pdf)

## The three methods on one line

Let \(c\) = claims to date, \(p\) = percent reported (or \(1/\mathrm{LDF}\)), \(U\) = a priori ultimate (usually ELR × on-level premium).

| Method | Ultimate | IBNR / unpaid |
|---|---|---|
| Chain ladder (CL) | \(c/p\) | \(c(1/p-1)\) |
| Bornhuetter-Ferguson (BF) | \(c + (1-p)U\) | \((1-p)U\) |
| Benktander (B) / iterated BF | \(c + (1-p)\cdot(\text{CL/BF mix})\) | \((1-p)\times\) a credibility ultimate |

Benktander (1976) is the intuitive mix: use BF, but replace the a priori ultimate \(U\) with a first-pass estimate that already listened to the data. Mack writes it as a credibility formula and computes mean squared errors under a simple model.

## Benktander as credibility / iterated BF

Two equivalent exam writings. Use whichever the item’s notation matches.

**IBNR form (safest):**

\[
\text{IBNR}_B = (1-p)\bigl(p\cdot\hat{U}_{CL} + (1-p)\cdot U\bigr) = (1-p)\cdot\hat{U}_{BF}
\]

That is BF run a second time using the first-pass BF ultimate as the new prior (“iterated BF”).

**Ultimate form:**

\[
\hat{U}_B = p\cdot\hat{U}_{CL} + (1-p)\cdot\hat{U}_{BF} = c + \text{IBNR}_B
\]

The weight on the data-driven piece grows with \(p\):

- Early years (small \(p\)): Benktander IBNR sits near BF. You do not trust the chain ladder yet.
- Mature years (large \(p\)): Benktander sits nearer CL. The data has spoken.

Do not write \(\hat{U}_B = p\cdot\hat{U}_{CL}+(1-p)U\). That collapses to BF and you will miss the IBNR difference.

## Why it usually wins on MSE (A9)

Mack’s model is deliberately simple (independent accident years, a reported-percent structure). Under it he compares MSEs:

- BF has lower MSE than CL when the prior is decent and \(p\) is small.
- CL has lower MSE than BF when \(p\) is large or the prior is weak.
- **Benktander’s MSE is almost always below both**, and close to an exact Bayesian procedure.

You do not need the proof. You need the ranking and the intuition: Benktander is the first iterate toward the Bayesian estimate. One more iterate is “iterated BF”; it usually adds little.

## Neuhaus (you will meet him again in Hurlimann)

Neuhaus (1992) is another pragmatic credibility weight between CL and BF. Mack/Hurlimann treat Benktander, Neuhaus, and “optimal” weights as a family. For this paper, remember:

- Benktander uses \(Z=p\)
- That choice is simple, almost optimal, and easy to compute in a spreadsheet item

## Diagnostics and assumptions (A1, A11, A12)

Benktander inherits **both** parents’ assumptions:

- From CL: development pattern \(p\) is the right one; no AY/CY interaction that wrecks the latest diagonal.
- From BF: the prior \(U\) is unbiased. A 20% low ELR pulls Benktander low, just less than it pulls BF.

Reasonableness tests:

- If \(\hat{U}_B\) is outside the range of CL and BF, you made an algebra error. It is a convex combination.
- If CL and BF already agree, Benktander cannot save you; go look at the pattern and the prior.
- Plot \(Z=p\) by year. Recent years should look BF-like. If someone applied a 90% weight to CL on a 12-month year, that is not Benktander.

## Exam grab bag

- Given \(c\), LDF (so \(p=1/\mathrm{LDF}\)), and \(U\), compute CL, BF, and Benktander ultimates and IBNR.
- State \(Z=p\) and say why a new AY should sit near BF.
- MSE ranking: Benktander \(\lesssim\) min(CL, BF) \(\le\) the worse of the two.
- “Iterated BF” = Benktander. Say that in one sentence if they ask for the relationship.
