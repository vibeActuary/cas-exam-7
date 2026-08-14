# Taylor & McGuire — Stochastic Loss Reserving Using GLMs (Monograph 3, Ch. 1–6)

Tasks: **A9, A10, A11, A12**  
**2026 syllabus: Chapters 1–6** (older outlines stopped at Ch. 3).

Official: [monographs_papers_03-taylor.pdf](https://www.casact.org/sites/default/files/database/monographs_papers_03-taylor.pdf)

## The monograph in one paragraph

Chain ladder is a GLM. Once you write it that way, you get a distribution for the reserve (A9–A10), residual diagnostics that tell you when to leave chain ladder (A11–A12), and a clean list of extensions (AY effects, CY effects, smoothing, different error families) that still live in the same likelihood.

## GLM reminder (they will assume Exam 5 / MAS)

A GLM has:

- Random component: \(Y\) from an exponential-dispersion family (Poisson, over-dispersed Poisson, gamma, Tweedie, …)
- Systematic component: \(\eta = X\beta\)
- Link: \(g(E[Y])=\eta\)

For reserving, \(Y\) is usually the **incremental** paid or incurred in cell \((i,j)\).

## Chain ladder as a GLM

The classical chain ladder on incrementals is (up to the usual caveats about the last diagonal and the tail):

\[
E[Y_{ij}] = \alpha_i\cdot\beta_j
\quad\text{or, with a log link,}\quad
\log E[Y_{ij}] = a_i + b_j
\]

That is a **cross-classified** model: one parameter per accident year, one per development year, no interaction, no calendar year. The ODP (over-dispersed Poisson) version — variance \(=\phi\mu\) — is the stochastic model whose MLE mean matches the classical chain-ladder forecasts. That is the bridge to Shapland’s bootstrap.

Important consequences:

- The reserve mean from ODP-GLM chain ladder ≈ classical chain ladder unpaid (A9).
- Prediction error has process + parameter pieces, now from GLM theory (inverse Fisher information, or bootstrap).
- You can **test** the chain-ladder mean: add a calendar-year covariate, a diagonal interaction, a smoothing spline on \(b_j\), and see if deviance drops by more than the extra parameters deserve (A12).

## Chapters 1–6 map (2026)

You are responsible through the extensions, not only the slogan “CL is a GLM.”

| Ch | What to take into the exam |
|---|---|
| 1–2 | Motivation; reserve as a random variable; process vs estimation error |
| 3 | Chain ladder in GLM form; ODP; log-link cross-classification |
| 4 | Diagnostics: deviance residuals, Pearson residuals, leverage, hat matrix. This is Venter in GLM clothes. |
| 5 | Do you need to leave CL? Nested-model tests, CY terms, changing development |
| 6 | Natural GLM extensions: different variance functions, smoothing development factors, exposure offsets (Cape Cod-like), maybe Tweedie / gamma |

If an item cites “Taylor-McGuire” and asks for a test of chain-ladder assumptions, answer with a GLM nested test plus residual plots, not with Mack’s \(\sigma^2\) formula.

## Prediction error and predictive distributions (A9, A10)

- Mean reserve: sum of fitted future incrementals.
- Prediction variance: process (\(\phi\mu\) for ODP) plus parameter (delta method or bootstrap of \(\hat\beta\)).
- Predictive distribution: simulate \(\beta\) from its covariance, then simulate future \(Y_{ij}\) from the EDF; or residual bootstrap (Shapland). Analytical percentiles are rare except under strong assumptions.

Over-dispersion \(\phi>1\) is normal for real triangles. \(\phi=1\) (pure Poisson) understates SEs badly.

## Diagnostics (A11, A12)

Look at:

- Residuals vs AY, vs DY, vs CY (heatmap of the triangle)
- Scale: is \(\widehat{\mathrm{Var}}/\hat\mu\) constant? If not, change the variance function.
- One cell with huge Pearson residual: data problem (A1) before model problem.
- Adding a CY parameter that is significant: do **not** still report a Mack SE as if nothing happened.

## Exam grab bag

- Write \(\log E[Y_{ij}]=a_i+b_j\) and name it as the GLM chain ladder.
- ODP + that mean ⇒ classical CL forecasts.
- Two reasons to leave CL: significant CY term; variance not proportional to mean.
- Prediction error = process + parameter; \(\phi\) multiplies the process piece.
- 2026: you can be asked about the Ch. 4–6 extensions, not just the slogan.
