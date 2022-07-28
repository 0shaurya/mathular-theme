import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, .01)
y = 2*x
a = x**2+0
b = x**2+2
c = x**2-1
d = x**2-4

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xticks(np.arange(min(x), max(x)+1, 2.0))
plt.yticks(np.arange(-5, 5+1, 2.0))
plt.plot(x, y)
plt.plot(x, a, label="x² + 0", alpha = 0.6)
plt.plot(x, b, label="x² + 2", alpha = 0.6)
plt.plot(x, c, label="x² - 1", alpha = 0.6)
plt.plot(x, d, label="x² - 4", alpha = 0.6)
plt.grid(True)
plt.show()