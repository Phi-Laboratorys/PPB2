from matplotlib.pyplot import colorbar
import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif',size=20)

data = ['Versuch_Chaos/Daten/Pendel/3.3b/1/06_09_2021_17_21_54_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3b/2/06_09_2021_17_20_15_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3b/3/06_09_2021_17_23_41_G11_pendel_0.dat']


df1 = pd.read_csv(data[0], delim_whitespace=True, skiprows=7, decimal=',')
 
df1 = df1[['t(s)','Ua(V)','-dUa/dt(V)']]
df1 = df1.dropna()

x_p1, y_p1 =  df1['Ua(V)'], df1['-dUa/dt(V)']

plt.figure(figsize=(12, 8), dpi=80)

#plt.plot(x_p1,y_p1,label='Schwingung 1')
plt.plot(x_p1[0:len(df1)-1],y_p1[0:len(df1)-1],label='Schwingung 1')
#plt.plot(x_p1[1150:len(df1)-1],y_p1[1150:len(df1)-1],label='Schwingung 1')
#plt.plot(x_p1[len(df1)-1],y_p1[len(df1)-1],'x',color='g')
#plt.plot(x_p1[1150],y_p1[1150],'x',color='r')

df2 = pd.read_csv(data[1], delim_whitespace=True, skiprows=7, decimal=',')
 
df2 = df2[['t(s)','Ua(V)','-dUa/dt(V)']]
df2 = df2.dropna()

x_p2, y_p2 =  df2['Ua(V)'], df2['-dUa/dt(V)']

#plt.plot(x_p2,y_p2,label='Schwingung 2')
plt.plot(x_p2[239:len(df2)-1],y_p2[239:len(df2)-1],label='Schwingung 2')
#plt.plot(x_p2[1389:len(df2)-1],y_p2[1389:len(df2)-1],label='Schwingung 2')
#plt.plot(x_p2[len(df2)-1],y_p2[len(df2)-1],'x',color='g',label='Startpunkt')
#plt.plot(x_p2[1389],y_p2[1389],'x',color='r',label='Endpunkt')

print(df1['t(s)'][len(df1)-1]-df1['t(s)'][0]-(df2['t(s)'][len(df2)-1]-df2['t(s)'][239]))

plt.xlabel(r'$U_a$ in V')
plt.ylabel(r'$\dot{U_a}$ in $\frac{\mathrm{V}}{\mathrm{s}}$')

plt.legend()
#plt.savefig("Versuch_Chaos/Bilder/Pendel/3.3b/Startwert.pdf",bbox_inches='tight')
plt.savefig("Versuch_Chaos/Bilder/Pendel/3.3b/Schwinungall.pdf",bbox_inches='tight')
plt.show()

