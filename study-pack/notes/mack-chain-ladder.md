# Mack — Measuring the Variability of Chain Ladder Reserve Estimates (1994)

Tasks: **A2, A6, A7, A8**

Official: [7_Mack_1994.pdf](https://www.casact.org/sites/default/files/2021-03/7_Mack_1994.pdf)

Companion (not separately listed, but the clean formula paper): Mack, ASTIN 1993, distribution-free SE of chain ladder.

## What the chain ladder actually assumes

For cumulative losses \(C_{i,k}\) (AY \(i\), age \(k\)):

1. **Proportionality:** \(E[C_{i,k+1}\mid C_{i,1},\ldots,C_{i,k}] = f_k\, C_{i,k}\)
2. **Variance:** \(\mathrm{Var}(C_{i,k+1}\mid C_{i,1},\ldots,C_{i,k}) = \sigma_k^2\, C_{i,k}\)
3. **Independence of accident years**

The usual volume-weighted age-to-age factor is the unbiased estimator of \(f_k\):

\[
\hat f_k = \frac{\sum_i C_{i,k+1}}{\sum_i C_{i,k}}
\]

and

\[
\hat\sigma_k^2 = \frac{1}{n_k-1}\sum_i C_{i,k}\left(\frac{C_{i,k+1}}{C_{i,k}}-\hat f_k\right)^2
\]

where the sums run over years that have both ages. The last \(\sigma\) (one observation) is extrapolated, often \(\hat\sigma_{I-1}^2=\min(\hat\sigma_{I-2}^4/\hat\sigma_{I-3}^2,\;\min(\hat\sigma_{I-2}^2,\hat\sigma_{I-3}^2))\).

Point estimate (A2): \(\hat C_{i,I} = C_{i,I+1-i}\cdot\hat f_{I+1-i}\cdots\hat f_{I-1}\), reserve \(\hat R_i=\hat C_{i,I}-C_{i,\text{latest}}\).

## Mean squared error of prediction (A6–A7)

The reserve is a random variable, not a parameter. Mack’s **standard error** estimates \(\sqrt{\mathrm{mse}(\hat R_i)}=\sqrt{E[(\hat R_i-R_i)^2\mid\text{triangle}]}\).

For one accident year, mse splits into:

- **Process variance** — future development would be random even if the \(f_k\) were known.
- **Parameter / estimation variance** — you estimated the \(f_k\) from a finite triangle. Factors are uncorrelated under the model, so you can add those pieces.

Rough structure you should be able to narrate:

\[
\frac{\mathrm{mse}(\hat C_{i,I})}{\hat C_{i,I}^2}
\approx \sum_{k}\frac{\hat\sigma_k^2}{\hat f_k^2}\left(\frac{1}{\hat C_{i,k}}+\frac{1}{\sum_{j\text{ used}}C_{j,k}}\right)
\]

(process term uses \(1/\hat C_{i,k}\); parameter term uses \(1/\sum C_{j,k}\)).

**Total reserve** is not the sum of SEs. Years share the same \(\hat f_k\), so they are correlated. Mack gives a formula that adds a covariance piece. If you just RSS the year SEs you **understate** the portfolio SE.

## Confidence intervals and simulation (A7, A8)

Mack is distribution-free for the SE. To get percentiles you must add a distributional assumption:

- Normal: \(\hat R \pm z\cdot\mathrm{se}\) — often terrible because reserves are skewed and can go negative.
- Lognormal on the ultimate or on the reserve, matching mean and mse.
- Bootstrap the triangle (that is Shapland’s world) or simulate future increments from the Mack variance function.

On the exam: if they ask for a 90th percentile from Mack alone, say you need an extra distributional assumption and state which one you are using.

## When **not** to use Mack (this is also Venter)

The 1994 paper is as much a “when is chain ladder legal” paper as an SE paper. If age-to-age factors trend with year, if variance is not proportional to \(C_{i,k}\), if calendar-year shocks hit the diagonal, the SE is a precise number attached to the wrong model.

## Exam grab bag

- Write the three Mack assumptions.
- Compute \(\hat f_k\) and \(\hat\sigma_k^2\) from a tiny triangle.
- Split process vs parameter variance in words.
- “Can I add the year SEs?” → No. Shared factors ⇒ positive covariance.
- Last \(\sigma\) needs an extrapolation rule. Name one.
- SE is not a percentile. Percentile needs a distribution.
