import numpy as np
import pandas as pd
#from scipy import optimize as opt
import matplotlib.pyplot as plt


daten = 'Versuch_Alpha_Gamma_Spektroskopie/Daten/CSV/Uranerz.csv'
df = pd.read_csv(daten)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#ax.spines['left'].set_position('center')
#ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')
#plt.ylim((0,0.5))
#plt.xlim((0,:))


#Bennenung des Plots
plt.title('Gammaspektum Uranerz')
plt.xlabel('Energie in MeV')
plt.ylabel('Count (arb. u.)')


#Plot machen
plt.plot(df['Energie']/1e6,df['Count'], color = 'r')


#plt.errorbar(df['Dicke'],df['Zaehlrate (1/s)'],xerr= 0.1, yerr=popt[2],capsize = 2, ls = 'None',  color = 'black',elinewidth = 0.5)

plt.show()

