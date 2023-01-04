---
title: Solving Equations with Trigonometry
layout: page
menuInclude: yes
menuLink: yes
menuTopTitle: Precalculus
menuSubs:
- title: Solving Equations with Trigonometry
  index: 3
excerpt: "How to solve equations involving trigonometric functions."
questions:
  - ['Solve for \(x\):\(\,\,\) \(2\cos(x)=-\sqrt3\)', '\(\cos(x)=\frac{-\sqrt3}{2}\\x=\frac{\pi}{6}+2\pi n,x=\frac{5\pi}{6}+2\pi n\)']
  - ['Solve for \(x\):\(\,\,\) \(\sin^2(x)+2=3\)', '\(\sin^2(x)=1\\\sin(x)=\pm 1\\x=\frac{\pi}{2}+\pi n\)']
---


<h1>Precalculus</h1>

<h2>Solving Equations with Trigonometry</h2><br>


Using algebra to solve equations is a fairly straightforward process most of the time if the operations are simple. However, it's a lot harder for equations with trigonometric functions inside of them. Let's find out how to solve those types of problems.

Let's start with the unit circle. In the last chapter we talked about the unit circle and how it relates to sine and cosine. Remember that the unit circle is the circle centered at (0, 0) with a radius of 1. We related it to trigonometric functions by drawing right triangles inside it, and discovered that \\(\sin(\theta)\\) is equal to the height of the right triangle that has a vertex on the origin and a hypotenuse of length 1.

<img src="../../visuals/unitcircleinstance.png" style="width:50%;height:auto;display:block;margin:auto;">

Using this knowledge, we can figure out the value of \\(\sin(\theta)\\) for select values of \\(\theta\\). Let's try to find \\(\sin(\theta)\\) for values of \\(\theta = \frac{\pi}{3}, \frac{\pi}{4}\\), and \\(\frac{\pi}{6}\\). First, let's try to find \\(\sin(\frac{\pi}{6})\\), or \\(\sin(30^{\circ})\\). This is the corresponding diagram:

<img src="../../visuals/unitcircleinstance30.png" style="width:50%;height:auto;display:block;margin:auto;">

Our triangle has a 30 degree angle, 60 degree angle, and 90 degree angle. Notice how we can reflect the triangle over the x-axis to get a triangle whose angles are all equal to 60 degrees. This means that the triangle is equilateral, and so all sides are the same length:

<img src="../../visuals/unitcircle30step1.png" style="width:50%;height:auto;display:block;margin:auto;">

If all sides are the same length, and side \\(H\\) has a length of 1, then that must mean that \\(2\cdot\sin(\frac{\pi}{6}) = 1\\), and therefore \\(\sin(30^{\circ}) = 0.5\\). Using Pythagorean's Theorem, we can find the length of the final side of the triangle, side \\(A\\): \\(A^2+(0.5)^2 = 1^2\\), so \\(A\\) must equal \\(\frac{\sqrt{3}}{2}\\). Because \\(A = \cos(\theta)\\), \\(\cos(\theta) = \frac{\sqrt{3}}{2}\\). This gives us a triangle for \\(\theta = \frac{\pi}{3}\\):

<img src="../../visuals/unitcircle30complete.png" style="width:50%;height:auto;display:block;margin:auto;">

We have successfully found the values of \\(\sin(\frac{\pi}{3})\\) and \\(\cos(\frac{\pi}{3})\\). Because taking \\(\theta=\frac{\pi}{3}\\) also gives us a 30-60-90 triangle, we can use the same method to find the values of \\(\sin(\frac{\pi}{3})\\) and \\(\cos(\frac{\pi}{3})\\).

Finding the value of \\(\sin(\frac{\pi}{4})\\) and \\(\cos(\frac{\pi}{4})\\) is a lot easier. Let's draw a triangle for \\(\theta=\frac{\pi}{4}\\), or \\(\theta=45^{\circ}\\):

<img src="../../visuals/unitcircle45instance.png" style="width:50%;height:auto;display:block;margin:auto;">

Because we have a 45-45-90 triangle, we know that it must be isosceles because two of the angles are the same. By the definition of an isosceles triangle, \\(\sin(\theta) = \cos(\theta)\\). Using Pythagorean's theorem we know \\(2\sin^2(\theta) = 1\\), so \\(\sin(\theta) = \frac{1}{\sqrt2}\\). Multiply both the numerator and denominator by \\(\sqrt2\\) to find \\(\sin(\frac{\pi}{4}) = \cos(\frac{\pi}{4}) = \frac{\sqrt2}{2}\\).

Now that we have values for those three values, we can fill in the following table for various values of \\(\theta\\):

|\\(\theta\\)|\\(\sin(\theta)\\)|\\(\cos(\theta)\\)|
|:-:|:-:|:-:|
|\\(0\\)|\\(0\\)|\\(1\\)|
|\\(\pi/6\\)|\\(\sqrt3/2\\)|\\(1/2\\)|
|\\(\pi/4\\)|\\(\sqrt2/2\\)|\\(\sqrt2/2\\)|
|\\(\pi/3\\)|\\(1/2\\)|\\(\sqrt3/2\\)|
|\\(\pi/2\\)|\\(1\\)|\\(0\\)|

Because \\(\sin(\theta)\\) is directly equal to the y-value and \\(\cos(\theta)\\) is directly equal to the x-value, we can also produce the following graph:

(unit circle graph)

Now that we know the unit circle, we can solve an equation like this:

$$\cos(\theta) = \frac{1}{2}$$

Take a look at our unit circle. We're looking for values of \\(\theta\\) where the x-value is equal to \\(\frac{1}{2}\\) (because cosine is represented by the x-value). Looking at our unit circle, we can see that those x-values appears when \\(\theta\\) equals \\(\frac{\pi}{3}\\) and \\(\frac{5\pi}{3}\\). However, remember that \\(\cos(\theta)\\) has a period of \\(2\pi\\) - this means that values for cosine will repeat every \\(2\pi\\) units, so the actual answer is:

$$\theta = \frac{\pi}{3} + 2\pi k, \theta = \frac{5\pi}{3} + 2\pi k$$

where \\(k\\) is any integer. We can visually see this on a graph:

<img src="../../visuals/unitcircle.png" style="width:50%;height:auto;display:block;margin:auto;">
<center><caption>Credit to <a href="https://commons.wikimedia.org/wiki/File:Unit_circle_angles.svg">Gustavb</a></caption></center>

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

We can clearly see that \\(\theta\\) is equal to \\(\frac{5\pi}{6} + \pi k\\). So we have our final answer:

$$\tan(x)=-\frac{1}{\sqrt3} \\
x = \frac{5 \pi}{6} + \pi k
$$

We have learned how to solve equations involving trigonometric functions using certain values of \\(\theta\\) in the unit circle.
