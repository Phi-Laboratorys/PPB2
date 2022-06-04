import numpy as np
from scipy.signal import argrelextrema

data = np.loadtxt('dicke.txt',skiprows=1)
print(data[0])
angel = data[:,3]
value = data[:,1]
print(value)
minimums = argrelextrema(value, np.greater)
n=np.array([])
for i in minimums:
    n=np.append(n,value[i])
print(np.shape(n))
