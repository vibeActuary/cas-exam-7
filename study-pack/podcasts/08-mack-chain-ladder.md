# Episode 08 — Mack chain-ladder variance

**Hosts:** Riley and Sam  
**Length:** about 18 minutes  
**Tasks:** A2, A6–A8  
**Paper:** Mack 1994

---

**Riley:** I can run chain ladder in my sleep. Mack wants the standard error. What did I actually assume?

**Sam:** Three things, and you should be able to write them.

One. Proportionality. Expected next cumulative, given the past of that accident year, is f-sub-k times this cumulative. Line through the origin.

Two. Variance. Variance of the next cumulative, given the past, is sigma-sub-k squared times this cumulative.

Three. Accident years are independent.

The volume-weighted age-to-age, sum of C-k-plus-one over sum of C-k, is the unbiased estimator of f-k under those assumptions. It is not a vibe. It is optimal **if** the variance function is right. If Venter later shows the variance function is wrong, even the point estimate weights are wrong.

**Riley:** Sigma-hat.

**Sam:** Sigma-k squared hat is one over n-k minus one, times the sum of C-i-k times (the observed factor minus f-hat) squared. The last sigma has one observation. You extrapolate. A common rule: min of sigma-I-minus-two to the fourth over sigma-I-minus-three squared, and the min of the last two sigmas. Name a rule if they ask. Do not invent a 0.01.

**Riley:** Point estimate, A2.

**Sam:** Ultimate for year i is the latest cumulative times the remaining f-hats. Reserve is ultimate minus latest. That is ordinary chain ladder. Mack did not change the mean.

**Riley:** Mean squared error of prediction. Why not “the variance of f”?

**Sam:** Because the reserve is a random variable, not a parameter. Even if you knew every f, future development would still bounce. That is process variance. On top of that, you estimated the f’s from a finite triangle. That is parameter variance. Mack’s standard error estimates the square root of the expected squared difference between your reserve estimate and the true unpaid, given the triangle.

**Riley:** The formula in words.

**Sam:** For one accident year, mse over ultimate squared is approximately a sum over future ages of: sigma-k squared over f-k squared, times (one over this year’s C-k, plus one over the sum of C-k used to estimate f-k). The first one-over is process. The second is parameter. You do not need to expand every index on the plane. You need to narrate those two pieces.

**Riley:** Total reserve. Can I add the year standard errors?

**Sam:** No. That is the most-tested sentence in the paper. Years share the same f-hats, so the year estimates are positively correlated. Mack’s portfolio formula adds a covariance piece. If you root-sum-square the year SEs you understate the portfolio SE. If you add the SEs you overstate it. Use the formula they want, and say “shared factors, positive covariance.”

**Riley:** Percentiles. A7, A8.

**Sam:** Mack is distribution-free for the SE. A ninetieth percentile is not in the paper. You must add a distribution. Normal on the reserve: often terrible, skewed, can go negative. Lognormal on the ultimate or on the reserve, matching mean and mse: common. Or simulate future increments from the Mack variance function, or bootstrap — that is Shapland’s episode.

If they ask for a ninetieth from Mack alone, write: I need a distributional assumption, I am using lognormal on the unpaid with this mean and this mse, here is the percentile.

**Riley:** When not to use Mack.

**Sam:** If age-to-age factors trend with year, if variance is not proportional to C, if a calendar-year shock painted the latest diagonal, the SE is a precise number on the wrong model. Episode 09 is the test suite. Episode 12 is Meyers saying Mack on incurred failed out-of-sample validation on the CAS database.

**Riley:** Exam grab bag.

**Sam:** Write the three assumptions. Compute f-hat and sigma-hat from a tiny triangle. Split process versus parameter. Do not add year SEs. Last sigma needs an extrapolation rule. SE is not a percentile.

**Riley:** Repeat the portfolio sentence.

**Sam:** Shared development factors create positive covariance. The portfolio SE is not the sum of the year SEs and not the RSS either — use Mack’s total-reserve formula.
