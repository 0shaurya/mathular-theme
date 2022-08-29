---
layout: page
title: About this site
menuInclude: yes
menuLink: yes
menuTopTitle: About
menuTopIndex: 100
excerpt: A short introduction to the content of this site.
terms:
  - ['Congruent Angles',   'They have the same angle measure (in degrees or radians). They are present in equilateral triangles, isosceles triangles, or when a transversal intersects two parallel lines. They are denoted by the symbol "≅", so if we want to represent ∠A is congruent to ∠B, we will write it as ∠A ≅ ∠B.']
  - ['second term', 'second definition']
questions:
  - ['Example question', 'Example answer']
---

This is a placeholder in the theme.

You can edit this page in the file `pages/about/about.md`

This is the 'Classic-Jekyll-Theme'. See "Jekyll -> Static Generator" for a general description of what Jekyll is.

![This is an image](https://upload.wikimedia.org/wikipedia/commons/e/e7/Everest_North_Face_toward_Base_Camp_Tibet_Luca_Galuzzi_2006.jpg)

# Algebra

## Variables and Equations

Often in math, we have to deal with problems that force us to find what number something is. For example, say Alice and Bob have a combined total of 10 apples. We know Alice has 6 apples, so how much does Bob have? Our goal is to find the number of apples Bob has. Let's talk about this scenario in a math way:

$$\text{Number of apples Alice has} + \text{Number of apples Bob has} = 10$$

Because Alice has 6 apples, Bob must have four to make this equation work:

$$6 + \text{Number of apples Bob has} = 10$$

It's important to notice that the Number of apples Bob has is an unknown, because the question does not give the straight number - we have to solve the problem to figure that out. We call these unknowns variables. Variables just represent an unknown number.

Because writing out “Number of apples Bob has” can get tedious, let's just shorten that to “b”, for Bob. \\(b\\) is a variable. So, we can model the question in the following way:

$$6 + b = 10 \\
\text{Solve for }b$$

Here, \\(6 + b = 10\\) is an equation. An equation is simply two expressions with an equal sign in between. Here, our expressions are \\(6 + b\\) and \\(10\\). Expressions are simply a set of numbers or variables that interact with each other using operations. Operations are things like addition, subtraction, multiplication, and division. Important note: whenever you see a number next to a variable, that signifies multiplication. For example, \\(6x = 6\cdot5 = 6\\) x \\(5\\).

Another important thing to know is what a constant is. A constant is simply a number. In our equation, \\(6\\) and \\(10\\) are constants.

![](https://lh4.googleusercontent.com/5Jm4SfoJqfxe5i2BwTKSmQK-hvhH6KZXy-t598Pd_WBXEQWO2Fnwub19D0StHCVdAe6_H1z4Kxgqn_DDc6H-jkj-pXGT5a1jRuIU4T-54OQDRXrWg_rIczRmiCEjCcFmF_gmx6uv1FVOC7SvPv1FTg)![](https://lh5.googleusercontent.com/fjP-igX7nSYmoKCHxgEOIYb4Lvh63uBze3QDiKP9RqJftlMax6svC1G75qRr-Yq2c5dzpAXgE1MUJcos--5gkPyqUQ71FsF3rY-KFtApz08mgQgAvDxQGUkNW81SQ2KEnzw4pyKuDypzXpfUOdR9gA)

## Linear Equations

In the last chapter, we covered the parts of an equation. Now, let's talk about a certain type of an equation: the <b>Linear Equation</b>. A linear equation is an equation that consists of a variable multiplied by a number, added to a constant. For example, \\(12x-5=0\\) is a linear equation. So is \\(58x+119=0\\). In general, a linear equation can be written as:

$$ax+b = 0$$

where \\(a\\) and \\(b\\) are constants and and \\(x\\) is a variable. Note that you will often see \\(x\\) as a variable.

In a linear equation, \\(a\\) is a <b>coefficient</b>. A coefficient is the number next to a variable - the coefficient is always multiplied by the variable. The coefficient is negative if the term is being subtracted.

## Solving Equations

Sometimes, you will need to solve for a variable in an equation. This means that you have to do math to figure out what number the variable is.

Whenever solving an equation, your goal should always be to get the variable on one side of the equals sign, and all the numbers on the other side of the equals sign. That way, by the end, you will have found what number the variables equals to. To do this, our first step should be to combine like terms. To understand what that means, let's break it down. First, a term is an expression that does not contain any pluses or minuses. A term can have numbers, variables, exponents, etc, but it can't have a plus or minus. An expression may contain multiple smaller terms inside of it. For example, in \\(23x^4p+5y+x^3-4+3x^3\\), there are 4 terms:

$$23x^4p,\\5y,\\x^3,\\-4,\\3x^3$$

Note that \\(-4\\) is the third term, and not \\(4\\), because there is a minus sign before the four. If there is a minus sign before aterm, it will change to a negative sign and stay in the term.

To combine like terms, figure out what terms have the same variables with the same exponents. Then, add the coefficients of each term, while keeping the variable(s) the same. Remember that the coefficient is the number next to the variable.

For the next step, there is one important rule you always have to remember:

When doing something to one side of the equals sign, always do the exact same to the other side of the equals sign. This maintains equality.

For example, look at the following:

$$2=2$$

Everyone knows that \\(2\\) is equal to \\(2\\). However, say you multiply by 3 on the left hand side. Then, we get:

$$6 = 2$$

Obviously, this is not true. To fix it, we have to multiply 3 to the other side as well:

$$2\cdot3 = 2\cdot3$$

After combining like terms, subtract every term (or add if the term is negative) that doesn't have the variable you are trying to solve for. Remember our rule from earlier: if you have to subtract a term from the left side, do it to the right side too. Then, when you are left with a single term on the side with the variable, divide by the coefficient. This should leave you with the variable on one side of the equals sign, with a number on the other side of the equals sign.

Let's try this with the following equation:

$$5x+12x-14=-6+x$$

Combine like terms.

$$17x-14=-6+x$$

Subtract both sides by x to get only numbers on the right side.

$$16x-14=-6$$

Add both sides by 3 to get a single term on the left side.

$$16x=8$$


Divide by the coefficient of the left side.

$$x=1/2$$

One final thing: if the equation has an exponent in it, use the inverse of the exponent (the root) to make x by itself. For example in:

$$x^2=16$$

Take the square root of both sides.

$$
\begin{align*}
x&=\sqrt16\\
x&=4
\end{align*}$$

To recap, the steps for solving equations are:
1. Combine like terms.
2. Subtract any terms that do not have the variable you are trying to solve for in it and get x on only one side of the equation.
3. Divide by the coefficient of x, or apply the n-th root if the x is to the n-th power.

## Functions and Graphing

Let's begin by going over what a function is. At its simplest level, a function will take in a number, apply some operation to it, and output another number. Let's go over notation first.

Functions are denoted by \\(f(x) = \text{Some function}\\). Note that it doesn't have to be f(x), it could be \\(g(x)\\), \\(h(x)\\), or any other letter. However, it's usually \\(f(x)\\). Some example of functions are:

$$f(x) = x^3+2\\
g(x) = \frac{2}{x}-3\\
h(x) = \sqrt{x}$$

The input here is the \\(x\\) in parentheses after the \\(f\\), \\(g\\), and \\(h\\). When inputting a number into the x value, we substitute every x inside the function for that number. For example:

$$
\begin{align*}
f(x) &= x^3+2\\
f(5) &= 5^3+2\\
f(5) &= 127
\end{align*}$$

$$
\begin{align*}
g(x) &= \frac{2}{x}-3\\
g(0.5) &= \frac{2}{0.5}-3\\
g(0.5) &= 1
\end{align*}$$

That's how we write functions algebraically. We can also visualize them using tables. Consider the following table for the function \\(f(x) = 3x+1\\):

//table

Or, we can use graphs. Functions on graphs are very useful and common. This is the graph for the same function \\(f(x) = 3x+1\\). On the x-axis (big horizontal line), lies the value of an x value (an input to the function). On the y-axis (big vertical line), lies the corresponding f(x) value. For example, 3 units to the right of the origin (the origin is where the two axes cross), the y value is 10, because \\(f(3) = 10\\).

An important note about functions: when inputting a number into a function, the function should always return either 1 or 0 numbers. In other words, inputting a number into a function can never give 2 (or more) results. For example, the following graph is not a function:

because at \\(x=??????\\), there are two y values. You can use something called the vertical line test to test if a function on a graph is actually a function. If you can make at least 1 vertical line on the graph that crosses the function at least twice, that is automatically not a function. Look at the following for an example of the vertical line test:

Feel free to play with functions as you want here:

<br><br><iframe href=”desmos.com/calculator”>

## Polynomials

We have already gone over what equations are, and even one type of them (linear equations). Now, let's cover a different type of equation: polynomials. A polynomial is a huge umbrella that contains many different types of equations (including linear equations!). The form of a polynomial is:

$$P(x)=a_{n}x^{n}+a_{n-1}x^{n-1}+\cdots+a_{2}x^{2}+a_{1}x+a_{0}$$ \\(a_{n}\\) is the coefficient of the variable, \\(x\\). an can be any number. In each term, x is raised to some exponent, \\(n\\). \\(n\\) is always an integer that is at least 0. These terms are separated by addition (or subtraction, if the term after has a negative coefficient). There are two observations that are important. First, that if \\(a_{n}\\) is 0, then the entire term is multiplied by 0 and is therefore canceled out. Also, if the exponent of \\(x\\) is 0, then that means that the corresponding term is whatever the coefficient is, because \\(x^0\\) is always equal to 1. Some examples of polynomials are:

$$f(x)=3x^5+x^4+13x^3−11x+x^2+10\\
g(x)=x+x^2-3\\
h(x)=7x^4−2x−\frac{18}{5}$$

Some examples of functions that are *not* polynomials are:

$$i(x)=\frac{x^2+5x}{x^9-35}\text{ because the entire equation is a fraction}$$

$$j(x)=x^3-2x^2+8x-4+3x^{-1}\text{ because there is at least one negative exponent}$$

$$k(x)=2x^3+x^\frac{1}{2}\text{ because there is at least one non-integer exponent}$$

The <b>constant</b> of a polynomial is the term that has \\(x^0\\) as it's variable part. The constant is just a number. For example, in the polynomial

$$f(x)=3x^5+x^4+13x^3−11x^2+10$$

the constant is \\(10\\). In the polynomial

$$g(x)=x+x^2-3$$

the constant is \\(-3\\).

The <b>degree</b> of the polynomial is equal to the highest exponent of the polynomial. For example, in the polynomial

$$f(x)=3x^5+x^4+13x^3−11x^2+10$$

the degree is \\(5\\). In the polynomial

$$g(x)=x+x^2-3$$

the degree is \\(2\\).

As a final note, know that polynomials are usually ordered with the highest exponent on the far left to the lowest exponent (the constant) on the far right. A polynomial doesn't have to be ordered like that, but that is how they should be ordered in most cases.

## Complex Numbers

Now that we've covered how to solve equations, let's see how to solve the following equation for \\(x\\):

$$x^2=-1$$

To get x alone, we take the square root of both sides:

$$x=\sqrt{-1}$$

So, \\(x\\) is equal to the square root of negative one. But, what does that actually mean? Well, let's remember that the square root of something is the number that, when multiplied by itself, equals that something. For example, the square root of \\(25\\) is \\(5\\) because \\(5\cdot5=25\\). So, what number times itself equals \\(-1\\)?

When we multiply a positive number by itself, the answer is positive. When we multiply a negative number by itself, the answer is positive as well, because a negative times a negative equals a positive. For example:

$$
\begin{align*}
-5\cdot-5&=25\\
-6\cdot-6&=36
\end{align*}$$

This means that no matter what number we multiply by itself, we will never get a negative answer. Because of this, there is no number that we can square to get \\(-1\\), so \\(\sqrt{-1}\\) does not have an answer.

To solve this problem, mathematicians introduced a new number to solve this problem: \\(i\\). We define \\(i\\) squared to be negative 1:

$$
\begin{align*}
i^2=-1\\
i = \sqrt{-1}
\end{align*}$$

\\(i\\) is not a variable. It is a number, in the same way that 1, 2, 3, 4… are all numbers. However, it is a different type of number - an <b>imaginary number</b>. An imaginary number is a regular number multiple by \\(i\\). For example, \\(5i\\) is an imaginary number because it is \\(5\cdot i\\), or \\(5\cdot \sqrt{-1}\\).

## Quadratic Equations

Let's go over one type of polynomial, quadratic equations. Quadratic equations are functions that can be written in the following form:

$$f(x)=ax^2+bx+c$$

where a, b, and c are real numbers. A quadratic equation is called a parabola, and has a U shape on a graph. All of these are examples of quadratic equations, or parabolas:

![](https://lh5.googleusercontent.com/AfnbtWRS53SZwZGHLKaXj22zrZLCgjCqlxM3N7cA0PB5HolY6NT5zW6IuFEKxBV_jc-OOucws3zBWHxfLAIAJbXw00zbf9dGQBIpaaSWWki77Yqd__GsbQ2EViOuSZvBDtiHR33TmdDW4JUtkMnB8lY)

As you can see, parabolas can either open down or open up. The orange and blue parabolas open up, and the green and red parabolas open down. A parabola opens up when $$a$$ is positive, and open downs when $$a$$ is negative. When $$a$$ is $$0$$, the entire first term is canceled out and it becomes a linear function.

Another thing to notice is the root(s) of an equation. The root of a quadratic equation $$f(x)$$ is when it hits the x-axis, or when $$f(x)=0$$. A quadratic equation can have 0, 1, or 2 real roots. In the earlier image, the red and orange parabolas have 2 roots, because they cross the x-axis twice, the blue parabola has 0 roots, because it never crosses the x-axis, and the green parabola has 1 root, because it crosses the x-axis only once.

Sometimes, it's important to find the x-values of the roots of an equation. The roots of an equation are the answer to the following expression:

$$x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

## Systems of Equations

A <b>system of equations</b> is a group of multiple equations with multiple variables. Usually, it is mostly impossible to solve for an equation if you are only given one equation - however, with multiple equations, we can solve for multiple variables.

Take a look at the following system of equations:

$$\text{This is a system of equations} = \begin{cases}
2b=3a \\
b-7=-2a
\end{cases} $$

Here, \\(a\\) and \\(b\\) are variables. We are trying to solve for the combination of \\(a\\) and \\(b\\) that make both equations true. To understand it better, let's look at a graph:

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

# Geometry

## Angles, lines, and shapes

## Congruency

## Proofs

## Intro to trig

## Transformations

# Precalculus

## Simple and Compound Interest

A bank will give you <b>interest</b> on money stored in an account. Interest is the money paid regularly at a specified percentage. For example, if Alice keeps \\(100\\) in her bank account, and it has an interest rate of 3% monthly, she will get 3 more dollars in her account the next month.

There are two types of interest. The first type is <b>simple interest</b>. Simple interest is when the bank pays you back at a percentage of the initial value deposited. For example, if Bob deposits \\(1,000\\) into his bank account initially (note that the initial value deposited is known as the <b>principal</b> value), with a simple interest of 10% yearly, he will gain \\(0.1\cdot1000=100\\) dollars every year. Bob's account will look like the following:

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

Here, \\(n\\) is the new parameter. \\(n\\) represents the number of times the money is compounded in the time period \\(t\\). For example, if \\(t\\) is measured in years and the money is compounded monthly, \\(n\\) would be 12. If \\(t\\) was measured in years and the money was compounded years, \\(n\\) would be 1.

Let's plug our new formula into Charlie's situation to find out how much money he would have after 3 years:

$$A = P(1+\frac{r}{n})^{nt}$$

$$\begin{align*}
A &= 1000(1+\frac{0.01}{12})^{12\cdot3}\\
A &= 1000(\frac{12.01}{12})^{36}\\
A &= 1000(1.03044)\\
A &= 1030.44
\end{align*}$$

Charlie will have \\(1030.44\\) at the end of the 3 years.

## Trigonometry

In geometry, you learned about the three common trigonometric functions: sine, cosine, and tangent. Let's do a little bit of review:

To get the sine of an angle, take the length of the side opposite the angle and divide that by the length of the hypotenuse. Cosine and tangent work the same, except cosine is adjacent divided by hypotenuse and tangent is opposite divided by adjacent.

(images)

Before moving forward, it's important to have a firm understanding of <b>radians</b>. A degree is a unit measurement for an angle, with 360° being a full circle and 180° being a straight line. A radian is a similar measurement for a degree, except it is in terms of \\(\pi\\).

0 degrees corresponds to 0 radians. While 360 degrees is a full circle, 2pi radians is also a full circle. From those two facts, we can fill in the blanks. A right angle in degrees is \\(\frac{360}{4}\\), and a right angle in radians is \\(\frac{2\pi}{4} = \frac{\pi}{2}\\). The formula for converting degrees to radians is

$$\text{radians} = \text{degrees} \cdot \frac{\pi}{180}$$

The formula for converting radians to degrees is

$$\text{degrees} = \text{radians} \cdot \frac{180}{\pi}$$

(table for degrees and radians)

Now, let's look at sine, cosine, and tangent as functions instead of geometrically. Let's look at the sine function. The sine function takes in an angle measurement (usually in radians) and will output a number between \\(-1\\) and \\(1\\). That number is the ratio of the opposite side to the hypotenuse. To find out the shape of this graph, it is helpful to look at a circle. Take a look at the following circle with radius 1 (known as a <b>unit circle</b>, with triangles within it:

(image)

No matter the angle \\(\theta\\), line ????? stays at a length of 1. This is because of the nature of equidistance in circles. However, line ????? varies in length. Let's zoom into one instance of this circle:

(image)

It seems like a right triangle just pops out of nowhere. Labeling the sides, we have:

(image)

Now, using our definition from earlier, we can clearly see that \\(\sin(\theta) = \frac{\text{length of line ????}}{\text{length of line }?????}\\). Because the length of line ????? is always 1, we can say that \\(\sin(\theta) = \frac{\text{length of line }????}{\text{length of line }?????}\\). This is an important discovery - it shows us that \\(\sin(\theta)\\) is directly equal to the height of line ??????.

Using this information, we can follow \\(\theta\\) around the full \\(2pi\\) radians to see the following:

(image)

This gives us the shape of \\(\sin(\theta)\\).

Now, let's do a similar process for cosine.

Here, we can see that \\(\cos(\theta)\\) is equal to the length of line ???? divided by the length of the hypotenuse. Again, because the length of the hypotenuse is always \\(1\\) no matter the value of \\(\theta\\), \\(\cos(\theta)\\) is equal to the length of line ?????

This gives us the shape of the cosine curve:

(image)

Something to notice is how the graphs of sine and cosine will repeat. Because the unit circle has a circumference of \\(2\pi\\), it means that the values for sine and cosine will repeat every \\(2\pi\\) units. This is known as the <b>period</b> of the curve. The period is how long it takes for the curve to repeat its pattern.

  

Now, let's talk about tangent. \\(\tan(x)\\) is defined to be \\(\sin(x)\\) divided by \\(\cos(x)\\). This is why the tangent of an angle is equal to opposite over adjacent.

$$\begin{align*}
\sin(x) &= \frac{\text{Opp}}{\text{Hyp}}\\
\cos(x) &= \frac{\text{Adj}}{\text{Hyp}}\\
\tan(x) &= \frac{\sin(x)}{\cos(x)}\\
\tan(x) &= \frac{\frac{\text{Opp}}{\text{Hyp}}}{\frac{\text{Adj}}{\text{Hyp}}}\\
\tan(x) &= \frac{\text{Opp}}{\cancel{\text{Hyp}}}\cdot\frac{\cancel{\text{Hyp}}}{\text{Adj}}\\
\tan(x) &= \frac{\text{Opp}}{\text{Adj}}
\end{align*}$$

This is the graph of \\(\tan(x)\\) overlaid over the graphs of \\(\sin(x)\\) and \\(\cos(x)\\). You can see how when \\(\sin(x)\\) is 0, \\(\tan(x)\\) is 0 (because 0 divided by anything is 0), and when \\(\cos(x)\\) is 0, \\(\tan(x)\\) has no value (because anything divided by 0 is undefined).

  

(image)

  

There are three other functions to know: \\(\csc(x)\\), \\(\sec(x)\\), and \\(\cot(x)\\). They are fairly simple:

  

$$\csc(x) = \frac{1}{\sin(x)}$$

$$\sec(x) = \frac{1}{\cos(x)}$$

$$\cot(x) = \frac{1}{\tan(x)}$$

  

Here are their graphs:

  

(image)

  

And here are the graphs of all 6 functions overlaid:

  

(image, use matplotlib legend)

## Solving Equations with Trig

Using algebra to solve equations is a fairly straightforward process most of the time if the operations are simple. However, it's a lot harder for equations with trigonometric functions inside of them. Let's find out how to solve those types of problems.

Let's start with the unit circle. In the last chapter we talked about the unit circle and how it relates to sine and cosine. Remember that the unit circle is the circle centered at (0, 0) with a radius of 1. We related it to trigonometric functions by drawing right triangles inside it, and discovered that \\(\sin(\theta)\\) is equal to the height of the right triangle that has a vertex on the origin and a hypotenuse of length 1.

(image)

Using this knowledge, we can figure out the value of \\(\sin(\theta)\\) for select values of \\(\theta\\). Let's try to find \\(\sin(\theta)\\) for values of \\(\theta = \frac{\pi}{3}, \frac{\pi}{4}, and \frac{\pi}{6}\\). First, let's try to find \\(\sin(\frac{\pi}{3}\\), or \\(\sin(30^{\circ})\\). This is the corresponding diagram:

(image)

Our triangle has a 30 degree angle, 60 degree angle, and 90 degree angle. Notice how we can reflect the triangle over the x-axis to get a triangle whose angles are all equal to 60 degrees. This means that the triangle is equilateral, and so all sides are the same length:

(image)

If all sides are the same length, and side \\(H\\) has a length of 1, then that must mean that \\(2\cdot\sin(\frac{\pi}{3}) = 1\\), and therefore \\(\sin(30^{\circ}) = 0.5\\). Using Pythagorean's Theorem, we can find the length of the final side of the triangle, side \\(A\\): \\(A^2+(0.5)^2 = 1^2\\), so \\(A\\) must equal \\(\frac{\sqrt{3}}{2}\\). Because \\(A = \cos(\theta)\\), \\(\cos(\theta) = \frac{\sqrt{3}}{2}\\). This gives us a triangle for \\(\theta = \frac{\pi}{3}\\):

(image)

We have successfully found the values of \\(\sin(\frac{\pi}{3})\\) and \\(\cos(\frac{\pi}{3})\\). Because taking \\(\theta=\frac{\pi}{3}\\) also gives us a 30-60-90 triangle, we can use the same method to find the values of \\(\sin(\frac{\pi}{3})\\) and \\(\cos(\frac{\pi}{3})\\).

Finding the value of \\(\sin(\frac{\pi}{4})\\) and \\(\cos(\frac{\pi}{4})\\) is a lot easier. Let's draw a triangle for \\(\theta=\frac{\pi}{4}\\), or \\(\theta=45^{\circ}\\):

(image)

Because we have a 45-45-90 triangle, we know that it must be isosceles because two of the angles are the same. By the definition of an isosceles triangle, \\(\sin(\theta) = \cos(\theta)\\). Using Pythagorean's theorem we know \\(2\sin^2(\theta) = 1\\), so \\(\sin(\theta) = \frac{1}{\sqrt2}\\). Multiply both the numerator and denominator by \\(\sqrt2\\) to find \\(\sin(\frac{\pi}{4}) = \cos(\frac{\pi}{4}) = \frac{\sqrt2}{2}\\).

Now that we have values for those three values, we can fill in the following table for various values of \\(\theta\\):

Because \\(\sin(\theta)\\) is directly equal to the y-value and \\(\cos(\theta)\\) is directly equal to the x-value, we can also produce the following graph:

(unit circle graph)

Now that we know the unit circle, we can solve an equation like this:

$$cos(\theta) = \frac{1}{2}$$

Take a look at our unit circle. We're looking for values of \\(\theta\\) where the x-value is equal to \\(\frac{1}{2}\\) (because cosine is represented by the x-value). Looking at our unit circle, we can see that those x-values appears when \\(\theta\\) equals \\(\frac{\pi}{3}\\) and \\(\frac{5\pi}{3}\\). However, remember that \\(\cos(\theta)\\) has a period of \\(2\pi\\) - this means that values for cosine will repeat every \\(2\pi\\) units, so the actual answer is:

$$\theta = \frac{\pi}{3} + 2\pi k, \theta = \frac{5\pi}{3} + 2\pi k$$

where \\(k\\) is any integer. We can visually see this on a graph:

(image)

Using the unit circle, we can solve more complicated equations involving trigonometric functions by just good old algebra. Here's an example:

$$4\sin^2(3x) - 1 = 0$$

While this looks daunting at first, we can use simple algebra to get it to an equation with just a \\(\sin(x)\\):

$$\begin{align*}
4\sin^2(3x) - 1 &= 0 \\
4\sin^2(3x) &= 1 \\
\sin^2(3x) &= \frac{1}{4} \\
\sin(3x) &= \frac{1}{2} \\
3x &= \frac{\pi}{6}+2\pi k, \frac{5\pi}{6}+2\pi k\\
x &= \frac{\pi}{18}+\frac{2\pi k}{3}, \frac{5\pi}{18}+\frac{2\pi k}{3}
\end{align*}$$

Here's a problem involving tangent:

$$\tan(x)=-\frac{1}{\sqrt3}$$

The key here is to manipulate the equation to something familiar - something inside the unit circle. In this case, we can rewrite the above equation to the following: 

$$\frac{\sin(x)}{\cos(x)}=\frac{- \frac{1}{2}}{\frac{\sqrt3}{2}}$$ 

Now, we know that \\(x\\) can be \\(\frac{11\pi}{6}\\), because \\(\sin(\frac{11\pi}{6}) = -\frac{1}{2}\\) and \\(\cos(\frac{11\pi}{6}) = \frac{\sqrt3}{2}\\). If you aren't certain about this, take a look at the unit circle.

We can rewrite the equation again in the following way: 

$$\frac{\sin(x)}{\cos(x)}=\frac{\frac{1}{2}}{- \frac{\sqrt3}{2}}$$

Notice that now the negative sign is the denominator. Looking at the unit circle, we know \\(x\\) can be \\(\frac{5\pi}{6}\\). So we have

$$\tan(x)=-\frac{1}{\sqrt3}\\
x = \frac{5\pi}{6}, \frac{11\pi}{6}
$$

Here are those values of \\(\theta\\) on the unit circle:

(image)

We can clearly see that \\(\theta\\) is equal to \\(\frac{5\pi}{6} + \pi k\\). So we have our final answer:

$$\tan(x)=-\frac{1}{\sqrt3} \\
x = \frac{5 \pi}{6} + \pi k
$$

Now we have learned how to solve equations involving trigonometric functions using certain values of \\(\theta\\) in the unit circle.

## Exponentials and Logarithms

Let's discuss another umbrella of functions, <b>exponential functions</b>. An exponential function is a function written in the form of

$$f(x)=ab^x$$

The important part here is how \\(x\\) is in the exponent - this key part is what makes it an exponential function. This is in contrast to polynomial functions, where \\(x\\) is in the base. Here is a graph of the function \\(2^x\\):

(image)

The first thing to notice is that \\(2^x\\) grows very fast. This is because the y-value doubles after each unit step in the x direction. This is because every time we add 1 to the x-value, the y value will be multiplied by 2 another time:

$$\begin{align*}
2^3 &= 2\cdot2\cdot2 = 8 \\
2^4 &= 2\cdot2\cdot2\cdot2 = 16 \\
2^5 &= 2\cdot2\cdot2\cdot2\cdot2 = 32
\end{align*}$$

Another thing to notice is what happens when \\(x=0\\). Any number raised to the 0th power is 1, meaning

$$f(0)=ab^0$$

$$f(0)=a\cdot1$$

$$f(0)=a$$

Thus, the y-intercept of an exponential function in the form \\(f(x)=ab^x\\) is always \\(a\\). We can verify this by graphing some more exponential functions:

(image)

Exponential equations come up a lot in the real world. For example, imagine 5 bacteria on a petri dish. Every hour, the number of bacteria doubles. This means that the number of bacteria follow the function \\(B(t)=5\cdot2^t\\), with \\(t\\) being the number of hours.


Now, let's talk about solving equations with exponentials. Suppose we wanted to solve the equation \\(3^x=10\\), how would we go about doing it? \\(3^2\\) is 9 and \\(3^3=27\\), so we know the answer is very close to 2, but we do not have an exact form. Fortunately, we can use a <b>logarithm</b>.

A logarithm is the inverse function of the exponential, in the same way that multiplication is the inverse of division and subtraction is the inverse of addition.

A logarithm looks like:

$$g(x)=\log_bx$$

Here, \\(b\\) is the base of the logarithm. Logarithms are just a family of functions, and \\(b\\) is a parameter. We can relate exponential functions and logarithms by solving an equation:

$$3^x=10$$

Let's apply a logarithm here. The base of the exponential is \\(3\\), so let's apply a logarithm with base 3 to both sides.

$$\log_{3}{3^x}=\log_{3}{10}$$

Here is the key part of a logarithm - a logarithm of a base next to an exponential with the same base will cancel out, leaving only the power. In general:

$$\log_{b}{b^a} = \cancel{\log_{b}}\cancel{b}^a = a$$

This means that

$$\cancel{\log_{3}}\cancel{3}^x=\log_{3}{10}$$

$$x=\log_{3}{10}$$

Which, if you plug into a calculator, you will find is approximately \\(2.096\\). Here is a handy diagram that might help you relate exponentials and logarithms:

(image)

When we graph logarithms, we should remember that logarithms are just an inverse of exponentials. So, to graph a logarithmic function, we flip the corresponding exponential function over the line \\(y=x\\). This means that

(image)

In general, the graph of a logarithm will look like a sideways exponential, with a vertical asymptote at \\(x=0\\), just like how the graph of an exponential has a horizontal asymptote at \\(y=0\\).

Now, let's discuss some properties of logarithms. There are four main properties to know. Let's start with the first one, the <b>product rule law</b>, which says

$$\log_{b}{M\cdotN}\ = \log_{b}{M}+\log_{b}{N}]]

For example, \\(\log_{2}{14} = \log_{2}{2\cdot6} = \log_{2}{2}+\log_27 = 1+\log_27\\). This works because it is a parallel to the product rule for exponents law.

The second law is the <b>quotient rule law</b>. This says

$$\log_{b}{\frac{M}{N}} = \log_{b}{M} - \log_{b}{N}$$

For example, \\(\log_{5}{\frac{2}{5}}=\log_{5}{2}-\log55=\log_52-1\\). This law works because it is parallel to the quotient rule for exponents law.

The third law is the <b>power rule law</b>. This says

$$\log_{b}{a^c}=c\cdot\log_{b}{a}$$

For example, \\(\log_{3}{32} = \log_{3}{2^5} = 5\log{3}{2}\\). This law works because it is just the product rule repeated \\(c\\) times.

The fourth law is the <b>change of base law</b>. This law says that

$$\log_{b}{a} =\frac{\log_da}{\log_db}$$

\\(d\\) can be any number. For example, \\(\log_27 = \frac{\log_37}{\log_32} = \frac{\log_47}{\log_42} = \frac{\log_57}{\log_52}\\)

## Vectors

A <b>vector</b> is a geometric object that we draw as arrows on a graph. Here are some examples of vectors on a graph:

(image)

The main thing to notice here is that all vectors contain two properties: a <b>magnitude</b> and a <b>direction</b>. The magnitude is the length of the vector. The direction is an angle. The direction is usually described by a number in degrees or radians. Because those are the only two properties vectors have, all vectors originate from the origin. This is why all of the tails of the vectors in the image start from the origin.

Vectors are written down as a letter with a small arrow over it: \\(\vec{v}\\). Each vector has two components, a horizontal component and a vertical component. The horizontal component is the horizontal distance from the tail to the head of the arrow, and the vertical component is the vertical distance from the tail of the head to the arrow. We write a vector by listing out the horizontal and vertical components surrounded by pointy brackets. Here is an example of a vector and how to write it:

(image)

As mentioned earlier, the magnitude of the vector is the shortest distance from its tail to its head. The notation of the magnitude of a vector is two straight vertical lines around it on each side. For example, the magnitude of vector \\(\vec{v}\\) is \\(\vert\vert \vec{v} \vert\vert\\). To find the magnitude of a 2-dimensional vector, we can use the Pythagorean theorem:

Because the horizontal component of the vector is ???????? and the vertical component is ??????????, we can see the magnitude is \\(\sqrt{?????^2+?????^2} = ???????\\). This gives us the general formula for the magnitude of a vector:

$$||\vec{v}|| = \sqrt{x^2+y^2}$$

where \\(x\\) is the horizontal component and \\(y\\) is the vertical component.

If the angle \\(\theta\\) of a vector is not given, we can use trigonometry to find it. For example, take the following vector:

(image)

Although we are not explicitly given \\(\theta\\), we can figure it out by using trigonometry. We know \\(\sin(\theta) = \frac{?????}{?????}\\), so we can take the inverse sine of both sides to find \\(\theta = ??????\\). Thus,

(image)

We can also add vectors. Let's first add vectors geometrically. To add two vectors geometrically, just place them such that the tail of one vector is on the head of another. This will give us a third vector:

(image)

To add a vector algebraically, we can just add the horizontal component of the first vector with the horizontal component of the second vector and do the same with the vertical components. This will give us the components of the vector sum. Here is an image explaining why this works:

(image)

To find the magnitude and direction of the vector sum, we can use the methods discussed earlier.

The negative of a vector is simply the opposite horizontal and vertical components. For example, here is the opposite of vector \\(\vec{v}\\):

(image)

Knowing this information, we can now subtract vectors, because adding a negative is the same as subtracting. Here is an example of subtracting a vector algebraically:

(example using mathjax)

We can also multiply a vector by a <b>scalar</b>. A scalar is just a regular number, like 5, -6, or \\(\pi\\). To multiply a vector by a scalar, we just multiply the horizontal and vertical components of the vector by the scalar quantity:

(example using mathjax)

Here is the example but geometrically:

(image)

## Sequences, Summations, and Series

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

## Probability

To begin with probability, let's first define what an <b>event</b> is. An event is simply an outcome of an experiment. For example, when drawing a card from a deck, some examples of events are drawing a 4 of hearts, drawing a 6 of clubs, drawing a king of any suit, or drawing a card with hearts. The complete set of all events is known as the <b>sample space</b>.

The most basic formula for probability is

$$P(A) = \frac{\text{\# of outcomes in A}}{\# \text{ of outcomes in sample space}}$$

This formula assumes all outcomes are equally likely. Here, \\(A\\) is an event, and \\(P(A)\\) is the probability of event \\(A\\) occurring.

This only covers the probability of one event occurring. Let's now go over the probability when events interact with one another. Before continuing, let's define two new terms: <b>independent events</b> and <b>dependent</b> events. An independent event is an event whose probability does not change when another event occurs. For example, owning a dog and getting heads when flipping a coin are independent of each other because one outcome does not affect the other. A dependent event is an event whose probability does depend on another event happening. For example, drawing a card from a deck and then drawing another card from the same deck without putting the first card back in.

First, let's start with the probability of two events both happening. This is known as an “and” event. The formula for event \\(A\\) and event \\(B\\) both happening is

$$P(A\cap B) = P(A) \cdot P(B)$$

The \\(\cap\\) symbol represents “and”. We multiply the probabilities of events \\(A\\) and \\(B\\) to find the probability of both of them happening. For example, the probability of rolling a 2 on a 6-sided die and getting a tails when flipping a coin is

$$P(A\cap B) = P(A) \cdot P(B)$$

$$P(\text{rolling a 2}\cap \text{flipping a tails}) = \frac{1}{6}\cdot  \frac{1}{2}$$

$$\frac{1}{12}$$

This formula only works for independent events.

The probability of one event or another event happening is given by the formula

$$P(A\cup B) = P(A) + P(B) - P(A\cap B)$$

The \\(\cup\\) symbol represents “or”. \\(A\\) and \\(B\\) are events. This formula is best explained by a venn diagram:

(image)

We can see that we subtract the probability of events \\(A\\) and \\(B\\) happening to avoid double counting the middle section. For example, the probability of rolling a 2 on a six sided die or getting a tails when flipping a coin is

$$\begin{align*}
P(\text{rolling a 2}\cup\text{flipping a tails}) &= P(\text{rolling a 2}) + P(\text{flipping a tails}) - P(\text{rolling a 2}\cap\text{flipping a tails})\\
P(\text{rolling a 2}\cup\text{flipping a tails}) &= \frac{1}{6} + \frac{1}{2} - P(\text{rolling a 2}) \cdot P(\text{flipping a tails})\\
P(\text{rolling a 2}\cup\text{flipping a tails}) &= \frac{1}{6} + \frac{1}{2} - \frac{1}{6}\cdot\frac{1}{2}\\
P(\text{rolling a 2}\cup\text{flipping a tails}) &= \frac{1}{6} + \frac{3}{6} - \frac{1}{12}\\
P(\text{rolling a 2}\cup\text{flipping a tails}) &= \frac{8}{12} - \frac{1}{12}\\
P(\text{rolling a 2}\cup\text{flipping a tails}) &= \frac{7}{12}
\end{align*}$$

The third operation is <b>given</b>. The probability of event \\(A\\) given \\(B\\) is the probability of event \\(A\\) occurring given that event \\(B\\) has already occurred. Here is the probability for \\(A\\) given \\(B\\):

$$P(A\mid B) = P(\text{event } A \text{ occurring given that event } B \text{ has already occured}) = P\left(\frac{P(A\cap B)}{P(B)}\right)$$

For example, a city has a 10% chance of raining on any day, assuming that there was no rain the previous day. However, if there was rain the previous day, there is a 15% chance of rain. To find the probability of two days of rain in a row, we can let event \\(F\\) be rain falling on the first day and event \\(S\\) be rain falling on the second day. Let's assume there was no rain on the day before the first day. From the problem, we know

$$P(S\mid F) = 15%$$

And using our formula, we know

$$P(S\mid F) = \frac{P(F\cap S)}{P(F)} = 15\%$$

From the problem we know the chance of rain on the first day, so

$$\frac{P(F\cap S)}{10\%} = 15\%$$

Multiplying by 10% on both sides, we get our answer:

$$P(F\cap S) = 1.5\%$$

The chance of two days in a row of rain is 1.5%, assuming there was no rain on the day before the first day.

Another important term is <b>expected value</b>. Expected value is the weighted average of the outcomes possible. For example, the expected value of a dice roll is 3.5. Even though 3.5 is not an actual option from a dice roll, it is the average off all the possible outcomes:

$$\frac{1+2+3+4+5+6}{6} = 3.5$$

Notice how we can rewrite that equation into the following:

$$\frac{1}{6}+\frac{2}{6}+\frac{3}{6}+\frac{4}{6}+\frac{5}{6}+\frac{6}{6} = 3.5$$

We know that the probability of each outcome is one-sixth. Because of this, we can write the the above equation into

$$\sum{}{}{i\cdot P(i)} = 3.5$$

This is actually the general formula for any sample space. For example, say a carnival game costs \\(3\\) to play and has the following outcomes:

|Probability|Outcome|
|--- |--- |
|50%|\\(0\\)|
|20%|\\(3\\)|
|10%|\\(5\\)|
|5%|\\(8\\)|
|5%|\\(10\\)|

What is the expected value of the outcome? We know each of the outcomes and their probabilities, so we can plug those numbers into the formula for expected value

$$\text{Expected value} = \sum{}{}{[i\cdot P(i)]} = 0.5\cdot0+0.2\cdot3+0.1\cdot5+.05\cdot8+.05\cdot10$$

# Calculus I

## Limits and Discontinuities

A <b>limit</b> is a fairly simple concept, but is the basis of all of calculus. As the input of a function approaches a certain value, the output of a function will approach some other value - this value is what the limit is.

For example, take the following graph of \\(x^2\\):

(graph) x^2

As the x-value approaches 2, the y-value of the function approaches 4. This means that the limit of the function as x approaches 2 approaches 4. Or, we can write it with math notation:

$$\lim_{x\to 2} x^2 = 4$$

Here, the notation is saying that in the function \\(x^2\\), as x approaches 2, the function's value will approach 4. This is an obvious result, because \\(2^2 = 4\\). However, this is not so obvious for other functions. Take the function \\(f(x) = \frac{1}{x^2}\\). What is the limit of this function as \\(x\\) approaches 0?

$$\lim_{x \to 0} \frac{1}{x^2} = ?$$

In the earlier problem, we could just plug in 2 to the limit to get our answer. Now, if we plug in 0 this doesn't work, because \\(\frac{1}{0^2}\\) is undefined. So, what's the answer? Well, let's look at the graph of \\(f(x) = \frac{1}{x^2}\\).

(graph) 1 over x^2

Notice how as the x-value approaches 0, \\(f(x)\\) approaches \\(\infty\\). Because of this, we can say that

$$\lim_{x \to 0} \frac{1}{x^2} = \infty$$

This doesn't seem right, because we aren't used to seeing \\(\infty\\) in equations. However, in the case of limits, it's fine, because we aren't saying \\(\frac{1}{0^2} = \infty\\), we are saying that the <i>limit</i> approaches \\(\infty\\). Or, in other words, as the x-value get's closer and closer to 0, \\(\frac{1}{x^2}\\) gets closer and closer to \\(\infty\\).

Let's now look at limits for functions that are discontinuous. There are three types of discontinuities. The first is a <b>removable discontinuity</b>. A removable discontinuity in any function \\(f(x)\\)is where the limit to a number \\(a\\) exists, but \\(f(a)\\) does not.

Let's see if we can find the following limit:

$$\lim_{x \to -5} \frac{2x^{2}+10x}{x^{2}-25}$$

Our first step should be to plug in \\(-5\\). However, after doing that, we get \\(\frac{0}{0}\\), which does not help us. We can take a look at this graph of \\(g(x) = \frac{2x^{2}+10x}{x^{2}-25}\\):

(graph) rationalfunction.png

The open circle at \\(x = -5\\) shows that \\(g(x)\\) does not actually exist at that point (because it is dividing by 0). However, we can see that when \\(x = -5\\), the y-value approaches \\(1\\). Thus,

$$\lim_{x \to 5} \frac{2x^{2}+10x}{x^{2}-25} = 1$$

That was a removable discontinuity, because despite \\(g(-5)\\) not existing, \\(\lim_{x \to 5} g(x)\\) does. If we don't have a graph for \\(g(x)\\), we can also use some algebra to get the same answer:

$$\begin{align*}
&\phantom{=} \lim_{x \to -5} \frac{2x^{2}+10x}{x^{2}-25} \\
&= \lim_{x \to -5} \frac{2x(x+5)}{(x+5)(x-5)} \\
&= \lim_{x \to -5} \frac{2x\cancel{(x+5)}}{\cancel{(x+5)}(x-5)} \\
&= \lim_{x \to -5} \frac{2x}{x-5} \\
&= \frac{2(-5)}{(-5)-5} \\
&= 1
\end{align*}$$

  

By factoring the numerator and denominator, we can <b>manipulate</b> the expression to get it into a form where we can just plug in the value x approaches without any issue. Manipulation is a rearrangement of certain expressions that does not change the actual value or function, but turns it into a form that is easier to work with. In the above scenario, we manipulated the expression by factoring and then canceling.

Let's look at another type of discontinuity - a <b>jump discontinuity</b>. A jump discontinuity is where the function seems to “jump” from one point to another. Take the following piecewise function:

$$h(x) =
\begin{cases}
(x-1)^2 & \text{if } x > 1\\
3x - 4 & \text{if } x \le 1
\end{cases}$$

On a graph, this looks like

(graph) jumpdiscontinuity.png

Let's see if we can find \\(\lim_{x \to 1} h(x)\\). The issue here is that from the left side of \\(x = 1\\), y approaches \\(-1\\). However, on the right side, y approaches \\(0\\). Because of the discrepancy in the two sides, although \\(h(1)\\) exists, we say that the limit as \\(x\\) approaches 1 \\(DNE\\). \\(DNE\\) stands for “does not exist”:

$$\lim_{x \to 1} h(x) = \text{DNE}$$

We can use some notation to describe the limit approaching from either the left or right side. We said earlier that in the above function \\(h(x)\\), the left side approached \\(-1\\) and the right side approached \\(0\\). We can differentiate these two cases with a small minus or plus sign below the limit:

$$\lim_{x \to 1^-} h(x) = -1 \\
\lim_{x \to 1^+} h(x) = 0$$

The minus sign means the limit as \\(x\\) approaches 1 from the negative (or left) side. The plus sign means the limit as \\(x\\) approaches 1 from the positive (or right) side. We can also use this notation to say

$$\text{If } \lim_{x \to a^-} f(x) \ne \lim_{x \to a^-} f(x) \text{, then } \lim_{x \to a} f(x) = \text{DNE}$$

where \\(a\\) is any number and \\(f\\) is any function.

Take a look at the following function:

$$i(x) =
\begin{cases}
2 & \text{if } x \ne 3\\
4 & \text{if } x = 3
\end{cases}
$$

The graph of \\(i(x)\\) is

(graph) piecewisefunction2

What's the limit as x approaches 3? Despite \\(i(3)\\) equalling 4, the correct answer is \\(2\\). This is because we aren't looking for \\(i(3)\\), we are looking for the value of \\(i(x)\\) as \\(x\\) gets closer and closer to \\(3\\). And as \\(x\\) gets closer to \\(3\\), \\(i(x)\\) gets closer and closer to \\(2\\).

The third type of discontinuity is an <b>essential discontinuity</b>. This is when one or both sides of a function at a point either goes to either positive or negative \\(\infty\\). Take the function \\(j(x) = \frac{1}{x+1}\\):

(graph) 1 over x+1

\\(j(x)\\) is discontinuous at \\(x=-1\\). What is \\(\lim_{x \to -1} j(x)\\)? We can see that \\(\lim_{x \to -1^-} j(x) = -\infty\\) and \\(\lim_{x \to -1^+} j(x) = \infty\\). Because those two values are not equal, \\(\lim_{x \to -1} j(x) = \text{DNE}\\).

Here's another example of an essential discontinuity:

$$
k(x) =
\begin{cases}
-\frac{1}{x^2} & \text{if } x \ne 0\\
0 & \text{if } x = 0
\end{cases}
$$

(graph) -1 over x^2

Both \\(\lim_{x \to 0^-}\\) and \\(\lim_{x \to 0^+}\\) equal \\(-\infty\\). Because of this, we can say that \\(\lim_{x \to 0} = -\infty\\). The fact that the \\(k(0) = 0\\) does not matter, because we are simply looking for the function value as \\(x\\) <i>approaches</i> 0, not when \\(x\\) equals 0.

## Limit properties

In the last chapter, we went over limits, what they are, and how to evaluate them using a graph. Now, let's go over how to solve them algebraically. There are a lot of certain properties to know that are useful in many situations.

Here is a list of all the important limit properties. In the following examples, \\(f(x)\\) and \\(g(x)\\) will be any function and \\(a\\) and \\(c\\) will be any number. Assume that \\(\lim_{x \to a} f(x)\\) exists (so no jump discontinuities).

|Name|Definition|Example|
|--- |:-: |--- |
|constant multiple law|\\(\displaystyle \lim\limits_{x \to a} [c \cdot f(x)] = c\cdot \lim\limits_{x \to a} f(x)\\) <br> \\(\text{only works for constants or variables}\\) <br> \\(\text{that are not dependent on the limit}\\)|\\(\lim\limits_{x \to 1} 5(x^2+2) = 5\lim\limits_{x \to 1} [x^2+2] = 15\\)|
|sum law|\\(\lim\limits_{x \to a} [f(x) \pm g(x)] = \lim\limits_{x \to a} f(x) \pm \lim\limits_{x \to a} g(x)\\)|\\(\lim\limits_{x \to 7} [x^2+x] = \lim\limits_{x \to 7} x^2 + \lim\limits_{x \to 7} x = 56\\)|
|product law|\\(\lim\limits_{x \to a} [f(x) \cdot g(x)] = \lim\limits_{x \to a} f(x) \cdot \lim\limits_{x \to a} g(x)\\)|\\(\lim\limits_{x \to 4} [x(2-x)] = \lim\limits_{x \to 4} x \cdot \lim\limits_{x \to 4} [2-x] = -8\\)|
|quotient law|\\(\displaystyle \lim\limits_{x \to a} \bigg[\frac{f(x)}{g(x)}\bigg] = \frac{\lim\limits_{x \to a} f(x)}{\lim\limits_{x \to a} g(x)}\\) \\(\text{assuming } g(x) \ne 0\\)|\\(\displaystyle \lim\limits_{x \to 1} \frac{x^2+5x}{3x^2-5} = \frac{\lim\limits_{x \to 1} [x^2+5x]}{\lim\limits_{x \to 1} [3x^2-5]}= -3\\)|
|exponent law|\\(\lim\limits_{x \to a} \big[(f(x))^c\big] = \Big[\lim\limits_{x \to a} f(x)\Big]^c\\)|\\(\lim\limits_{x \to 2} [(3x)^2] = \Big[\lim\limits_{x \to 2} 3x \Big]^2 = 36\\)|
|root law|\\(\lim\limits_{x \to a} \sqrt[\large c]{f(x)} = \sqrt[\large c]{\lim\limits_{x \to a} f(x)}\\)|\\(\lim\limits_{x \to 7} \sqrt{x+2} = \sqrt{\lim\limits_{x \to 7} [x+2]} = 3 \\)|
||\\(\lim_{x \to a}f(x) = f\Big(\lim_{x \to a}x\Big) \\ \text{as long as } f(x)\text{ is continuous around } a\\)|\\(\lim_{x \to 25}\sqrt{x} = \sqrt{\lim_{x \to 25}x} = 5\\)|


All of these properties work because of the fact that \\(\lim_{x \to a} f(x)\\) exists as just a number. This allows us to treat the limit as any other number and apply corresponding rules.

There are also some limits that are important to know because they come up very often. These include:

$$\lim_{x \to 0^- } \frac{c}{x} = -\infty$$

$$\lim_{x \to 0^+ } \frac{c}{x} = \infty$$

$$\lim_{x \to 0 } \frac{x}{c} = 0$$

$$\lim_{x \to \infty} \frac{c}{x} = 0$$

$$\lim_{x \to \infty} \frac{x}{c} = \infty$$

where \\(c>0\\). Use the constant multiple rule to figure out what happens if \\(c\\) is negative. All of these limits can be found either by looking at a graph, or by thinking about what happens to the expression as \\(x\\) approaches \\(0\\) or \\(\infty\\).

Whenever evaluating a limit of a continuous function algebraically, the first step should always be to plug in the number. This method is known as <b>direct substitution</b>.Most of the time, this will be enough to get you the right answer. In the next section, we'll go over when direct substitution won't work.

## Indeterminate Forms

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

## \\(e\\), the universal growth constant

\\(e\\) is an irrational number equal to about \\(2.718\\). It is an integral part of calculus, although it appears in far more fields. \\(e\\) represents the concept of continuous growth, and we will see how \\(e\\) can be derived and why it is so important.

Imagine a type of 2D goo that exists in an infinite 2D world. This special type of goo will grow and spread in a special way. To begin, let's define the intervals it will grow in. The goo below grows in intervals of 1 second with a growth rate of 100%. This means that every one second, the goo will grow by 100%:

(image)

Notice that at the end of 1 second, there are 2 units of goo present. This makes sense, because the goo grew by 100% after the first second. Now, let's imagine the same situation, but the goo grows in intervals of half a second instead. Every half second, the goo will grow by 50%:

(image)

Here, every 0.5 seconds, the amount of goo increases by 50%. After one second, the goo has gone through two iterations, and it's final amount is \\(2.25\\), because

$$\begin{align*}
1 & ~~ \text{ Amount after 0 iterations (0 sec)} \\
\underline{+ ~~ \text{50\% of 1}} & \\
1.5 & ~~ \text{ Amount after 1 iteration (0.5 sec)} \\
\underline{+ ~~ \text{50\% of 1.5}} & \\
2.25 & ~~ \text{ Amount after 2 iterations (1 sec)}
\end{align*}$$

Let's imagine another situation, where the goo grows in intervals of every one third of a second. Every one third of a second, the goo will grow by \\(33.\overline{3}\%\\):

(image)

At the end of the 1 second, our final amount of goo will be \\(2.\overline{370}\\):

$$\begin{align*}
1& ~~ \text{ Amount after 0 iterations (0 sec)}\\
\underline{+ ~~ \text{33.}\overline{3}\text{\% of 1}} &\\
1.\overline{33}& ~~ \text{ Amount after 1 iteration (0.}\overline{3}\text{ sec)} \\
\underline{+ ~~ \text{33.}\overline{3} \% \text{ of 1.}\overline{33}} &\\
1.\overline{77} & ~~ \text{ Amount after 2 iterations (0.}\overline{6}\text{ sec)} \\
\underline{+ ~~ \text{33.}\overline{3} \% \text{ of 1.}\overline{77}} &\\
2.\overline{370} & ~~ \text{ Amount after 3 iterations (1 sec)}
\end{align*}$$

So, how does this tie into \\(e\\)? Well, \\(e\\) is the amount of goo we have after 1 second when there are an infinite number of intervals between 0 seconds and 1 second. In the examples above, we had the number of intervals be \\(1\\), \\(2\\), and then \\(3\\). To get a nice closed form for \\(e\\), let's figure out the pattern.

The amount of goo always started at \\(1\\). Whenever we had \\(n\\) number of intervals, the goo increased by \\(\frac{100}{n}\%\\) every \\(\frac{1}{n}\\) seconds. For example, when we had three intervals, the amount of goo increased by \\(\frac{100}{3}\% = 33.\overline{3}\%\\) every \\(\frac{1}{3}\\) seconds.

$$\underbrace{1}_{\substack{\text{starting} \\ \text{value}}}\cdot \underbrace{\left(1+\frac{100}{3}\%\right)}_{\text{1st iteration}}\cdot\underbrace{\left(1+\frac{100}{3}\%\right)}_{\text{2nd iteration}}\cdot\underbrace{\left(1+\frac{100}{3}\%\right)}_{\text{3rd iteration}} = 2.\overline{370}$$

Because the \\(1\\) at the front doesn't really matter (anything multiplied by \\(1\\) is itself), we can just pretend like it isn't there. Now we have

$$\underbrace{\left(1+\frac{100}{3}\%\right)}_ {\text{1st iteration}}\cdot\underbrace{\left(1+\frac{100}{3}\%\right)}_{\text{2nd iteration}}\cdot\underbrace{\left(1+\frac{100}{3}\%\right)}_{\text{3rd iteration}}$$

Notice how we have repeated multiplication here. More specifically, we multiply the \\(1+\frac{100}{3}\%\\) term by itself \\(3\\) times. Because repeated multiplication is just exponentiation, we can replace that entire expression with

$$\left(1+\frac{100}{3}\%\right)^{\displaystyle 3}$$

This is just the case for \\(3\\) intervals though. If we have a general case of \\(n\\) intervals, our expression would be

$$\left(1+\frac{100}{n}\%\right)^{\displaystyle n}$$

  

Remember, we want to find \\(e\\), which takes \\(\infty\\) intervals. Now that we know the concept of a limit, let's use that to find the definition for \\(e\\) by just taking the number of intervals, or \\(n\\) to infinity.

  

$$e = \lim_{x \to \infty}\left(1+\frac{100}{n}\%\right)^{\displaystyle n}$$

  

Because \\(100\% = 1\\), we can make this look a little cleaner:

  

$$e = \lim_{x \to \infty}\left(1+\frac{1}{n}\right)^{\displaystyle n}$$

  

This is the definition of \\(e\\). The equation \\(e^x\\) is also very important, because if the goo grows the same way for, then \\(e^x\\) represents the amount of goo after \\(x\\) seconds. Note that

  

$$e^x = \lim_{n \to \infty}\left(1+\frac{x}{n}\right)^n$$

  

We can prove this: If \\(e = \lim_{x \to \infty}\left(1+\frac{1}{n}\right)^{n}\\), then

  

$$\begin{align*}
e^x &= \left[\lim_{n \to \infty}\left(1+\frac{1}{n}\right)^n\right]^x\\
&=\lim_{n \to \infty} \left[\left(1+\frac{1}{n}\right)^{n^x}\right]\\
&=\lim_{n \to \infty} \left(1+\frac{1}{n}\right)^{nx}\\
\end{align*}$$

  

We can let \\(u=nx\\). This means that \\(\frac{1}{n} = \frac{x}{u}\\) and as \\(n \to \infty\\), \\(u \to \infty\\) as well. Performing these substitutions, we have

  

$$\begin{align*}
e^x &= \left[\lim_{n \to \infty}\left(1+\frac{1}{n}\right)^n\right]^x\\
&=\lim_{n \to \infty} \left[\left(1+\frac{1}{n}\right)^{n^x}\right]\\
&=\lim_{n \to \infty} \left(1+\frac{1}{n}\right)^{nx}\\
&=\lim_{u \to \infty} \left(1+\frac{x}{u}\right)^u
\end{align*}$$

  

We have proven that \\(e^x = \lim_{n \to \infty} \left(1+\frac{x}{n}\right)^n\\). Later on, we'll see how \\(e^x\\) is arguably the most important equation in calculus.

  

Because \\(e^x\\) is so important, it's useful to have an equation that represents the inverse of \\(e^x\\). In precalculus, we covered how logarithms are the inverse of exponentials. Recall that \\(\log_b(x)\\) is the inverse of \\(b^x\\). In other words, \\(log_b(b^x) = x\\) and \\(b^{\log_b{x}} = x\\). Thus, the inverse of \\(e^x\\) is \\(\log_e(x)\\). Here is a graph of \\(e^x\\) and \\(\log_e(x)\\) - notice how they are the same graph, but flipped about \\(y=x\\).

  

(graph) e^x and lnx

  

Because \\(\log_e(x)\\) is such an important function, mathematicians decided to give it its own name, \\(\ln(x)\\). This is known as the <b>natural log</b>:

  

$$\ln(x) = \log_e(x)\\
e^{\ln(x)} = x\\
\ln(e^x) = x$$

  

## Derivatives

In algebra, we learned what the slope of a linear function was. To review, the slope of a linear equation was the increase in y units for every 1 unit increase on the x-axis. For example, take a look at the following graph of \\(y = \frac{3}{2}x -1\\):

  

(graph) 3x over 2 - 1

  

Because the line goes up 1.5 units for every 1 unit it goes to the right, we can say that the slope of this line is equal to 1.5. However, this will not work for other functions.

  

For example, look at the function \\(a(x)\\) below:

  

(graph), a(x)

  

Because this function is curved, it doesn't have a single slope. Instead, the slope of the curve varies at different x-values. To show this, we can look at lines <b>tangent</b> to the curve at various points:

  

(graph), a(x) tangent lines

  

A tangent line is the line with the same slope at a point on a curve. In this case, because the slope of the tangent changes as \\(x\\) changes, we know that there is not one constant slope for the entire curve. This is in contrast to a linear equation, where there would just be one tangent line, and therefore one slope for the entire line.

  

Let's see we wanted to make another function, \\(b(x)\\), that describes the slope of \\(a(x)\\) for various values of \\(x\\). \\(b(x)\\) would look something like this:

  

(graph), b(x)

  

Why is it like this? Well, \\(b(x)\\) is dependent on the slope of the tangent line to \\(a(x)\\) at \\(x\\). Notice that for every x-value, the slope of the tangent line to \\(a(x)\\) is equal to \\(b(x)\\). Or, shown visually:

  

(image), gif

  

We call \\(b(x)\\) the <b>derivative</b> of \\(a(x)\\). The derivative of a function is another function, whose values are the slopes of the respective tangent lines of \\(a(x)\\). Let's try to figure out how to construct the derivative of any function \\(f(x)\\).

  

We know that the derivative of a function will be another function in terms of \\(x\\). Thus, we are looking for some operation on a function \\(f(x)\\) (\\(f(x)\\) represents any function in terms of \\(x\\)). Let's take advantage of the slope formula we learned in algebra. The slope formula is

  

$$\text{slope of a linear function} = \frac{y_2-y_1}{x_2-x_1}$$

  

where \\((x_1, y_1)\\) and \\((x_2, y_2)\\) are coordinates on the line. At first glance, this doesn't look that useful, because that equation only works for linear functions and we are trying to find the derivative of a curve. But, this is still useful. Look at the following animation:

  

(image), gif

  

This animation shows how we can approximate any function using just lines. Now that we can construct any function with just lines, we can use the slope formula repeatedly. The more lines we use to approximate a curve, the more accurate the approximation will be. Or, written in another way, the smaller the x distance between lines, the closer the approximation will be to the true function.

  

To see this visually, let's zoom in on a very small part of this function. Let \\(h\\) be the x-distance between lines:

  

(image)

  

Notice how the ????? line is a good approximation of the curve between points ?????? and ?????, and decreasing the value of \\(h\\) will make that approximation more accurate.

  

Or, to write this algebraically,

  

$$\text{slope of a curve at } x \approx \frac{f(x+h)-f(x)}{(x+h)-(x)}$$

  

This is only an approximation. To make this exactly equal, we can use a limit:

  

$$\text{slope of a curve at } x = \lim_{h \to 0} \frac{f(x+h)-f(x)}{(x+h)-(x)}$$

  

Because the derivative is simply the slope of a curve at every \\(x\\) value, we can generalize this further to cover all \\(x\\) values:

  

$$\text{The derivative of a function } f(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{(x+h)-(x)}$$

  

Which can be simplified to

  

$$\text{The derivative of a function } f(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}$$

  

This is the definition of the derivative. Let's look at an example. Say we want to find the derivative of function \\(g(x)=???????\\). Plugging into the definition of derivative, we have:

  

(example)

  

Thus, the derivative of ?????? is ???????. Overlaying these two functions on a graph, we see

  

(graph)

  

This graph makes sense. For example, at \\(x=?????\\), the slope of \\(???????\\) seems negative. Indeed, at \\(x=?????\\), \\(???????\\) has a negative value. Or, at \\(x=??????\\) the slope of \\(???????\\) seems about 0. And at \\(x=?????\\), \\(???????\\) is 0. This works for all \\(x\\) values.

  

Let's talk about notation. One way of writing “the derivative of \\(a(x)\\)” in shorthand notation is by using something called <b>Lagrange notation</b> (or prime notation). Lagrange notation involves drawing an apostrophe between the \\(f\\) and \\((x)\\) in a function:

  

$$\text{Derivative of function } f(x) = f'(x)$$

  

For example, when we found that the derivative of \\(???????\\) = \\(?????\\), we could say:

  

$$
f(x) = ??????? \\
f'(x) = ??????
$$

  

Another type of notation is using <b>Leibniz notation</b>. Leibniz notation is written as a fraction, with \\(d\\) in the numerator and \\(dx\\) in the denominator.

  

$$\frac{d}{dx} f(x) = f'(x) = \text{The derivative of f(x)}$$

  

There is a nice intuition for this type of notation. Remember when we used a line to approximate a curve? Let's zoom into that again. However, we will label the lines something different:

  

(image)

  

The \\(dx\\) and \\(dy\\) stands for the change in \\(x\\) and \\(y\\) between points \\(????\\) and \\(????\\) The idea here is that the slope is equal to \\(\frac{dy}{dx}\\), and because \\(y=f(x)\\), by saying \\(\frac{df(x)}{dx}\\) we are basically saying “the slope of the function f(x)”, which is a good loose definition of the derivative. Assuming \\(y=f(x)\\), all of these are equal:

  

$$\text{Assuming } y = f(x) \text{,} \\
\text{The derivative of } f(x) = f'(x) = y' = \frac{df(x)}{dx} = \frac{d}{dx}f(x) = \frac{dy}{dx}$$

## Derivative Rules

In the last chapter, we learned what a derivative was and how to calculate one using the definition of the derivative. However, using the definition of the derivative to calculate derivatives is incredibly hard, even with functions that aren't that complicated. This is because the definition of the derivative involves many terms, a fraction, and a limit. To make <b>differentiating</b> (to differentiate means to take the derivative of) functions easier, mathematicians use several rules.

  

The first rule we will learn is the <b>constant term rule</b>. This says that the derivative of a constant is 0. Remember that a constant is just a number (i.e., no \\(x\\) inside the function). Or, written mathematically,

  

$$\frac{d}{dx} [c] = 0 \text{where } c \text{ is a constant}$$

  

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
\frac{d}{dx}[f(x)\cdot(g(x)]= f(x)g'(x)+g(x)f'(x)
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

## Derivatives of Certain Functions

Let's now go over the derivatives of some common functions that you'll see often.

First, let's go over the derivatives of trigonometric functions. The basis of all of these derivatives will be the derivative of \\(\sin(x)\\), so we will cover that one first. Because \\(\sin(x)\\) is its own function that isn't based on any other, there's no rule that we can use. Let's use the definition of the derivative instead. 

$$
\lim_{h \to 0} \frac{\sin(x+h)-\sin(x)}{h} \\
$$

We can use the addition formula for sine to expand the \\(\sin(x+h)\\).

$$
\lim_{h \to 0} \frac{\sin(x)\cos(h)+\cos(x)\sin(h)-\sin(x)}{h} \\
\lim_{h \to 0} \bigg[\frac{\sin(x)\cos(h) -\sin(x)}{h}+\frac{\cos(x)\sin(h)}{h}\bigg] \\
\lim_{h \to 0} \bigg[\frac{\sin(x)\cos(h) -\sin(x)}{h}\bigg]+\lim_{x \to 0}\bigg[\frac{\cos(x)\sin(h)}{h}\bigg] \\
\lim_{h \to 0} \bigg[\frac{\sin(x)(\cos(h) -1)}{h}\bigg]+\lim_{x \to 0}\bigg[\frac{\cos(x)\sin(h)}{h}\bigg]
$$

Because \\(\sin(x)\\) and \\(\cos(x)\\) are not dependent on the first and second limit, we can pull them outside.

$$
\sin(x) \lim_{h \to 0} \bigg[\frac{\cos(h) -1}{h}\bigg]+ \cos(x) \lim_{x \to 0}\bigg[\frac{\sin(h)}{h}\bigg]
$$

Now, we just have to figure out the first and second limit. Unfortunately, plugging \\(h=0\\) into both of the limits gets us \\(\frac{0}{0}\\). Let's graph \\(y=\frac{cos(x)-1}{x}\\) and \\(y=\frac{sin(x)}{x}\\):

(graph), sinx over x and cosx - 1 over x

We can see that as \\(x\\) approaches 0, \\(\frac{cos(x)-1}{x}\\) approaches 0 and \\(\frac{sin(x)}{x}\\) approaches 1.

$$
\sin(x) \lim_{h \to 0} \underbrace{\bigg[\frac{\cos(h) -1}{h}\bigg]}_ {=0}+ \cos(x) \underbrace{\lim_{x \to 0}\bigg[\frac{\sin(h)}{h}\bigg]}_ {=1} = \cos (x)$$

We have shown that the derivative of \\(\sin(x)\\) is \\(\cos(x)\\). From that, we can also prove the derivative of cosine. We only need to know the following identities that relate sine to cosine:
 
$$\sin(x+\frac{\pi}{2}) = \cos(x) \\[0.5em]
\cos(x+\frac{\pi}{2}) = -\sin(x)$$

These can be proved using the sine and cosine addition formulas. To find \\(\frac{d}{dx} \cos(x)\\), let's rewrite \\(\cos(x)\\) as \\(\sin(x+\frac{\pi}{2})\\) and use chain rule. Keep in mind that we know the derivative of \\(\sin(x)\\) is \\(\cos(x)\\).

$$
\begin{align*}
\frac{d}{dx} \cos(x) &= \frac{d}{dx} \sin(x+\frac{\pi}{2}) \\
&= \cos(x+\frac{\pi}{2}) \cdot \frac{d}{dx} \bigg[x+\frac{\pi}{2} \bigg]
&= \cos(x+\frac{\pi}{2})
\end{align*}
$$

Which, we know from the identity above, is equal to \\(-\sin(x)\\). Thus,

\\(\frac{d}{dx} \cos(x) = -\sin(x)\\)

Now that we know the derivatives of sine and cosine, we can find the derivative of tangent:

$$
\frac{d}{dx} \tan(x) = \frac{d}{dx}\frac{\sin(x)}{\cos(x)} \\
$$

  

because \\(\tan(x) = \left(\frac{\sin(x)}{\cos(x)}\right)\\). From the quotient rule:

$$
= \frac{\cos(x)\cos(x)+\sin(x)\sin(x)}{\cos^2(x)} \\
= \frac{\cos^2(x)+\sin^2(x)}{\cos^2(x)} \\
$$

Using the pythagorean identity, we can simplify the numerator, and find our final answer:

$$
= \frac{1}{\cos^2(x)} \\
= \sec^2(x)
$$

Because \\(\csc(x)\\), \\(\sec(x)\\), and \\(\cot(x)\\) are all equal to reciprocals of other trigonometric functions, we can just use quotient rule for all of them.

$$
\begin{align*}
\frac{d}{dx} \csc(x) &= \frac{d}{dx} \frac{1}{\sin(x)}\\
&=\frac{\sin(x)(0)-(1)\cos(x)}{\sin^2(x)} \\
&=-\cot(x)\csc(x)
\end{align*}
$$
  
$$
\begin{align*}
\frac{d}{dx} \sec(x) &= \frac{d}{dx} \frac{1}{\cos(x)}\\
&=\frac{\cos(x)(0)-1(-\sin(x))}{\cos^2(x)} \\
&=\sec(x)\tan(x)
\end{align*}
$$

$$
\begin{align*}
\frac{d}{dx} \cot(x) &= \frac{d}{dx} \frac{\cos(x)}{\sin(x)}\\
&=\frac{\sin(x)\cdot-\sin(x)-\cos(x)\cdot\cos(x)}{\sin^2(x)} \\
&=\frac{-\sin^2(x)-\cos^2(x)}{\sin^2(x)}\\
&=\frac{-1(\sin^2(x)+\cos^2(x))}{\sin^2(x)}\\
&=\frac{-1(\sin^2(x)+\cos^2(x))}{\sin^2(x)}\\
&=-\csc(x)
\end{align*}
$$

Now, let's go over the derivative of \\(\ln(x)\\). Remember that \\(\ln(x)\\) is the logarithm with base \\(e\\). Because we don't have an easy formula or rule for this, let's use the definition of the derivative:

$$
\begin{align*}
\frac{d}{dx} \ln(x) &= \lim_{h \to 0} \frac{\ln(x+h)-\ln(x)}{h} \\
\end{align*}
$$

Using logarithm properties, we can combine the \\(\ln\\)s in the numerator:

$$
\begin{align*}
&=\lim_{h \to 0} \frac{\ln(\frac{x+h}{x})}{h} \\
&=\lim_{h \to 0} \frac{1}{h}\ln(1+\frac{h}{x})\\
\end{align*}
$$

Using another logarithm property:

$$
=\lim_{h \to 0} \ln\Bigg(\bigg(1+\frac{h}{x}\bigg)^{\frac{1}{h}}\Bigg)\\
$$

Now, we can see that this is fairly close to the definition of \\(e\\), which says that \\(e^x = \lim_{n \to \infty} \bigg(1+\frac{x}{n}\bigg)^n\\). However, one key difference is that in the definition of \\(e\\), the limit goes to \\(\infty\\). To make this more similar, let's make a substitution where \\(u = \frac{1}{h}\\):

$$
\begin{align*}
&=\lim_{u \to \infty} \ln\Bigg(\bigg(1+\frac{1}{xu}\bigg)^{u}\Bigg)\\
&=\lim_{u \to \infty} \ln\Bigg(\bigg(1+\frac{\frac{1}{x}}{u}\bigg)^{u}\Bigg)\\
\end{align*}
$$

Now, we can use the definition of \\(e\\).

$$
\begin{align*}
&=\ln(e^\frac{1}{x})\\
&=\frac{1}{x}
\end{align*}
$$

The derivative of \\(\ln(x)\\) is\\(\frac{1}{x}\\).

The final fact to know is an important one: \\(\frac{d}{dx} e^x = e^x\\). In other words, the derivative of \\(e^x\\) is itself. This is incredibly rare - in fact, \\(ce^x\\) (where \\(c\\) is a constant) are the only functions (besides \\(y=0\\)) whose derivative is itself. This is why \\(e^x\\) is so incredibly important to calculus.

Here is a table of all of these derivatives:

(table)

## L'Hôpital's Rule

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

## Implicit Differentiation

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

## Antiderivatives

We've gone over what the derivative of a function actually means - the rate of change of the function at a given \\(x\\) value. We've also gone over how to find the derivative of a function using certain rules. Now, let's go over another type of problem - finding a function based on its derivative.

For example, what function \\(a(x)\\) makes the following equation true?

$$\frac{d}{dx} a(x) = 2x$$

In other words, what function's derivative is \\(2x\\)? Well, because of the power rule, \\(f(x) = x^2\\). What we have just found is an <b>antiderivative</b> - the inverse operation of a derivative. In other words, the antiderivative of the derivative of a function is equal to the function itself. The antiderivative of \\(2x\\) is \\(x^2\\) because the derivative of \\(x^2\\) is \\(2x\\). Note that this is not quite the full answer; continue reading to see why the real answer is slightly different.

We symbolize the antiderivative of a function f(x) with the following notation:

$$\int f(x)\,dx$$

There are three parts to the notation of the antiderivative. The first is the \\(\int\\) symbol at the far left. This is supposed to represent an outstretched “S” (this “s” stands for <i>sum</i> - we'll talk about why later). The second part is the \\(dx\\) at the far right. In a sense, we are multiplying \\(f(x)\\) with \\(dx\\). You should recognize this symbol from the denominator of the derivative symbol. Why does the \\(dx\\) symbol appear here? Recall that we divide by \\(dx\\) when taking a derivative. Because the antiderivative is the inverse operation of a derivative, it makes sense we multiply by \\(dx\\), because multiplication is the inverse operation of the derivative. The third and final part is the \\(f(x)\\). This is the actual function we are finding the antiderivative of. This is enclosed between the \\(\int\\) and the \\(dx\\). Much like how a left parentheses cannot be written without a right parentheses, a \\(\int\\) cannot be written without a \\(dx\\).

Let's try to see if we can find the antiderivative of some functions. Let's go back to the \\(2x\\) example. Earlier, we said that the antiderivative of \\(2x\\), or \\(\int 2x\,dx\\), was \\(x^2\\). While it's true that \\(\frac{d}{dx} x^2 = 2x\\), the following are true as well:

$$\frac{d}{dx}x^2=2x\\
\frac{d}{dx}[x^2+1]=2x\\
\frac{d}{dx}[x^2-40]=2x\\
\frac{d}{dx}\left[x^2+\frac{\pi}{4}\right]=2x$$

The reason all of the above are true is because the derivative of any constant is just 0. Because of this, there are actually an infinite number of functions whose derivative is \\(2x\\). However, all of them can be written as

$$x^2+c$$

where \\(c\\) is a constant. This constant is known as the <b>constant of integration</b> (usually represented by \\(c\\). Thus, the actual antiderivative if \\(2x\\) is \\(x^2+c\\). Or, in mathematical terms,

$$\int2x\,dx = x^2+c$$

The reason the constant of integration is needed can be visualized on a graph. Here, we can see the graphs of \\(2x\\), as well as \\(x^2+c\\) with multiple values of \\(c\\).

(graph) x^2+c

Let's find the antiderivatives of some other functions. To start off, what is the antiderivative of \\(\cos(x)\\)? Remember the derivatives of trig functions. The derivative of \\(\sin(x)\\) is \\(\cos(x)\\), so the antiderivative of \\(\cos(x)\\) is \\(\sin(x)+c\\):

$$\int\cos(x)\,dx=\sin(x)+c$$

What is the antiderivative of \\(3x^2+5x^4\\)? Remember that in general, \\(\frac{d}{dx} x^n = nx^{n-1}\\) by the power rule. Knowing that,

$$\int3x^2+5x^4\,dx=x^3+x^5+c$$

because \\(\frac{d}{dx} x^3+x^5+c = 3x^2+5x^4\\).

## Antidifferentiation Rules and Methods

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

## The Limit Definition of an Integral

Finding the area under a linear function is fairly easy. For example, take a look at the following graph of \\(y=-\frac{1}{2}x+4\\):

(graph), -1 over 2 + 4

What is the area underneath the line and between the x-axis, \\(x=2\\), and \\(x=4\\)? Here is that region shaded:

(image)

The area of the shaded region is composed solely of a triangle and rectangle, meaning we can just add the areas for those shapes to find the total area. In this case, \\((2)(2)+\frac{1}{2}(2)(1)=5\\). However, this is not as easy for curves. For example, here is the graph of \\(f(x) = -\frac{1}{8}x^{2}+3\\) with the same region shaded:

(image)

Finding the area of this is considerably harder. Notice that this is similar to the problem we were facing when trying to calculate the slope of a curve - we could find the slope of a linear equation easily, but finding the slope of a curve was considerably harder. Eventually, we were able to formalize that concept to the derivative by using approximations and limits. Here, we will do the same.

To start approximating this value, let's start by identifying a shape that we <i>do</i> know how to find the area of. The easiest shape of those is probably the rectangle, because all we have to do is multiply the width times the height. Let's cover the shaded region with some rectangles:

(image)

Here, we covered the area with two rectangles, each with width \\(1\\). This doesn't solve our problem, because the area covered by the rectangles is a little less than the shaded regions. We can make this approximation slightly better though by increasing the number of rectangles. Here, we have four rectangles, each with width \\(0.5\\):

(image)

The more rectangles we have, the better the approximation will be. This can be visualized by the following gif, where the difference between the total area of the rectangles and the area under the curve is shaded in red. Notice how the difference decreases, meaning the total area in the rectangles gets closer and closer to matching the area under the curve.

(image), gif

To formalize this problem, let's add some variables. Let \\(A\\) be the <i>actual</i> area under the curve, and let \\(n\\) be the number of rectangles. Let \\(a\\) and \\(b\\) be the starting and ending x values of the area we're trying to find (in this case, \\(2\\) and \\(4\\)). Knowing that, we can calculate the width of each rectangle, \\(dx\\), to be \\(\frac{b-a}{n}\\).

(image)

The reason we call the width of a rectangle \\(dx\\) is for a similar reason we have \\(dx\\) in the denominator of the derivative symbol:

(image)

\\(dx\\) is supposed to represent a tiny nudge in the x direction, and we want the widths of each rectangle to be as tiny as possible so that the approximation is as accurate as possible.

Now that we have all those variables, we can formalize this by turning it into a formula:

$$\text{Area under curve} \approx (\text{Area of Rectangle 1})+(\text{Area of Rectangle 2})+(\text{Area of Rectangle 3})+\cdots$$

We assigned the area under the curve to be \\(A\\). To find the area of each rectangle, we should multiply each rectangle's width by each rectangle's height. The width of every rectangle is \\(dx\\), but the height varies. More specifically, the height of each rectangle is dependent on the <i>function's value</i> at the x-value where the rectangle touches the function:

(image)

The first rectangle comes into contact with \\(f(x)\\) at \\(x=2.5\\), the second rectangle comes into contact with \\(f(x)\\) at \\(x=3\\), the third rectangle comes into contact with \\(f(x)\\) at \\(x=3.5\\), and so on. This is because the width of each rectangle (or \\(dx\\)) is \\(0.5\\). In general, the height for the \\(i^{\text{th}}\\) rectangle is \\(f(a + i\cdot dx)\\).

Now that we know that the height of the \\(i^{th}\\) rectangle is \\(f(i\cdot dx)\\) and the width of each rectangle is \\(dx\\), we can finally find the true area underneath the curve. Recalling that \\(n\\) is the number of rectangles and \\(dx\\) = \\(\frac{b-1}{n}\\),

$$\begin{array}{r c c l}
\text{Area under curve} &\approx& & (\text{Area of Rectangle 1})\\
& &+& (\text{Area of Rectangle 2})\\
& &+& (\text{Area of Rectangle 3})\\
& &+& (\text{Area of Rectangle 4})\\
& &\vdots& \\
& &+& (\text{Area of Rectangle } n)\\
\end{array}$$

$$\begin{array}{r c c l}
\text{Area under curve} &\approx& & f(2+1\cdot dx)\cdot dx\\
& &+& f(2+2\cdot dx)\cdot dx\\
& &+& f(2+3\cdot dx)\cdot dx\\
& &+& f(2+4\cdot dx)\cdot dx\\
& &\vdots& \\
& &+& f(2+n\cdot dx)\cdot dx\\
\end{array}$$

There's a clear pattern in the addition here. The only thing that changes from term to term is the number that is being multiplied to \\(dx\\). We can use summation notation to simplify this formula:

$$A \approx \sum_{i=1}^{n} [f(2+i \cdot dx) \cdot dx]$$

Remember earlier that we said that as \\(n\\) gets bigger, the approximation gets more and more accurate. If we had an infinite number of rectangles, the approximation would be exactly perfect. Thus,

$$A = \lim_{n \to \infty} \sum_{i=1}^{n} [f(2+i \cdot dx) \cdot dx]$$

Remember that \\(2\\) was just the starting x-coordinate of the area we were trying to find. We assigned the starting x-coordinate to \\(a\\), so we will use that variable instead. We have found the formula for the area under a curve:

$$A = \lim_{n \to \infty} \sum_{i=1}^{n} f(a+i\cdot dx) dx\\\text{where } n \text{ is the number of rectangles}\\a \text{ is the leftmost point for the area}\\b \text{ is the rightmost point for the area}\\\text{and }dx =\frac{b-a}{n}$$

(image)

The area underneath a curve is known as an <b>integral</b>. This name comes from constructing the area from rectangles and bringing the rectangles closer - or integrating them together - to find the true area. For example, let's say we wanted to find the integral of \\(x^2\\) between \\(x=1\\) and \\(x=4\\), If we know \\(a=1\\) and \\(b=4\\), then \\(dx = \frac{4-1}{n} = \frac{3}{n}\\)

$$A = \lim_{n \to \infty} \sum_{i=1}^{n} f(a+i\,dx) dx \\
A = \lim_{n \to \infty} \sum_{i=1}^{n} \left[\left(1+i\left(\frac{3}{n}\right)\right)^{\displaystyle2} \left(\frac{3}{n}\right)\right]$$

Here is a visual of the above integral:

(image), gif

Actually solving the integral to find the area is very difficult using limits and sums, but in the next chapter, we'll go over a <i>much</i> easier way.

## Integration

Now that we have an understanding of both antiderivatives and integrals, we can explore the connection between them. By the end of this chapter, we'll see see how the area under a curve can simply