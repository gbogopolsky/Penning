from matplotlib.pyplot import *
import numpy as np

sol = np.loadtxt('2penning.res')
Z = sol[:,3]
T = sol[:,0]
plot(T,Z)
show()

