import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif')


data37 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=37kO/06_09_2021_19_25_22_G11_shinriki_0.dat'
data39 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=39kO/06_09_2021_19_28_22_G11_shinriki_0.dat'
data40 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=40kO/06_09_2021_19_29_53_G11_shinriki_0.dat'
data45 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=45kO/06_09_2021_19_31_20_G11_shinriki_0.dat'
data60 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=60kO/06_09_2021_19_32_51_G11_shinriki_0.dat'
data66 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=66kO/06_09_2021_19_34_38_G11_shinriki_0.dat'
data70 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=70kO/06_09_2021_19_36_25_G11_shinriki_0.dat'
data73 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=73kO/06_09_2021_19_37_54_G11_shinriki_0.dat'
data74 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=74kO/06_09_2021_19_39_09_G11_shinriki_0.dat'
data87 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=87kO/06_09_2021_19_41_14_G11_shinriki_0.dat'
data91 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=91kO/06_09_2021_19_42_12_G11_shinriki_0.dat'
data100 = 'Versuch_Chaos/Daten/Shinriki/Aufg-b/R1=100kO/06_09_2021_19_43_06_G11_shinriki_0.dat'

datE = 'Versuch_Chaos/Daten/Shinriki/Aufg-e/Rekonstruktion/06_09_2021_20_31_55_G11_shinriki_0.dat'

data = data70
df = pd.read_csv(data, delim_whitespace=True, skiprows=7, decimal=',')

#print(df.head())

v1=df['V1(V)']#[0:1000]
v2=df['V2(V)']#[0:1000]
v3=df['V3(V)']#[0:1000]

dftFreq = df['DFTfq(Hz)']
dftPow = df['DFTY(power)']


#Ploting
#fig = plt.figure()

#ax1 = fig.add_subplot(projection='3d')
#ax1.plot(v1, v2, v3, color='k')
#ax1.set_xlabel('$V_1$ in V')
#ax1.set_ylabel('$V_2$ in V')
#ax1.set_zlabel('$V_3$ in V')
#ax1.view_init(azim=145, elev=40)
#ax1.set_xlim(-2.5,2.5)
#ax1.set_ylim(-0.5,0.5)
#ax1.set_zlim(-0.5,0.5)

fig2 = plt.figure()
ax2 = fig2.add_subplot()
ax2.plot(dftFreq, dftPow, color='k')
ax2.set_xlabel('frequency in Hz')
ax2.set_ylabel('scaled power')
ax2.set_yscale('log')
ax2.set_xlim(0,10000)
ax2.grid()

plt.show()