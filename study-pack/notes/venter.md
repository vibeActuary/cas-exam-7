# Venter — Testing the Assumptions of Age-to-Age Factors (1998)

Tasks: **A2, A6, A12**

Official: [proceed98/980807.pdf](https://www.casact.org/pubs/proceed/proceed98/980807.pdf)

## Why this paper exists

Chain ladder / Mack / any age-to-age factor method stands on assumptions you can **test on the triangle you actually have**. Venter turns those assumptions into residual plots and formal tests so you do not run Mack on a triangle that is not a chain-ladder triangle.

## The assumptions, in testable form

Age-to-age factors assume, roughly:

1. **Linearity through the origin:** \(C_{k+1}\approx f\cdot C_k\). No intercept. A significant intercept means a Cape Cod / additive / BF-style term is missing (or there is a fixed amount of late development unrelated to current size).
2. **Same \(f\) for every accident year** (no AY slope, no regime change).
3. **Homoscedasticity after the Mack scaling** — or whatever variance function you claimed. If raw factor scatter fans out, the weights on \(\hat f\) are wrong and so is \(\hat\sigma^2\).
4. **No calendar-year effect.** A diagonal of residuals with the same sign is a CY shock (inflation burst, statute change, settlement speed-up).
5. **No development-year leftover** after the factor — the model is not missing a shape change at late ages.
6. **Independence of accident years** — one huge year should not be teaching the others a calendar lesson.

## Tests you should be able to describe (A12)

Venter works in the regression view: for each age, plot \(C_{k+1}\) vs \(C_k\), or plot link ratios vs \(C_k\), or plot residuals vs AY, vs age, vs calendar year.

High-yield tests:

- **Intercept test.** Regress \(C_{k+1}\) on \(C_k\) with an intercept. If the intercept is significant, a pure multiplicative LDF is the wrong mean function. Clark’s Cape Cod and BF live here.
- **Slope stability.** Split the years (oldest half vs newest half) and compare \(\hat f\). A trend in factors is an AY or CY problem.
- **Residual vs size.** If residuals grow faster or slower than \(\sqrt{C_k}\), Mack’s \(\sigma_k^2 C_k\) is wrong. That breaks the SE, not just the point estimate weights.
- **Calendar residual plot.** Sum or average residuals on each diagonal. A run of positives on the latest diagonal is the classic “do not use last-diagonal-only factors” case.
- **High-leverage points.** One large AY dominates \(\hat f_k=\sum C_{k+1}/\sum C_k\). That is a feature of volume-weighting; say so, and consider a robust or credibility-weighted factor (Brosius).

He also discusses **weighted least squares** age-to-age factors and when simple averages, volume-weighted averages, and geometric averages disagree. Disagreement is a diagnostic, not a menu.

## What to do when a test fails (A2 / A6)

The exam wants a *method change*, not “I will judgmentally pick 1.05.”

| Failure | Better model |
|---|---|
| Significant intercept | BF, Cape Cod, Clark Cape Cod, additive incremental model |
| Factor trend by AY | Varying ELR, changing mix, Shapland CY parameter, Meyers CSR |
| CY diagonal | Calendar-year parameter in a GLM (Taylor), or adjust the triangle first |
| Variance ≠ \(\sigma^2 C\) | Different variance function; ODP / GLM / bootstrap with the right weights |
| Thin / one huge year | Brosius / credibility factors; do not let one year own \(\hat f\) |

## Exam grab bag

- Name three plots and what a failure looks like on each.
- “Mack SE is 12% so we are fine” → not if Venter’s intercept test already failed.
- Intercept ≠ 0 ⇒ multiplicative chain ladder is biased. Give an alternative.
- Latest diagonal all positive residuals ⇒ CY inflation or speed-up; a higher tail factor is treating the symptom.
- Volume-weighted \(\hat f\) is optimal **under Mack’s variance function**. If that function is wrong, the “standard” factor is not even the best point estimate.
