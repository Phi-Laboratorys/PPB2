import numpy as np
import pandas as pd
from scipy import optimize as opt
import matplotlib.pyplot as plt

#Deklaration
def Zerfall(x, A0, mu, rausch):
    return A0*np.exp(-x*mu)+rausch







daten = 'Daten/CSV/AbsobtionskoeffizeintAlu.csv'
df = pd.read_csv(daten)

df['Zaehlrate (1/s)'] = df['Integral']/df['Zeit']

#Fitten des Graphen
popt, pcov = opt.curve_fit(Zerfall, df['Dicke'],df['Zaehlrate (1/s)'])

perr = np.sqrt(np.diag(pcov))

print('Linearer Absortionksoeffizient: '+str(popt[1]))
print('Fehler linearer Absortionksoeffizient: '+str(perr[1]))


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#ax.spines['left'].set_position('center')
#ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')
#plt.ylim((0,0.5))


#Bennenung des Plots
plt.title('Gefittete Exponentialfunktion bei Aluminium')
plt.xlabel('Dicke $d$ (cm)')
plt.ylabel('Zählrate (cps)')


#Plot machen
plt.plot(df['Dicke'],df['Zaehlrate (1/s)'], marker = 'x', color = 'r', ls = 'None')
plt.plot(np.linspace(0,df.iloc[-1,0]*1.1,100),Zerfall(np.linspace(0,df.iloc[-1,0]*1.1,100),popt[0],popt[1],popt[2]))

plt.errorbar(df['Dicke'],df['Zaehlrate (1/s)'],xerr= 0.1, yerr=popt[2],capsize = 2, ls = 'None',  color = 'black',elinewidth = 0.5)

plt.show()

