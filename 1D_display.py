import numpy as np
import matplotlib.pyplot as plt

sol = np.loadtxt('2penning.res')
x = sol[:,1]
y = sol[:,2]
z = sol[:,3]
t = sol[:,0]

fig = plt.figure() # Ouverture de la figure dans laquelle nous allons tracer
limits = (np.min(t), np.max(t))

# Première figure
plt.subplot(311)
plt.plot(t, x, linewidth=1.2)
plt.xlabel('t (s)')
plt.title('Coordonnées x(t), y(t) et z(t) de la particule.')
plt.ylabel('x (m)')
plt.xlim(limits)

# Deuxième figure
plt.subplot(312)
plt.plot(t, y, linewidth=1.2)
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.xlim(limits)

# Troisième figure
plt.subplot(313)
plt.plot(t, z, linewidth=1.2)
plt.xlabel('t (s)')
plt.ylabel('z (m)')
plt.xlim(limits)

# Affichage de la figure ainsi tracée
plt.tight_layout()
plt.show()
