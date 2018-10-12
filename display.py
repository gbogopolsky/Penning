################################################################################
#                               LIEN UTILE :                                   #
#                                                                              #
#          http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html            #
#                                                                              #
################################################################################

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams['legend.fontsize'] = 13

data = np.loadtxt('2penning.res')
x = data[:,1]
y = data[:,2]
z = data[:,3]

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')

ax.plot(x, y, z, label='Trajectoire de la particule')
ax.legend()

plt.show()