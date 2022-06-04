import matplotlib.pyplot as plt
import numpy as np
w = 4
h = 3
d = 70
plt.figure(figsize=(w, h), dpi=d)
x = [0, np.nan, 1, 4]
y = [0, np.nan, 2, 3]
positions = (1, 2, 3)
labels = ("A", "B", "C")
plt.xticks(positions, labels)
plt.plot(x, y)
plt.show()