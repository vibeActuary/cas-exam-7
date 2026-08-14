# Formula card (screenshot this)

Spoken forms are in parentheses. Episode numbers match `podcasts/`.

## Credibility development — Ep 02, 03

**Brosius**

\(L(X)=Z\cdot(X/d)+(1-Z)E[Y]\)  
(“L of X equals Z times X over d, plus one minus Z times the prior ultimate.”)

\(Z=\mathrm{VHM}/(\mathrm{VHM}+\mathrm{EVPV})\)

**Benktander / Mack 2000**

\(p=1/\mathrm{LDF}\) (percent reported)

\(\hat U_{CL}=c/p,\quad \hat U_{BF}=c+(1-p)U,\quad \hat U_B=p\cdot\hat U_{CL}+(1-p)U\)

\(\mathrm{IBNR}_B=(1-p)\hat U_B\)  
Benktander weight on CL is \(Z=p\).

**Hürlimann**

Individual LR reserve = CL-style gross-up of this origin period.  
Collective LR reserve = premium × collective LR × unreported %.  
Credible reserve \(= Z\cdot\text{individual}+(1-Z)\cdot\text{collective}\).  
Cape Cod is the “same premiums ⇒ same collective” member. Skip proofs.

## Clark — Ep 04

\(G_{\text{Weibull}}(t)=1-\exp(-(t/\theta)^\omega)\)

\(G_{\text{loglogistic}}(t)=t^\omega/(t^\omega+\theta^\omega)\)

\(E[\text{increment}_{i,j}]=\mu_i\bigl(G(t_j)-G(t_{j-1})\bigr)\)

- LDF model: \(\mu_i\) free per AY  
- Cape Cod: \(\mu_i=\mathrm{ELR}\times\text{exposure}_i\)

Predictive variance \(\approx\) process + parameter (MLE Hessian).

## Layers — Ep 05, 06

\(S(L_a,L_b)=\dfrac{\mathrm{LEV}(p_a)-\mathrm{LEV}(d_a)}{\mathrm{LEV}(p_b)-\mathrm{LEV}(d_b)}\)

\(F^{(X)}=F^{(B)}\cdot S_\infty(X,B)/S_j(X,B)\)

Limited: \(E[X\wedge D]\). Excess: \(E[(X-D)_+]\).  
Higher attachment or higher trend ⇒ larger tail LDF.

## Retro premium asset — Ep 07

\(P=(BP+CF\cdot L)\times TM\), then min/max.

If open: \(dP=CF\cdot TM\cdot dL\).  
If at max: \(dP=0\).  
Book-wide: \(dP/dL\in[0,\,CF\cdot TM]\).

## Mack chain ladder — Ep 08

\(E[C_{i,k+1}\mid C_{i,k}]=f_k C_{i,k}\)

\(\mathrm{Var}(C_{i,k+1}\mid C_{i,k})=\sigma_k^2 C_{i,k}\)

\(\hat f_k=\sum C_{i,k+1}/\sum C_{i,k}\)

\(\hat\sigma_k^2=\frac{1}{n_k-1}\sum C_{i,k}(C_{i,k+1}/C_{i,k}-\hat f_k)^2\)

mse = process + parameter.  
Portfolio SE: include covariance (shared \(\hat f\)). Do not add year SEs.  
Percentile needs an extra distributional assumption.

## Venter — Ep 09

Test: intercept, factor stability, residual vs size, residual vs CY.  
Intercept ≠ 0 ⇒ drop pure multiplicative CL.

## GLM / Taylor — Ep 10

\(\log E[Y_{ij}]=a_i+b_j\) (ODP ⇒ classical CL mean)

\(\mathrm{Var}(Y)=\phi\mu\) (ODP)

Prediction error = process + parameter. Nested test to leave CL (add CY, change variance).

## ODP bootstrap / Shapland — Ep 11

Fit → residuals → resample → refit (parameter) → simulate future (process) → histogram.  
Range ≠ two percentiles of a failed model.

## Meyers — Ep 12

Posterior predictive = MCMC parameter draws × future process draws.  
CSR = paid, changing settlement. CAY = incurred, correlated AYs.  
CoC margin = PV of cost of capital on the runoff, after dependence.

## Verrall — Ep 13

Expert selection ~ true ultimate + noise(\(\tau^2\)).  
Mean = credibility mix. Small \(\tau\) pulls hard. Do not shift a bootstrap after the fact.

## Marshall — Ep 14

Margin = conversion of **independent + systemic** uncertainty at a stated standard.  
Triangle tools miss systemic risk. Aggregate with a dependence assumption.

## Reinsurance — Ep 15–16

Quota share ceded \(\approx\) % × gross, after corridors/commissions.  
Excess unpaid from size model / exposure / BF, not from a 6-year excess CL.  
Cedent: push gross unpaid through the contract.  
Reinsurer: ELR / BF / Cape Cod, slower lag.  
Aggregate cover: ceded IBNR is an option on the subject ultimate.  
Open layer: add reinstatement premium.
