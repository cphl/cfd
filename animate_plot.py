# -*- coding: utf-8 -*-
"""
Plotting (separation of function from discretization method and timestepping)
@author: cepuuher, adapted from materials by http://jakevdp.github.com
"""
import numpy
from matplotlib import pyplot
from matplotlib import animation

# TODO: make this script accept solution array of any size
# These will be set by plot_t_by_x_array (the wrong way to do it)
solution_array = numpy.zeros((25, 41))
xmin = 0
xmax = 0
nt = 0
xgrid_size = 0

fig = pyplot.figure()
ax = pyplot.axes(xlim=(0, 2), ylim=(0, 2))
line, = ax.plot([], [], lw=2)  # will add data to empty line


def init():
    line.set_data([], [])
    return line,


def animate(j):
    """ Animate the solutions given an array of time-stepped solutions.
    solution_array -- numpy array with each row being a spatial solution at t
    frame_delay -- number of milliseconds between drawing new frames
    """
    x = numpy.linspace(xmin, xmax, xgrid_size)
    y = solution_array[j, :]
    line.set_data(x, y)
    return line,


def plot_t_by_x_array(solution_array, frame_delay=50):
    global xgrid_size
    xgrid_size = solution_array.shape[1]
    global xmin
    xmin = solution_array[0, 0]
    global xmax
    xmax = solution_array[0, xgrid_size-1]
    global nt
    nt = solution_array.shape[0]  # show every frame, TODO: sample in future

#    anim =
    animation.FuncAnimation(fig, animate, init_func=init,
                            frames=nt, interval=frame_delay, blit=True)
    pyplot.show()

# TODO make it work