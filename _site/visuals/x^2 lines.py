import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, .01)
x1 = np.arange(-0.5, 0.5, .01)
x2 = np.arange(-1.5, -0.5, .01)
x3 = np.arange(0.5, 1.5, .01)
x4 = np.arange(-2.5, -1.5, .01)
x5 = np.arange(1.5, 2.5, .01)
y = x**2
y1 = x1*0
y2 = -2*x2-1
y3 = 2*x3-1
y4 = -4*x4-4
y5 = 4*x5-4

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.xlim(-5, 5)
plt.ylim(0, 5)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(0, 5+1, 1.0))
plt.plot(x1, y1, linewidth=1.5, c="red", alpha=1)
plt.plot(x2, y2, linewidth=1.5, c="red", alpha=1)
plt.plot(x3, y3, linewidth=1.5, c="red", alpha=1)
plt.plot(x4, y4, linewidth=1.5, c="red", alpha=1)
plt.plot(x5, y5, linewidth=1.5, c="red", alpha=1)
plt.plot(x, y,   linewidth=1,c="blue", alpha=1)
plt.grid(True)
plt.show()