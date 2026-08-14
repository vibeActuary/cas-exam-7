# Episode 04 — Clark LDF curve fitting

**Hosts:** Riley and Sam  
**Length:** about 18 minutes  
**Tasks:** A2, A3, A6–A8, A11  
**Paper:** Clark 2003

---

**Riley:** I am tired of a different LDF at every age. Clark says fit a curve. Which curves?

**Sam:** Two workhorses. Write them in words.

Weibull: G of t equals one minus e to the minus t over theta, to the omega.

Loglogistic: G of t equals t to the omega, over t to the omega plus theta to the omega.

G of t is the percent of ultimate emerged by age t. Theta is scale — a typical settlement age. Omega is shape — how steep the climb is.

**Riley:** Again. Weibull.

**Sam:** One minus exp of minus (t over theta) to the omega.

**Riley:** Expected increment.

**Sam:** Expected incremental loss in age j for accident year i equals mu-sub-i times (G of t-j minus G of t-j-minus-one). The curve gives the percent of that year’s ultimate that lives in the increment.

Then you choose mu.

LDF model: mu-sub-i is a free ultimate for each accident year. That is chain ladder with a smooth pattern.

Cape Cod model: mu-sub-i is ELR times exposure-sub-i. One ELR, known exposures. That is Cape Cod wearing a growth curve.

**Riley:** Why does he love Cape Cod?

**Sam:** Because the exposure base borrows strength across years and cuts the standard error of the total reserve. His numerical example is Mack’s triangle. The total SE drops when you switch from free ultimates to Cape Cod. If the item gives you on-level premium or policy counts, using the LDF model anyway is leaving A6 points on the table.

**Riley:** Likelihood. What variance?

**Sam:** Over-dispersed style. Variance proportional to the mean, times a dispersion sigma-squared. Maximize the loglikelihood in the curve parameters, and in the ELR if you are Cape Cod. You will not maximize a function by hand on the exam. You will write the expected increment, name the parameters, and say that the MLE standard errors come from the curvature of the loglikelihood — the Hessian, the observed information.

**Riley:** Process versus parameter. A6, A7, A8.

**Sam:** Process: even if theta, omega, and ELR were handed down on stone, the triangle is still random. Parameter: you estimated them. Total predictive variance is approximately process plus parameter.

Simulation, A8: draw the parameters from the approximate normal — mean at the MLE, covariance equal to the inverse information. Then, given those parameters, draw the future increments. Sort the unpaid. That is a percentile without pretending the reserve is normal.

**Riley:** Tail.

**Sam:** If the last age in the triangle is not ultimate, G of t has to run past the last age. That is a model assumption. Say it. Two curves can agree inside the triangle and disagree in the tail. If the unpaid lives in the tail, show both or show a sensitivity. That is A3.

**Riley:** Residuals. A11.

**Sam:** Plot residuals versus age and versus fitted increment. You want scatter around zero, no fan, no leftover stripe at twelve and twenty-four. Clark’s own example is a little messy at the early ages. He does not reject the model outright. If residuals trend with calendar year, omega will not save you. You are missing a CY settlement-speed effect. That is Meyers CSR later, or a Taylor calendar term.

**Riley:** Age definition.

**Sam:** Age from the average accident date if the book is not written flat through the year. Using January first on a book that writes in December tilts G of t.

**Riley:** What Clark does not do.

**Sam:** Changing mix, changing limits, a shock CY. Those are A1. Fit after you restate.

**Riley:** Exam grab bag.

**Sam:** Write expected increment equals mu times delta G. Name the two mus. Write Weibull and loglogistic G of t. Explain why Cape Cod SE is smaller. Split process and parameter. Name one residual plot. Say the tail is an extrapolation.

**Riley:** Repeat Cape Cod mu.

**Sam:** ELR times exposure. One ELR. That is the whole SE reduction.
