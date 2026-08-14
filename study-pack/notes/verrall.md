# Verrall — Obtaining Predictive Distributions for Reserves Which Incorporate Expert Opinion (2007)

Tasks: **A9, A13**

Official: [7_Verrall.pdf](https://www.casact.org/sites/default/files/2021-03/7_Verrall.pdf)

## The problem

A pure bootstrap or Mack SE pretends the triangle is the only information. In real life the appointed actuary has a **selected** ultimate: maybe Cape Cod on the young years, a tail pick, a catastrophe load, a “we are not booking the 95th.” Verrall’s question: how do you build a **predictive distribution** whose mean (or whose location) respects that expert selection, without pretending the selection has no uncertainty and without throwing away the triangle’s stochastic model.

This is the A13 paper: a range / distribution of indications that is allowed to listen to a human.

## The mechanism (Bayesian, in words)

1. Start with a stochastic reserving model (ODP / GLM / chain-ladder likelihood on incrementals).
2. Treat the expert’s selected ultimates (or selected loss ratios, or selected tail) as **data about the parameters**, not as a replacement for the model.
3. Encode the expert opinion as a prior, or as a second likelihood (“the selected ultimate is the true ultimate plus noise with variance \(\tau^2\)”).
4. The posterior predictive distribution of unpaid is then a compromise:
   - If the expert is very sure (\(\tau\) small) and the triangle is thin, the distribution sits on the selection.
   - If the expert is vague (\(\tau\) large) or the triangle is rich, the distribution sits on the model.
5. The **mean** of that predictive distribution is a credibility mix of the model mean and the expert selection (A9). The **spread** widens if you admit the expert might be wrong.

That last point is the exam trap. Baking in a point selection and then bootstrapping **around the raw triangle** as if you had not selected is incoherent. Either:

- the selection is treated as certain (distribution too tight, mean forced), or
- the selection is ignored (mean ≠ booked number).

Verrall’s point is to do neither.

## How this differs from nearby papers

| Paper | Role of judgment |
|---|---|
| Brosius / Benktander / Hurlimann | Judgment enters as a prior ultimate / ELR; credibility weight is formulaic |
| Shapland | Mix whole distributions after the fact |
| Verrall | Put the expert **inside** the predictive distribution |
| Marshall | Judgment dominates the **risk margin**, structured qualitatively |
| Meyers | Priors are on model parameters; validation is against outcomes, not against an appointed-actuary pick |

## Practical encoding of “expert opinion”

You should be able to propose one of:

- Prior on AY loss ratios around the selected ELR, with a stated CV
- A likelihood for the selected ultimate \(U_i^{\text{sel}} \sim N(U_i, \tau_i^2)\)
- A constraint on the tail factor with a prior, not a fixed 1.05
- Different \(\tau\) by year: tight on mature years (where the actuary and the triangle already agree), looser on the current AY

Then simulate the posterior predictive (MCMC or a conjugate shortcut if they give you one).

## Ranges (A13)

A range of indications from Verrall is not “CL to BF.” It is a set of percentiles from a distribution that already includes the selection, **or** a set of distributions under different \(\tau\) (sensitivity to how hard you pull toward the expert). If management wants the booked number to be the mean, say that and back out the implied \(\tau\). That is a clean constructed-response ending.

## Exam grab bag

- Why “bootstrap the triangle then shift the mean to the selected ultimate” is not a predictive distribution.
- Expert opinion = prior or second likelihood; \(\tau\) controls the pull.
- Mean is a credibility mix; variance is larger than “selection is true.”
- A13: produce percentiles from that posterior predictive, and show a sensitivity to \(\tau\).
- Mature year: small \(\tau\) is fine. Immature year: small \(\tau\) is you pretending you know the cat year.
