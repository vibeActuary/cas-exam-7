# Episode 11 — Shapland, ODP bootstrap

**Hosts:** Riley and Sam  
**Length:** about 18 minutes  
**Tasks:** A1, A9–A11, A13  
**Paper:** CAS Monograph 4

---

**Riley:** Six steps. In order. I will repeat them.

**Sam:** One: fit a chain-ladder or ODP-GLM mean to the incremental triangle. Two: compute Pearson or deviance residuals, scaled for over-dispersion. Three: residual bootstrap — resample residuals, add them back to the fitted means, get a pseudo-triangle. Four: refit the model on the pseudo-triangle. That is parameter uncertainty. Five: simulate a future triangle from the refitted means plus a process-error draw. That is process uncertainty. Six: repeat thousands of times. The histogram of unpaid is the predictive distribution.

**Riley:** One, fit. Two, residuals. Three, resample onto the mean. Four, refit — parameter. Five, simulate the future — process. Six, histogram. Mean of the histogram should be close to deterministic chain-ladder unpaid. If it is not, my residual adjustment is wrong.

**Sam:** Yes. Spread is prediction error, A9. The sample is the distribution, A10. Percentiles and a range can come from the same sample, A13 — but only if the model is legal.

**Riley:** Why is the monograph long?

**Sam:** Because real triangles break the textbook. The exam wants the adjustment list, not Stan.

Negatives. Paid incrementals can be negative. Pearson residuals need a strategy. A GLM bootstrap that allows signed residuals is one.

Heteroscedasticity. One phi for the whole triangle is often a lie. Scale residuals by age, or change the variance function.

Zeros. Log-link and Pearson residuals misbehave. Small offset or a different residual. Do not drop the cell silently.

Calendar-year effects. Standard ODP-CL has no CY parameter. If Venter or Taylor found a diagonal, bootstrap a model that includes one, or adjust the data first.

Tail. The bootstrap only knows ages in the triangle. A tail factor is an extra assumption. Bootstrap it or it is a hidden delta.

Heterogeneous exposures. Weight, or use an exposure offset, so a tiny year is not treated like a large one.

Paid versus incurred. Incurred bootstraps often look too tight because case reserves already embed judgment. Meyers will confirm that.

**Riley:** A1 connection.

**Sam:** A single coded claim can own the ninety-ninth percentile. That is not “the book has fat tails.” That is a data issue. Outlier first, bootstrap second.

**Riley:** Diagnostics, A11.

**Sam:** Residual plots versus AY, DY, CY. Residual histogram after scaling. One-way actual versus expected by age. Does the bootstrap’s implied age-to-age cloud contain the historical factors? Drop the latest diagonal: does the predictive mean move more than process noise allows? If diagnostics fail, do not publish the ninetieth anyway.

**Riley:** Range of indications, A13.

**Sam:** Shapland is explicit. The ODP bootstrap is a tool, not the answer. Mix it with Mack, with a GLM that has extra covariates, with a BF-style mean, the same way you mix point estimates. A range is not “fifth to ninety-fifth of one broken model.”

**Riley:** Exam grab bag.

**Sam:** List the six steps and tag process versus parameter. Name three practical adjustments: negatives, zeros, tail, CY, residual scaling. A ninety-fifth is only a number if diagnostics passed and the tail was modeled. Range means mix models. Bootstrap mean should sit near deterministic CL.

**Riley:** Repeat process versus parameter.

**Sam:** Refit on the pseudo-triangle is parameter. Draw the future incrementals is process. You need both or the histogram is too tight.
