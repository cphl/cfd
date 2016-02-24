# -*- coding: utf-8 -*-
"""
Plot one spatial solution given a set of timestepped solutions and a certain t

Created on Mon Feb 15 08:48:46 2016
@author: cepuuher
"""

import numpy
from matplotlib import pyplot
#import pdb


def plot_at(t, solutions, debug_on=False):
    """Plot all points in the spatial solution at given time t
    If debug_on, output the 1-d array for the spatial solution at the given t
    """
    if debug_on:
        print "The spatial solution at t=%s is:" % t
        print "%s" % solutions[t]
    nx = len(solutions[0])  # number of points along x
    xmin = min(solutions[0])
    xmax = max(solutions[0])
    xgrid = numpy.linspace(xmin, xmax, nx)  # future might not be even-spaced
    pyplot.figure()
    pyplot.axes(xlim=(0, 4), ylim=(0, 2.5))
#    pyplot.show(pyplot.plot(xgrid, solutions[t]))
    pyplot.plot(xgrid, solutions[t])
    pyplot.show(block=False)
