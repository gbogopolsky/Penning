import numpy as np
import matplotlib.pyplot as plt


sol = np.loadtxt('2penning.res')
Z = sol[:,3]
T = sol[:,0]

plt.plot(T,Z, label='Z(T)')

plt.show()
