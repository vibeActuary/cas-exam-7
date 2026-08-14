# Meyers — Stochastic Loss Reserving Using Bayesian MCMC Models, 2nd ed. (Monograph 8)

Tasks: **A9, A10, A11, A14**  
**2026 reading is Monograph #8, not #1.**

Official: [08-Meyers.pdf](https://www.casact.org/sites/default/files/2021-02/08-Meyers.pdf)

## Why a second edition exists

Monograph 1 already said: test models on the CAS Loss Reserve Database (hundreds of triangles **with outcomes**), and replace models that fail with Bayesian MCMC models. Edition 2 keeps the validation idea and adds the models you will actually be asked about:

1. Correlation between accident years (incurred data)
2. Changing claim settlement rate (paid data)
3. A unified paid + incurred model
4. Dependence between lines
5. A **cost-of-capital risk margin** (this is the A14 hook shared with Marshall)

## The validation punchline (A11)

On the CAS database:

- **Mack on incurred** often looks good in-sample and then **fails out-of-sample**. Incurred triangles are smoother because case reserves already contain judgment; Mack’s independence-of-years + variance function does not capture the way those judgments move together.
- **ODP bootstrap on paid** also fails a lot of outcomes: paid data have settlement-speed changes that a static development pattern cannot see.

“The SE is 8%” is not validation. Meyers’ standard is: hold out the later outcomes and ask whether the predictive distribution actually covered them at the rate it promised.

## Bayesian MCMC in one stanza (A10)

You write a full probability model (likelihood of the triangle given parameters + prior on parameters). MCMC draws from the **posterior** of the parameters. For each draw you simulate the future cells. The resulting unpaid sample is the **predictive distribution**, with process and parameter uncertainty included automatically. No Hessian, no residual-resampling choreography.

You do not need Stan code. You need:

- Likelihood + prior + posterior predictive
- Why MCMC is used (the posterior is not a pretty normal)
- What a posterior predictive check is (A11)

## Models to be able to name and place

| Model | Data | What problem it fixes |
|---|---|---|
| Cross-classified (CRC) | paid or incurred | Bayesian version of \(\alpha_i\beta_j\) / GLM CL |
| Stochastic Cape Cod (SCC) | paid or incurred | Shared ELR + premium/exposure; cuts parameter variance (Clark’s point, Bayesian) |
| Changing settlement rate (CSR) | **paid** | Development speeds up or slows down over calendar time |
| Correlated accident year (CAY) | **incurred** | Case-reserve adequacy / inflation hits many AYs together |
| CAY + CSR / unified paid-incurred | both | Uses both triangles; settlement and adequacy identified separately |
| Multi-line dependence | several lines | Shared shocks; needed before you add standalone risk margins |

If the item says “paid triangle, settlement has been speeding up,” the keyword is **CSR**.  
If it says “incurred, all recent years strengthened together,” the keyword is **CAY**.

## Risk margin (A14)

Meyers proposes a **cost-of-capital** risk margin: hold capital against the unpaid runoff, charge for that capital, discount. That is a market-consistent / Solvency-II-flavored margin, not “75th percentile minus mean.”

Contrast with Marshall (Episode 14):

- Marshall: structured qualitative + quantitative framework; CoC is one of several families.
- Meyers: an explicit CoC calculation sitting on top of a Bayesian predictive distribution, and a way to bring in multi-line dependence so you do not triple-count capital.

On an exam, if they ask for a risk margin from Meyers, write:

1. Get a predictive distribution of unpaid (and of future capital needs).
2. Choose a capital standard (e.g. a percentile or a 1-year shock).
3. Risk margin = present value of the cost of holding that capital over the runoff.
4. Diversification across lines uses the dependence model; summing standalone margins is too big.

## Exam grab bag

- Mack / ODP bootstrap **failed validation** on the CAS outcome database; say on which data (incurred vs paid).
- Name CSR vs CAY and which triangle each one is for.
- Predictive distribution = posterior draws × future process draws.
- Risk margin in this monograph is cost-of-capital, not a raw percentile gap.
- Edition 2 extras vs Monograph 1: CSR, CAY, paid+incurred, multi-line, CoC margin.
