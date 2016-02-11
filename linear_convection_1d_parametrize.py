# -*- coding: utf-8 -*-
"""
CFD Step 1 - http://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/
"""
from __future__ import division
import numpy  # the array library
from matplotlib import pyplot  # plotting library

def lin_convection(nx=41, nt=25, dt=0.025, c=1):
    """ Time-step a solution grid for linear convection.
    
    nx -- number of grid points (original was 41);
    nt -- number of timesteps (original was 25);
    dt -- delta t, the size of timestep (original was 0.025);
    c -- wavespeed, a constant here, because linear (original was 1)
    """
    dx = 2/(nx-1)

    # initial conditions
    u = numpy.ones(nx)
    u[0.5/dx: 1/dx + 1] = 2  # given init conds. TODO: check why int warning

    pyplot.plot(numpy.linspace(0, 2, nx), u)    
    
    # timestepping
    un = numpy.ones(nx)
    
    for n in range(nt):
        un = u.copy()
        pyplot.plot(numpy.linspace(0, 2, nx), u)  # extra plot tp show steps
        for i in range(nx):
            u[i] = un[i] - c*dt/dx * (un[i] - un[i-1])
    # plot
    # pyplot.plot(numpy.linspace(0,2,nx),u);  # original location of plot code
