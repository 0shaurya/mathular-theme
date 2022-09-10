import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, .01)
y = 2**x
z = 3*(3)**x
a = 5*3**x
b = (-6)*4**x

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xticks(np.arange(min(x), max(x)+1, 2.0))
plt.yticks(np.arange(-10, 10+1, 2.0))
plt.plot(x, y, label=r"$2^x$")
plt.plot(x, z, label=r"$3$")
plt.plot(x, a, label=r"$5\cdot3^x$")
plt.plot(x, b, label=r"$(-6)\cdot4^x$")

ax.legend(loc='upper left', frameon=True)

plt.grid(True)
plt.show()