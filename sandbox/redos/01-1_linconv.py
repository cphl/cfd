# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 22:43:44 2016
Redoing the steps to make sure everything works
@author: cepuuher
"""

from __future__ import division
import numpy as np
from matplotlib import pyplot as plt


def linear_convection_1(nx, x_max, dt, nt, u0, c=1):
    """Propagates the initial condition to give the solution at nt step later
    nx -- number of points on spatial grid
    x_max -- spatial range goes from 0 to max_x
    dt -- size of timestep interval
    nt -- number of timesteps to take total
    u0 -- 1 by nx array representing the initial condition
    c -- wave speed, default=1
    """
    dx = x_max/(nx-1)  # x grid spacing
    u = np.ones((nt, nx))  # time=rows, space=columns
    u[0, :] = u0  # set initial condition to be soln at t=0

    for t in range(1, nt):
        u[t, 1:] = u[t-1, 1:] - c*dt/dx*(u[t-1, 1:] - u[t-1, :-1])
        # shift 1 right = prev t - const*(prev t - prev t one to the left)
    return u

nx = 71  # 41 for Figure 1, 81 for figure 2, 83 for fig 3
x_max = 2
dt = 0.025
nt = 40
dx = x_max/(nx-1)
u0 = np.ones(nx)
u0[0.5/dx: 1/dx + 1] = 2
solns = linear_convection_1(nx, x_max, dt, nt, u0)


def plot1d(solns_array, n, x_max):
    """Plot the n-th timestep from the solutions array
    solns_array -- nt by nx array of timestepped spatial solutions
    n -- a solution at timestep n in [0, nt]
    x_max -- plot will be from x=0 to x=x_max
    """
#    plt.plot(np.linspace(0, x_max, np.size(solns_array, 0)), solns_array[n, :])
    plt.plot(np.linspace(0, 2, nx), solns_array[n, :])
    plt.show()

# code for Figure 1 in report:
for i in range(35):
    plot1d(solns, i, x_max)

# code for Figure 2, 3, 4 in report:
figure()
plot1d(solns, i, x_max)

# ok pretty solid until here. But not solid on animation. But will skip :(