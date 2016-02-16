# -*- coding: utf-8 -*-
"""
Driver runs 3 steps together: function generation, time stepping, plotting
This script will call the time_stepping and plotting script when you enter the
initial conditions (function) below

A little clunky right now:
* Need to run plot and animate steps one by one
* Close the figure window before the next plot or animate can appear

@author: cepuuher
"""

#TODO figure out how to not require closing window before next plot can appear

import numpy
# Not standard modules: ensure these files are in the current directory
import timestep as ts
import simple_plot as sp
import simple_animate as sa

# Sample initial condition and code for testing
#dx = 0.025
xmax = 2.0
nx = 41
dx = xmax/(nx-1)
nt = 50
test_ic = numpy.zeros((1, nx))  # put at assert to accept 1-by-nx ICs
test_ic[0, 0.5/dx: 1/dx + 1] = 2
test_solution = ts.timestep(test_ic, 'fd')

sp.plot_at(24, test_solution)
sa.animate_it(test_solution)


# try a different IC - Double hat
test_ic_2 = test_ic.copy()
test_ic_2[0, 0.7/dx: 0.9/dx] = 0
test_solution_2 = ts.timestep(test_ic_2, 'fd')
sp.plot_at(0, test_solution_2)  # see initial condition
sp.plot_at(24, test_solution_2)  # see final state
sa.animate_it(test_solution_2)
