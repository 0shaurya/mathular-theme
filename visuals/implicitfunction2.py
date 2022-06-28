import matplotlib.pyplot as plt
from numpy import *

delta = 0.025
x, y = meshgrid(
    arange(-5, 5, delta),
    arange(-5, 5, delta)
)

plt.contour(
    x, y,
    arctan(y**x),
    [0]
)

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')


plt.grid(True)
plt.axvline(x=1)

plt.show()