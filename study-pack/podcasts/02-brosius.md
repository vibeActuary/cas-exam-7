# Episode 02 — Brosius, credibility LDFs

**Hosts:** Riley and Sam  
**Length:** about 18 minutes  
**Tasks:** A1, A2, A3, A6, A11  
**Paper:** Brosius 1993

---

**Riley:** I have a small state. The fifteen-to-twenty-seven month factors are 1.22, 1.26, 1.29, 1.86, 1.05, 2.75. The newest year is already high. If I put a 1.40 on it I feel sick. That is the Brosius opening, right?

**Sam:** That is literally his table-one mood. Link ratios treat the latest diagonal as fully credible. When the year is thin, one claim owns the factor. Practitioners already weight developed losses toward a prior. Brosius puts that inside the development step and gives it a least-squares / Bühlmann name.

**Riley:** Setup in words.

**Sam:** X is reported to date. Y is ultimate. d is the expected percent reported. E of Y is the budgeted or prior ultimate. The naïve link-ratio ultimate is X over d. The naïve prior is E of Y. He estimates Y with a straight line in X: L of X equals a plus b X, chosen to minimize expected squared error. That line can be rewritten as a credibility mix.

**Riley:** Formula card. I need this in my mouth.

**Sam:** L of X equals Z times X over d, plus one minus Z times the prior ultimate.

Z equals VHM over VHM plus EVPV.

VHM — variance of hypothetical means — is “years really are different.” Big VHM, trust the data.

EVPV — expected process variance — is “the reporting process is noisy given the true ultimate.” Big EVPV, trust the prior.

**Riley:** Again.

**Sam:** L of X equals Z times X over d, plus one minus Z times E of Y. Z equals VHM over VHM plus EVPV.

**Riley:** Limits.

**Sam:** If reporting is almost deterministic, EVPV goes to zero, Z goes to one, you are back to a pure link ratio. If the prior is almost certain and the reported-to-date is junk, VHM goes to zero, Z goes to zero, you stay with the budget. Thin years, excess layers, new states: high EVPV, low Z. Fat, stable years: Z near one.

**Riley:** They give me pairs of early-age and late-age losses across accident years. What do I compute?

**Sam:** A regression. Later versus earlier. The slope is a credibility-adjusted age-to-age. The intercept is the piece that goes to the prior. Or they hand you EVPV, VHM, d, X, and E of Y, and you just compute Z and L of X. That is an A2 / A6 fill-in-the-blank.

**Riley:** A3. How do I test this?

**Sam:** Credibility does not fix a bad prior. If E of Y is twenty percent low, L of X is pulled low. Compare Brosius ultimates to Cape Cod, BF, and chain ladder. If Brosius sits on a prior that the rest of the world has abandoned, the problem is the prior, not Z.

Also: if a calendar-year shock hit the latest diagonal, X is not the X the model had in mind. That is episode 01 and episode 09. Do not credibility-weight a CY event into “the year was just thin.”

**Riley:** A11, test the output of a distribution. Brosius is a point-estimate paper. Why is it mapped to A11?

**Sam:** Because Z is a parameter of a loss-development distribution. If you later bootstrap or Mack a triangle of Brosius-adjusted factors, you still have to ask whether the Z’s are sane. A Z of 1.4 is an algebra error. A Z of 0.95 on a twelve-month excess year is you ignoring EVPV.

**Riley:** Versus Benktander, which is next.

**Sam:** Brosius credibility-weights the development function. Benktander credibility-weights the chain-ladder ultimate against the BF ultimate, and the weight is the percent reported. Related instinct, different object. If an item says “least squares development” or “regression of later on earlier,” it is Brosius. If it says “iterated BF” or “Z equals p,” it is Mack two-thousand.

**Riley:** Limitations I should write in a constructed response.

**Sam:** Linearity is an approximation. A fully Bayesian development function can be nonlinear. You still need a prior — credibility is not a method for having no expected loss ratio. Inflation and changing limits sit outside the simple model. Independence dies if a CY shock hits everyone at once.

**Riley:** Exam grab bag.

**Sam:** Write L of X equals Z times X over d plus one minus Z times E of Y. Define Z. Say what happens to Z if the year is thin: EVPV up, Z down. If they give a scatter, intercept is the prior residual, slope is the credible LDF. Do not use Brosius to launder a prior you do not believe.

**Riley:** Repeat Z.

**Sam:** VHM over VHM plus EVPV. Thin year, EVPV up, Z down, sit on the prior.
