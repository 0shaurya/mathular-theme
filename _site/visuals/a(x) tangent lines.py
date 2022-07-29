import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, .01)
y = x-(x**3/24)
a = x/2 + 2/3
b = 16/3 - x
c = -x/8 - 9/4

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
plt.plot(x, a, "--")
plt.plot(x, b, "--")
plt.plot(x, c, "--")
plt.grid(True)
plt.show()