# -*- coding: utf-8 -*-
"""
12 steps by Lorna Barba. 04_5_Step_5 Burger's Equation

Nonlinear convection and diffusion together
New IC and BC (so that analytical solution can be matched?)

@author: cepuuher
"""
from __future__ import division  # need this to solve ZeroDivisionError
import numpy
import sympy
from sympy import init_printing
import pylab

#----------------------- symbolic stuff ------------------------#
init_printing(use_latex=True)
x, nu, t = sympy.symbols('x nu t')
phi = sympy.exp(-(x-4*t)**2/(4*nu*(t+1))) \
    + sympy.exp(-(x-4*t-2*numpy.pi)**2/(4*nu*(t+1)))
phi

phiprime = phi.diff(x)
phiprime

print(phiprime)

from sympy.utilities.lambdify import lambdify

u = -2*nu*(phiprime/phi)+4
print(u)

ufunc = lambdify((t, x, nu), u)
print(ufunc(1, 4, 3))

#------------------- end of symbolic stuff --------------------#

from matplotlib import pyplot

###variable declarations
nx = 101
nt = 100
dx = 2*numpy.pi/(nx-1)
nu = .07
dt = dx*nu

x = numpy.linspace(0, 2*numpy.pi, nx)
#u = numpy.empty(nx)
un = numpy.empty(nx)
t = 0

u = numpy.asarray([ufunc(t, x0, nu) for x0 in x])
u
#----#
pyplot.figure(figsize=(11, 7), dpi=100)
pyplot.plot(x, u, marker='o', lw=2)
pyplot.xlim([0, 2*numpy.pi])
pyplot.ylim([0, 10])
# sawtooth


for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        u[i] = un[i] - un[i] * dt/dx * (un[i] - un[i-1]) + nu * dt/dx ** 2 *\
            (un[i+1]-2*un[i]+un[i-1])
    u[0] = un[0] - un[0] * dt/dx * (un[0] - un[-2]) + nu * dt/dx ** 2 *\
        (un[1]-2*un[0]+un[-2])
    u[-1] = un[-1] - un[-1] * dt/dx * (un[-1] - un[-2]) + nu * dt/dx ** 2 *\
        (un[0]-2*un[-1]+un[-2])

u_analytical = numpy.asarray([ufunc(nt*dt, xi, nu) for xi in x])

pyplot.figure(figsize=(11, 7), dpi=100)

# something funny here, maybe don't "show()" both?
pyplot.plot(x, u, marker='o', lw=2, label='Computational')
pyplot.plot(x, u_analytical, label='Analytical')
pyplot.xlim([0, 2*numpy.pi])
pyplot.ylim([0, 10])
pyplot.legend()
pyplot.show()
