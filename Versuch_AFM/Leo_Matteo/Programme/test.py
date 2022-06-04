import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(0,20,100)
y = np.cos(x)
ax.plot(x,y,ls = ':')
plt.show()