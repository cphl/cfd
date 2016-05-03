# -*- coding: utf-8 -*-
"""
Animate surface plots.
Take in a 3d array: 2d solutions changing with time
Option to plot as surface or to show colourmap for values in flat xy

@author: cepuuher
Surface wireframe plot adapted from
http://scicomp.stackexchange.com/questions/7030\
      /plotting-a-2d-animated-data-surface-on-matplotlib

"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm  # colourmap


def animate_it(u_soln, v_soln, style="surface", stride=1):
    """Displays animated plot
    u_soln, v_soln -- same sized 3d arrays (nx by nx) by t
    Show surface plot by default. Also: "wireframe", "flat" colourmap
    Default to selecting every timestepped solution,
    otherwise take every stride-th solution (e.g. stride=2 takes every other)
    """
    # useful numbers extracted from solution array
    ny = np.size(u_soln, 0)  # number of points along y
    nx = np.size(u_soln, 1)
    nt = np.size(u_soln, 2)

    # range of x and y, I believe I need these...
    #TODO: I have to think about this... also internet not working argh!
#    xmin = min(v_soln[0])
#    xmax = max(v_soln[0])

    # set up figure, axis, plot element to animate
    fig = plt.figure()
    ax = axes3d.Axes3D(fig)

    xs = np.linspace(0, 2, nx)  # min, max, nx
    ys = np.linspace(0, 2, ny)  # min, max, ny

    X, Y = np.meshgrid(xs, ys)
    if style == "wireframe":
        wframe = ax.plot_wireframe([], [], [], lw=1)

    if style == "surface":
        surf = ax.plot_surface([], [], [])
    if style == "flat":
        colourmap = plt.pcolormesh(X, Y, v_soln[:, :, 0])
    ax.set_zlim(0, 5)  # TODO might want to let this go unconstrained

    def update(t, ax, fig):  # we had called analogous function "animate" in 1d
        ax.cla()  # <-- maybe this is what could go in an init function?
        ax.set_zlim(0, 5)  # TODO free these hardcoded numbers

        if style == "wireframe":
            wframe = ax.plot_wireframe(X, Y, v_soln[:, :, t],
                                       rstride=2, cstride=2)
            return wframe,

        if style == "surface":
            surf = ax.plot_surface(X, Y, v_soln[:, :, t],
                                   rstride=6, cstride=6, cmap=cm.gist_heat)
            return surf,

        if style == "flat":
            colourmap = plt.pcolormesh(X, Y, v_soln[:, :, t],
                                          rstride=1,
                                          cmap=cm.gist_heat)
            return colourmap,

    ani = animation.FuncAnimation(fig, update,
                                  frames=nt,  # was frames=xrange(100)
                                  fargs=(ax, fig), interval=30)
# TODO: figure out why frame rate is so slow: better with higher STRIDE
# TODO: fix colourmap style
    plt.show(block=False)
#    plt.colorbar()

# TODO: add option to sample from provided array, important for high timesteps
# Use something like solutions[::stride_length, :]
# TODO: not sure best place to filter this out
# TODO: output to movie file
