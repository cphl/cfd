# -*- coding: utf-8 -*-
"""
12 Steps: 10 Step 8: Burgers' in 2D, with finer spatial grid and more timesteps
Separating into a function. Plotting done separately.
"""

from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import pyplot
import numpy


def solve_burgers(nx=501, ny=101, nt=3000, sigma=0.0009, nu=0.01):
    """Timestep for Burgers.
    nx, ny -- size of spatial gridding in x and y
    nt -- number of timesteps
    sigma -- default is 0.0009
    nu -- default 0.01
    u, v --initial conditions
    Returns 2d array of solutions.
    """

    dx = 2/(nx-1)
    dy = 2/(ny-1)
    dt = sigma*dx*dy/nu

    u = numpy.ones((ny, nx))  # create a 1xn vector of 1's
    v = numpy.ones((ny, nx))
    un = numpy.ones((ny, nx))
    vn = numpy.ones((ny, nx))

    # Set initial conditions
    u[.5/dy:1/dy+1, .5/dx:1/dx+1] = 2  # hat func IC
    v[.5/dy:1/dy+1, .5/dx:1/dx+1] = 2  # hat func IC

    for n in range(nt+1):  # loop across number of time steps
        un = u.copy()
        vn = v.copy()

        u[1:-1, 1:-1] = un[1:-1, 1:-1] - dt/dx * un[1:-1, 1:-1] *\
            (un[1:-1, 1:-1] - un[1:-1, 0:-2]) - dt/dy*vn[1:-1, 1:-1] *\
            (un[1:-1, 1:-1] - un[0:-2, 1:-1]) + nu*dt/dx**2 *\
            (un[1:-1, 2:] - 2*un[1:-1, 1:-1] + un[1:-1, 0:-2]) + \
            nu*dt/dy**2 * (un[2:, 1:-1] - 2*un[1:-1, 1:-1] + un[0:-2, 1:-1])

        v[1:-1, 1:-1] = vn[1:-1, 1:-1] - dt/dx*un[1:-1, 1:-1] *\
            (vn[1:-1, 1:-1] - vn[1:-1, 0:-2]) - dt/dy*vn[1:-1, 1:-1] *\
            (vn[1:-1, 1:-1] - vn[0:-2, 1:-1]) + nu*dt/dx**2 *\
            (vn[1:-1, 2:] - 2*vn[1:-1, 1:-1] + vn[1:-1, 0:-2]) + \
            nu*dt/dy**2 * (vn[2:, 1:-1] - 2*vn[1:-1, 1:-1] + vn[0:-2, 1:-1])

        # I believe this makes the boundaries fixed values - reset each time
        u[0, :] = 1
        u[-1, :] = 1
        u[:, 0] = 1
        u[:, -1] = 1

        v[0, :] = 1
        v[-1, :] = 1
        v[:, 0] = 1
        v[:, -1] = 1

    return (u, v)


# Call the function with these parameters
nx = 501
ny = 101
nt = 3000
sigma = 0.0009
nu = 0.01

u_solution, v_solution = solve_burgers(nx, ny, nt, sigma, nu)
# Originally, in the non-function form, initial and final states were plotted
## (plot ICs) (from beforloop)
#fig = pyplot.figure(figsize=(11, 7), dpi=100)
#ax = fig.gca(projection='3d')
#x = numpy.linspace(0, 2, nx)
#y = numpy.linspace(0, 2, ny)
#
#X, Y = numpy.meshgrid(x, y)
## Plot surface, we have small grid (matplotlib bug for wireframe)
#surf1 = ax.plot_surface(X, Y, u[:], cmap=cm.gist_heat)
#surf2 = ax.plot_surface(X, Y, v[:], cmap=cm.gist_heat)
#
##ax.set_xlim(1,2)
##ax.set_ylim(1,2)
##ax.set_zlim(1,5)
#
#pyplot.show(block=False)


# Now just plot final state
# TODO: add a dimension to the array so that we save solutions at every time
fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)
X, Y = numpy.meshgrid(x, y)
surf1 = ax.plot_surface(X, Y, u_solution, cmap=cm.gist_heat)
surf2 = ax.plot_surface(X, Y, v_solution, cmap=cm.gist_heat)
#ax.set_xlim(1,2)
#ax.set_ylim(1,2)
#ax.set_zlim(1,5)
pyplot.show()
