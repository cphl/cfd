# -*- coding: utf-8 -*-
"""
12 steps: 14_Optimizing loops, numba
Demo via Laplace Equation
"""

from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np
from numba import autojit

##variable declarations
nx = 81
ny = 81
c = 1
dx = 2.0/(nx-1)
dy = 2.0/(ny-1)

##initial conditions
p = np.zeros((ny, nx))  # create a XxY vector of 0's

##plotting aids
x = np.linspace(0, 2, nx)
y = np.linspace(0, 1, ny)

##boundary conditions
p[:, 0] = 0		# p = 0 @ x = 0
p[:, -1] = y		# p = y @ x = 2
p[0, :] = p[1, :]     # dp/dy = 0 @ y = 0
p[-1, :] = p[-2, :]   # dp/dy = 0 @ y = 1


# From Step 9
@autojit
def laplace2d(p, y, dx, dy, l1norm_target):
    l1norm = 1
    pn = np.empty_like(p)

    while l1norm > l1norm_target:
        pn = p.copy()
        p[1:-1, 1:-1] = (dy**2*(pn[2:, 1:-1] + pn[0:-2, 1:-1])
                         + dx**2*(pn[1:-1, 2:] + pn[1:-1, 0:-2]))\
            / (2*(dx**2+dy**2))
        p[0, 0] = (dy**2*(pn[1, 0]+pn[-1, 0])+dx**2*(pn[0, 1]+pn[0, -1]))\
            / (2*(dx**2+dy**2))
        p[-1, -1] = (dy**2*(pn[0, -1]+pn[-2, -1])
                     + dx**2*(pn[-1, 0] + pn[-1, -2])) / (2*(dx**2+dy**2))

        p[:, 0] = 0           # p = 0 @ x = 0
        p[:, -1] = y          # p = y @ x = 2
        p[0, :] = p[1, :]     # dp/dy = 0 @ y = 0
        p[-1, :] = p[-2, :]   # dp/dy = 0 @ y = 1
        l1norm = (p.sum(np.abs(p[:])-np.abs(pn[:]))) / np.sum(np.abs(pn[:]))

    return p
