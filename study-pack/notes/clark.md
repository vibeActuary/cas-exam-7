# Clark — LDF Curve Fitting and Stochastic Reserving (2003)

Tasks: **A2, A3, A6, A7, A8, A11**

Official: [7_Clark.pdf](https://www.casact.org/sites/default/files/2021-03/7_Clark.pdf)

## The idea

Instead of a separate LDF for every age, fit a **smooth growth curve** \(G(t)\) = percent of ultimate emerged by age \(t\), by maximum likelihood, using the incremental triangle. Then you get:

- a point estimate of unpaid (A2)
- a process-variance estimate and, with the Hessian / information matrix, parameter uncertainty (A6–A8)
- residuals you can plot (A11)

Two workhorse curves (know both):

- **Weibull:** \(G(t) = 1-\exp(-(t/\theta)^\omega)\)
- **Loglogistic:** \(G(t) = t^\omega / (t^\omega + \theta^\omega)\)

\(\theta\) is a scale (roughly a typical settlement age). \(\omega\) is a shape (how steep the emergence is).

## Two models that share the same curve

Clark writes incremental expected loss as

\[
E[\text{increment in age } j \text{ for AY } i] = \mu_i \cdot \bigl(G(t_j)-G(t_{j-1})\bigr)
\]

and then chooses what \(\mu_i\) is:

| Model | What \(\mu_i\) is | Familiar cousin |
|---|---|---|
| **LDF model** | a free ultimate for each accident year | chain ladder with a fitted pattern |
| **Cape Cod model** | \(\text{ELR}\times\text{exposure}_i\) (one ELR, known exposures) | Cape Cod / exposure-based BF |

The Cape Cod version is the star of the paper: borrowing strength across years through the exposure base **cuts the standard error** of the total reserve. Clark’s numerical example (Mack’s triangle) shows the total SE dropping when you switch from LDF to Cape Cod.

## Likelihood and the variance assumption (A6–A8)

He models incrementals with a variance function suitable for MLE (over-dispersed style: variance proportional to the mean, with a dispersion \(\sigma^2\)). Maximize the loglikelihood in the curve parameters (and the ELR, for Cape Cod).

What you can be asked to do:

- Write the expected increment as \(\mu\cdot\Delta G\).
- Recognize that MLE SEs come from the curvature of the loglikelihood (observed information / Hessian).
- Split **process variance** (the triangle is random even if parameters were known) from **parameter variance** (you estimated \(\theta,\omega,\mathrm{ELR}\)).
- Total predictive variance \(\approx\) process + parameter. Simulation (A8): draw parameters from the approximate normal (MLE, covariance = inverse information), then draw future increments given parameters.

Extrapolation: if the last age is not ultimate, you must let \(G(t)\) run past the triangle. That is a model assumption, not a data fact. Say so.

## Residuals and reasonableness (A3, A11)

Clark plots residuals vs age and vs fitted increment. You want:

- scatter around zero
- no fan that screams “variance is not proportional to mean”
- no systematic leftover at 12 and 24 months (his own example is a bit messy there; he does not reject the model outright)

If residuals trend with calendar year, the growth curve is missing a CY settlement-speed effect. Do not “fix” that by picking a weirder \(\omega\).

## Practical points they test

- **Exposure matters.** If you have a good on-level premium or policy count, Cape Cod Clark usually beats free-ultimate LDF Clark on SE.
- **Curve choice is not free.** Weibull vs loglogistic can change the tail. Show both, or show a sensitivity, if the unpaid lives in the tail.
- **Age definition.** Age from average accident date, not from January 1, if the book is not written evenly.
- **Does not automatically handle changing mix, changing limits, or a shock CY.** Those are A1 issues you fix before you fit.

## Exam grab bag

- Write \(E[c_{i,j}]=\mu_i(G(t_j)-G(t_{j-1}))\) and name the two choices of \(\mu_i\).
- Write Weibull and loglogistic \(G(t)\).
- Explain why Cape Cod SE < LDF SE (shared ELR + exposures).
- List process vs parameter variance and how you would simulate a reserve percentile.
- Name one residual plot and what a problem would look like.
