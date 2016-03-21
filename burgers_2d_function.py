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


def solve_burgers(u0, v0, area=[3, 2], nx=501, ny=101,
                  nt=3000, sigma=0.0009, nu=0.01):
    """Timestep for Burgers.
    u0, v0 -- initial conditions, ny by nx arrays
    plot_area = [x_size, y_size] -- the x by y area of interest
    nx, ny -- size of spatial grid in x and y
    nt -- number of timesteps
    sigma -- default is 0.0009
    nu -- default 0.01
    Returns 2d array of solutions.
    """

    dx = area[0]/(nx-1)
    dy = area[1]/(ny-1)
    dt = sigma*dx*dy/nu

    u = numpy.ones((ny, nx, nt))  # 1 spatial soln per distinct value of t
    v = numpy.ones((ny, nx, nt))

    # Set initial conditions
    u[:, :, 0] = u0  # hat func IC
    v[:, :, 0] = v0  # hat func IC

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


# TODO: avoid hard-coding 0 and 2 in the plot function(s)
def plot2D(u_solution, v_solution, t):
    """t is the timestep number
    Example usage: plot2D(u_solution, v_solution, -1)  # -1 for `final time'
    """
    x = numpy.linspace(0, 2, numpy.size(u_solution, 1))  # min, max, nx
    y = numpy.linspace(0, 2, numpy.size(u_solution, 0))  # min, max, ny
    fig = pyplot.figure(figsize=(11, 7), dpi=100)
    ax = fig.gca(projection='3d')
    X, Y = numpy.meshgrid(x, y)
    #surf = ax.plot_surface(X, Y , p[:, :, t], rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False )
    surf1 = ax.plot_surface(X, Y, u_solution[:, :, t], cmap=cm.gist_heat)
    surf2 = ax.plot_surface(X, Y, v_solution[:, :, t], cmap=cm.gist_heat)
#    ax.set_xlim(0, 2)
#    ax.set_ylim(0, 2)
#    ax.view_init(30, 225)


# TODO: instead of surface, do 2D colourmap to show value
def plot2D_flat(u_solution, v_solution, t):
    """t is the timestep number (i.e. which solution to plot, -1 = final)
    Example usage: plot2D_flat(u_solution, v_solution, -1)
    """
    x = numpy.linspace(0, 2, numpy.size(u_solution, 1))  # min, max, nx
    y = numpy.linspace(0, 2, numpy.size(u_solution, 0))  # min, max, ny
    fig = pyplot.figure(figsize=(11, 7), dpi=100)
    X, Y = numpy.meshgrid(x, y)
    #surf = ax.plot_surface(X, Y , p[:, :, t], rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False )
    # TODO: using pcolormesh for larger arrays, was pcolor originally
    surf1 = pyplot.pcolormesh(X, Y, u_solution[:, :, t], cmap=cm.gist_heat)
    surf2 = pyplot.pcolormesh(X, Y, v_solution[:, :, t], cmap=cm.gist_heat)

# TODO: animate it