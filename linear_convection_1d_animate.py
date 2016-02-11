# -*- coding: utf-8 -*-
"""
CFD Step 1 - http://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/
"""
from __future__ import division
import numpy  # the array library
from matplotlib import pyplot  # plotting library
from matplotlib import animation
#import pylab


# all_solutions = numpy.zeros((41, 25))  # rows = time, cols = x
def lin_convection(nx=41, nt=25, dt=0.025, c=1, xmax=2.0):
    """ Time-step a solution grid for linear convection.
    nx -- number of grid points (original was 41);
    nt -- number of timesteps (original was 25);
    dt -- delta t, the size of timestep (original was 0.025);
    c -- wavespeed, a constant here, because linear (original was 1)
    xmax -- how far along the x-axis we go
    """
    # set up array to hold all solutions over time
    all_solutions = numpy.zeros((nt, nx))  # rows = time, cols = x

    dx = xmax/(nx-1)  # this is where it can become zero if int

    # initial conditions
    all_solutions[0, 0.5/dx: 1/dx + 1] = 2  # set 1st row = init condition

    # to see initial state
#    pylab.show(pyplot.plot(numpy.linspace(0, 2, nx), all_solutions[0, :]))

    # timestepping
    for n in range(1, nt):
        for i in range(nx):
            all_solutions[n, i] = all_solutions[n-1, i] \
                - c*dt/dx * (all_solutions[n-1, i] - all_solutions[n-1, i-1])

    # to see final state
#    pylab.show(pyplot.plot(numpy.linspace(0, 2, nx), all_solutions[nt-1, :]))

# above works, just the displaying of stuff is weird: need to close first
# window before next plot shows
    return all_solutions

tmp = lin_convection()  # to see it happen!

# ------------ Select times to use for animation ----------- #
# For now, select every row we have, in future will want to sample

# Adapted from examples from:
# author: Jake Vanderplas
# email: vanderplas@astro.washington.edu
# website: http://jakevdp.github.com
# set up figure, axis, plot element to animate


fig = pyplot.figure()
ax = pyplot.axes(xlim=(0, 2), ylim=(0, 2))
line, = ax.plot([], [], lw=2)  # add data to empty line later, don't need?


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,


# animate function. Called sequentially
# I had gotten rows mixed up with columns!!
def animate(j):  # j is the frame number, plot changes depend on this
    x = numpy.linspace(0, 2, 41)
    y = tmp[j, :]
    line.set_data(x, y)
    return line,
#
# call the animator. blit=True means only redrwa the part that changed
# interval -- milliseconds between drawing new frames (was 20)
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=25, interval=100, blit=True)

pyplot.show()
