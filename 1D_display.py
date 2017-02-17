import matplotlib.pyplot as plt
import numpy as np

sol = np.loadtxt('2penning.res')
Z = sol[:,3]
T = sol[:,0]
plt.plot(T,Z)
plt.show()
