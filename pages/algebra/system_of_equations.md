---
title: Systems of Equations
layout: page
menuInclude: yes
menuLink: yes
menuTopTitle: Algebra
menuSubs:
- title: Systems of Equations
  index: 8
excerpt: "An excerpt is used as the page description and can be up to 160 characters long..."
terms:
  - ['System of Equations', 'A group of multiple equations with at least 2 variables in total']
  - ['Substitution', 'A method of solving systems of equations where we solve for one variable in terms of the other, and then substitute that into the other equation']
questions:
  - ['What is the solution to the following system of equations?', '']
---


<h1>Algebra</h1>

<h2>Systems of Equations</h2><br>

A <b>system of equations</b> is a group of multiple equations with at least 2 variables in total. Usually, it is mostly impossible to solve for multiple variables if you are only given one equation - however, with multiple equations, we can solve for multiple variables.

Take a look at the following system of equations:

$$\text{This is a system of equations} = \begin{cases}
2b=3a \\
b-7=-2a
\end{cases} $$

Here, \\(a\\) and \\(b\\) are variables. We are trying to solve for the combination of \\(a\\) and \\(b\\) that make both equations true. To understand it better, let's look at a graph:

(image)

We can clearly see that both equations intersect at \\(a=2\\) and \\(b=3\\). This is our solution, because both the equations intersect at this point. We have just graphically solved the system of equations. Let's try to solve it algebraically now.

We will employ a technique known as <b>substitution</b>. Substitution is a method of solving one variable in terms of the other variable, and then substituting that into the other equation. Let's solve for b in terms of a:

$$\begin{align*}b-7&=-2\\
b&=-2a+7\end{align*}$$

Now that we have \\(b\\) in terms of \\(a\\), we can substitute that back into the first equation.

$$\begin{align*}
2b&=3a\\
2b&=3a\\
2(-2a+7)&=3a\\
-4a+14&=3a\\
-7a+14&=0\\
-7a&=-14\\
a&=2
\end{align*}$$

We have solved for \\(a\\) now. To find \\(b\\), we need to plug the value of \\(a\\) back into an equation (it doesn't matter which one). Let's use the first equation.

$$
\begin{align*}
2b&=3a\\
2b&=3(2)\\
2b&=6\\
b&=3
\end{align*}$$

We now have our answers: \\(a=2, b=3\\). These match up with the intersection on the graph.

To recap, the steps for solving a system of equations are:
1. Solve the first variable in terms of the second using an equation.
2. Substitute the first variable for the other equation to solve for the second variable..
3. Solve for the first variable by plugging the second variable into any equation.
