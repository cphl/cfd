# -*- coding: utf-8 -*-
"""
Time-stepping (separation of function from discretization method)
@author: cepuuher
"""

from __future__ import division
import numpy


def forward_difference(nt, dt, c, xmax, ic):
    """ Use forward differencing to time step the initial condition"""
    nx = ic.size  # number of x value to solve for
    print xmax
    print nx
    print nx-1
    dx = xmax / (nx-1)  # set CFL constraint

    all_solutions = numpy.zeros((nt, nx))  # initialize array
    all_solutions[0, :] = ic  # set the initial condition in the solution grid
    for n in range(1, nt):
        for i in range(nx):
            all_solutions[n, i] = all_solutions[n-1, i] \
                - c*dt/dx * (all_solutions[n-1, i] - all_solutions[n-1, i-1])
    return all_solutions


def timestep(ic, method='fd', nt=25, dt=0.025, c=1, xmax=2.0):
    """ Time step an initial condition using a given iteration method
    ic -- initial condition (array with known x values at t=0)
    method -- options for timestepping methods: 'fd' = forward difference
    nt -- nt number of timesteps to take
    dt -- size of time step
    c -- wavespeed (default is constant = 1)
    xmax -- extent of solution along the x-axis (default 2), xmin in future?
    """
    if method == 'fd':
        all_solutions = forward_difference(nt, dt, c, xmax, ic)
    else:  # put future methods in elif blocks
        print 'not implemented'
        all_solutions = ""
    return all_solutions


# Sample initial condition and code for testing
xmax = 2.0
nx = 41
dx = xmax/(nx-1)  # dx = 0.025 will mess up the IC
nt = 25
test_ic = numpy.zeros((1, nx))  # put at assert to accept 1-by-nx ICs
test_ic[0, 0.5/dx: 1/dx + 1] = 2

test_solution = timestep(test_ic, 'fd')
