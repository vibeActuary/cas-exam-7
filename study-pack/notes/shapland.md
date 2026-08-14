# Shapland — Using the ODP Bootstrap Model: A Practitioner’s Guide (Monograph 4)

Tasks: **A1, A9, A10, A11, A13**

Official: [monographs_papers_04-shapland.pdf](https://www.casact.org/sites/default/files/database/monographs_papers_04-shapland.pdf)  
Open the errata. The xlsm files on pp. 61–62 are for understanding, not for the exam software.

## What the ODP bootstrap is

1. Fit a chain-ladder / ODP-GLM mean to the incremental triangle.
2. Compute Pearson (or deviance) residuals, scaled so they have the right over-dispersion.
3. **Residual bootstrap:** resample residuals, add them back to the fitted means, get a pseudo-triangle.
4. Refit the model on the pseudo-triangle (parameter uncertainty).
5. Simulate a future triangle from the refitted means plus a process-error draw (process uncertainty).
6. Repeat thousands of times. The histogram of unpaid amounts **is** the predictive distribution (A10).

Mean of the histogram ≈ CL unpaid (A9). Spread = prediction error. Percentiles and a range of indications come from the same sample (A13).

## Why Shapland wrote a monograph instead of a three-page recipe

Real triangles break the textbook bootstrap. The monograph is the list of **adjustments a practitioner must make** and the **diagnostics that tell you the model is lying**.

### Practical adjustments (high-frequency exam list)

- **Negative incrementals / negative residuals.** Paid triangles can go negative (recoveries). Pearson residuals need a strategy (including a GLM bootstrap that can handle signed residuals).
- **Heteroscedasticity / changing mix.** One \(\phi\) for the whole triangle is often wrong. Consider residual scaling by age, or a GLM with a better variance function.
- **Zero cells.** Log-link and Pearson residuals misbehave. Use a small offset or a different residual definition; do not drop the cell silently.
- **Calendar-year effects.** Standard ODP-CL has no CY parameter. If Venter/Taylor diagnostics find a diagonal, bootstrap a model that includes one, or adjust the data first (A1).
- **Tail / extrapolation.** The bootstrap only knows ages in the triangle. A tail factor is an extra assumption; bootstrap it or it is a hidden delta.
- **Heterogeneous exposures.** Weight or use an exposure offset (Cape Cod style) so a tiny AY is not treated like a large one.
- **Paid vs incurred.** Incurred bootstraps often look too tight because case reserves already embed judgment. Meyers later shows Mack/bootstrap can fail validation on real CAS triangles.

### Combining models (A13)

Shapland is explicit: the ODP bootstrap is a **tool**, not the answer. Credibility-weight or mix:

- ODP bootstrap distribution
- Mack / GLM analytic
- a prior / BF-style mean
- another bootstrap (GLM bootstrap with extra covariates)

the same way you mix point estimates. The “range of indications” is not “5th to 95th of one broken model.”

## Diagnostics you must be able to name (A1, A11)

- Residual plots vs AY, DY, CY (same as Taylor/Venter)
- Residual histogram: should look roughly standardized after scaling
- One-way actual vs expected by age
- Predictive checks: does the bootstrap’s implied age-to-age cloud contain the historical factors?
- Stability: drop the latest diagonal and see whether the predictive mean moves more than process noise allows
- Outliers: a single coded claim can own the 99th percentile. That is an A1 data issue.

If diagnostics fail, **do not** publish the 90th percentile anyway. Change the model (GLM bootstrap, CY term, different variance, split the triangle).

## Exam grab bag

- List the six bootstrap steps in order, and say which step is process vs parameter.
- Name three practical adjustments (negatives, zeros, tail, CY, residual scaling).
- “The 95th percentile is $42M” → only if diagnostics passed and the tail/CY were modeled.
- Range of indications: mix models, do not just read two percentiles off one histogram.
- ODP-CL bootstrap mean should be close to deterministic CL. If it is not, your residual adjustment is wrong.
