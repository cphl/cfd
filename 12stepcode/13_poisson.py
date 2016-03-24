# -*- coding: utf-8 -*-
"""
From 12 Steps: 2D Poisson, "13_Step_10"
Created on Thu Mar 24 13:47:05 2016

@author: cepuuher
"""
from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import pyplot as plt
import numpy as np

# Parameters
nx = 50
ny = 50
nt = 100
xmin = 0
xmax = 2
ymin = 0
ymax = 1

dx = (xmax-xmin)/(nx-1)
dy = (ymax-ymin)/(ny-1)

# Initialization
p = np.zeros((ny, nx))
pd = np.zeros((ny, nx))
b = np.zeros((ny, nx))
x = np.linspace(xmin, xmax, nx)
y = np.linspace(xmin, xmax, ny)

# Source
b[ny/4, nx/4] = 100
b[3*ny/4, 3*nx/4] = -100

# Advance solution
for it in range(nt):

    pd = p.copy()

    p[1:-1, 1:-1] = ((pd[1:-1, 2:] + pd[1:-1, :-2])*dy**2 +
                    (pd[2:, 1:-1]+pd[:-2, 1:-1])*dx**2 -
                     b[1:-1, 1:-1]*dx**2*dy**2)/(2*(dx**2+dy**2))

    p[0, :] = 0
    p[ny-1, :] = 0
    p[:, 0] = 0
    p[:, nx-1] = 0


# same plotting function as laplace step
# TODO: package this function
def plot2D(x, y, p):
    fig = plt.figure(figsize=(11, 7), dpi=100)
    ax = fig.gca(projection='3d')
    X, Y = np.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, p[:], rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.view_init(30, 225)

plot2D(x, y, p)
plt.show()
