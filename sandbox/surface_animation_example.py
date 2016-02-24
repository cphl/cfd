# -*- coding: utf-8 -*-
"""
Surface animation example from:
http://www.nugnux.my.id/2014/12/3d-surface-plot-animation-using.html
"""

import numpy
from matplotlib import pyplot
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D


def data(i, z, line):
    z = numpy.sin(x + y + i)
    ax.clear()
    line = ax.plot_surface(x, y, z, color='b')
    return line,

n = 2.*numpy.pi
fig = pyplot.figure()
ax = fig.add_subplot(111, projection='3d')

x = numpy.linspace(0, n, 100)
y = numpy.linspace(0, n, 100)
x, y = numpy.meshgrid(x, y)
z = numpy.sin(x + y)
line = ax.plot_surface(x, y, z, color='b')

ani = animation.FuncAnimation(fig, data, fargs=(z, line),
                              interval=50, blit=False)

pyplot.show()
