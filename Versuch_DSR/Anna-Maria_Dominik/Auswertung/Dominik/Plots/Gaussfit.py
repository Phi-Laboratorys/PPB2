import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from astropy import modeling
from scipy import optimize
from scipy.optimize import fmin
from sympy import *

all_data =np.genfromtxt("all.dat",skip_header = 1, dtype=float)
fig, ax = plt.subplots()


#gauss fit
def gauss(x,a,x0,sigma, y):
    return y-a*np.exp(-(x-x0)**2/(2*sigma**2))

print(all_data)
y1 =all_data[875:1862,8]
x1 = all_data[875:1862,0]
x11=x1[0:247]
y11=y1[0:247]
x22=x1[247:444]
y22=y1[247:444]
x33=x1[592:705]
y33=y1[592:705]
x44=x1[774:944]
y44=y1[774:944]
bounds1=[0.04,153.59,2.8,0]
bounds2=[0.03,156.21,2.5,0]
bounds3=[0.025,162.92,1.5,0]
bounds4=[0.05,167.54,2.8,0.05]
popt1,pcov = optimize.curve_fit(gauss,x11,y11,bounds1)
popt2,pcov = optimize.curve_fit(gauss,x22,y22,bounds2)
popt3,pcov = optimize.curve_fit(gauss,x33,y33,bounds3)
popt4,pcov = optimize.curve_fit(gauss,x44,y44,bounds4)
#print ('popt1', popt1)


plt.plot(x1, y1,color = 'black')
plt.plot(x11, gauss(x11, *popt1),color = 'red')
plt.plot(x22, gauss(x22, *popt2),color = 'blue')
plt.plot(x33, gauss(x33, *popt3),color = 'blue')
plt.plot(x44, gauss(x44, *popt4),color = 'red')
print(popt1)
print(popt2)
print(popt3)
print(popt4)

plt.xlabel('Laser Current in mA')
plt.ylabel('amplitude in V')
print('------')
print(popt1[0]*np.sqrt(2*np.pi*popt1[2]**2))
print(popt2[0]*np.sqrt(2*np.pi*popt2[2]**2))
print(popt3[0]*np.sqrt(2*np.pi*popt3[2]**2))
print(popt4[0]*np.sqrt(2*np.pi*popt4[2]**2))
plt.show()