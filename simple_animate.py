# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:30:10 2016
Test way of running anumate in a nested fashion
@author: cepuuher
"""
import numpy
from matplotlib import pyplot
from matplotlib import animation


def animate_it(solutions):
    """ Accept the solution array (nt by nx), product animated plot"""
    # useful numbers extrated from solutsion array
    nx = len(solutions[0])  # number of points along x
    xmin = min(solutions[0])
    xmax = max(solutions[0])

    # set up figure, axis, plot element to animate
    fig = pyplot.figure()
    ax = pyplot.axes(xlim=(xmin, xmax*2), ylim=(0, 2.5))  # TODO: modify ylim
    line, = ax.plot([], [], lw=2)  # add data to empty line later, don't need?

    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        return line,

    # animate function. Called sequentially
    def animate(j):  # j is the frame number, plot changes depend on this
        x = numpy.linspace(xmin, xmax*2, nx)
        y = solutions[j, :]
        line.set_data(x, y)
        return line,

    # call the animator. blit=True means only redrwa the part that changed
    # interval -- milliseconds between drawing new frames (was 20)
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=50, interval=80, blit=True)
    
    pyplot.show()
