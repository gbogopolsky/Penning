################################################################################
#                               LIEN UTILE :                                   #
#                                                                              #
#          http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html            #
#                                                                              #
################################################################################

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
