---
layout: page
menuInclude: yes
menuLink: yes
menuTopTitle: Precalculus
menuSubs:
- title: Sequences, Summations, and Series
  index: 6
excerpt: "An excerpt is used as the page description and can be up to 160 characters long..."
---


<h1>Precalculus</h1>

<h2>Sequences, Summations, and Series</h2><br>

A <b>sequence</b> is a set of numbers that is ordered. An example of a sequence is

$$3, 5, 7, 9, 11, 13$$

We can assign a symbol to the above sequence, as well as a symbol for each number inside it. For example, we can let \\(a = 3, 5, 7, 9, 11, 13\\). Then, we can say that

$$a = 3, 5, 7, 9, 11, 13\\a_1=3\\a_2=5\\a_3=7\\\text{etc.}$$

Let's try to find a formula for finding \\(a_n\\), the \\(n\\)th term in the sequence. We know that the sequence starts at 3, and increases by 2 each time. This means that we can describe the sequence like this:

$$a_n = 2 + 3(n-1)$$

This kind of sequence is known as an <b>arithmetic sequence</b>. Arithmetic sequences have a starting value and add by the same amount each time. The general formula of an arithmetic sequence is

$$a_n = a_1+(n-1)d$$

where \\(a_n\\) is the \\(n\\)th term in the sequence, \\(a_1\\) is the first term, and \\(d\\) is the amount the number increases by. The \\(d\\) stands for difference.

Another type of sequence is a <b>geometric sequence</b>. A geometric sequence is similar to an arithmetic sequence, but instead of adding a certain amount each iteration, it multiplies by a number instead. An example of a geometric sequence is

$$b = 4, 6, 9, 13.5, 20.25$$

This is a geometric sequence that starts at \\(4\\) and has a <b>common ratio</b> of \\(1.5\\). The common ratio is the amount multiplied by each iteration. We can describe this sequence as the following:

$$b_n = 4(1.5)^{n-1}$$

The general formula for a geometric sequence is

$$b_n = b_1(r)^{n-1}$$

where \\(b_n\\) is the \\(n\\)th term in the sequence, \\(b_1\\) is the first term, and \\(r\\) is the common ratio.

Let's talk about <b>summations</b>. A summation is a bunch of numbers added together. For example,

$$0+2+4+6+8$$

is a summation. We can use a special type of notation to describe that sequence. This notation is known as <b>summation notation</b>. Here is an example of sum notation:

$$\sum_{i=0}^{4}{2i}$$

There are four main parts to the summation notation. First is the summation sign, \\(\sum\\). This symbol is known as capital sigma and is a greek letter. Second, the \\(i=0\\) creates what is known as the <b>index variable</b>. Here, the index variable is \\(i\\) and starts at 0. \\(i\\) is substituted into the expression on the right, \\(2i+3\\). Then, the index variable counts up by 1 and gets plugged into the same expression. This repeats until \\(i\\) reaches the top number, or 5 in this case. Each term is added together. This means that

$$
\begin{align*}
\sum_{i=0}^{4}{2i} &= ((2(0))+(2(1))+(2(2))+(2(3))+(2(4)))) \\
&=0+2+4+6+8 \\
&=20
\end{align*}
$$

Summation notation is useful for condensing long summations. We can also use summation notation to describe summing up sequences. For example, in the sequence \\(d\\), we can add up all the terms in the \\(d\\) by using the following notation:

$$\sum{n}{}{d_n}$$

Despite n not being assigned an initial value nor a number above the symbol, this notation can still be used to describe the summation of a sequence.

A <b>series</b> is a summation, but has infinite terms. We will go over one type of series, the <b>geometric series</b>. A geometric series is a series whose terms have a common ratio between them. An example of a geometric series is

$$S = 4+8+16+32+64+\cdots$$

Here, the common ratio is 2 and the starting value is 4. We can write this series in summation notation:

$$S = 4+8+16+32+64+\cdots = \sum_{n=0}^{\infty}{4(2)^n}$$

\\(4+8+16+32+64+\cdots\\) equals \\(\infty\\). If a series equals \\(\infty\\) or \\(-\infty\\), we say the series <b>diverges</b>.

The opposite of a diverging series is a <b>converging</b> series. An example of a converging geometric series is

$$3+1+\frac{1}{3}+\frac{1}{9}+\frac{1}{27}+\frac{1}{81}+\cdots = \sum_{n=0}^{\infty}{3 \left(\frac{1}{3} \right)^n}$$

This series converges to a specific number. To find this number, we can use the following formula

$$\frac{a}{1-r}$$

where \\(a\\) is the starting value and \\(r\\) is the common ratio. Note that this formula only works for values of \\(r < \vert 1 \vert \\), because for any value of \\(r\\) greater than or equal to 1 any geometric series will diverge.
