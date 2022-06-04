import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#%% daten e i n l e s e n
all_data =np.genfromtxt("20092021_15_41_33_group6_60_L1.dat",skip_header = 5, dtype=float)
data_1=np.genfromtxt("l1_p1.txt", dtype=float)
x_1=data_1[:,0]
y_1=data_1[:,1]
x_all = all_data[:,0]
y_all = all_data[:,1]
#plt.plot(x,y)
a01=0.308
b01=141.88
c01=0.45
d01=0.18
#fitten
def fitFunction(x,a,b,c,d):
    return a*c/((x-b)**2+c**2)+d
p1=(a01,b01,c01,d01)#startwertefürdieparameter
fitParams1,fitCovariances=curve_fit(fitFunction,x_1,y_1,p1)
print(fitParams1)
print(fitCovariances)
#plotthedata
plt.plot(x_all,y_all)
#nowplotthebestfitcurve
plt.plot(x_1,fitFunction(x_1,fitParams1[0],fitParams1[1],fitParams1[2],fitParams1[3]))
plt.xlabel('Current (mA)')
plt.ylabel('Amplitude (V)')
#saveplottoafile
#plt.savefig('dataFitted.png',bbox_inches=0)
data_2=np.genfromtxt("l1_p2.txt", dtype=float)
x_2=data_2[:,0]
y_2=data_2[:,1]
a02=0.42
b02=142.05
c02=0.09
d02=0.3
p2=(a02,b02,c02,d02)#startwertefürdieparameter
fitParams2,fitCovariances2=curve_fit(fitFunction,x_2,y_2,p2)
plt.plot(x_2,fitFunction(x_2,fitParams2[0],fitParams2[1],fitParams2[2],fitParams2[3]))
data_3=np.genfromtxt("l1_p3.txt", dtype=float)
x_3=data_3[:,0]
y_3=data_3[:,1]
a03=0.31
b03=142.13
c03=0.05
d03=0.24
p3=(a03,b03,c03,d03)#startwertefürdieparameter
print(p3)
fitParams3,fitCovariances3=curve_fit(fitFunction,x_3,y_3,p3)
plt.plot(x_3,fitFunction(x_3,fitParams3[0],fitParams3[1],fitParams3[2],fitParams3[3]))
data_4=np.genfromtxt("l1_p4.txt", dtype=float)
x_4=data_4[:,0]
y_4=data_4[:,1]
a04=0.27
b04=142.23
c04=0.11
d04=0.25
p4=(a04,b04,c04,d04)#startwertefürdieparameter
print(p4)
fitParams4,fitCovariances4=curve_fit(fitFunction,x_4,y_4,p4)
plt.plot(x_4,fitFunction(x_4,fitParams4[0],fitParams4[1],fitParams4[2],fitParams4[3]))
data_5=np.genfromtxt("l1_p5.txt", dtype=float)
x_5=data_5[:,0]
y_5=data_5[:,1]
a05=0.31
b05=142.30
c05=0.21
d05=0.14
p5=(a05,b05,c05,d05)#startwertefürdieparameter
print(p5)
fitParams5,fitCovariances5=curve_fit(fitFunction,x_5,y_5,p5)
plt.plot(x_5,fitFunction(x_5,fitParams5[0],fitParams5[1],fitParams5[2],fitParams5[3]))


print('-------------')

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

plt.savefig('linie1.png',bbox_inches=0)
plt.show()