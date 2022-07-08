import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, .01)
y = 2**x

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.xlim(-5, 5)
plt.ylim(-10, 10)
plt.xticks(np.arange(min(x), max(x)+1, 2.0))
plt.yticks(np.arange(-10, 10+1, 2.0))
plt.plot(x, y)
plt.grid(True)
plt.show()