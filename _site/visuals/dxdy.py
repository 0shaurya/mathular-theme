import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2, 5, .01)
x1 = np.arange(3, 3.75, .01)
y = x**2
y1 = 9 + 0*x1

ax = plt.gca()
# ax.spines['top'].set_color('none')
# ax.spines['left'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['bottom'].set_position('zero')

plt.xlim(2, 5)
plt.ylim(8, 17)
plt.xticks(np.arange(2, 5.5, .5))
plt.yticks(np.arange(8, 17+1, 1))
plt.plot(x, y)
plt.plot(x1, y1)
plt.vlines(x = 3.75, ymin=9, ymax=(3.75**2), color="green")

plt.text(3.8, 11.5, "dy", color="green")
plt.text(3.33, 8.6, "dx", color="orange")
plt.grid(True)
plt.show()