import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import rc

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=15)

'''
#############################
##                         ##
##     Teilaufgabe a1      ##
##                         ##
#############################

data1 = 'Versuch_SRV/04-Versuchsauswertung/Paul/42a1.csv'

df1 = pd.read_csv(data1)

#print(df.head())
fig1, ax1 = plt.subplots(figsize=(12, 6), dpi=80)

x_tast = np.linspace(0, 40)
y_tast = (1/2)*x_tast

ax1.plot(df1['$f_{Abtast}$ in kHz'], df1['$f_{Mes} in kHz$'], 'o', linestyle='-', label='Messpunkte')
ax1.plot([40,40], [0,21], linestyle='--', color='gray', label=r'$f_\mathrm{crit}$')
ax1.plot(x_tast, y_tast, linestyle='--', color='r', label=r'$\frac{1}{2}\cdot f_\mathrm{Abtast}$')

ax1.tick_params(direction = "in")
ax1.set_xlabel(r'$f_\mathrm{Abtast}$ in kHz')
ax1.set_ylabel(r'$f_\mathrm{Mess}$ in kHz')

ax1T = ax1.secondary_xaxis('top')
ax1T.tick_params(direction = "in")
ax1T.xaxis.set_ticklabels([])
ax1R = ax1.secondary_yaxis('right')
ax1R.tick_params(direction = "in")
ax1R.yaxis.set_ticklabels([])

ax1.legend()
plt.savefig('Versuch_SRV/Bilder/Paul/42a1.pdf', bbox_inches = 'tight')
plt.show()
'''

'''
#############################
##                         ##
##     Teilaufgabe a1      ##
##                         ##
#############################
    
data2 = 'Versuch_SRV/04-Versuchsauswertung/Paul/42a2.csv'

df2 = pd.read_csv(data2)

#print(df.head())
fig2, ax2 = plt.subplots(figsize=(12, 6), dpi=80)

ax2.plot(df2['$f_{Quelle}$ in kHz'], df2['$f_{Mes} in kHz$'], 'o', label='Messpunkte')
ax2.plot([10,10], [0,11], linestyle='--', color='gray', label=r'$f_\mathrm{crit}$')

ax2.tick_params(direction = "in")
ax2.set_xlabel(r'$f_\mathrm{Quelle}$ in kHz')
ax2.set_ylabel(r'$f_\mathrm{Mess}$ in kHz')

ax2T = ax2.secondary_xaxis('top')
ax2T.tick_params(direction = "in")
ax2T.xaxis.set_ticklabels([])
ax2R = ax2.secondary_yaxis('right')
ax2R.tick_params(direction = "in")
ax2R.yaxis.set_ticklabels([])

ax2.legend()
plt.savefig('Versuch_SRV/Bilder/Paul/42a2.pdf', bbox_inches = 'tight')
plt.show()
'''

#'''
#############################
##                         ##
##      Teilaufgabe b      ##
##                         ##
#############################
    
data = 'Versuch_SRV/Daten/42/b/05_10_2021_13_30_44_G11_sampling_42b_Dreieck_f3kHz_A1V_fs7kHz.dat'

df = pd.read_csv(data, skiprows=3, sep='\s+')
df = df.sort_values(by=['Fqscale-FFT'])

#print(df.head())
fig, ax = plt.subplots(figsize=(12, 6), dpi=80)

ax.plot(df['Fqscale-FFT']/1000, df['y-FFTcurve'], color='black')

ax.tick_params(direction = "in")
ax.set_xlabel(r'$f$ in kHz')
ax.set_ylabel(r'$A$ in dB')

axT = ax.secondary_xaxis('top')
axT.tick_params(direction = "in")
axT.xaxis.set_ticklabels([])
axR = ax.secondary_yaxis('right')
axR.tick_params(direction = "in")
axR.yaxis.set_ticklabels([])

plt.savefig('Versuch_SRV/Bilder/Paul/42b-fs7kHz.pdf', bbox_inches = 'tight')
plt.show()
#'''