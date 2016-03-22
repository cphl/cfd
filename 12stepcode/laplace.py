# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:15:40 2016

12 Steps: 12_Step_9 - Laplace equation
Independent initial pass

@author: cepuuher
"""

from __future__ import division
from matplotlib import pyplot
import numpy


def laplace(nx=41, ny=41, sigma=0.0009, nu=0.01):
    """ Solves equilibtrium state for laplace """

    # Set other dependent variables required for computation
    # - spatial grid
    dx = 2/(nx-1)
    dy = 2/(ny-1)
    x = numpy.linspace(0, 2, nx)
    y = numpy.linspace(0, 2, ny)

    p = numpy.ones((ny, nx))  # solution array
    pn = numpy.ones((ny, nx))
    dp = numpy.ones((ny, nx))
    dpn = numpy.ones((ny, nx))

    # Boundary conditions
    p[:, 0] = 0  # p=0 at all x=0
    p[:, 2] = y  # p=y at all x=2
    dp[0, :] = 0  # dp/dy = 0 at all y=0
    dp[1, :] = 0  # dp/dy = 0 at all y=1

