import numpy as np
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc
import matplotlib.cm as cm
from scipy.signal import argrelextrema
from scipy.optimize import curve_fit
import scipy.constants as const

rc('text', usetex=True)
rc('font', family='serif', size=22)

'''
#############################
##                         ##
##      Teilaufgabe a      ##
##                         ##
#############################

data = 'Versuch_SRV/Daten/44/a/LockIn_Filter.csv'
df = pd.read_csv(data)

data41 = 'Versuch_SRV/Daten/44/a/Daten_41.csv'
df41 = pd.read_csv(data41)

df[['Usin(V)','Usquare(V)','Utri(V)']] = df[['Usin(V)','Usquare(V)','Utri(V)']]*np.sqrt(2)

x = df['f(kHz)']
y_sq, y_tri = df['Usquare(V)'], df['Utri(V)']

fig, ax = plt.subplots(figsize=(12,8), dpi=80)

# Square
theo = []
k = 1
while k < len(y_sq)+1:
    theo.append(4/np.pi * 1/(2*k-1))
    k+=1

df['U_sqTheo(V)'] = theo

df['U_sqDiff(muV)'] = abs(-df['U_sqTheo(V)'] + df['Usquare(V)'])*1E6
    
ax.plot(x,df['U_sqDiff(muV)'],'o',label='Rechteck', color='#ff7f0e')
ax.plot(x,df41['U_sqDiff(muV)'],'o',label='Rechteck aus 4.1', color='orange')
    
# tri
theo = []
k = 1
while k < len(y_tri)+1:
    theo.append(8/(np.pi**2) * 1/((2*k-1)**2))
    k+=1

df['U_triTheo(V)'] = theo

df['U_triDiff(muV)'] = abs(-df['U_triTheo(V)'] + df['Utri(V)'])*1E6

ax.plot(x,df['U_triDiff(muV)'],'o',label='Dreieck', color='#1f77b4')
ax.plot(x,df41['U_triDiff(muV)'],'o',label='Dreieck aus 4.1', color='blue')

ax.tick_params(direction = "in")
ax.set_xlabel('$f$ in kHz')
ax.set_ylabel('$\Delta U$ in $\mu$V')

axT = ax.secondary_xaxis('top')
axT.tick_params(direction = "in")
axT.xaxis.set_ticklabels([])

axR = ax.secondary_yaxis('right')
axR.tick_params(direction = "in")
axR.yaxis.set_ticklabels([])
ax.legend()

plt.savefig('Versuch_SRV/Bilder/Manuel/44/ResiduumVergleich.pdf',bbox_inches='tight')
plt.show()

print(df.to_latex())
'''
#'''
#############################
##                         ##
##      Teilaufgabe b      ##
##                         ##
#############################

data = ['Versuch_SRV/Daten/44/b/Bandbreite_30ms_6dB.csv', 'Versuch_SRV/Daten/44/b/Bandbreite_30ms_18dB.csv']
name = ['6dB', '18dB']
color = ['#ff7f0e','#1f77b4']

def response(f,t,n):
    return (1 + (2*np.pi*t*(f - 1))**2)**(-n/2)

#fig, ax = plt.subplots(figsize=(12,8),dpi=80)

for i,q,c in zip(data,name,color):
    df = pd.read_csv(i)
    
    x, y = df['f(Hz)']/1000, df['Ueff(V)']
    
    y = y/y.max()
    
    popt, _ = curve_fit(response, x, y)
    print(*popt)
    
    x_fit = np.linspace(x.min(), x.max(), 1000)
    
    fig, ax = plt.subplots(figsize=(12,8),dpi=80)
    
    ax.plot(x_fit, response(x_fit, *popt), label = 'Fit', lw=2,color=c)
    ax.plot(x,y,'o',label='Messreihe',color=c)
    #ax.plot(x_fit, response(x_fit, *popt), label = 'Fit '+q, lw=2,color=c)
    #ax.plot(x,y,'o',label='Messreihe '+q,color=c)
    
    ax.tick_params(direction = "in")
    ax.set_xlabel(r'$f$ in kHz')
    ax.set_ylabel(r'A (normiert)')

    axT = ax.secondary_xaxis('top')
    axT.tick_params(direction = "in")
    axT.xaxis.set_ticklabels([])

    axR = ax.secondary_yaxis('right')
    axR.tick_params(direction = "in")
    axR.yaxis.set_ticklabels([])
    
    ax.legend()
    plt.savefig('Versuch_SRV/Bilder/Manuel/44/'+q+'.pdf',bbox_inches='tight')
    plt.show()

#plt.savefig('Versuch_SRV/Bilder/Manuel/44/All.pdf',bbox_inches='tight')
#plt.show()
#'''