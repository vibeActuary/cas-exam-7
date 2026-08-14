# Episode 10 — Taylor and McGuire, GLM reserving

**Hosts:** Riley and Sam  
**Length:** about 18 minutes  
**Tasks:** A9–A12  
**Paper:** CAS Monograph 3, **chapters 1–6** (2026)

---

**Riley:** “Chain ladder is a GLM.” I have heard the slogan. What do I actually write?

**Sam:** Incremental paid or incurred in cell i, j is Y-i-j. Log of expected Y equals a-sub-i plus b-sub-j. One parameter per accident year, one per development year, no interaction, no calendar year. That is a cross-classified model. Put an over-dispersed Poisson around it — variance equals phi times mu — and the MLE mean matches the classical chain-ladder forecasts. That is the bridge to Shapland’s bootstrap.

**Riley:** Repeat the mean.

**Sam:** Log E of Y-i-j equals a-i plus b-j. ODP plus that mean gives classical CL unpaid.

**Riley:** Why bother writing it as a GLM?

**Sam:** Because then the reserve has a distribution, A9 and A10. Residuals have names — deviance, Pearson, leverage — A11. And you can test whether you need to leave chain ladder by adding a calendar-year covariate or changing the variance function and asking whether deviance dropped enough, A12. That is Venter in GLM clothes, with a likelihood ratio instead of a vibe.

**Riley:** Twenty twenty-six added chapters four through six. What is in them?

**Sam:** One and two are motivation: reserve is a random variable, process versus estimation error. Three is the slogan. Four is diagnostics: residual plots, hat matrix, leverage. Five is “do you need to leave CL?” Nested-model tests, CY terms, changing development. Six is the extensions: different variance functions, smoothing the development parameters, exposure offsets that make it Cape Cod-like, Tweedie or gamma if ODP is the wrong shape.

If an item says Taylor-McGuire and asks for a test of chain-ladder assumptions, do not write Mack’s sigma formula. Write a nested GLM test plus residual plots.

**Riley:** Prediction error.

**Sam:** Mean reserve: sum of fitted future incrementals. Prediction variance: process — phi times mu for ODP — plus parameter, from the inverse Fisher information or from a bootstrap of beta-hat. Predictive distribution: draw beta from its covariance, then draw future Y from the exponential-dispersion family. Analytical percentiles are rare. Over-dispersion phi bigger than one is normal. Phi equals one, pure Poisson, understates SEs badly. Say that if they give you a Poisson-looking model on real dollars.

**Riley:** Diagnostics I will be shown.

**Sam:** Residual heatmap versus accident year, development year, calendar year. Scale: is variance over mu constant? If not, change the variance function. One cell with a huge Pearson residual is an A1 data problem before it is a model problem. A significant calendar-year parameter means you do not still report a Mack SE as if nothing happened.

**Riley:** Exam grab bag.

**Sam:** Write log E Y-i-j equals a-i plus b-j. ODP implies classical CL forecasts. Two reasons to leave CL: significant CY term, or variance not proportional to the mean. Prediction error is process plus parameter. Phi multiplies process. Twenty twenty-six can ask the chapter four through six extensions, not just the slogan.

**Riley:** One sentence for the grader.

**Sam:** I will treat chain ladder as an ODP GLM, test a calendar-year term, and only then quote a prediction error.
