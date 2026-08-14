# Sahasrabuddhe — Claims Development by Layer (2010, rev. 2013)

Tasks: **A4**

Official: [7_Sahasrabuddhe.pdf](https://www.casact.org/sites/default/files/2021-03/7_Sahasrabuddhe.pdf)

## The one-sentence thesis

Trend, development, and the size-of-loss model are **not** three independent knobs. Limited development factors move when inflation moves the size distribution through a deductible or limit. If you ignore that, your excess LDFs and your ILFs are internally inconsistent.

Cook (1970) killed the “overlap fallacy” (do not double-count trend and development). Sahasrabuddhe says: they do not overlap, but they **are connected**, and the connector is the claim-size model.

## Notation you need

- Layer \(L=(d,p)\): truncated below at deductible/attachment \(d\), censored above at limit \(p\).
- Ground-up unlimited (GUU): \(d=0\), \(p=\infty\).
- \(C_{i,j}^{(L)}\) = cumulative claims in layer \(L\) for AY \(i\) at age \(j\).
- \(T_{i,j}\) = cost-level index for GUU claims (can vary by AY and by development/calendar direction).
- \(\Phi_{i,j}\) = size-model name and parameters at that cost level.
- \(\mathrm{LEV}(x;\Phi)\) = limited expected value to \(x\).
- Limit-adjustment factor:

\[
S_{i,j}(L_a,L_b)=\frac{\mathrm{LEV}(p_a;\Phi_{i,j})-\mathrm{LEV}(d_a;\Phi_{i,j})}{\mathrm{LEV}(p_b;\Phi_{i,j})-\mathrm{LEV}(d_b;\Phi_{i,j})}
\]

- Development factor: \(F_{i,j}^{(L)}=E[C_{i,\infty}^{(L)}/C_{i,j}^{(L)}]\).

## The result they want you to compute (A4)

If you have a **basic-limit** development pattern \(F^{(B)}\) at a reference cost level, the development factor for any other layer \(X\) at any other cost level is the basic factor times a ratio of size-model limited means:

\[
F_{i,j}^{(X)} = F_{j}^{(B)}\cdot \frac{S_{i,\infty}(X,B)}{S_{i,j}(X,B)}
\]

In words: **excess layers develop longer** because inflation and late reporting move more mass through the attachment. A ground-up basic-limit factor applied to an excess layer is usually too small.

Practical shortcut when you only have an ultimate size model and one diagonal of observed layer ratios \(R_j = \) (layer \(X\) / basic) at the current valuation:

\[
F_{i,j}^{(X)} \approx F_j^{(B)}\cdot \frac{S_{i,\infty}(X,B)}{R_j}
\]

That is the “I do not have a size model at every age” version. Know when it is justified: cost-level differences in the *ratio* of layers are judged immaterial.

## Procedure on an exam spreadsheet

1. State the base layer \(B\) (where the triangle is credible) and the target layer \(X\).
2. Trend the size-model parameters with the GUU cost-level indices (lognormal \(\mu\) shifts by \(\ln T\); scale parameters of Pareto/exponential move with \(T\)).
3. Adjust the historical triangle to a common limit and cost level using LEV ratios (his equation 3.2) **before** you pick LDFs.
4. Convert the basic pattern to the target layer with the \(S\) ratio.
5. Apply those layer-specific LDFs to the target layer’s current diagonal.

## Consistency checks (this is how they catch you)

- Unlimited GUU + trend only in the AY direction ⇒ ordinary LDFs are fine. That is the special case.
- Higher attachment ⇒ larger tail LDF, all else equal.
- Higher trend ⇒ excess LDFs increase (more claims pierce the layer later).
- ILFs, trend, and LDFs must be computed from the **same** \(\Phi\). If your pricing ILF assumes a Pareto \(\alpha=1.5\) and your reserve LDFs assume lognormal, you have an A4 inconsistency even if each piece looks reasonable.

## What this paper is not

- It is not Pinto/Gogol (fit excess LDFs vs retention from a giant industry database). Sahasrabuddhe is for the actuary who has a size model and a primary pattern but not that database.
- It does not pick the size model for you. Garbage \(\Phi\) ⇒ garbage layer LDFs.

## Exam grab bag

- “Why does a $1M xs $1M layer have a larger 12-to-ult than ground-up $100k limited?” → size model + trend push late development into the excess layer.
- Write the \(S\) ratio and the conversion \(F^{(X)}=F^{(B)}\cdot S_\infty(X,B)/S_j(X,B)\).
- Name the three objects that must be internally consistent: development, trend, size model.
- State the Cook overlap-fallacy point in one clause, then the Sahasrabuddhe connector in the next.
