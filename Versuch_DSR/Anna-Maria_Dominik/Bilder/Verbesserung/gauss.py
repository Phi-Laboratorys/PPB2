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
p1='C:/Users/froes\Documents/GitHub/PPB2-Fortgeschrittenes-Praktikum/3. Dopplerfreie Spektroskopie von Rubidium/Auswertung/Dominik/Plots/l1_p1.txt'
p2='C:/Users/froes\Documents/GitHub/PPB2-Fortgeschrittenes-Praktikum/3. Dopplerfreie Spektroskopie von Rubidium/Auswertung/Dominik/Plots/l1_p2.txt'
p3='C:/Users/froes\Documents/GitHub/PPB2-Fortgeschrittenes-Praktikum/3. Dopplerfreie Spektroskopie von Rubidium/Auswertung/Dominik/Plots/l1_p3.txt'
p4='C:/Users/froes\Documents/GitHub/PPB2-Fortgeschrittenes-Praktikum/3. Dopplerfreie Spektroskopie von Rubidium/Auswertung/Dominik/Plots/l1_p4.txt'
p5='C:/Users/froes\Documents/GitHub/PPB2-Fortgeschrittenes-Praktikum/3. Dopplerfreie Spektroskopie von Rubidium/Auswertung/Dominik/Plots/l1_p5.txt'
#df = pd.read_csv(data, sep='\s+', header=(0), skiprows=(0,1,2,3,4))
fig, ax = plt.subplots()
data2 = np.loadtxt(data,skiprows=5)
data1 = np.loadtxt(data3,skiprows=2)
#'''
p1 = np.loadtxt(p1)
p2 = np.loadtxt(p2)
p3 = np.loadtxt(p3)
p4 = np.loadtxt(p4)
p5 = np.loadtxt(p5)
#'''
x1=data1[400:1370,0]
y1=data1[400:1370:,8]
intensity = data1[400:1370:,11]
#'''
#intensity = data2[300:1300,5]

x2=data2[300:1300,0]
y2=data2[300:1300,1]
#'''
lp1x=p1[:,0]
lp1y=p1[:,1]
lp2x=p2[:,0]
lp2y=p2[:,1]
lp3x=p3[:,0]
lp3y=p3[:,1]
lp4x=p4[:,0]
lp4y=p4[:,1]
lp5x=p5[:,0]
lp5y=p5[:,1]
#'''
p1x=data1[400:620,0]
p1y=data1[400:620,8]
p2x=data1[620:900,0]
p2y=data1[620:900,8]
p3x=data1[900:1120,0]
p3y=data1[900:1120,8]
p4x=data1[1120:1300,0]
p4y=data1[1120:1300,8]
#gauss fit
def gauss(x,a,x0,sigma, y):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))+y
def loentz(x,a,x0,sigma, y):
    return a*x0/((x-x0)**2+sigma**2)+y
#B Gauss
b1=[-0.02,142.26,1.5,0]
b2=[-0.04,147.33,1.3,0]
b3=[-0.05,153.33,1.8,0]
b4=[-0.03,156.26,1.2,0]
#Fits Gauss
popt1,pcov = optimize.curve_fit(gauss,p1x,p1y,b1,maxfev=10000)
popt2,pcov = optimize.curve_fit(gauss,p2x,p2y,b2,maxfev=10000)
popt3,pcov = optimize.curve_fit(gauss,p3x,p3y,b3,maxfev=10000)
popt4,pcov = optimize.curve_fit(gauss,p4x,p4y,b4,maxfev=10000)

'''#B Lorentz
b1=[0.31,141.88,0.45,0.18]
b2=[0.42,142.05,0.09,0.30]
b3=[0.31,142.13,0.05,0.24]
b4=[0.27,142.23,0.11,0.25]
b5=[0.31,142.3,0.21,0.14]
#y1 =df.iloc[6:198742,1]
#x1 = df.iloc[6:198742,0]
'''
'''#Fits Lorentz
popt1,pcov = optimize.curve_fit(loentz,lp1x,lp1y,b1,maxfev=10000)

popt2,pcov = optimize.curve_fit(loentz,lp2x,lp2y,b2,maxfev=10000)
popt3,pcov = optimize.curve_fit(loentz,lp3x,lp3y,b3,maxfev=10000)
popt4,pcov = optimize.curve_fit(loentz,lp4x,lp4y,b4,maxfev=10000)
popt5,pcov = optimize.curve_fit(loentz,lp5x,lp5y,b5,maxfev=10000)
#print ('popt1', popt1)
'''
'''#Test nicht beachten
m1 = y1.idxmin(axis = 0)
print ('Minimum y-Index:', m1)

m2y = min(gauss(x1, *popt1))
print('Minimum Gauß-y:', m2y)

popt1=[0.086,40.93,1.65540785, 0.029]'''

peaks = sp.find_peaks(intensity, prominence=0.002)
plt.plot(x1, y1,color='black',marker='o')
peaks = peaks[0]
print(len(peaks))
xI=[]
yI=[]
for i in peaks:
    xI.append(x1[i])
    yI.append(intensity[i])
n=[0]
print(np.mean(xI))
m=[]
for i in range(len(xI)-1):
    m.append(xI[i]-xI[i+1])
    
print((xI[-1]-xI[0])/(len(xI)-1))
print(np.sqrt(((xI[-1]-xI[0])/(len(xI)-1)**2)**2+2*(0.01/(len(xI)-1))**2))#Mittlere Distance ignorieren
for i in range(len(xI)-1):
    a = (i+1)*0.1154#FSR Berechenn
    n.append(round(a,2))
a=[]
b=[]
#plt.plot(xI, yI,color='black',marker='o') # Überprüfung FPI Peaks
print(n)
for i in range(len(n)):#Nur jeden n-ten Peak anzeigen
    if(i%10==0):
        print(i)
        a.append(xI[i])
        b.append(n[i])
print(a)
print(b)
a=a[:]#Peaks auschließen, damit die range der Peaks im dafür vorgesehenen Bereich liegt
b=b[:]
#Plot Gauss
plt.plot(p1x, gauss(p1x, *popt1),color='blue')
plt.plot(p2x, gauss(p2x, *popt2),color='red')
plt.plot(p3x, gauss(p3x, *popt3),color='red')
plt.plot(p4x, gauss(p4x, *popt4),color='blue')

'''#Plot Lorentz
plt.plot(lp1x, loentz(lp1x, *popt1),color='orange')
plt.plot(lp2x, loentz(lp2x, *popt2),color='green')
plt.plot(lp3x, loentz(lp3x, *popt3),color='red')
plt.plot(lp4x, loentz(lp4x, *popt4),color='black')
plt.plot(lp5x, loentz(lp5x, *popt5),color='brown')
'''
#plt.plot(xI,yI)
plt.xticks(a,b)#Relative Frequency
plt.xlabel('realtive frequency [GHz]')
plt.ylabel('amplitude [V]')
print('---------')
#print(popt1)

plt.show()