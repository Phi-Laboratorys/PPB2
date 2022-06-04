import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from astropy import modeling
from scipy import optimize
from scipy.optimize import fmin
from sympy import *

data='C:/Users/froes/Documents/GitHub/PPB2-Fortgeschrittenes-Praktikum/5. FTS/Protokoll_Messung/Bereinigt/peaks_Natrium_einhuellende1.txt'
data3='C:/Users/froes/Documents/GitHub/PPB2-Fortgeschrittenes-Praktikum/5. FTS/Protokoll_Messung/Bereinigt/Natrium_einhuellende_0.dat'
#df = pd.read_csv(data, sep='\s+', header=(0), skiprows=(0,1,2,3,4))
fig, ax = plt.subplots()
data2 = np.loadtxt(data3,skiprows=5)
data1 = np.loadtxt(data,skiprows=1)
x1=data1[:,0]
y1=data1[:,1]
x2=data2[:,0]
y2=data2[:,1]
#gauss fit
def gauss(x,a,x0,sigma, y):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))+y

b=[0.095,41.23,5.4,0.02]
#y1 =df.iloc[6:198742,1]
#x1 = df.iloc[6:198742,0]

popt2,pcov = optimize.curve_fit(gauss,x2,y2,b)
#print ('popt1', popt1)
'''
m1 = y1.idxmin(axis = 0)
print ('Minimum y-Index:', m1)

m2y = min(gauss(x1, *popt1))
print('Minimum Gauß-y:', m2y)
'''
popt1=[0.086,40.93,1.65540785, 0.029]
plt.plot(x2, y2,color='blue')
plt.plot(x2, gauss(x2, *popt2),color='red')
#plt.plot(x2, gauss(x2, *popt1),color='orange')


plt.xlabel('Position [mm]')
plt.ylabel('Intensiät [V]')
plt.show()