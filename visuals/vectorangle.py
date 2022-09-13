import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, .01)

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xticks(np.arange(min(x), max(x)+1, 2.0))
plt.yticks(np.arange(-10, 10+1, 2.0))
plt.grid(True)
plt.arrow(0, 0, 3, 4, length_includes_head=True, head_width=0.5, color="blue", overhang=1)
plt.text(3.1, 3.4, "<3, 4>")
plt.text(0.6, 0.2, "θ = 53.13 degrees")
plt.show()