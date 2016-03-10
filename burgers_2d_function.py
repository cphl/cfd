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

    # TODO: add a dimension to arrays for saving solutions at every timestep
    u = numpy.ones((ny, nx, nt))  # 1 spatial soln per distinct value of t
    v = numpy.ones((ny, nx, nt))

    # Set initial conditions
    u[.5/dy:1/dy+1, .5/dx:1/dx+1, 0] = 2  # hat func IC
    v[.5/dy:1/dy+1, .5/dx:1/dx+1, 0] = 2  # hat func IC

    for t in range(nt-1):  # loop across number of time steps, was nt+1

        u[1:-1, 1:-1, t+1] = u[1:-1, 1:-1, t] - dt/dx * u[1:-1, 1:-1, t] *\
            (u[1:-1, 1:-1, t] - u[1:-1, 0:-2, t]) - dt/dy*v[1:-1, 1:-1, t] *\
            (u[1:-1, 1:-1, t] - u[0:-2, 1:-1, t]) + nu*dt/dx**2 *\
            (u[1:-1, 2:, t] - 2*u[1:-1, 1:-1, t] + u[1:-1, 0:-2, t]) + \
            nu*dt/dy**2 *\
            (u[2:, 1:-1, t] - 2*u[1:-1, 1:-1, t] + u[0:-2, 1:-1, t])

        v[1:-1, 1:-1, t+1] = v[1:-1, 1:-1, t] - dt/dx * u[1:-1, 1:-1, t] *\
            (v[1:-1, 1:-1, t] - v[1:-1, 0:-2, t]) - dt/dy*v[1:-1, 1:-1, t] *\
            (v[1:-1, 1:-1, t] - v[0:-2, 1:-1, t]) + nu*dt/dx**2 *\
            (v[1:-1, 2:, t] - 2*v[1:-1, 1:-1, t] + v[1:-1, 0:-2, t]) + \
            nu*dt/dy**2 *\
            (v[2:, 1:-1, t] - 2*v[1:-1, 1:-1, t] + v[0:-2, 1:-1, t])

        # Reset boundary values every iteration
        u[0, :, t+1] = 1
        u[-1, :, t+1] = 1
        u[:, 0, t+1] = 1
        u[:, -1, t+1] = 1

        v[0, :, t+1] = 1
        v[-1, :, t+1] = 1
        v[:, 0, t+1] = 1
        v[:, -1, t+1] = 1

    return (u, v)


# Call the function with these parameters
nx = 81
ny = 81
nt = 200  # start smaller while creating 3d arrays to hold all solutions
sigma = 0.0009
nu = 0.01

u_solution, v_solution = solve_burgers(nx, ny, nt, sigma, nu)
# Originally, in the non-function form, initial and final states were plotted
# (plot ICs) (from beforloop)
fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

X, Y = numpy.meshgrid(x, y)
# Plot surface, we have small grid (matplotlib bug for wireframe)
surf1 = ax.plot_surface(X, Y, u_solution[:, :, 0], cmap=cm.gist_heat)
surf2 = ax.plot_surface(X, Y, v_solution[:, :, 0], cmap=cm.gist_heat)

#ax.set_xlim(1,2)
#ax.set_ylim(1,2)
#ax.set_zlim(1,5)

pyplot.show(block=False)


# Now just plot final state
fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)
X, Y = numpy.meshgrid(x, y)
surf1 = ax.plot_surface(X, Y, u_solution[:, :, -1], cmap=cm.gist_heat)
surf2 = ax.plot_surface(X, Y, v_solution[:, :, -1], cmap=cm.gist_heat)
#ax.set_xlim(1,2)
#ax.set_ylim(1,2)
#ax.set_zlim(1,5)
pyplot.show()
