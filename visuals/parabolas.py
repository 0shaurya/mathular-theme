import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, .01)
y = x**2+x+2
z = 1.2 * x**2-7 * x+9
a = -1.5 * x**2 - 5 * x - (25/6)
b = -.6 * x**2-3 * x+1

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
plt.plot(x, z)
plt.plot(x, a)
plt.plot(x, b)
plt.grid(True)
plt.show()