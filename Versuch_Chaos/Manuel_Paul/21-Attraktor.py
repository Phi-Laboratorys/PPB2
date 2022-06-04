# Source: http://jupiter-online.net/roessler-attraktor-zeichnen-mit-matplotlib/
# Source: http://jupiter-online.net/lorenz-attraktor-zeichnen-mit-matplotlib/

# Module importieren
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from mpl_toolkits.mplot3d import Axes3D

'''Roessler Attraktor'''
def roessler(x, y, z, a, b, c):
    dx = -(y + z)
    dy = x + a * y
    dz = b + z * (x - c)
    return dx, dy, dz

'''Lorentz Attraktor'''
def lorentz(x, y, z, a, b, c):
    dx = a * (y - x)
    dy = b * x - y - x * z
    dz = x * y - c * z
    return dx, dy, dz

def test(x ,y , z ,a ,b ,c):
    dx = a*(y-x)+y*z
    dy = b*x - y -x*z
    dz = x*y-c*z
    return dx, dy, dz

# Schrittweite und Anzahl der Schritte definieren
dt = 0.01
numSteps_r = 30000
numSteps_l = 5000
 
# Arrays für x, y und z Werte initialisieren
x_r = np.zeros(numSteps_r + 1)
y_r = np.zeros(numSteps_r + 1)
z_r = np.zeros(numSteps_r + 1)

x_l = np.zeros(numSteps_l + 1)
y_l = np.zeros(numSteps_l + 1)
z_l = np.zeros(numSteps_l + 1)
 
# Starwerte festlegen
x_r[0], y_r[0], z_r[0] = (0, 0, 0)
a_r, b_r, c_r = (0.2, 0.2, 5.7)

x_l[0], y_l[0], z_l[0] = (1.0, 1.0, 1.0)
a_l, b_l, c_l = (10, 28, 8/3)

# x, y und z Positionen Schrittweise berechnen
for i in range(numSteps_r):
    dx_r, dy_r, dz_r = roessler(x_r[i], y_r[i], z_r[i], a_r, b_r, c_r)
    x_r[i + 1] = x_r[i] + (dx_r * dt)
    y_r[i + 1] = y_r[i] + (dy_r * dt)
    z_r[i + 1] = z_r[i] + (dz_r * dt)

for i in range(numSteps_l):   
    dx_l, dy_l, dz_l = lorentz(x_l[i], y_l[i], z_l[i], a_l, b_l, c_l)
    x_l[i + 1] = x_l[i] + (dx_l * dt)
    y_l[i + 1] = y_l[i] + (dy_l * dt)
    z_l[i + 1] = z_l[i] + (dz_l * dt)
    
rc('text', usetex=True)
rc('font', family='serif',size=14)

fig = plt.figure(figsize=(8, 6), dpi=80)

ax_r = fig.add_subplot(1, 2, 1, projection='3d')
ax_l = fig.add_subplot(1, 2, 2, projection='3d')
       
ax_r.plot(x_r, y_r, z_r, lw=0.5, color='black')
ax_r.set_xlabel("x")
ax_r.set_ylabel("y")
ax_r.set_zlabel("z")
ax_r.axis('off')
#ax_r.set_title("Rössler Attraktor")

ax_l.plot(x_l, y_l, z_l, lw=1.0, color='black')
ax_l.set_xlabel("x")
ax_l.set_ylabel("y")
ax_l.set_zlabel("z")
ax_l.axis('off')
#ax_l.set_title("Lorenz Attraktor")
 
# Bild anzeigen
plt.subplots_adjust(wspace=0)
plt.show()