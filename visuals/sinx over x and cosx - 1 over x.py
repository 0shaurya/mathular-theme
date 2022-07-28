import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
rc('text', usetex=True)

d = 0.001  # smaller value of d for more accurate graph

x = np.arange(-2 * np.pi, 2 * np.pi, d)

y = np.sin(x) / x
z = (np.cos(x) - 1) / x


ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.xlim(-np.pi*2, np.pi*2)
plt.ylim(-2, 2)
ax.set_xticks(np.arange(-2*np.pi, 2*np.pi+np.pi/2, np.pi /2))
labels = [r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$', r'$-\pi/2$', '$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']
ax.set_xticklabels(labels)

plt.plot(x, y, label=r"sin(x)/x")
plt.plot(x, z, label=r"(cos(x)+1)/x")

plt.legend(loc="lower right")

plt.grid(True)
plt.show()