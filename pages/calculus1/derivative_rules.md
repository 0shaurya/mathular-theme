---
title: Derivative Rules
layout: page
menuInclude: yes
menuLink: yes
menuTopTitle: Calculus I
menuSubs:
- title: Derivative Rules
  index: 6
excerpt: "Derivatives might be hard at first, but these rules turn calculating them into a step-by-step process."
terms:
  - ['Differentiation', 'the process of taking the derivative of a function']
  - ['Constant Term Rule', 'Rule that says the derivative of any constant is \(0\)']
  - ['Constant Multiple Rule', '\(\frac{d}{dx}[af(x)]=a\frac{d}{dx}[f(x)]\)']
  - ['Sum Rule', '\(\frac{d}{dx}[f(x)\pm g(x)] = \frac{d}{dx}f(x)\pm \frac{d}{dx}\)']
  - ['Product Rule', '\(\frac{d}{dx}[f(x)\cdot(g(x)]= f(x)g'(x)+g(x)f'(x)\)']
  - ['Quotient Rule', '\(\frac{d}{dx}\bigg[\frac{f(x)}{g(x)}\bigg] = \frac{g(x)f'(x)-f(x)g'(x)}{g(x)^2}\)']
  - ['Power Rule', '\(\frac{d}{dx} x^a = ax^{a-1}\)']
  - ['Chain Rule', '\(\frac{d}{dx} f(g(x)) = f'(g(x) \cdot g'(x)\)']
---


<h1>Calculus I</h1>

<h2>Derivative Rules</h2><br>


In the last chapter, we learned what a derivative was and how to calculate one using the definition of the derivative. However, using the definition of the derivative to calculate derivatives is incredibly hard, even with functions that aren't that complicated. This is because the definition of the derivative involves many terms, a fraction, and a limit. To make <b>differentiating</b> (to differentiate means to take the derivative of) functions easier, mathematicians use several rules.

  

The first rule we will learn is the <b>constant term rule</b>. This says that the derivative of a constant is 0. Remember that a constant is just a number (i.e., no \\(x\\) inside the function). Or, written mathematically,

  

$$\frac{d}{dx} [c] = 0 \text{ where } c \text{ is a constant}$$

  

The reason this works is because the derivative of a function measures the change in that function over values of \\(x\\). If we graph a function that's just a constant, we will see it is just a straight horizontal line. For example, look at this graph of \\(y=2\\):

  

(graph) y=2

  

No matter the change in \\(x\\), the change in \\(y\\) is <i>always</i> 0. Because of that, the derivative of \\(y=2\\) is just \\(0\\), as is the case for every other constant.

  

The second rule we will learn is the <b>constant multiple rule</b>. The constant multiple rule says that the derivative of a constant multiplied by a function is equal to the constant multiplied by the derivative of that function. Or, written mathematically,

  

$$\frac{d}{dx} [af(x)] = a\frac{d}{dx} [f(x)]$$

  

where \\(a\\) is any number. To prove this, let's use the definition of the derivative.

  

$$
\begin{align*}
\frac{d}{dx}[cf(x))] &= \lim_{h \to 0} \frac{cf(x+h)-cf(x)}{h}\\
&=\lim_{h \to 0} \frac{c(f(x+h)-f(x))}{h} \\
\end{align*}
$$

  

Because the limit is not dependent on \\(a\\) (it is only dependent on \\(h\\)), we can pull the \\(a\\) out using the constant multiple rule for limits that we learned the last chapter:

  

$$
=c\cdot\lim_{h \to 0} \frac{f(x+h)-f(x)}{h} \\
=c\cdot f'(x)
$$

  

Let's look at an example for this. In the last chapter, we used the definition of the derivative to say that \\(\frac{d}{dx} ???? = ?????\\). Now, using that knowledge, what is the derivative of \\(???????\\)?. Well, because \\(??????\\) is just a constant, we know that \\(\frac{d}{dx}[??????] = ??????\\).

  

The third rule we will learn is the <b>sum rule</b>. The sum rule simply says that the derivative of a sum is equal to the sum of the derivatives. Or, written mathematically,

  

$$\frac{d}{dx}[f(x)\pm g(x)] = \frac{d}{dx}f(x)\pm \frac{d}{dx}$$



For example, let's say we want to find the derivative of \\(??????\\). Because we know that the derivative of \\(????????\\) is \\(???????\\) and the derivative of \\(???????\\) is \\(???????\\), we can say that

  

$$\frac{d}{dx} ?????????????????$$

  

Note that because subtraction is simply addition with a negative sign, the rule holds true for differences as well. \\(\frac{d}{dx} [f(x)-g(x)] = \frac{d}{dx}f(x)-\frac{d}{dx}\\).

  

The fourth rule is the <b>product rule</b>. The product rule says the derivative of a product is equal to the first factor times the second factor's derivative, added to the second factor times the first factor's derivative. Or, written mathematically,

  

$$
\frac{d}{dx}[f(x)\cdot(g(x)] = f(x) \frac{d g(x)}{dx} + g(x) \frac{d f(x)}{dx} \\
\text{or written more compactly:}\\
\frac{d}{dx}[f(x)\cdot g(x)]= f(x)g'(x)+g(x)f'(x)
$$

  

The proof of this is quite complicated, but we can still prove it using the definition of the derivative:

  

$$
?????
$$

  

As an example, ??????????

  

The fifth rule is the <b>quotient rule</b>, which is similar to the product rule but for quotients instead of products. The quotient rule is:

  

$$\frac{d}{dx}\bigg[\frac{f(x)}{g(x)}\bigg] = \frac{g(x)f'(x)-f(x)g'(x)}{g(x)^2}$$


We will prove the quotient rule with the definition of the derivative:


$$????????$$


As an example, ????????

The sixth rule we will learn is the <b>power rule</b>. The power rule is for functions with the form \\(x^a\\), where \\(a\\) is a number. The power rule says

$$\frac{d}{dx} x^a = ax^{a-1}$$

For example, \\(\frac{d}{dx} x^2 = 2x\\) and \\(\frac{d}{dx} x^3 = 3x^2\\). \\(\frac{d}{dx} x^{32}6 = 326x^{325}\\).

Despite this rule being pretty simple, the proof is fairly complicated. Because exponents are just repeated multiplication, we can use the product rule to prove this:

$$
\begin{align*}
\frac{d}{dx}x^a =\frac{d}{dx}[x^{a-1}x] &= x\frac{d}{dx}[x^{a-1}]+x^{a-1}\underbrace{\frac{d}{dx}[x]}_ {=1}\\
&=x\frac{d}{dx}[x^{a-1}]+x^{a-1}\\
\end{align*}
$$
 
But what is \\(\frac{d}{dx}[x^{a-1}]\\)?
 
$$\begin{align*}
\frac{d}{dx}x^{a-1} =\frac{d}{dx}[x^{a-2}x] &= x\frac{d}{dx}[x^{a-2}]+x^{a-2}\underbrace{\frac{d}{dx}[x]}_ {=1}\\
&= x\frac{d}{dx}[x^{a-2}]+x^{a-2}\\
\end{align*}
$$

Recall that
 
$$\begin{align*}
\frac{d}{dx}x^a =\frac{d}{dx}[x^{a-1}x] &=x\frac{d}{dx}[x^{a-1}]+x^{a-1}\\
\end{align*}
$$

Now that we know what \\(\frac{d}{dx}[x^{a-1}]\\), let's plug that in:

$$\begin{align*}
\frac{d}{dx}x^a =\frac{d}{dx}[x^{a-1}x] &=x\frac{d}{dx}[x^{a-1}]+x^{a-1}\\
&=x[x\frac{d}{dx}[x^{a-2}]+x^{a-2}]+x^{a-1}\\
&=x^2\frac{d}{dx}[x^{a-2}]+x^{a-1}+x^{a-1}\\
&=x^2\frac{d}{dx}[x^{a-2}]+2x^{a-1}\\
\end{align*}$$

Now, we can find what \\(\frac{d}{dx}[x^{a-2}]\\) is using the same method and plug that in the above equation. Let's skip all the steps. We get
 
$$\frac{d}{dx}x^a=x^3\frac{d}{dx} [x^a-3] +3x^{a-1}$$
 
By now, you can see the pattern of repeatedly finding \\(\frac{d}{dx} x^{a-1}\\), then \\(\frac{d}{dx} x^{a-2}\\), then \\(\frac{d}{dx} x^{a-3}\\), and so on. After \\(n\\) iterations in the process, we have
 
$$\frac{d}{dx}x^a = x^n \frac{d}{dx} [x^{a-n}]+nx^{a-1}$$
 
Now, imagine doing this process for \\(a\\) iterations. After \\(a\\) iterations, we have

$$\frac{d}{dx}x^a = x^a \frac{d}{dx} [x^{a-a}]+ax^{a-1}$$

which can be simplified to
 
$$\frac{d}{dx}x^a = x^a \frac{d}{dx} [x^{0}]+ax^{a-1}$$

because anything to the power of 0 is 1, the constant term rule we learned earlier says that
 
$$
\begin{align*}
\frac{d}{dx}x^a &= x^a(0)+ax^{a-1}\\
\ &= ax^{a-1}\end{align*}$$

We have proven the power rule. Note that this proof only works for positive integers (due to the nature of doing things iteratively), but the rule works for all numbers. In a later chapter, we will learn the proof for the power rule that extends to every number.

The seventh rule we will learn is the <b>chain rule</b>. The chain rule is the hardest rule, but will be the most useful. The chain rule involves composites of functions. A function composite is one function inside of another.

$$f(g(x))$$

is a composite function, with \\(f\\) being the outside function and \\(g\\) being the inside function. The chain rule says
 
$$\frac{d}{dx} f(g(x)) = f'(g(x))\cdot g'(x)$$

This looks complicated, and it definitely is. The process for using chain rule is:
 
1. Take the derivative of the outside function
2. Substitute every \\(x\\) in the outside function's derivative for the inside function
3. Multiply all of that by the derivative of the inside function

For example, what is

$$\frac{d}{dx} (x^2+x)^3$$

Let's identify the outside and inside functions first. When going outside in, the very first thing we see is \\(\text{something}^3\\). Because that's the first thing we see, the outside function is \\(x^3\\). The inside function is \\(x^2+x\\), because that is what the outside function is being applied on. Now that we know the outside and inside functions, let's follow the step-by-step process:

1. Take the derivative of the outside function

The derivative of \\(x^3\\) is \\(3x^2\\) by the power rule.

2. Substitute every \\(x\\) in the outside function's derivative for the inside function

We now have \\(3(x^2+x)^2\\)

3. Multiply all of that by the derivative of the inside function

The derivative of \\(x^2+x\\) is \\(2x+1\\) by the power rule and sum rule. So, our final answer is \\(3(x^2+x)^2(2x+1)\\)

Thus, by the chain rule,

$$\frac{d}{dx} (x^2+x)^3 = 3(x^2+x)^2(2x+1)$$

Also, notice that to find that answer we not only used the chain rule, but the power rule and sum rule as well. Very rarely will you use only one rule to solve a problem.
