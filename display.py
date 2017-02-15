################################################################################
#                               LIEN UTILE :                                   #
#                                                                              #
#          http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html            #
#                                                                              #
################################################################################
"""
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

l = np.loadtxt('2penning.res')
x = l[:,1]
y = l[:,2]
z = l[:,3]

ax.plot(x, y, z, label='Trajectoire')
ax.legend()

plt.show()
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# Solutions for the trajectories
l = np.loadtxt('2penning.res')
x_t = l[:,-3:]


# Set up figure & 3D axis for animation
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1], projection='3d')


# Set up line representing the trajectory
line, = ax.plot([], [], [], '-')
point, = ax.plot([], [], [], 'o')

# Prepare the axes limits
ax.set_xlim((-0.005, 0.005))
ax.set_ylim((-0.005, 0.005))
ax.set_zlim((-0.005, 0.005))

# Initialization function:
def init():
    """ Initialize animation. """
    line.set_data([],[])
    line.set_3d_properties([])

    point.set_data([], [])
    point.set_3d_properties([])
    return line + point

# Animation function. This will be called sequetially with the frame number
def animate(i):
    """ Animation function. """
    x, y, z = x_t.T
    line.set_data(x, y)
    line.set_3d_properties(z)

    point.set_data(x[-1:], y[-1:])
    point.set_3d_properties(z[-1:])

    fig.canvas.draw()
    return line + point




ani = animation.FuncAnimation(fig, animate, init_func=init, frames = 500,
                                interval=20, blit=True)

# Save the animation as an mp4. Requires ffmpeg or mencoder to be installed.
# The extra_args ensure that the used by ffmpeg is x264, for html5 embedding.
#ani.save('penning_trap.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
