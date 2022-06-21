import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 1)
y = 3*x+1

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.ylim(-5, 5)
plt.ylim(-5, 5)
plt.plot(x, y)
plt.grid(True)
plt.show()