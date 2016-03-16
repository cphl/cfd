# -*- coding: utf-8 -*-
"""
Burger driver
Use this to call the solver and plotting functions
Vary input parameters including initial conditions here
@author: cepuuher
"""
from __future__ import division
import numpy
import burgers_2d_function as bgr
from matplotlib import pyplot


# Call the function with these parameters
nx = 201
ny = 41
nt = 2000  # start smaller while creating 3d arrays to hold all solutions
sigma = 0.0009
nu = 0.01
area = [3, 2]  # original was 2 x 2

# Hat function (for initial condition), original given:
dx = 3/(nx-1)
dy = 2/(ny-1)
dt = sigma*dx*dy/nu
u0 = numpy.ones((ny, nx))
v0 = numpy.ones((ny, nx))
u0[.5/dy:1/dy+1, .5/dx:1/dx+1] = 2  # hat func IC
v0[.5/dy:1/dy+1, .5/dx:1/dx+1] = 2  # hat func IC

u_solution, v_solution = bgr.solve_burgers(u0, v0, area, nx, ny, nt, sigma, nu)

# using the plot surface function
bgr.plot2D(u_solution, v_solution, -1)  # -1 gives the final time
pyplot.show(block=False)

# use flat plot function
bgr.plot2D_flat(u_solution, v_solution, 0)
pyplot.show(block=False)
bgr.plot2D_flat(u_solution, v_solution, -1)
pyplot.show()
