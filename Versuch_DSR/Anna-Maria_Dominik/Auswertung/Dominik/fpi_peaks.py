import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from astropy import modeling
from scipy import optimize
from scipy.optimize import fmin
from sympy import *
import scipy.signal as sp

data='C:/Users/froes\Documents/GitHub/PPB2-Fortgeschrittenes-Praktikum/3. Dopplerfreie Spektroskopie von Rubidium/Auswertung/Dominik/Plots/20092021_15_41_33_group6_60_L1.dat'
data3='C:/Users/froes/Documents/GitHub/PPB2-Fortgeschrittenes-Praktikum/3. Dopplerfreie Spektroskopie von Rubidium/Protokoll_Messung/Daten_60_bearbeitet/Alle Linien/L_b1.dat'
#df = pd.read_csv(data, sep='\s+', header=(0), skiprows=(0,1,2,3,4))
fig, ax = plt.subplots()
data2 = np.loadtxt(data,skiprows=5)
data1 = np.loadtxt(data,skiprows=5)
x1=data1[:,0]
y1=data1[:,2]
intensity = data1[400:1370:,5]
'''
x2=data2[:,0]
y2=data2[:,1]
p1x=data1[400:610,0]
p1y=data1[400:610,8]
p2x=data1[610:900,0]
p2y=data1[610:900,8]
p3x=data1[900:1123,0]
p3y=data1[900:1123,8]
p4x=data1[1123:1370,0]
p4y=data1[1123:1370,8]
'''
#gauss fit
def gauss(x,a,x0,sigma, y):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))+y

b1=[-0.02,142.27,1,0]
b2=[-0.04,147.33,1.25,0]
b3=[-0.05,153.53,1,0]
b4=[-0.03,156.24,1.25,0]
#y1 =df.iloc[6:198742,1]
#x1 = df.iloc[6:198742,0]

#popt1,pcov = optimize.curve_fit(gauss,p1x,p1y,b1)
#popt2,pcov = optimize.curve_fit(gauss,p2x,p2y,b2)
#popt3,pcov = optimize.curve_fit(gauss,p3x,p3y,b3)
#popt4,pcov = optimize.curve_fit(gauss,p4x,p4y,b4)
#print ('popt1', popt1)
'''
m1 = y1.idxmin(axis = 0)
print ('Minimum y-Index:', m1)

m2y = min(gauss(x1, *popt1))
print('Minimum Gauß-y:', m2y)

popt1=[0.086,40.93,1.65540785, 0.029]'''

peaks = sp.find_peaks(intensity, prominence=0.002)
plt.plot(x1, y1,color='black',marker="o")
peaks = peaks[0]
print(len(peaks))
xI=[]
yI=[]
for i in peaks:
    xI.append(x1[i])
    yI.append(intensity[i])
n=[0]
for i in range(len(xI)-1):
    a = (i+1)*0.1154
    n.append(round(a,2))
a=[]
b=[]
print(n)
for i in range(len(n)):
    if(i%1==0):
        print(i)
        a.append(xI[i])
        b.append(n[i])
print(a)
print(b)
#plt.plot(p1x, gauss(p1x, *popt1),color='blue')
#plt.plot(p2x, gauss(p2x, *popt2),color='red')
#plt.plot(p3x, gauss(p3x, *popt3),color='red')
#plt.plot(p4x, gauss(p4x, *popt4),color='blue')

#plt.plot(xI,yI)
#plt.xticks(a,b)
plt.xlabel('realtive frequency [GHz]')
plt.ylabel('amplitude [V]')
plt.show()