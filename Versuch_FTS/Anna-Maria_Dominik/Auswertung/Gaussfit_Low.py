import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from astropy import modeling
from scipy import optimize
from scipy.optimize import fmin
from sympy import *

data='/Users/annapleyer/Desktop/FTS/Einhüllende/hg-low_einhuellende_1.dat'
df = pd.read_csv(data, sep='\s+', header=(0), skiprows=(0,1,2,3,4))
fig, ax = plt.subplots()


#gauss fit
def gauss(x,a,x0,sigma, y):
    return y-a*np.exp(-(x-x0)**2/(2*sigma**2))


y1 =df.iloc[6:198742,1]
x1 = df.iloc[6:198742,0]

popt1,pcov = optimize.curve_fit(gauss,x1,y1,bounds = ([-3, 40.2,0.0001 ,-50],[10, 41.2,14,50]))
print ('popt1', popt1)

m1 = y1.idxmin(axis = 0)
print ('Minimum y-Index:', m1)

m2y = min(gauss(x1, *popt1))
print('Minimum Gauß-y:', m2y)

plt.plot(x1, y1)
plt.plot(x1, gauss(x1, *popt1))


plt.xlabel('Position in mm')
plt.ylabel('Intensiät in V')