import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np

fig = plt.figure()

leftnum = -2
rightnum = 2
bottomnum = -2
topnum = 2

x = np.arange(leftnum, rightnum, .0001)
y = (1-x**2)**(1/2)
z = -(1-x**2)**(1/2)

framerate = 50

axis = plt.axes(xlim = (leftnum, rightnum), ylim = (bottomnum, topnum))

c1y = []
for i in range(-5000, 5001):
	c1y.append((1-(i/5000)**2)**(1/2))

c2y = []
for i in range(-5000, 5001):
	c2y.append(-(1-(i/5000)**2)**(1/2))

circle1y, = axis.plot([], [])
circle2y, = axis.plot([], [])
line1, = axis.plot([], [])
line2, = axis.plot([], [])
line3, = axis.plot([], [])

def init(): 
    line1.set_data([], [])
    return line1,

def animate(i):
	theta = (2*np.pi/500)*i

	if   theta < np.pi/2:
		ax = np.arange(0, np.cos(theta), .0001)
		ay = np.tan(theta)*ax

		bx = np.arange(0, np.cos(theta), .0001)
		by = 0

		cx = np.cos(theta)
		cy = np.arange(0, np.sin(theta), .0001)
	elif theta == np.pi/2:
		ax = np.full(10000, 0)
		ay = np.arange(0, 1, .0001)

		bx = np.arange(0, np.cos(theta), .0001)
		by = 0

		cx = np.cos(theta)
		cy = np.arange(0, np.sin(theta), .0001)
	elif theta <= np.pi:
		ax = np.arange(np.cos(theta), 0, .0001)
		ay = np.tan(theta)*ax

		bx = np.arange(np.cos(theta), 0, .0001)
		by = 0

		cx = np.cos(theta)
		cy = np.arange(0, np.sin(theta), .0001)
	elif theta < 3*np.pi/2:
		ax = np.arange(np.cos(theta), 0, .0001)
		ay = np.tan(theta)*ax

		bx = np.arange(np.cos(theta), 0, .0001)
		by = 0

		cx = np.cos(theta)
		cy = np.arange(np.sin(theta), 0, .0001)
	elif theta == 3*np.pi/2:
		ax = np.full(10000, 0)
		ay = np.arange(-1, 0, .0001)

		bx = np.arange(0, np.cos(theta), .0001)
		by = 0

		cx = np.cos(theta)
		cy = np.arange(np.sin(theta), 0, .0001)
	elif theta <= 2*np.pi:
		ax = np.arange(0, np.cos(theta), .0001)
		ay = np.tan(theta)*ax

		bx = np.arange(0, np.cos(theta), .0001)
		by = 0

		cx = np.cos(theta)
		cy = np.arange(np.sin(theta), 0, .0001)

	line1.set_label("test")
	line1.set_data([ax], [ay])
	line2.set_data([bx], [by])
	line3.set_data([cx], [cy])
	circle1y.set_color("blue")
	circle2y.set_color("blue")
	circle1y.set_data(np.arange(-1, 1.0001, .0002), c1y)
	circle2y.set_data(np.arange(-1, 1.0001, .0002), c2y)

	return line1, line2, line3

axis.legend(loc='upper left', frameon=False)

anim = ani.FuncAnimation(fig, animate, init_func = init, frames = 500, interval = 1000/framerate, blit = True)

fig.set_size_inches(8, 8, True)

anim.save('unitcircletriangle.mp4', writer = 'ffmpeg', fps = framerate, dpi = 100)