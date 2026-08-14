# Brosius — Loss Development Using Credibility (1993)

Tasks: **A1, A2, A3, A6, A11**

Official: [studynotes_brosius6.pdf](https://www.casact.org/sites/default/files/database/studynotes_brosius6.pdf)

## The problem he is solving

Link ratios treat the latest diagonal as fully credible. When a year is thin, one large claim or one late report blows the ultimate around. Practitioners already credibility-weight developed losses toward a prior. Brosius puts that instinct on a least-squares / Bühlmann footing and applies credibility **inside** the development step, not only after it.

## Setup

- \(X\) = amount reported to date (what you observe)
- \(Y\) = ultimate loss (what you want)
- \(d = E[X/Y]\) = expected percent reported, if you are thinking in “budgeted ultimate” language
- Prior / budgeted ultimate \(E[Y]\)

The naïve link-ratio estimate is \(X/d\). The naïve prior is \(E[Y]\). Brosius estimates \(Y\) with a linear function of \(X\):

\[
L(X) = a + bX
\]

chosen to minimize expected squared error. That is the least-squares development function.

## The credibility form you must be able to write

The best linear estimator can be rewritten as a credibility mix of the link-ratio ultimate and the prior ultimate:

\[
L(X) = Z\cdot\frac{X}{d} + (1-Z)\cdot E[Y]
\]

with Bühlmann-style credibility

\[
Z = \frac{\mathrm{VHM}}{\mathrm{VHM}+\mathrm{EVPV}}
\]

in the development setting:

- **VHM** (variance of hypothetical means) = uncertainty in the *true* ultimate / reporting mean across years. Big VHM means years really are different, so the data should get more weight.
- **EVPV** (expected process variance) = noise in the reporting process given the true ultimate. Big EVPV means the latest diagonal is noisy, so the prior should get more weight.

Intuition you should say out loud on the exam:

- If reporting is almost deterministic (\(EVPV \approx 0\)), \(Z \to 1\) and you are back to a pure link ratio.
- If the prior is almost certain and the reported-to-date figure is junk (\(VHM \approx 0\)), \(Z \to 0\) and you stay with the budgeted ultimate.
- Thin years, excess layers, and new states look like high EVPV. Stable, high-volume years look like high VHM relative to process noise.

## What you actually compute from a triangle

Brosius walks a small-state example where 15-to-27 month link ratios jump around (1.05 to 2.75). The method:

1. Treat development as a regression of later-age losses on earlier-age losses.
2. The slope is a credibility-adjusted age-to-age factor; the intercept is the complement going to the prior.
3. You can also estimate EVPV and VHM from the scatter of observed pairs \((X, Y)\) across accident years, then plug into \(Z\).

On a constructed-response item they usually give you either:

- enough pairs to compute a least-squares slope and intercept, or
- EVPV, VHM, \(d\), \(X\), and \(E[Y]\) and ask for \(Z\) and \(L(X)\).

## Diagnostics (A1 / A11)

Use Brosius thinking when the triangle is screaming:

- One year with a huge factor and tiny volume
- A new AY with almost no reported loss
- A line that is changing mix so the prior \(E[Y]\) is stale

The method **does not** fix a bad prior. If \(E[Y]\) is systematically low, \(L(X)\) is pulled low. That is an A3 reasonableness point: compare Brosius ultimates to Cape Cod / BF / chain ladder and ask whether the prior, not the data, is the problem.

## Limitations they like to test

- Linearity is an approximation. A fully Bayesian development function can be nonlinear.
- Independence / stability assumptions break if there is a calendar-year shock (law change, settlement speed-up) hitting the latest diagonal.
- You still need a prior. “Credibility” is not a substitute for having no expected loss ratio.
- Inflation and changing limits are outside the simple model; if you ignore them you mis-estimate both \(d\) and \(E[Y]\).

## Exam grab bag

- Write \(L(X)=Z(X/d)+(1-Z)E[Y]\) and define \(Z\).
- Say what happens to \(Z\) if a year is thin (EVPV up, \(Z\) down).
- Contrast with Benktander (Episode 03): Brosius credibility-weights the *development function*; Benktander credibility-weights CL vs BF *reserves*.
- If they give a scatter of early vs late losses, the intercept is the “prior residual” and the slope is the credible LDF piece.
