---
title: L'Hôpital's Rule
layout: page
menuInclude: yes
menuLink: yes
menuTopTitle: Calculus I
menuSubs:
- title: L'Hôpital's Rule
  index: 8
excerpt: "An excerpt is used as the page description and can be up to 160 characters long..."
terms:
  - ['L''Hôpital’s Rule', 'A very powerful technique for solving limits that are equal to \(\frac{0}{0}\) or \(\frac{\infty}{\infty}\). It says that \(\\ \text{If } \lim_{x\to a} \frac{f(x)}{g(x)} = \frac{0}{0} \text{ or } \frac{\infty}{\infty}, \\ \lim_{x\to a} \frac{f(x)}{g(x)} = \lim_{x\to a} \frac{f'(x)}{g'(x)}\)']
---


<h1>Calculus I</h1>

<h2>L'Hôpital's Rule</h2><br>


<b>L'Hôpital's rule </b> is an incredibly powerful rule that uses derivatives to solve limits with indeterminate forms. Despite being very simple, it will be invaluable in solving limits due to its effectiveness. L'Hôpital's rule says:

$$\text{If } \lim_{x\to a} \frac{f(x)}{g(x)} = \frac{0}{0} \text{ or } \frac{\infty}{\infty}, \\ \lim_{x\to a} \frac{f(x)}{g(x)} = \lim_{x\to a} \frac{f'(x)}{g'(x)}$$

Recall that both \\(\frac{0}{0}\\) and \\(\frac{\infty}{\infty}\\) are both indeterminate forms. Usually, if we have a limit that equals an indeterminate form, we would have to simplify the limit somehow using factorization or conjugate multiplication. However, now, if we a limit that is \\(\frac{0}{0}\\) or \\(\frac{\infty}{\infty}\\), we can simply take the derivative of the top and bottom and come to our answer that way. Let's look at a couple examples.

$$\lim_{x \to \infty} \frac{x^2}{x+2}$$

Using direct substitution, we get \\(\frac{\infty}{\infty}\\). Let's use L'Hôpital's rule. We should first identify the top function, the bottom function, and then separately find the derivatives of each. In this case, the top function is \\(x^2\\) and the bottom function is \\(x+2\\). The derivatives of each are, by the power rule, \\(2x\\) and \\(1\\), respectively. This means that, by L'Hôpital's rule ,

$$\lim_{x \to \infty} \frac{x^2}{x+2} \stackrel{\small \text{L'H}}{=}\lim_{x \to \infty} \frac{2x}{1}$$

We use the little “L'H” above the equals sign to signify we used L'Hôpital's rule for that step. Now, we can use direct substitution:

$$\frac{2x}{1} =\infty$$

This is our final answer. Let's look at another example:

$$\lim_{x \to \pi} \frac{\tan(x)}{x-\pi}$$

This equals \\(\frac{0}{0}\\), so let's use L'Hôpital's rule.

$$\lim_{x \to \pi} \frac{\tan(x)}{x-\pi} \stackrel{\small \text{L'H}}{=} \lim_{x \to \pi} \frac{\sec^2(x)}{1} = \sec^2(\pi)$$

Because \\(\sec(x) = \frac{1}{\cos(x)}\\) by definition, we can find the answer using the unit circle.

$$= \frac{1}{\cos^2(\pi)} = 1$$

Our final answer is \\(1\\).

There is no reason why we can't repeat this rule if necessary. For example,

$$\lim_{x \to \infty} \frac{x^3+2x}{x^4+3x^2+7x+1} \stackrel{\small \text{L'H}}{=} \lim_{x \to \infty} \frac{3x^2+2}{4x^3+6x+7} \stackrel{\small \text{L'H}}{=} \lim_{x \to \infty} \frac{6x}{12x^2+6} \stackrel{\small \text{L'H}}{=} \lim_{x \to \infty} \frac{6}{24x} = 0$$

Here, we applied L'Hôpital's rule three times in a row, because the first two times we got \\(\frac{\infty}{\infty}\\) again. It was only after the third time we got an answer we could use.

However, remember that there were 5 other indeterminate forms besides just \\(\frac{0}{0}\\) and \\(\frac{\infty}{\infty}\\). These were:

$$0\cdot\infty ,~ \infty -\infty ,~ 0^{0},~ 1^{\infty }, {\text{ and }} \infty ^{0}$$

L'Hôpital's rule doesn't apply to these forms. However, we can transform all of these to be in one of the forms L'Hôpital's rule does apply in, and then go from there. For example:

$$\lim_{x \to 0^+} x\ln(x)$$

This limit, after direct substitution, leads to \\(0 \cdot \infty\\), an indeterminate form. However, we can convert it to the following:

$$\lim_{x \to 0^+} x\ln(x) = \lim_{x \to 0^+} \frac{\ln(x)}{\frac{1}{x}}$$

Now, after direct substitution, we get \\(\frac{\infty}{\infty}\\). Thus, we can now use L'Hôpital's rule on this limit.

$$\lim_{x \to 0^+} x\ln(x) = \lim_{x \to 0^+} \frac{\ln(x)}{\frac{1}{x}} \stackrel{\small \text{L'H}}= \lim_{x \to 0^+} \frac{\frac{d}{dx}\ln(x)}{\frac{d}{dx}\frac{1}{x}} = \lim_{x \to 0^+} \frac{\frac{1}{x}}{-\frac{1}{x^2}} = \lim_{x \to 0^+}[-x] = 0$$

Our answer is 0. Here, we converted a limit in the form \\(0 \cdot 0\\) to \\(\frac{\infty}{\infty}\\) by the fact that \\(f(x) \cdot g(x) = \frac{f(x)}{\frac{1}{g(x)}}\\).

Let's also go over how to deal with exponentials in a limit. L'Hôpital's rule does not play nice with exponentials, but we can change that using a logarithm. Take the following example:

$$\lim_{x \to \infty} x^{\frac{1}{x}}$$

This is an indeterminate form, and we cannot use L'Hôpital's rule. However, let's assign this limit to a variable, \\(y\\), and then take the natural log of both sides:

$$\begin{align*}
\lim_{x \to \infty} x^{\frac{1}{x}} &= y\\
\ln(\lim_{x \to \infty} x^{\frac{1}{x}}) &= \ln(y)
\end{align*}$$

Because \\(\ln(x)\\) is continuous around \\(\infty\\), we can put the natural log inside the limit:

$$\begin{align*}
\ln(\lim_{x \to \infty} x^{\frac{1}{x}}) &= \ln(y)\\
\lim_{x \to \infty} \ln(x^{\frac{1}{x}}) &= \ln(y)\\
\end{align*}$$

Because of limit properties,

$$\begin{align*}
\lim_{x \to \infty} \ln(x^{\frac{1}{x}}) &= \ln(y)\\
\lim_{x \to \infty} \frac{1}{x}\ln(x) &= \ln(y)\\
\lim_{x \to \infty} \frac{\ln(x)}{x} &= \ln(y)
\end{align*}$$

Now, we can use L'Hôpital's rule because as \\(x\\) approaches infinity, both \\(\ln(x)\\) and \\(x\\) approach infinity.

$$
\ln(y)=\lim_{x \to \infty} \frac{\ln(x)}{x} \stackrel{\small\text{L'H}}{=} \lim_{x \to \infty} \frac{\frac{d}{dx}\ln(x)}{\frac{d}{dx}x} = \lim_{x \to \infty} \frac{\frac{1}{x}}{1} = 0
$$

Now, we know that \\(\ln(y) = 0\\). However, remember that \\(y\\) is the actual value of the limit, so we should now solve for \\(y\\).

$$
\begin{align*}
\ln(y) &= 0\\
e^{\ln(y)} &= e^0\\
y&=1
\end{align*}
$$

We have our answer now. \\(y = \lim_{x \to \infty} x^{\frac{1}{x}} = 1\\). The important bit here was the natural log. Whenever you have the limit of an exponential, consider taking the natural log to bring the exponent down to try to use L'Hôpital's rule. Just remember that you should only try this method if the limit is approaching a value greater than 0, because \\(\ln(x)\\) is not continuous otherwise.
