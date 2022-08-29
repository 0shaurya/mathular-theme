---
layout: page
menuInclude: yes
menuLink: yes
menuTopTitle: Precalculus
menuSubs:
- title: Probability
  index: 7
excerpt: "An excerpt is used as the page description and can be up to 160 characters long..."
---


<h1>Precalculus</h1>

<h2>Probability</h2><br>

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
