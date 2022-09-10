import matplotlib.pyplot as plt
import numpy as np

def f1(x):
	if x < -1:
		return 1/(x+1)

def f2(x):
	if x > -1:
		return 1/(x+1)

x = np.linspace(-5, 5, 1000)

y=[]
for i in x:
	y.append(f1(i))

z=[]
for i in x:
	z.append(f2(i))

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.yticks(np.arange(-5, 5+1, 1.0))
plt.plot(x, y)
plt.plot(x, z, c='C0')
plt.grid(True)
plt.show()