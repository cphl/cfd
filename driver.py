# -*- coding: utf-8 -*-
"""
Driver runs 3 steps together: function generation, time stepping, plotting
This script will call the time_stepping and plotting script when you enter the
initial conditions (function) below

@author: cepuuher
"""
import numpy
# Not standard modules: ensure these files are in the current directory
import timestep as ts
import simple_plot as sp
import animate_plot as ap

# Sample initial condition and code for testing
#dx = 0.025
xmax = 2.0
nx = 41
dx = xmax/(nx-1)
nt = 25
test_ic = numpy.zeros((1, nx))  # put at assert to accept 1-by-nx ICs
test_ic[0, 0.5/dx: 1/dx + 1] = 2
test_solution = ts.timestep(test_ic, 'fd')
# TODO: does SOMETHIHNG, but it's not the solution (compare prev)
# That plot is WEIRD! it happens in timestep.py

sp.plot_at(24, test_solution)
