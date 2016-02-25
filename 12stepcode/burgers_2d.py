# -*- coding: utf-8 -*-
"""
12 Steps: 10 Step 8: Burgers' in 2D, with finer spatial grid and more timesteps
"""

from __future__ import division
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import pyplot
import numpy

###variable declarations
nx = 41
ny =  41
nt = 120
dx = 2/(nx-1)
dy = 2/(ny-1)
sigma = .0009
nu = 0.01
dt = sigma*dx*dy/nu


x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

u = numpy.ones((ny, nx))  # create a 1xn vector of 1's
v = numpy.ones((ny, nx))
un = numpy.ones((ny, nx))
vn = numpy.ones((ny, nx))
comb = numpy.ones((ny, nx))

###Assign initial conditions

u[.5/dy:1/dy+1, .5/dx:1/dx+1] = 2  # hat func IC: u(.5<=x<=1 && .5<=y<=1 ) is 2
v[.5/dy:1/dy+1, .5/dx:1/dx+1] = 2  # hat func IC: u(.5<=x<=1 && .5<=y<=1 ) is 2

###(plot ICs)
fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)
wire1 = ax.plot_wireframe(X, Y, u[:], cmap=cm.coolwarm)
wire2 = ax.plot_wireframe(X, Y, v[:], cmap=cm.coolwarm)
#ax.set_xlim(1,2)
#ax.set_ylim(1,2)
#ax.set_zlim(1,5)

pyplot.show(block=False)

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

    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1

    v[0, :] = 1
    v[-1, :] = 1
    v[:, 0] = 1
    v[:, -1] = 1

fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)
wire1 = ax.plot_wireframe(X, Y, u)
wire2 = ax.plot_wireframe(X, Y, v)
#ax.set_xlim(1,2)
#ax.set_ylim(1,2)
#ax.set_zlim(1,5)
pyplot.show()
