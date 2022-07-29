import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, .01)
y = 1.5*x
z = -2*x+7

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(-5, 5+1, 1.0))
plt.xlabel("                                          a-axis", weight="black")
plt.ylabel("                                              b-axis", weight="black")
# plt.legend(["test", "test2"], loc="upper right")

plt.plot(x, y, label="2y=3x")
plt.plot(x, z, label="y-7=-2x")
plt.legend(loc="lower right")

plt.grid(True)
plt.show()