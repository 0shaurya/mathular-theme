import matplotlib.pyplot as plt
import numpy as np

xl = -15
xr = 15
yb = -15
yt = 15

x = np.arange(xl, xr+1, 1)
y = 2*x

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

ax.fill_between(x, 0, y, where=(x>=2) & (x<=5), alpha=0.3, color="red")
plt.text(5.5, 1, 'Shaded area = 21')

plt.xlim(xl, xr)
plt.ylim(xl, xr)
plt.xticks(np.arange(min(x), max(x)+1, 5.0))
plt.yticks(np.arange(xl, xr+1, 5.0))
plt.plot(x, y)
plt.grid(True)
plt.show()