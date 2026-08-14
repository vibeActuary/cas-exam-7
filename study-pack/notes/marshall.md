# Marshall, Collings, Hodson, O’Dowd — A Framework for Assessing Risk Margins (2008)

Tasks: **A14**

Official: [7_Marshall_et_al.pdf](https://www.casact.org/sites/default/files/2021-03/7_Marshall_et_al.pdf)

## The thesis

A risk margin is not “the 75th minus the mean from one bootstrap.” Historical quantitative analysis **cannot** capture all future uncertainty. Judgment will often dominate. The paper’s contribution is a **framework** that forces you to name the sources of uncertainty, run the quantitative tools that actually apply, and then apply judgment in a structured way instead of a vibes-based 10%.

This is an Australian GI-seminar paper. The exam wants the framework, not APRA paragraph numbers.

## Sources of uncertainty to list on command

Split them; do not dump “parameter, process, model” and sit down.

**Independent risk (diversifies in a large portfolio)**

- Process / random variation around the mean
- Some parameter error on frequency/severity if the book is huge

**Systemic risk (does not diversify, or diversifies badly)**

- Event / catastrophe
- Underwriting cycle and inflation
- Legislative / judicial change
- Claim-management / settlement-speed change
- Model error and “unknown unknowns”
- Correlation across lines and across years (Meyers CAY lives here)

A risk margin that only bootstraps last year’s triangle has **almost no systemic piece**. That is the paper’s central warning.

## Quantitative toolkit (advantages / disadvantages)

You should be able to match a tool to a source:

| Tool | Good for | Weak for |
|---|---|---|
| Analytical SE (Mack) | Process + CL parameter error, one triangle | CY shocks, model error, multi-line, future inflation |
| Bootstrap / GLM (Shapland, Taylor) | Full predictive shape, some model variants | Still mostly historical independent risk |
| Bayesian MCMC (Meyers) | Parameter uncertainty, CSR/CAY, dependence | Prior specification; still thin on legislative risk |
| Scenario / stress | Systemic events, law change, inflation | Probability calibration |
| Industry benchmarks / peer margins | External check | Different books, different accounting |
| Cost of capital | Market / regulatory margin (Meyers Ch. 11) | Circular if capital itself is a guessed percentile |

No single tool is enough. The framework is: run what you can, then **explicitly add** the pieces the tool cannot see.

## The structured-judgment part (this is the paper)

They want a documented path, not a mysterious overlay:

1. **Identify** each material source of uncertainty for *this* book.
2. **Quantify** what the data/models can quantify. Write down what they cannot.
3. **Assess** the systemic / judgment items with a scale (low / medium / high, or a chosen CV), using scenarios and external evidence.
4. **Aggregate** with a dependence story (not “sum the CVs,” not “assume independence”). Copulas, correlation matrices, or at least a stated diversification credit.
5. **Convert** the aggregate uncertainty into a margin at the required sufficiency standard (percentile, CTE, CoC, regulatory formula).
6. **Communicate** the margin as a function of the standard and the sources, so a 75th-percentile margin is not compared naïvely to a CoC margin.

## How this sits next to Meyers

- Meyers: a specific CoC calculation on a Bayesian predictive distribution, plus multi-line dependence.
- Marshall: the governance wrapper. CoC is one conversion step. Most of the mark is for naming missing systemic risk and not double-counting.

If an item gives you a bootstrap CV of 8% and asks for a risk margin for a long-tailed liability book, the Marshall answer is: 8% is not the margin. Add inflation, judicial, CY, and dependence, then pick a standard.

## Exam grab bag

- Define risk margin vs central estimate.
- List at least four systemic sources the triangle does not contain.
- “Why is a Mack 75th too small for a risk margin?”
- Sketch the six framework steps.
- Aggregation: independence understates; comonotonicity overstates; you need a dependence assumption.
- Do not invent APRA/Solvency II numbers unless they are given.
