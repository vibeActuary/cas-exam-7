# Episode 09 — Venter, testing age-to-age factors

**Hosts:** Riley and Sam  
**Length:** about 16 minutes  
**Tasks:** A2, A6, A12  
**Paper:** Venter 1998

---

**Riley:** Mack gave me an SE. Venter asks whether I was allowed to run Mack.

**Sam:** Correct. Age-to-age methods stand on assumptions you can test on the triangle you have. Venter turns those assumptions into residual plots and regressions so you do not publish a Mack SE on a triangle that is not a chain-ladder triangle.

**Riley:** Assumptions in testable form.

**Sam:** One. Linearity through the origin. Next cumulative is f times this cumulative. No intercept. A significant intercept means a Cape Cod, additive, or BF-style term is missing.

Two. The same f for every accident year. No slope, no regime change.

Three. After whatever variance function you claimed — Mack’s sigma-squared times C — the residuals behave. If the factor scatter fans out, your weights on f-hat are wrong and so is sigma-hat.

Four. No calendar-year effect. A diagonal of residuals with the same sign is inflation, statute, or settlement speed.

Five. No leftover development-year shape after the factor.

Six. Accident years independent. One huge year should not be teaching the others a calendar lesson.

**Riley:** Tests I can describe in a constructed response.

**Sam:** Intercept test. Regress C-k-plus-one on C-k with an intercept. If the intercept is significant, a pure multiplicative LDF is the wrong mean. Clark Cape Cod and BF live here.

Slope stability. Oldest half versus newest half. If f moved, you have an AY or CY problem.

Residual versus size. If residuals grow faster or slower than square-root C, Mack’s variance function is wrong. That breaks the SE, and it also breaks the claim that the volume-weighted factor is optimal.

Calendar residual plot. Average residuals on each diagonal. A run of positives on the latest diagonal is the classic “do not use last-diagonal-only factors” case.

High leverage. One large AY owns the volume-weighted f. Feature, not a bug, of the formula. Consider Brosius.

**Riley:** They disagree — simple average, volume-weighted, geometric. Which do I pick?

**Sam:** Disagreement is a diagnostic, not a menu. If they disagree a lot, the triangle is heteroscedastic or has outliers. Do not average the averages and call it judgment. Change the model.

**Riley:** A test failed. What do I write instead of “I will judgmentally pick 1.05”?

**Sam:** Intercept not zero: BF, Cape Cod, Clark Cape Cod, additive incremental.

Factor trend by AY: varying ELR, changing mix, Shapland CY parameter, Meyers changing settlement rate.

CY diagonal: calendar-year parameter in a GLM — Taylor — or adjust the triangle first, episode 01.

Variance not sigma-squared C: different variance function, ODP, GLM, bootstrap with the right weights.

Thin or one huge year: Brosius. Do not let one year own f-hat.

**Riley:** The sentence that kills a sloppy A6 answer.

**Sam:** “Mack SE is twelve percent so we are fine” is false if the intercept test already failed. Precision is not validity.

**Riley:** Exam grab bag.

**Sam:** Name three plots and what failure looks like. Intercept not zero means multiplicative chain ladder is biased — give an alternative. Latest diagonal all positive is a CY story, not a higher tail factor. Volume-weighted f is optimal only under Mack’s variance function.

**Riley:** Repeat the intercept moral.

**Sam:** Significant intercept, drop pure multiplicative CL. Go Cape Cod or BF or add a constant emergence term.
