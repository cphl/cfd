# -*- coding: utf-8 -*-
"""
12 Steps to Navier-Stokes: 06 Array Operations
"""
import numpy
u = numpy.array((0, 1, 2, 3, 4, 5))

for i in range(1, len(u)):
    print u[i] - u[i-1]

# compare to slice
u[1:] - u[0:-1]  # run this line alone to see the result
# the -1 represents "end" of the array, i.e. the -1th position

# 2D linear convection code vectorized
nx = 81
ny = 81
nt = 100
c = 1
dx = 2/(nx-1)
dy = 2/(ny-1)
sigma = .2
dt = sigma*dx

x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

u = numpy.ones((ny, nx))  # create a 1xn vector of 1's
un = numpy.ones((ny, nx))

###Assign initial conditions

u[0.5/dy:1/dy+1, 0.5/dx:1/dx + 1] = 2

# --- Compare using timeit --- #

#%%timeit  # is not liked even though typing in IPython console recogizes it
u = numpy.ones((ny, nx))
u[0.5/dy:1/dy+1, 0.5/dx:1/dx+1] = 2

for n in range(nt+1):  # loop across number of time steps
    un = u.copy()
    row, col = u.shape
    for j in range(1, row):
        for i in range(1, col):
            u[j, i] = un[j, i] - (c*dt/dx*(un[j, i] - un[j, i-1])) -\
                (c*dt/dy*(un[j, i]-un[j-1, i]))
            u[0, :] = 1
            u[-1, :] = 1
            u[:, 0] = 1
            u[:, -1] = 1

#%%timeit
u = numpy.ones((ny, nx))
u[0.5/dy:1/dy+1, 0.5/dx:1/dx+1] = 2

for n in range(nt+1):  # loop across number of time steps
    un = u.copy()
    u[1:, 1:] = un[1:, 1:] - (c*dt/dx*(un[1:, 1:]-un[1:, 0:-1])) -\
        (c * dt/dy * (un[1:, 1:] - un[0:-1, 1:]))
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1

# Know vectorized will be faster
