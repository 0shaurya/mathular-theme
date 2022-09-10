import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, .01)
y = 2 + x * 0

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
plt.plot(3, 4, 'wo', markeredgecolor='C0', markerfacecolor='C0', zorder=500)
plt.plot(3, 2, 'wo', markeredgecolor='C0', markerfacecolor='w', zorder=500)
plt.grid(True)
plt.show()