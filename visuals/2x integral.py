import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, .01)
y = x*2
x1 = np.arange(2, 5, .01)
y2 = x1*2

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xticks(np.arange(min(x), max(x)+1, 2.0))
plt.yticks(np.arange(-10, 10+1, 2.0))
plt.plot(x, y)

ax.fill_between(x1, 0, y2, color="red", alpha=0.5)

plt.text(2.3, 2.5, "Area=21")
plt.grid(True)
plt.show()