# -*- coding: utf-8 -*-
"""
Wave computations from:
CFD Step 1 - http://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/
Animation step adapted from:
https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
"""
from __future__ import division
import numpy  # the array library
from matplotlib import pyplot  # plotting library
from matplotlib import animation
#import pylab


# all_solutions = numpy.zeros((41, 25))  # rows = time, cols = x
def lin_convection(nx=41, nt=50, dt=0.025, c=1, xmax=2.0):
    """ Time-step a solution grid for linear convection.
    nx -- number of grid points (original was 41);
    nt -- number of timesteps (original was 25);
    dt -- delta t, the size of timestep (original was 0.025);
    c -- wavespeed, a constant here, because linear (original was 1)
    xmax -- ??
    """
    # set up array to hold all solutions over time
    all_solutions = numpy.zeros((nt, nx))  # rows = time, cols = x

    dx = xmax/(nx-1)  # this is where it can become zero if int

    # initial conditions
    all_solutions[0, 0.5/dx: 1/dx + 1] = 2  # set 1st row = init condition

    # timestepping
    for n in range(1, nt):
        for i in range(nx):
            all_solutions[n, i] = all_solutions[n-1, i] \
                - c*dt/dx * (all_solutions[n-1, i] - all_solutions[n-1, i-1])
    return all_solutions

tmp = lin_convection()  # to see it happen!

# ------------ Select times to use for animation ----------- #
# For now, select every row we have, in future will want to sample

# set up figure, axis, plot element to animate
fig = pyplot.figure()
ax = pyplot.axes(xlim=(0, 4), ylim=(0, 2.5))
line, = ax.plot([], [], lw=2)  # add data to empty line later, don't need?


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,


# animate function. Called sequentially
def animate(j):  # j is the frame number, plot changes depend on this
    x = numpy.linspace(0, 4, 41)
    y = tmp[j, :]
    line.set_data(x, y)
    return line,

# call the animator. blit=True means only redrwa the part that changed
# interval -- milliseconds between drawing new frames (was 20)
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=50, interval=80, blit=True)

pyplot.show()
