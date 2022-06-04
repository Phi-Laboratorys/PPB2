import numpy as np
import matplotlib.pyplot as plt

delta = 0.1
amp = 0.9
gamma = 3

b = np.linspace(0, 5, 100)

ws_p = 1 - 2*(delta**2) + 3/4*gamma*(b**2) + np.sqrt((amp/b)**2 + 4*(delta**2)*((delta**2) - (1 + 3/4*gamma*(b**2))))
ws_m = 1 - 2*(delta**2) + 3/4*gamma*(b**2) - np.sqrt((amp/b)**2 + 4*(delta**2)*((delta**2) - (1 + 3/4*gamma*(b**2))))


w_pp = np.sqrt(ws_p)
w_pm = np.sqrt(ws_m)
w_mp = -np.sqrt(ws_p)
w_mm = -np.sqrt(ws_m)

plt.plot(w_pp,b)
plt.plot(w_pm,b)
plt.xlim(0,5)
plt.ylim(0,5)
plt.plot(w_mp,b)
plt.plot(w_mm,b)

plt.show()