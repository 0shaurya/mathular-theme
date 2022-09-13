import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, .01)
y = -0.125 * x * x + 3
x1 = np.arange(2, 3, .01)
x2 = np.arange(3, 4, .01)
y1 = np.linspace(0, 0, 100)
y2 = np.linspace(-9/8 + 3, -9/8 + 3, 100)
y4 = np.linspace(1, 1, 100)

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(-5, 5+1, 1.0))
plt.plot(x, y)

ax.fill_between(x1, y1, y2, color="red", alpha=0.5)
ax.fill_between(x2, y1, y4, color="red", alpha=0.5)

# plt.text(2.3, -.4, "dx", color="red")
# plt.text(1.6, .85, "dy", color="red")
# 
# plt.text(1.9, -1, "a", color="green")
# plt.text(3.9, -1, "b", color="green")
# plt.text(1.7, -2, "n = # of rectangles", color="orange")
# plt.text(2.2, -2.5, "dx = (b-a)/n", color="purple")

plt.text(1.4, 1.7, "f(3)", c="green")
plt.text(1.4, 0.85, "f(4)", c="purple")

ax.hlines(y=(-9/8 + 3), xmin=2, xmax=3, linewidth=2, color='green', linestyle="dashed")
ax.hlines(y=(1), xmin=2, xmax=4, linewidth=2, color='purple', linestyle="dashed")

plt.grid(True)
plt.show()