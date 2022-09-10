import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
rc('text', usetex=True)

d = 0.001  # smaller value of d for more accurate graph

x  = np.arange(-2 * np.pi, 2 * np.pi, d)

x1 = np.arange(-2 * np.pi, -(3*np.pi/2), d)
x2 = np.arange(-(3*np.pi/2), -(np.pi), d)
x3 = np.arange(-(np.pi), -(np.pi/2), d)
x4 = np.arange(-(np.pi/2), 0, d)
x5 = np.arange(0, np.pi/2 - d, d)
x6 = np.arange(np.pi/2 + d, np.pi - d, d)
x7 = np.arange(np.pi + d, 3 * np.pi / 2 - d, d)
x8 = np.arange(3 * np.pi / 2 + d, 2 * np.pi, d)

sin  = np.sin(x)
cos  = np.cos(x)

tan1 = np.tan(x1)
tan2 = np.tan(x2)
tan3 = np.tan(x3)
tan4 = np.tan(x4)
tan5 = np.tan(x5)
tan6 = np.tan(x6)
tan7 = np.tan(x7)
tan8 = np.tan(x8)

ax = plt.gca()


plt.xlim(-np.pi*2, np.pi*2)
plt.ylim(-5, 5)
ax.set_xticks(np.arange(-2*np.pi, 2*np.pi+np.pi/2, np.pi /2))
labels = [r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$', r'$-\pi/2$', '$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']
ax.set_xticklabels(labels)

# plt.plot(eval("x" + str(1)), eval(str("csc") + str(1)), color="blue", label="csc(x)")
# for i in range(2, 9):
# 	plt.plot(eval("x" + str(i)), eval(str("csc") + str(i)), color="blue")
# plt.plot(eval("x" + str(1)), eval(str("sec") + str(1)), color="green", label="sec(x)")
# for i in range(2, 9):
# 	plt.plot(eval("x" + str(i)), eval(str("sec") + str(i)), color="green")
# plt.plot(eval("x" + str(1)), eval(str("sec") + str(1)), color="orange", label="cot(x)")
# for i in range(2, 9):
#  	plt.plot(eval("x" + str(i)), eval(str("cot") + str(i)), color="orange")

plt.plot(x, sin, color="blue", label="sin(x)")
plt.plot(x, cos, color="red", label="cos(x)")

plt.plot(eval("x" + str(1)), eval(str("tan") + str(1)), color="orange", label="tan(x)")
for i in range(2, 9):
 	plt.plot(eval("x" + str(i)), eval(str("tan") + str(i)), color="orange")

plt.legend(loc="lower right")
plt.grid(True)

ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.show()