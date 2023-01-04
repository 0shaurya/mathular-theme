---
title: Implicit Differentiation
layout: page
menuInclude: yes
menuLink: yes
menuTopTitle: Calculus I
menuSubs:
- title: Implicit Differentiation
  index: 9
excerpt: "Implicit Differentiation is a technique that combines algebra with differentiation, and is particularly useful in finding derivatives of implicit functions."
terms:
  - ['Explicit Function', 'A function written in terms of a single variable']
  - ['Implicit Function', 'A function not written in terms of a single variable. It contains more than one variable on either side.']
  - ['Implicit Differentiation', 'A differentiation technique that is used to differentaite implicit functions. It is done by taking the derivative of both sides of an implicit equation.']
questions:
  - ['Find \(\frac{dy}{dx}\) if \( \ln(y)=y+x \).', '\(\frac{d}{dx}[\ln(y)]=\frac{d}{dx}[y+x]\\\frac{1}{y}\frac{dy}{dx}=\frac{dy}{dx}+1\\\frac{dy}{dx}(1/y-1)=1\\\frac{dy}{dx}=\frac{1}{1/y-1}\\\frac{dy}{dx}=\frac{y}{1-y}\)']
---


<h1>Calculus I</h1>

<h2>Implicit Differentiation</h2><br>


So far, we have only learned how to take derivatives explicitly. Taking a derivative explicitly involves an <b>explicit function</b>. An explicit function is a function written in terms of a single variable, such as \\(y\\) or \\(f(x)\\). Some examples of explicit functions are

$$
y=3x\\
f(x)=\frac{4}{x}\\
p(x)=5x^2+3x+6\\
y=-7
$$

An <b>implicit function</b>, however, is a function that contains more than one variable on either side. Some examples of implicit functions include

$$
x^2y-y=5x\\
y=2y+x\\
xy=1
$$

Notice how in all of the above, neither side of the equals sign contains only \\(y\\). Sometimes, explicit functions can be written as explicit functions. For example,

$$\begin{align*}
yx^2&=3x+y~ \text{ An implicit function}\\
yx^2-y&=3x\\
y(x^2-1)&=3x\\
y&=\frac{3x}{x^2-1}~ \text{ An explicit function}
\end{align*}$$

Here, we started with the implicit function, and through algebra, ended up with an implicit function of \\(y\\) in terms of \\(x\\). However, other times, an implicit function can only be written implicitly. For example,

$$x+y+\sin(y)=0$$

cannot be written explicitly for \\(y\\) in terms of \\(x\\).

Now, let's talk about how this ties into calculus and derivatives. <b>Implicit differentiation</b> is a type of differentiation that applies to implicit functions. It involves heavy use of the chain rule and can be difficult to grasp at first. Let's look at how to differentiate the implicit function above.

To start, we need to look at how explicit differentiation (the differentiation you are used to) works. If we have an equation like

$$y=x^2$$

we know by explicit differentiation that $$\frac{d}{dx}y=2x$$. However, what's really going on here is algebra. Just like we can apply the square root operation on any equation as long as we do it on both sides, we can also apply the derivative operation on any equation as long as we do it on both sides. When we're differentiating \\(y=x^2\\), that's all we're doing.

$$\begin{align*}
y&=x^2 \\
\frac{d}{dx}y&=\frac{d}{dx}x^2
\end{align*}$$

\\(\frac{d}{dx}y = \frac{dy}{dx}\\) and \\(\frac{d}{dx}x^2 = 2x\\), so

$$
\begin{align*}
y&=x^2\\
\frac{d}{dx}y&=\frac{d}{dx}x^2\\
\frac{dy}{dx} &= 2x
\end{align*}
$$

Implicit differentiation is the exact same way. When we differentiate, we will apply the derivative operation on both sides. Let's look at how to differentiate the implicit function we looked at earlier, \\(x+y+\sin(y) = 0\\). To begin, we differentiate both sides:

$$\begin{align*}
\sin(y)+y+x&=0\\
\frac{d}{dx}\Big[x+y+\sin(y)\Big]&=\frac{d}{dx}\Big[0\Big]
\end{align*}$$

Differentiating the right side is easy, because the derivative of \\(0\\) is just \\(0\\). The left side is a bit trickier, so let's split this up term by term.

$$\begin{align*}
\sin(y)+y+x&=0\\
\frac{d}{dx}\Big[x+y+\sin(y)\Big]&=\frac{d}{dx}\Big[0\Big]\\
\frac{d}{dx}\Big[x\Big]+\frac{d}{dx}\Big[y\Big]+\frac{d}{dx}\Big[\sin(y)\Big]&=0\\
\end{align*}$$

Now, let's go through this term by term. \\(\frac{d}{dx} x = 1\\), so we have

$$1+\frac{d}{dx}\Big[y\Big]+\frac{d}{dx}\Big[\sin(y)\Big]=0$$

What's the derivative of \\(\frac{d}{dx} y\\)? You might be tempted to say \\(1\\), but we need to be more careful. When we are doing \\(\frac{d}{dx}\\), we are taking the derivative with respect to \\(x\\) (because \\(x\\) is in the denominator of the derivative symbol). Because of this, we cannot say \\(\frac{d}{dx}y=1\\) (although \\(\frac{d}{dy} y = 1\\). Instead, we just leave it as \\(\frac{d}{dx} y\\):

$$\begin{align*}
1+\frac{d}{dx}y+\frac{d}{dx}\Big[\sin(y)\Big]&=0\\
1+\frac{dy}{dx}+\frac{d}{dx}\Big[\sin(y)\Big]&=0\end{align*}$$

Now, we have to find the derivative of \\(\frac{d}{dx} \sin(y)\\). The key here is to recognize that \\(y\\) is a function. Thus, we have one function inside another function. This makes us have to use the chain rule. Recall that the chain rule says \\(\frac{d}{dx} f(g(x)) = f'(g(x))g'(x)\\). Here, our outside function is \\(\sin\\) and our inside function is \\(y\\). So,

$$\frac{d}{dx} \sin(y) = \sin'(y)\cdot y'$$

Because the derivative of \\(\sin\\) is \\(\cos\\) and \\(y' = \frac{d}{dx} y\\), we can turn this into

$$\frac{d}{dx} \sin(y) = \cos(y)\frac{d}{dx} y$$

We have found the derivative of \\(\sin(y)\\) with respect to \\(x\\). Let's plug this into our equation.

$$\begin{align*}
1+\frac{dy}{dx}+\frac{d}{dx}\Big[\sin(y)\Big]&=0\\
1+\frac{dy}{dx}+\Big(\cos(y)\frac{dy}{dx}\Big) &=0
\end{align*}$$

Remember that we're trying to find the derivative of \\(y\\), or \\(\frac{dy}{dx}\\). Because of this, we should try to get \\(\frac{dy}{dx}\\) by itself (think solving for a variable in algebra). We can treat \\(\frac{dy}{dx}\\) as any other mathematical expression. Let's get the \\(1\\) to the other side, and factor out the \\(\frac{dy}{dx}\\)s so we only have one of them:

$$\begin{align*}
1+\frac{dy}{dx}+\Big(\cos(y)\frac{dy}{dx}\Big) &=0\\
1+\frac{dy}{dx}+\cos(y)\frac{dy}{dx}&=0\\
\frac{dy}{dx}+\cos(y)\frac{dy}{dx}&=-1\\
\frac{dy}{dx}\Big(1+\cos(y)\Big) &=-1 ~ \text{ In this step, we are factoring out }\frac{dy}{dx}
\end{align*}$$

Now, we just have to divide both sides by \\(1+\cos(y)\\) and we have our final answer:

$$\begin{align*}
\frac{dy}{dx}\Big(1+\cos(y)\Big) &=-1\\
\frac{dy}{dx} &=\frac{-1}{1+\cos(y)}
\end{align*}$$

We have found the derivative of \\(x+y+\sin(y)=0\\) with respect to x to be \\(\frac{-1}{1+\cos(y)}\\). Notice that on the right side, we don't just have \\(x\\)s. This is fine. If you are asked to differentiate implicitly, then it is reasonable to expect the answer to also be in an implicit form.
