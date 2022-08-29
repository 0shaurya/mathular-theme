---
layout: page
menuInclude: yes
menuLink: yes
menuTopTitle: Calculus I
menuSubs:
- title: Indeterminate Forms
  index: 3
excerpt: "An excerpt is used as the page description and can be up to 160 characters long..."
---


<h1>Calculus I</h1>

<h2>Indeterminate Forms</h2><br>


In the last section, we went over the basics of solving limits of continuous functions algebraically. The first step to solving any continuous limit algebraically should always be to just plug the number in. Unfortunately, not all limits can be solved by that method. Consider the following expressions:

$$\frac {0}{0},~ {\frac {\infty }{\infty }},~0\cdot\infty ,~\infty -\infty ,~0^{0},~1^{\infty },{\text{ and }}\infty ^{0}$$

These are known as the seven <b>indeterminate forms</b>. If a limit is equal to one of the above, then more work is required to find the answer. This does not mean that the limit is undefined - it simply means that no conclusion can be drawn. Thus, simply plugging in \\(a\\) for \\(x\\) is sometimes not enough to solve a limit.

Why are these forms indeterminate? For each of the indeterminate forms, It is possible to find a set of limits that simplify down to the form yet do not equal each other. For example, for the indeterminate form \\(0 \cdot \infty\\):

$$\begin{align*}
\lim_{x \to 1} \Big[(1-x)\cdot \frac{x}{1-x}\Big] &= \lim_{x \to 1}[1-x]\cdot \lim_{x \to 1}\Big[\frac{x}{1-x}\Big] = 0\cdot \infty \\
&=\lim_{x \to 1}[\cancel{(1-x)}\frac{x}{\cancel{1-x}}] = 1
\end{align*}\\
\text{Thus } 0\cdot\infty = 1
$$

$$\begin{align*}
\lim_{x \to 1} \Big[(1-x)\cdot \frac{x+2}{1-x}\Big] &= \lim_{x \to 1}[1-x]\cdot \lim_{x \to 1}\Big[\frac{x+2}{1-x}\Big] = 0\cdot \infty \\
&=\lim_{x \to 1}[\cancel{(1-x)}\frac{x+2}{\cancel{1-x}}] = 3
\end{align*}\\
\text{Thus } 0\cdot\infty = 3$$

It seems like we have found one way to prove that \\(0\cdot\infty=1\\) and another way to prove that \\(0\cdot\infty=3\\). It obviously can't be equal to both, so which one is it? The error here is asserting that \\(0\cdot\infty\\) equals anything in the first place. In reality, the value of \\(0\cdot\infty\\) depends on the context it is being used in. Because it is not equal to one value, it is indeterminate. No conclusion can be drawn; try to use another method to find the answer instead. There are a couple of other methods to try, and which to use depends on the problem.

The first alternative method is by factoring. For example, take look at the following limit:

$$\lim_{x \to 7} \frac{3x-21}{x^2-49}$$

Plugging in \\(7\\) for \\(x\\), we get the indeterminate form \\(\frac{0}{0}\\). However if we factor:

$$\lim_{x \to 7} \frac{3x-21}{x^2-49} = \lim_{x \to 7}\frac{3(x-7)}{(x+7)(x-7)} = \lim_{x \to 7} \frac{3}{x+7} = \frac{3}{14}$$

we can see that the answer is \\(\frac{3}{14}\\).

Another alternative method is to multiply by the conjugate. This is especially useful when dealing with square roots. For example:

$$\lim_{x \to 25} \frac{x-25}{\sqrt{x}-5}$$

If we plug in \\(25\\) for \\(x\\), we will get \\(\frac{0}{0}\\). If we multiply the top and bottom by the conjugate \\(\sqrt{x}-5\\):

$$
\lim_{x \to 25} \frac{x-25}{\sqrt{x}-5} =
\lim_{x \to 25}\frac{(x-25)(\sqrt{x}+5)}{(\sqrt{x}-5)(\sqrt{x}+5)} =
\lim_{x \to 25} \frac{(x-25)(\sqrt{x}+5)}{x-25} = \lim_{x\to25}[\sqrt{x}+5] = 10$$

Always multiply by the conjugate of the numerator if the numerator contains the radical, and multiply by the conjugate of the denominator if the denominator contains the radical. Here is another, more complicated example:

$$\lim_{x \to 2} \frac{\sqrt2-\sqrt{3x-4}}{6-3x}$$

Since direct substitution leads to \\(\frac{0}{0}\\), let's multiply by the conjugate of the numerator:

$$=\lim_{x \to 2} \frac{(\sqrt2-\sqrt{3x-4})(\sqrt2+\sqrt{3x-4})}{(6-3x)(\sqrt2+\sqrt{3x-4})}$$

We can distribute the numerator and then cancel some terms:

$$
\begin{align*}
&= \lim_{x \to 2} \frac{2-(3x-4)}{(6-3x)(\sqrt2+\sqrt{3x-4})} \\
&= \lim_{x \to 2} \frac{1}{\sqrt2+\sqrt{3x-4}}
\end{align*}$$

Now, we can use direct substitution:

$$= \frac{1}{2\sqrt2}$$

We can also just try our best to simplify without factoring or conjugate multiplication. For example,

$$\lim_{x \to \pi} \frac{\tan(x)}{\sin(x)} = \frac{0}{0}$$

which is an indeterminate form. However, recall that \\(\tan(x) = \frac{\sin(x)}{\cos(x)}\\):

$$\lim_{x \to \pi} \frac{\tan(x)}{\sin(x)} = \lim_{x \to \pi} \frac{\frac{\sin(x)}{\cos(x)}}{\sin(x)} = \lim_{x \to \pi} \frac{1}{\cos(x)} = -1$$
