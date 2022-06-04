import numpy as np
import pandas as pd
#from scipy import optimize as opt
import matplotlib.pyplot as plt


daten = 'Versuch_Alpha_Gamma_Spektroskopie/Daten/CSV/Uranerzergebins.csv'
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
plt.title('Massenabsorptionskoeffizient Blei')
plt.xlabel('Energie in MeV')
plt.ylabel('Linearer Absorptionskoeffizient')


#Plot machen
plt.plot(df['Energie']/1e6,df['Abs']/11.342, color = 'r', ls = 'None', marker = 'x')


plt.errorbar(df['Energie']/1e6,df['Abs']/11.342,yerr= df['s_Abs']/11.342, capsize = 2, ls = 'None',  color = 'black',elinewidth = 0.5)

plt.show()

