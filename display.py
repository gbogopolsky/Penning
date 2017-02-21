################################################################################
#                               LIEN UTILE :                                   #
#                                                                              #
#          http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html            #
#                                                                              #
################################################################################
"""
VERSION 1 : FIXE, FONCTIONNELLE

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
#-------------------------------------------------------------------------------------
"""
VERSION 2 : ANIMATION, NON FONCTIONNELLE


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
    #Initialize animation.
    line.set_data([],[])
    line.set_3d_properties([])

    point.set_data([], [])
    point.set_3d_properties([])

# Animation function. This will be called sequetially with the frame number
def animate(i):
    #Animation function.
    x, y, z = x_t.T
    line.set_data(x, y)
    line.set_3d_properties(z)

    point.set_data(x[-1:], y[-1:])
    point.set_3d_properties(z[-1:])

    fig.canvas.draw()




ani = animation.FuncAnimation(fig, animate, init_func=init, frames = 500,
                                interval=20, blit=True)

# Save the animation as an mp4. Requires ffmpeg or mencoder to be installed.
# The extra_args ensure that the used by ffmpeg is x264, for html5 embedding.
#ani.save('penning_trap.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
"""
#------------------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

fig = plt.figure()
ax = p3.Axes3D(fig)

def update(frame, data, line):
    line.set_data(data[:2, :frame]) #valeurs de x et y pour la frame
    line.set_3d_properties(data[2, :frame]) #valeur de z pour la frame

l = np.loadtxt('2penning.res')
N = l.shape[0]
data = l[:,-3:].T
#on initialise line avec la premiere valeur en x, y et z de la particule
line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

# Parametres des axes
ax.set_xlim3d([-1e-4, 1e-4])
ax.set_xlabel('X')

ax.set_ylim3d([-1e-4, 1e-4])
ax.set_ylabel('Y')

ax.set_zlim3d([-1e-4, 1e-4])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=10000/N)
plt.show()
