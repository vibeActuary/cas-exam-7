# Episode 13 — Verrall, expert opinion inside the distribution

**Hosts:** Riley and Sam  
**Length:** about 15 minutes  
**Tasks:** A9, A13  
**Paper:** Verrall 2007, Variance 1(1)

---

**Riley:** I selected an ultimate. Then I bootstrapped the triangle. Then I shifted the histogram so the mean matched my selection. Verrall hates me.

**Sam:** He does. That object is not a predictive distribution. Either the selection is treated as certain — distribution too tight, mean forced — or the selection is ignored and the mean is not the booked number. Verrall’s job is to put the expert **inside** the distribution so the mean is a credibility mix and the spread admits the expert might be wrong.

**Riley:** Mechanism, in words.

**Sam:** Start with a stochastic model — ODP, GLM, chain-ladder likelihood on incrementals. Treat the selected ultimates, or selected loss ratios, or selected tail, as data about the parameters, not as a replacement for the model. Encode the expert as a prior, or as a second likelihood: selected ultimate is the true ultimate plus noise with variance tau-squared.

The posterior predictive of unpaid is then a compromise. If the expert is very sure — tau small — and the triangle is thin, the distribution sits on the selection. If the expert is vague — tau large — or the triangle is rich, the distribution sits on the model.

The mean, A9, is a credibility mix of the model mean and the expert selection. The spread widens if you admit the expert might be wrong. That last sentence is the trap. Baking in a point and then bootstrapping around the raw triangle as if you had not selected is incoherent.

**Riley:** How do I encode “expert opinion” on an exam?

**Sam:** Pick one and name it.

Prior on accident-year loss ratios around the selected ELR, with a stated CV.

A likelihood: U-selected is normal around the true U with variance tau-squared.

A prior on the tail factor, not a fixed 1.05.

Different tau by year: tight on mature years where the actuary and the triangle already agree, looser on the current year.

Then simulate the posterior predictive.

**Riley:** Versus the neighbors.

**Sam:** Brosius, Benktander, Hürlimann: judgment enters as a prior ultimate, weight is formulaic. Shapland: mix whole distributions after the fact. Verrall: put the expert inside. Marshall: judgment dominates the risk margin, structured qualitatively. Meyers: priors on model parameters, validation against outcomes, not against an appointed-actuary pick.

**Riley:** Ranges, A13.

**Sam:** A Verrall range is not “CL to BF.” It is percentiles from a distribution that already includes the selection, or a set of distributions under different tau — a sensitivity to how hard you pull toward the expert. If management wants the booked number to be the mean, say that and back out the implied tau. That is a clean constructed-response ending.

**Riley:** Immature catastrophe year, tiny tau.

**Sam:** You are pretending you know the cat year. Write that. Small tau is fine on a mature year. Small tau on an immature year is theater.

**Riley:** Exam grab bag.

**Sam:** Why “bootstrap then shift the mean” is not a predictive distribution. Expert opinion is a prior or a second likelihood. Tau controls the pull. Mean is a credibility mix. Variance is larger than “selection is true.” Produce percentiles, then a sensitivity to tau.

**Riley:** Repeat tau.

**Sam:** Small tau, hard pull to the expert, tighter distribution. Large tau, sit on the model. Immature year, do not use a tiny tau unless you want to lie about uncertainty.
