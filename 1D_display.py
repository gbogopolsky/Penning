import numpy as np
import matplotlib.pyplot as plt

sol = np.loadtxt('2penning.res')
x = sol[:,1]
y = sol[:,2]
z = sol[:,3]
t = sol[:,0]

fig = plt.figure() #Ouverture de la figure dans laquelle nous allons tracer

#Premiere figure
plt.subplot(311)
plt.plot(t, x)
plt.title('Les coordonnees x, y et z en fonction de t.')
plt.ylabel('x(t)')

#Deuxieme figure
plt.subplot(312)
plt.plot(t, y)
plt.ylabel('y(t)')

#Troisieme figure
plt.subplot(313)
plt.plot(t, z)
plt.xlabel('Temps t')
plt.ylabel('z(t)')

#Affichage de la figure ainsi tracee
plt.show()
