# Episode 14 — Marshall, risk margins

**Hosts:** Riley and Sam  
**Length:** about 16 minutes  
**Tasks:** A14  
**Paper:** Marshall, Collings, Hodson, O’Dowd 2008

---

**Riley:** I have a bootstrap. CV is eight percent. Seventy-fifth minus mean is my risk margin. Marshall is about to take my lunch.

**Sam:** A risk margin is not the seventy-fifth minus the mean from one bootstrap. Historical quantitative analysis cannot capture all future uncertainty. Judgment will often dominate. The paper’s contribution is a framework that forces you to name the sources, run the quantitative tools that actually apply, and then apply judgment in a structured way instead of a vibes-based ten percent. Australian GI seminar. The exam wants the framework, not APRA paragraph numbers.

**Riley:** Sources. Do not say “parameter, process, model” and sit down.

**Sam:** Split independent from systemic.

Independent, diversifies in a large portfolio: process variation around the mean. Some parameter error on frequency and severity if the book is huge.

Systemic, does not diversify, or diversifies badly: catastrophe. Underwriting cycle and inflation. Legislative and judicial change. Claim-management and settlement-speed change. Model error and unknown unknowns. Correlation across lines and across years — Meyers CAY lives here.

A risk margin that only bootstraps last year’s triangle has almost no systemic piece. That is the central warning.

**Riley:** Match a tool to a source.

**Sam:** Mack SE: process plus chain-ladder parameter error, one triangle. Weak on CY shocks, model error, multi-line, future inflation.

Bootstrap and GLM: full predictive shape, some model variants. Still mostly historical independent risk.

Bayesian MCMC: parameter uncertainty, CSR, CAY, dependence. Still thin on legislative risk. Priors matter.

Scenarios and stresses: systemic events, law change, inflation. Weak on probability calibration.

Industry benchmarks: external check. Different books, different accounting.

Cost of capital: market or regulatory margin — Meyers chapter eleven. Circular if capital itself is a guessed percentile.

No single tool is enough. Run what you can, then **explicitly add** the pieces the tool cannot see.

**Riley:** The six framework steps I will write.

**Sam:** One: identify each material source for *this* book. Two: quantify what the data and models can quantify, and write down what they cannot. Three: assess the systemic and judgment items with a scale — low, medium, high, or a chosen CV — using scenarios and external evidence. Four: aggregate with a dependence story. Not “sum the CVs.” Not “assume independence.” A copula, a correlation matrix, or at least a stated diversification credit. Five: convert the aggregate uncertainty into a margin at the required sufficiency standard — percentile, CTE, cost of capital, regulatory formula. Six: communicate the margin as a function of the standard and the sources, so a seventy-fifth is not compared naïvely to a cost-of-capital margin.

**Riley:** Versus Meyers.

**Sam:** Meyers: a specific CoC calculation on a Bayesian predictive distribution, plus multi-line dependence. Marshall: the governance wrapper. CoC is one conversion step. Most of the marks are for naming missing systemic risk and not double-counting.

**Riley:** Exam grab bag.

**Sam:** Define risk margin versus central estimate. List at least four systemic sources the triangle does not contain. Why a Mack seventy-fifth is too small for a risk margin. Sketch the six steps. Aggregation: independence understates, comonotonicity overstates, you need a dependence assumption. Do not invent Solvency II numbers they did not give.

**Riley:** Repeat the warning.

**Sam:** Eight percent bootstrap CV is not the margin. Add inflation, judicial, calendar-year, and dependence, then pick a standard.
