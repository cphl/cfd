# -*- coding: utf-8 -*-
"""
Burger driver
Use this to call the solver and plotting functions
Vary input parameters including initial conditions here
@author: cepuuher
"""
from __future__ import division
import numpy
from matplotlib import pyplot
import burgers_2d_function as bgr
import animate_2d_by_t

# Set flags for which plots to make:
plot_surface = False
plot_flat = False
animate = True


# Call the function with these parameters
nx = 41
ny = 41
nt = 800  # start smaller while creating 3d arrays to hold all solutions
sigma = 0.0009
nu = 0.01  # TODO: find different nu that will cause effects. Original: 0.01
area = [3, 2]  # original was 2 x 2

# Hat function (for initial condition), original given:
dx = 3/(nx-1)
dy = 2/(ny-1)
dt = sigma*dx*dy/nu
u0 = numpy.ones((ny, nx))
v0 = numpy.ones((ny, nx))

#u0a = u0.copy()
#v0a = v0.copy()
#u0a[.5/dy:1/dy+1, .5/dx:1/dx+1] = 2  # hat func IC
#v0a[.5/dy:1/dy+1, .5/dx:1/dx+1] = 2  # hat func IC
#


##TODO: make different initial conditions... This one just playing around
#u0b = u0.copy()
#v0b = v0.copy()
#u0b[0.2/dy: 0.3/dy, 0.2/dx: 0.3/dx] = 20
#u0b[0.9/dy: 1/dy, 0.9/dx: 1/dx] = 20
###u0b[0:4, 0:6] = 2
#v0b[0.5/dy: 1/dy+1, 0.5/dx: 1/dx+1] = 2  # hat func IC
#v0b[0.2/dy: 0.3/dy, 0.2/dx: 0.3/dx] = 2  # add junk, see what happens


# donut
u0c = u0.copy()
v0c = v0.copy()

u0c[0.5/dy+5: 1/dy+6, 0.5/dx+5: 1/dx+6] = 2  # hat func IC
v0c[0.5/dy: 1/dy, 0.5/dx: 1/dx] = 3  # hat func IC
v0c[0.6/dy: 0.9/dy, 0.6/dx: 0.9/dx] = 1  # hat hole IC


u_soln, v_soln = bgr.solve_burgers(u0c, v0c, area, nx, ny, nt, sigma, nu)

# to inspect final solution:
#u_final = u_soln[:,:,-1]
#v_final = v_soln[:,:,-1]

# plot surface: helpful if a feature is too skinny in one dimension
if plot_surface:
    bgr.plot2D(u_soln, v_soln, -1)  # -1 gives the final time
    pyplot.show(block=False)

# plot flat with colourmap
if plot_flat:
    bgr.plot2D_flat(u_soln, v_soln, 0)
    pyplot.show(block=False)
    bgr.plot2D_flat(u_soln, v_soln, 155)
    pyplot.show()

#TODO: write a simple_animate for surfaces and/or 2D-colourmap
if animate:
    animate_2d_by_t.animate_it(u_soln, v_soln);
    pyplot.show()
