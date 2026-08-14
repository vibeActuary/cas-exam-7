# Episode 12 — Meyers, Bayesian MCMC (Monograph 8)

**Hosts:** Riley and Sam  
**Length:** about 18 minutes  
**Tasks:** A9–A11, A14  
**Paper:** CAS Monograph 8, 2nd edition — **not** Monograph 1

---

**Riley:** I almost downloaded Monograph 1. That would have been bad.

**Sam:** Fatal for twenty twenty-six. Meyers is Monograph eight, second edition. Edition one already had the idea: test models on the CAS Loss Reserve Database — hundreds of triangles **with outcomes**. Edition two keeps the validation and adds the models they will name: correlated accident years on incurred, changing settlement rate on paid, a unified paid-plus-incurred model, dependence between lines, and a cost-of-capital risk margin. That last one is your A14 hook next to Marshall.

**Riley:** Validation punchline.

**Sam:** Mack on incurred often looks beautiful in-sample and fails out-of-sample. Incurred triangles are smooth because case reserves already contain judgment. Mack’s independent-years story does not capture those judgments moving together.

ODP bootstrap on paid also misses a lot of outcomes. Paid data have settlement-speed changes a static pattern cannot see.

“The SE is eight percent” is not validation. Meyers’ standard is: hold out later outcomes and ask whether the predictive distribution covered them at the rate it promised. That is A11 at the grown-up table.

**Riley:** Bayesian MCMC in one stanza. I do not need Stan.

**Sam:** You write a full probability model: likelihood of the triangle given parameters, and a prior on the parameters. MCMC draws from the posterior of the parameters. For each draw you simulate the future cells. The unpaid sample is the predictive distribution. Process and parameter uncertainty are both in it. No Hessian. No residual-resampling choreography.

You need those three words: likelihood, prior, posterior predictive. And you need to say why MCMC exists: the posterior is not a pretty normal.

**Riley:** Name the models and which triangle they fix.

**Sam:** Cross-classified: Bayesian alpha-i beta-j. GLM chain ladder with priors.

Stochastic Cape Cod: shared ELR plus premium. Clark’s SE reduction, Bayesian.

Changing settlement rate, CSR: **paid** data, development speeding up or slowing down over calendar time.

Correlated accident year, CAY: **incurred** data, case-reserve adequacy or inflation hitting many years together.

CAY plus CSR, or a unified paid-and-incurred model: uses both triangles so settlement and adequacy can be identified separately.

Multi-line dependence: shared shocks. You need this before you add standalone risk margins or you triple-count capital.

**Riley:** Paid triangle, settlement has been speeding up.

**Sam:** Keyword CSR.

**Riley:** Incurred, all recent years strengthened together.

**Sam:** Keyword CAY.

**Riley:** Risk margin, A14.

**Sam:** Meyers’ margin is cost of capital, not “seventy-fifth minus mean.” Hold capital against the unpaid runoff, charge for that capital, discount. Market-consistent, Solvency-II-flavored.

Steps you can write: get a predictive distribution of unpaid and of future capital needs. Choose a capital standard — a percentile or a one-year shock. Risk margin is the present value of the cost of holding that capital over the runoff. Diversification across lines uses the dependence model. Summing standalone margins is too big.

Marshall, next-plus-one episode, is the governance wrapper. CoC is one conversion. Marshall will yell at you if the only uncertainty you quantified is a bootstrap CV.

**Riley:** Exam grab bag.

**Sam:** Mack and ODP bootstrap failed validation on the CAS outcome database — incurred versus paid. CSR is paid. CAY is incurred. Predictive distribution equals posterior draws times future process draws. Risk margin here is cost-of-capital. Edition two extras: CSR, CAY, paid-plus-incurred, multi-line, CoC margin.

**Riley:** Repeat CSR versus CAY.

**Sam:** CSR, paid, settlement speed. CAY, incurred, years moving together.
