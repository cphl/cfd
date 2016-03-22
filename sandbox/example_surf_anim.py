# -*- coding: utf-8 -*-
"""
Surface wireframe example from:
http://scicomp.stackexchange.com/questions/7030\\
     /plotting-a-2d-animated-data-surface-on-matplotlib
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import axes3d


def generate(X, Y, phi):
    R = 1 - np.sqrt(X**2 + Y**2)
    return np.cos(2 * np.pi * X + phi) * R

fig = plt.figure()
ax = axes3d.Axes3D(fig)

xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
Z = generate(X, Y, 0.0)
wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
ax.set_zlim(-1, 1)


def update(i, ax, fig):
    ax.cla()
    phi = i * 360 / 2 / np.pi / 100
    Z = generate(X, Y, phi)
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
    ax.set_zlim(-1, 1)
    return wframe,

ani = animation.FuncAnimation(fig, update,
                              frames=xrange(100),
                              fargs=(ax, fig), interval=100)
plt.show()
