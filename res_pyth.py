from scipy import *
from matplotlib.pyplot import *
from pylab import *
from scipy.integrate import odeint

# Des sites utiles
# http://python-prepa.github.io/systemes_dynamiques.html
# http://python.physique.free.fr/outils_math.html

# Constantes
wz = 2 * np.pi * 60e6
wc = 2 * np.pi * 51e9
K = wz * wz / 2
M = wc

# Systeme d'equations
def systeme(syst, t):
	syst = [q0,q1,q2,q3,q4,q5]
	q0p = q3
	q1p = q4
	q2p = q5
	q3p = K * q0 - M * q4
	q4p = K * q1 + M * q3
	q5p = -2 * K * q2
	return [q0p, q1p, q2p, q3p, q4p, q5p]

# Echelle des temps
t0 = 0
tfin = 1e-4
steps = 20000
t = np.linspace(t0,tfin,steps)

# Conditions initiales et resolution
q0, q1, q2 = 0, 0, 1e-4
q3, q4, q5 = 0, 0, 0
sol = odeint(systeme, (q0,q1,q2,q3,q4,q5), t)

q0,q1,q2,q3,q4,q5 = sol.T
print(q2)
print(q5)

plt.plot(t,q5)

show()
