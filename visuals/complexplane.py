import matplotlib.pyplot as plt
import numpy as np

# create data of complex numbers
data = [-3, 2j, 3+4j]
  
# extract real part
x = [ele.real for ele in data]
# extract imaginary part
y = [ele.imag for ele in data]

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')


# plot the complex numbers
plt.scatter(x, y)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xticks(np.arange(-5, 5+1, 1.0))
plt.yticks(np.arange(-5, 5+1, 1.0))
plt.ylabel('                                                            Imaginary axis')
plt.xlabel('                                                                                            Real axis')

ax.annotate("(-3)", (-2.9, .2))
ax.annotate("(2i)", (0.1, 2.2))
ax.annotate("(3+4i)", (3.1, 4.2))

plt.vlines(3, 0, 4, color="k", linestyle="dashed")
plt.hlines(4, 0, 3, color="k", linestyle="dashed")
ax.annotate("Line for 4i", (.5, 4.2))
ax.annotate("Line for 3", (3.1, 1.2))

plt.show()