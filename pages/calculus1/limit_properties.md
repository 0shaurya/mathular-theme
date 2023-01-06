---
title: Limit Properties
layout: page
menuInclude: yes
menuLink: yes
menuTopTitle: Calculus I
menuSubs:
- title: Limit Properties
  index: 2
excerpt: "There are numerous properties for limits that make them useful and easier to calculate. Learn them here."
terms:
  - ['Direct Substitution', 'A method for solving limits that involves plugging in the limiting value for the variable and solving. This method always works, except in certain specific scenarios.']
questions:
  - ['What is \(\displaystyle \lim_{x\to3} 5x^2\cdot \frac{\sqrt{x}}{\pi x}\)?', '\(5(3)^2 \cdot \frac{\sqrt 3}{3\pi} = \frac{45 \sqrt 3}{3 \pi}\)']
  - ['What is \(\displaystyle \lim_{x\to 0^+}\frac{-3}{2x}\)?', 'By the constant multiple rule, we can pull out the \(\frac{-3}{2}\): \(\displaystyle \frac{-3}{2} \lim_{x\to 0^+}\frac{1}{x} = -\infty\).']
  - ['What is \(\displaystyle \lim_{x\to \infty}\left(\frac{3}{x}\right)^2\)?', '\(\displaystyle \lim_{x\to \infty} \frac{9}{x^2} = 0\).']
---


<h1>Calculus I</h1>

<h2>Limits Properties</h2><br>


In the last chapter, we went over limits, what they are, and how to evaluate them using a graph. Now, let's go over how to solve them algebraically. There are a lot of certain properties to know that are useful in many situations.

Here is a list of all the important limit properties. In the following examples, \\(f(x)\\) and \\(g(x)\\) will be any function and \\(a\\) and \\(c\\) will be any number. Assume that \\(\lim_{x \to a} f(x)\\) exists (so no jump discontinuities).

|Definition|Example|
|:-: |:-: |
|\\(\displaystyle \lim\limits_{x \to a} [c \cdot f(x)] = c\cdot \lim\limits_{x \to a} f(x)\\) <br> \\(\text{only works for constants or variables}\\) <br> \\(\text{that are not dependent on the limit}\\)|\\(\lim\limits_{x \to 1} 5(x^2+2) = 5\lim\limits_{x \to 1} [x^2+2] = 15\\)|
|\\(\lim\limits_{x \to a} [f(x) \pm g(x)] = \lim\limits_{x \to a} f(x) \pm \lim\limits_{x \to a} g(x)\\)|\\(\lim\limits_{x \to 7} [x^2+x] = \lim\limits_{x \to 7} x^2 + \lim\limits_{x \to 7} x = 56\\)|
|\\(\lim\limits_{x \to a} [f(x) \cdot g(x)] = \lim\limits_{x \to a} f(x) \cdot \lim\limits_{x \to a} g(x)\\)|\\(\lim\limits_{x \to 4} [x(2-x)] = \lim\limits_{x \to 4} x \cdot \lim\limits_{x \to 4} [2-x] = -8\\)|
|\\(\displaystyle \lim\limits_{x \to a} \bigg[\frac{f(x)}{g(x)}\bigg] = \frac{\lim\limits_{x \to a} f(x)}{\lim\limits_{x \to a} g(x)}\\) \\(\text{assuming } g(x) \ne 0\\)|\\(\displaystyle \lim\limits_{x \to 1} \frac{x^2+5x}{3x^2-5} = \frac{\lim\limits_{x \to 1} [x^2+5x]}{\lim\limits_{x \to 1} [3x^2-5]}= -3\\)|
|\\(\lim\limits_{x \to a} \big[(f(x))^c\big] = \Big[\lim\limits_{x \to a} f(x)\Big]^c\\)|\\(\lim\limits_{x \to 2} [(3x)^2] = \Big[\lim\limits_{x \to 2} 3x \Big]^2 = 36\\)|
|\\(\lim\limits_{x \to a} \sqrt[\large c]{f(x)} = \sqrt[\large c]{\lim\limits_{x \to a} f(x)}\\)|\\(\lim\limits_{x \to 7} \sqrt{x+2} = \sqrt{\lim\limits_{x \to 7} [x+2]} = 3 \\)|
|\\(\displaystyle \lim_{x \to a}f(x) = f\Big(\lim_{x \to a}x\Big)\\) <br> \\(\text{as long as } f(x)\text{ is continuous around } a\\)|\\(\lim_{x \to 25}\sqrt{x} = \sqrt{\lim_{x \to 25}x} = 5\\)|


All of these properties work because of the fact that \\(\lim_{x \to a} f(x)\\) exists as just a number. This allows us to treat the limit as any other number and apply corresponding rules.

There are also some limits that are important to know because they come up very often. These include:

$$\lim_{x \to 0^- } \frac{c}{x} = -\infty$$

$$\lim_{x \to 0^+ } \frac{c}{x} = \infty$$

$$\lim_{x \to 0 } \frac{x}{c} = 0$$

$$\lim_{x \to \infty} \frac{c}{x} = 0$$

$$\lim_{x \to \infty} \frac{x}{c} = \infty$$

where \\(c>0\\). Use the constant multiple rule to figure out what happens if \\(c\\) is negative. All of these limits can be found either by looking at a graph, or by thinking about what happens to the expression as \\(x\\) approaches \\(0\\) or \\(\infty\\).

Whenever evaluating a limit of a continuous function algebraically, the first step should always be to plug in the number. This method is known as <b>direct substitution</b>. Most of the time, this will be enough to get you the right answer. In the next section, we'll go over when direct substitution won't work.
