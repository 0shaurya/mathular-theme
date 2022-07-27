import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
rc('text', usetex=True)

d = 0.001  # smaller value of d for more accurate graph

x1 = np.arange(-2 * np.pi, -(3*np.pi/2), d)
x2 = np.arange(-(3*np.pi/2), -(np.pi), d)
x3 = np.arange(-(np.pi), -(np.pi/2), d)
x4 = np.arange(-(np.pi/2), 0, d)
x5 = np.arange(0, np.pi/2 - d, d)
x6 = np.arange(np.pi/2 + d, np.pi - d, d)
x7 = np.arange(np.pi + d, 3 * np.pi / 2 - d, d)
x8 = np.arange(3 * np.pi / 2 + d, 2 * np.pi, d)

csc1 = 1 / np.sin(x1)
csc2 = 1 / np.sin(x2)
csc3 = 1 / np.sin(x3)
csc4 = 1 / np.sin(x4)
csc5 = 1 / np.sin(x5)
csc6 = 1 / np.sin(x6)
csc7 = 1 / np.sin(x7)
csc8 = 1 / np.sin(x8)

sec1 = 1 / np.cos(x1)
sec2 = 1 / np.cos(x2)
sec3 = 1 / np.cos(x3)
sec4 = 1 / np.cos(x4)
sec5 = 1 / np.cos(x5)
sec6 = 1 / np.cos(x6)
sec7 = 1 / np.cos(x7)
sec8 = 1 / np.cos(x8)

cot1 = 1 / np.tan(x1)
cot2 = 1 / np.tan(x2)
cot3 = 1 / np.tan(x3)
cot4 = 1 / np.tan(x4)
cot5 = 1 / np.tan(x5)
cot6 = 1 / np.tan(x6)
cot7 = 1 / np.tan(x7)
cot8 = 1 / np.tan(x8)


ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.xlim(-np.pi*2, np.pi*2)
plt.ylim(-5, 5)
ax.set_xticks(np.arange(-2*np.pi, 2*np.pi+np.pi/2, np.pi /2))
labels = [r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$', r'$-\pi/2$', '$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']
ax.set_xticklabels(labels)

plt.plot(eval("x" + str(1)), eval(str("csc") + str(1)), color="blue", label="csc(x)")
for i in range(1, 9):
	plt.plot(eval("x" + str(i)), eval(str("csc") + str(i)), color="blue")
plt.plot(eval("x" + str(1)), eval(str("sec") + str(1)), color="green", label="sec(x)")
for i in range(1, 9):
	plt.plot(eval("x" + str(i)), eval(str("sec") + str(i)), color="green")
plt.plot(eval("x" + str(1)), eval(str("cot") + str(1)), color="orange", label="cot(x)")
for i in range(1, 9):
 	plt.plot(eval("x" + str(i)), eval(str("cot") + str(i)), color="orange")

plt.legend(loc="lower right")

plt.grid(True)
plt.show()