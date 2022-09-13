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

plt.grid(True)
plt.show()