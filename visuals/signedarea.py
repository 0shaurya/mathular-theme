import matplotlib.pyplot as plt
import numpy as np

x = [-5, -2, 0, 1, 2, 3, 4, 5]
y = [0, 0, 2, 2, 0, -1, -1, 0]
x1 = np.linspace(1.9, 2.1, 8)
x2 = np.linspace(1.9, 2.0, 8)

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

ax.fill_between(x, 0, y, where=(x<x1) , color="red", alpha=0.5)
ax.fill_between(x, 0, y, where=(x>x2) , color="green", alpha=0.5)

plt.grid(True)
plt.show()