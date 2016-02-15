# -*- coding: utf-8 -*-
"""
Plot one spatial solution given a set of timestepped solutions and a certain t

Created on Mon Feb 15 08:48:46 2016
@author: cepuuher
"""

import numpy
from matplotlib import pyplot
import pdb


def plot_at(t, solutions):
    """Plot all points in the spatial solution at given time t"""
    print "we are going to plot the 1-d array..."
    pdb.set_trace
    print "%s" % solutions[t]
    nx = len(solutions[0])  # number of points along x
    xmin = min(solutions[0])
    xmax = max(solutions[0])
    xgrid = numpy.linspace(xmin, xmax, nx)  # future might not be even-spaced
    pyplot.plot(xgrid, solutions[t])
