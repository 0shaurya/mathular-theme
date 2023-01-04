---
title: Simple and Compound Interest
layout: page
menuInclude: yes
menuLink: yes
menuTopTitle: Precalculus
menuSubs:
- title: Simple and Compound Interest
  index: 1
excerpt: "Who doesn't like making money?!"
terms:
  - ['Interest', 'Money put into bank account regularly at a specified percentage']
  - ['Simple Interest', 'A type of interest where the same amount of money is paid regularly. That amount is determined by the initial value deposited into the bank account.']
  - ['Principal', 'The initial amount of money deposited into a bank account']
  - ['Compound Interest', 'A type of interest where the amount of interest paid is a percentage of the money in the bank account at the time of interest being paid']
questions:
  - ['What is the simple interest gained for a bank account whose principal value was $150 if the interest rate is 10%?', '$15, because \(150 \cdot 0.1 = 15\).']
  - ['How much money will be in David''s bank account after 5 months if he starts with $100 and the simple interest rate is 3% monthly?', '\(A=100(1+(0.03)(5)) = 100(1.15) = $115\)']
  - ['How much money will be in Lisa''s bank account after 4 years if she starts with $500 and the compound interest rate is 2%, compounded monthly?', '\(A=500(1+\frac{0.02}{12})^{12\cdot 4} = $541.6\)']
---


<h1>Precalculus</h1>

<h2>Simple and Compound Interest</h2><br>

A bank will give you <b>interest</b> on money stored in an account. Interest is the money paid regularly at a specified percentage. For example, if Alice keeps $100 in her bank account, and it has an interest rate of 3% monthly, she will get 3 more dollars in her account the next month.

There are two types of interest. The first type is <b>simple interest</b>. Simple interest is when the bank pays you back at a percentage of the initial value deposited. For example, if Bob deposits $1,000 into his bank account initially (note that the initial value deposited is known as the <b>principal</b> value), with a simple interest of 10% yearly, he will gain \\(0.1\cdot1000=100\\) dollars every year. Bob's account will look like the following:

table

The formula for calculating how much money will be in an account after a certain amount of time depending on the simple interest rate is:

$$A=P(1+rt)$$

where \\(r\\) is the interest rate, \\(t\\) is the amount of time, \\(P\\) is the principal value, and \\(A\\) is the final amount. This formula works because the interest rate is added over and over again for the amount of time (that's what the multiplication of \\(r\\) and \\(t\\) represents). This number is added to the \\(1\\) - the \\(1\\) represents 100% of the principal value. We add the 1 because we want to add the initial principal value onto the interest to find the total amount.

For example, to find the money in Bob's account after 17 years, we can plug the following values into the formula to get

$$A = P(1+rt)$$

$$\begin{split}
A &= 1000(1+0.1\cdot17)\\
A &= 1000(1+1.7)\\
A &= 1000(2.7)\\
A &= 2700
\end{split}$$

Bob will have \\(2700\\) in his account after 17 years, assuming he does not withdraw or deposit any more money. The great thing about simple interest is that if Bob deposits \\(500\\) dollars midway through the 17 years, we know that he will end up with \\(3200\\). No matter when Bob adds the \\(500\\), we can safely just add \\(500\\) at the end to find his final amount.

<b>Compound interest</b> is the other type of interest. While simple interest adds a percentage of the principal value, compound interest adds a percentage of the current value. For example, if Charlie deposits \\(1000\\) as his principal value, and his interest rate is 1% monthly, his bank account will look like the following:

(table)

The formula for compound interest is quite a bit more complicated than the simple interest formula:

$$A = P(1+\frac{r}{n})^{nt}$$

Here, \\(n\\) is the new parameter. \\(n\\) represents the number of times the money is compounded per time period \\(t\\). For example, if \\(t\\) is measured in years and the money is compounded monthly, \\(n\\) would be 12. If \\(t\\) was measured in years and the money was compounded years, \\(n\\) would be 1.

Let's plug our new formula into Charlie's situation to find out how much money he would have after 3 years:

$$A = P(1+\frac{r}{n})^{nt}$$

$$\begin{align*}
A &= 1000(1+\frac{0.01}{12})^{12\cdot3}\\
A &= 1000(\frac{12.01}{12})^{36}\\
A &= 1000(1.03044)\\
A &= 1030.44
\end{align*}$$

Charlie will have \\(1030.44\\) at the end of the 3 years.
