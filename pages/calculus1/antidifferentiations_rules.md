---
title: Antidifferentiation Rules and Methods
layout: page
menuInclude: yes
menuLink: yes
menuTopTitle: Calculus I
menuSubs:
- title: Antidifferentiation Rules and Methods
  index: 11
excerpt: "An excerpt is used as the page description and can be up to 160 characters long..."
---


<h1>Calculus I</h1>

<h2>Antidifferentiation Rules and Methods</h2><br>


When we learned about differentiation, we went over the rules that we could use. Now, let's go over a few rules for antidifferentiation.

The first two are fairly simple and should remind you of their differentiation counterparts. First, the <b>sum rule</b> says

$$\int f(x)\pm g(x)\,dx=\int f(x)\,dx\pm\int g(x)\,dx$$

This is analogous to the sum rule for derivatives. The second rule is the <b>constant multiple rule</b>, which says

$$\int cf(x)\,dx = c\int f(x)\,dx$$

where \\(c\\) is any number. Similar to both limits and derivatives, we can simply pull out constants that are being multiplied.

The third and final rule is the <b>reverse power rule</b>. As the name implies, this rule will reverse the power rule that we used for differentiation. The reverse power rule says

$$\int x^n \,dx = \frac{1}{n+1}x^{n+1}$$

This rule works because if we differentiate the above, we get

$$\begin{align*}
\int x^n \,dx &= \frac{1}{n+1}x^{n+1}\\
\frac{d}{dx}\left[\int x^n \,dx\right]&=\frac{d}{dx}\left[\frac{1}{n+1}x^{n+1}\right]
\end{align*}$$

Because the derivative is the inverse of the antiderivative, they cancel out on the left side to leave only \\(x^n\\). On the right side, we can pull out the \\(\frac{1}{n+1}\\) because we are differentiating with respect to \\(x\\), not \\(n\\):

$$
x^n=\frac{1}{n+1}\frac{d}{dx}\left[x^{n+1}\right]
$$

Now, we can just use the power rule to differentiate \\(x^{n+1}\\):

$$\begin{align*}
x^n&=\frac{1}{n+1}\left[(n+1)x^n\right]\\
x^n&=\frac{1}{\cancel{n+1}}(\cancel{n+1})x^n\\
x^n&=x^n
\end{align*}$$

We have proven the reverse power rule. Let's try an example. What's the antiderivative of \\(3x^7\\)? By the constant multiple rule and reverse power rule,

$$\begin{align*}
\int3x^7\,dx&=3\int x^7\,dx\\
&=3\frac{1}{7+1}x^{7+1}\\
&=\frac{3}{8}x^8
\end{align*}$$

This checks out, because if we differentiate \\(\frac{3}{8}x^8\\), we will get \\(3x^7\\). It is always a good idea to check your answer afterwards by differentiating.

Unfortunately, those three rules are about the extent for antidifferentiation. Unlike differentiation, where you can just blindly follow a set of rules to find the answer, this is not really possible with antidifferentiation. However, there are many techniques of manipulating the expression to get it into a form we can work with. We will go over one of those methods.

Let's see if we can find \\(\int x\cos(x^2)\,dx\\). Here, we have multiple functions together. We know the antiderivatives of \\(x\\), \\(\cos(x)\\), and \\(x^2\\), but when we combine them together, it becomes a lot harder. To solve this, we can use <b>antidifferentiation by substitution</b>. Let's create a new variable \\(u\\), letting \\(u=x^2\\). Now, we have

$$\int x\cos(x^2)\,dx=\int x\cos(u)\,dx$$

We need to be careful. A requirement for antidifferentiating is that all the variables need to be the same. Right now, we have things in terms of \\(x\\) and \\(u\\). To try to convert everything into terms of \\(u\\), let's start by finding a way to convert the \\(dx\\) into a \\(du\\). Notice that

$$\frac{du}{dx}=\frac{d}{dx}u=\frac{d}{dx}\left[x^2\right]=2x$$

Therefore,

$$\begin{align*}
\frac{du}{dx}&=2x\\
du&=2xdx\\
\frac{du}{2x}&=dx
\end{align*}$$

Now that we have an expression for \\(dx\\) in terms of \\(u\\), we can substitute that back into the antiderivative.

$$\begin{align*}
\int x\cos(x^2)\,dx&=\int x\cos(u)\,dx\\
&=\int x\cos(u)\,\frac{du}{2x}\\
&=\int \frac{x\cos(u)}{2x}du
\end{align*}$$

Conveniently, the \\(x\\)'s on the top and bottom cancel out, leaving us with

$$\int \frac{\cos(u)}{2}du$$

Now that we have everything in terms of one variable, we can finally continue with the antidifferentiation process! By the constant multiple rule,

$$\frac{1}{2} \int \cos(u)du$$

Because we know that the antiderivative \\(\cos(u)\\) is \\(\sin(u)\\) (because the derivative of \\(\sin(u)\\) is \\(\cos(u)\\), we can write:

$$\int x\cos(x^2)\,dx = \frac{1}{2} sin(u)$$

We aren't quite done yet. Because our question was given to us in terms of \\(x\\), we have to leave the answer in terms of \\(x\\). Recall that we set \\(u = x^2\\). Let's substitute that in and add the constant of integration to find our final answer:

$$\frac{1}{2} \sin(x^2) + c$$

The antiderivative of \\(x\cos(x^2)\\) is \\(\frac{1}{2} \sin(x^2) + c\\). If we differentiate our answer, we get \\(x \cos(x^2)\\) back, showing us that we got the correct answer. The whole point of antidifferentiation by substitution is to turn a complicated expression into a simpler one, but it is important to change the \\(dx\\) at the end to match the variable we are using.

In general, there are certain substitutions that are good to make:
1. Let \\(u\\) equal an expression whose derivative is in another part of the function you are integrating.
2. Let \\(u\\) equal the denominator of a fraction.
3. Let \\(u\\) equal inside a radical.
4. Let \\(u\\) equal the inside of a composite of functions.

Note that antidifferentiation by substitution isn't guaranteed to work - it is just a method that simplifies the expression, making the process of antidifferentiation easier.
