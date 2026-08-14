# Episode 03 — Benktander, Neuhaus, Hürlimann

**Hosts:** Riley and Sam  
**Length:** about 20 minutes  
**Tasks:** A1–A3, A6, A9, A11–A12  
**Papers:** Mack 2000; Hürlimann 2009 (no proofs)

---

**Riley:** Three methods, one line. I want CL, BF, and Benktander in numbers I can say aloud.

**Sam:** c is claims to date. p is percent reported, which is one over the LDF. U is the a priori ultimate, usually ELR times on-level premium.

Chain ladder ultimate: c over p.  
BF ultimate: c plus one minus p, times U.  
Benktander ultimate: p times the CL ultimate, plus one minus p times U.

Benktander IBNR is one minus p, times the Benktander ultimate. That is BF, but the “prior” you plug in is already a mix of CL and U.

**Riley:** The famous Z.

**Sam:** In Mack’s simple model, the credibility weight on chain ladder is Z equals p. Percent reported. Early year, small p, you sit near BF. Mature year, large p, you sit near CL. You do not get to put ninety percent on CL at twelve months and call it Benktander.

**Riley:** Say a number.

**Sam:** Reported 400. LDF 2.0, so p is 0.5. Prior U is 1,000.

CL ultimate: 400 over 0.5 is 800.  
BF ultimate: 400 plus 0.5 times 1,000 is 900.  
Benktander ultimate: 0.5 times 800 plus 0.5 times 1,000 is 900. Wait — when p is one-half and those particular numbers, BF and Benktander can land close; let’s shift U.

Prior U is 1,200.  
BF: 400 plus 0.5 times 1,200 is 1,000.  
Benktander: 0.5 times 800 plus 0.5 times 1,200 is 1,000.

Okay, bad luck on the arithmetic twins. Change reported to 300, LDF still 2, p still 0.5, U still 1,200.

CL: 300 over 0.5 is 600.  
BF: 300 plus 0.5 times 1,200 is 900.  
Benktander: 0.5 times 600 plus 0.5 times 1,200 is 900.

Hmm. When Z equals p and IBNR is one minus p times the mixed ultimate, Benktander ultimate equals p times CL plus one minus p times U, which is c plus one minus p times U… that is BF!

**Riley:** Wait. Is Benktander just BF?

**Sam:** Careful. The *ultimate* written as Z times CL plus one minus Z times U with Z equals p is:

p times (c over p) plus (1-p) U, which is c plus (1-p) U, which is the BF ultimate.

The thing that is not BF is the **IBNR / unpaid** view people use, and the **iterated** version. Benktander (1976) / iterated BF uses the BF *procedure* a second time, but replaces U with the first-pass BF or CL-influenced ultimate. Mack writes the IBNR as:

IBNR_B equals (1-p) times (p times U_CL plus (1-p) times U).

That is not (1-p) times U. That is (1-p) times a credibility ultimate. Let’s do numbers that cannot collapse.

c = 400, p = 0.25 (LDF 4), U = 2,000.

CL ultimate = 400 / 0.25 = 1,600.  
BF IBNR = 0.75 times 2,000 = 1,500. BF ultimate = 400 + 1,500 = 1,900.  
Benktander credibility ultimate = 0.25 times 1,600 + 0.75 times 2,000 = 400 + 1,500 = 1,900.  
Benktander IBNR = 0.75 times 1,900 = 1,425.

There. CL IBNR is 1,200. BF IBNR is 1,500. Benktander IBNR is 1,425. Between the parents, closer to BF because p is only a quarter. That is the picture.

**Riley:** Repeat those three IBNRs.

**Sam:** CL 1,200. BF 1,500. Benktander 1,425. Z equals p equals 0.25.

**Riley:** MSE. A9.

**Sam:** Under Mack’s simple model, Benktander’s mean squared error is almost always below both CL and BF, and close to a full Bayesian procedure. You do not prove it. You rank it. BF wins when the prior is decent and p is small. CL wins when p is large or the prior is junk. Benktander is the first iterate toward the Bayesian estimate. A second iterate is “iterated BF” and usually adds little.

**Riley:** Assumptions. A12.

**Sam:** It inherits both parents. From CL: p is the right pattern, no CY wrecking the diagonal. From BF: U is unbiased. A low ELR pulls Benktander low, just less than it pulls BF. If Benktander ever falls outside the range of CL and BF, you made an algebra error — it is a convex combination of the ultimates used in the IBNR formula.

**Riley:** Hürlimann. No proofs. What do I keep?

**Sam:** He restates the family in loss-ratio language so the collective prior is reproducible. Individual loss-ratio reserve: this origin period’s own claims, grossed up. Collective loss-ratio reserve: premium times a portfolio burning-cost LR, times the unreported percent. Credible reserve is Z on individual, one minus Z on collective.

CL is Z equals 1. BF is Z equals 0. Benktander is Z equals p. Neuhaus is another closed-form Z. Cape Cod is the member where everyone used the same premiums and the same exposure-weighted LR. That is his advertised win over Mack’s BF prior: same premiums, same collective reserve.

**Riley:** Optimal Z, in words only.

**Sam:** More reported, more weight on individual. Noisier reporting, less. Stronger collective prior, less. If Z comes out outside zero to one, a parameter went negative or p is bigger than one. Do not derive the normal equations. The outline said you are not responsible for mathematical proofs.

**Riley:** Exam grab bag.

**Sam:** Given c, LDF, U, compute CL, BF, and Benktander IBNR. State Z equals p. Rank the MSEs. Place Cape Cod on the same line. Name Hürlimann’s two talking points: pragmatic parameters, reproducible collective reserve from premiums. No proofs.

**Riley:** One more time. Immature year, good prior.

**Sam:** Sit near BF. Benktander Z equals p, p is small. Do not CL a twelve-month year just because the factor exists.
