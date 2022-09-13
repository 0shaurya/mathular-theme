import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, .01)
y = -0.5 * x + 4
x1 = np.arange(2, 4, .01)
y1 = np.linspace(0, 0, 200)
y2 = -0.5 * x1 + 4

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

plt.grid(True)
plt.show()