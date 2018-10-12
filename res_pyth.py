import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Des sites utiles
# http://python-prepa.github.io/systemes_dynamiques.html
# http://python.physique.free.fr/outils_math.html

# Constantes
wz = 2 * np.pi * 60e6
wc = 2 * np.pi * 51e9
K = (6.e7)**2 * 2 * np.pi ** 2
M = 1e14

# Systeme d'equations
def systeme(t, syst):
	q0p = syst[3]
	q1p = syst[4]
	q2p = syst[5]
	q3p = K * syst[0] - M * syst[4]
	q4p = K * syst[1] + M * syst[3]
	q5p = -2 * K * syst[2]
	return [q0p, q1p, q2p, q3p, q4p, q5p]

# Echelle des temps
t0 = 0
tfin = 1e-4
steps = 20000
t = np.linspace(t0, tfin, steps)

# Conditions initiales et resolution
q0, q1, q2 = 1e-4, 1e-4, 1e-4
q3, q4, q5 = 0, 0, 0
sol = integrate.odeint(systeme, (q0, q1, q2, q3, q4, q5), t, tfirst=1)

q0, q1, q2, q3, q4, q5 = sol.T
print(sol)

plt.plot(t, q0, linewidth=1.2)
plt.xlim((np.min(t), np.max(t)))
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.show()
