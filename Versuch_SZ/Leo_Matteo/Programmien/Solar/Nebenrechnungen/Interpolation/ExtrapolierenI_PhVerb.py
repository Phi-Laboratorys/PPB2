import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

daten = 'Programmien/Solar/Nebenrechnungen/Beleuchtungsstärke/MoniSi.csv'
df = pd.read_csv(daten)
df['P_LICHT (sun)'] = df['P_LICHT (sun)']/(282/828)
df['FF'] = np.multiply(df['I_MPP (A)'],df['U_MPP (V)'])/np.multiply(df['U_OC (V)'], df['I_PH (A)'])
df['Wirkungsgrad'] = -np.multiply(df['I_MPP (A)'],df['U_MPP (V)'])/(df['P_LICHT (sun)']*1000*(0.125**2))


daten1 = 'Programmien/Solar/Nebenrechnungen/Beleuchtungsstärke/MultiSi.csv'
df1 = pd.read_csv(daten1)
df1['P_LICHT (sun)'] = df1['P_LICHT (sun)']/(282/828)
df1['FF'] = np.multiply(df1['I_MPP (A)'],df1['U_MPP (V)'])/np.multiply(df1['U_OC (V)'], df1['I_PH (A)'])
df1['Wirkungsgrad'] = -np.multiply(df1['I_MPP (A)'],df1['U_MPP (V)'])/(df1['P_LICHT (sun)']*1000*(0.125**2))


daten2 = 'Programmien/Solar/Nebenrechnungen/Beleuchtungsstärke/CIS.csv'
df2 = pd.read_csv(daten2)
df2['P_LICHT (sun)'] = df2['P_LICHT (sun)']/(282/828)
df2['FF'] = np.multiply(df2['I_MPP (A)'],df2['U_MPP (V)'])/np.multiply(df2['U_OC (V)'], df2['I_PH (A)'])
df2['Wirkungsgrad'] = -np.multiply(df2['I_MPP (A)'],df2['U_MPP (V)'])/(df2['P_LICHT (sun)']*1000*(0.06**2)*282/828)


parameter1 = np.polyfit(df['P_LICHT (sun)'],abs(df['I_PH (A)']),1)
parameter2 = np.polyfit(df['P_LICHT (sun)'],abs(df1['I_PH (A)']),1)
parameter3 = np.polyfit(df['P_LICHT (sun)'],abs(df2['I_PH (A)']),1)
x = np.linspace(0,1,1000)
y1 = parameter1[1]+parameter1[0]*x
y2 = parameter2[1]+parameter2[0]*x
y3 = (parameter3[1]+parameter3[0]*x)


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
plt.title('Extrapolierte Werte für Photostrom $I_{Ph}$')
plt.xlabel('Intensität (sun)')
plt.ylabel('Photostrom $I_{Ph}$ (A)')

#Plotten der Funktionen selbst
#plt.plot(x_achse, mess2, color = 'r',alpha = 0.7, label = 'Übersichtsmessung ohne Filter')
plt.plot(df['P_LICHT (sun)'], abs(df['I_PH (A)']), ls = 'None', color = 'r', marker= 'x', label = 'MonoSi')
plt.plot(df1['P_LICHT (sun)'], abs(df1['I_PH (A)']),ls = 'None',color = 'b',marker= 'x', label = 'MultiSi')
plt.plot(df2['P_LICHT (sun)'], abs(df2['I_PH (A)']),ls = 'None', color = 'y',marker= 'x', label = 'CIS')
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.xlim(0,0.30)
plt.ylim(0,2)


#Fehlerbalken
plt.errorbar(df['P_LICHT (sun)'], abs(df['I_PH (A)']), xerr = 0.1*df['P_LICHT (sun)']/3, yerr=0.044,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.errorbar(df1['P_LICHT (sun)'], abs(df1['I_PH (A)']), xerr = 0.1*df['P_LICHT (sun)']/3, yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.errorbar(df2['P_LICHT (sun)'], abs(df2['I_PH (A)']), xerr = 0.1*df['P_LICHT (sun)']/3, yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)



#Plotten der Legende
plt.legend()

plt.show()
print(y1[-1])
print(y2[-1])
print(y3[-1])