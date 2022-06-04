import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from astropy import modeling
from scipy import optimize
from scipy.optimize import fmin
from sympy import *

data1 =np.genfromtxt("23.txt",skip_header = 0, dtype=float)
data2 =np.genfromtxt("40.txt",skip_header = 0, dtype=float)
data3 =np.genfromtxt("60.txt",skip_header = 0, dtype=float)
fig, ax = plt.subplots()


#gauss fit
def gauss(x,a,x0,sigma, y):
    return y-a*np.exp(-(x-x0)**2/(2*sigma**2))
x11=data1[:,7]
y11=data1[:,6]
x22=data2[:,7]
y22=data2[:,6]
x33=data3[:,5]
y33=data3[:,3]
bounds1=[0.011,780.248,0.001,0]
bounds2=[0.025,780.254,0.001,0]
bounds3=[0.04,780.255,0.002,0]
popt1,pcov = optimize.curve_fit(gauss,x11,y11,bounds1,maxfev=2000)
popt2,pcov = optimize.curve_fit(gauss,x22,y22,bounds2,maxfev=2000)
popt3,pcov = optimize.curve_fit(gauss,x33,y33,bounds3,maxfev=2000)
#print ('popt1', popt1)


plt.plot(x33, y33,color = 'black')
plt.plot(x11, gauss(x11, *popt1),color = 'red')
plt.plot(x22, gauss(x22, *popt2),color = 'blue')
plt.plot(x33, gauss(x33, *popt3),color = 'blue')
print(popt1)
print(popt2)
print(popt3)

plt.xlabel('Laser Current in mA')
plt.ylabel('amplitude in V')
print('------')
plt.plot(x11,y11)
plt.plot(x22,y22)
plt.plot(x33,y33)
plt.show()