import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from astropy import modeling
from scipy import optimize
from scipy.optimize import fmin
from sympy import *

data='/Users/annapleyer/Desktop/Daten_bearbeitet_neu/Alle Linien/channel3/Channel31_dip1.dat'
df = pd.read_csv(data, sep='\s+', header=(0), skiprows=(0,1))
fig, ax = plt.subplots()


#gauss fit
def gauss(x,a,x0,sigma, y):
    return y-a*np.exp(-(x-x0)**2/(2*sigma**2))


y1 =df.iloc[2:230,1]
x1 = df.iloc[2:230,0]

popt1,pcov = optimize.curve_fit(gauss,x1,y1,bounds = ([0.0001, 142,0.0001 ,-5],[10, 143,10,5]))
print ('popt1', popt1)

m1 = y1.idxmin(axis = 0)
print ('Minimum y-Index:', m1)

m2y = min(gauss(x1, *popt1))
print('Minimum Gauß-y:', m2y)

plt.plot(x1, y1)
plt.plot(x1, gauss(x1, *popt1))

plt.xlabel('Laser Current in mA')
plt.ylabel('amplitude in V')