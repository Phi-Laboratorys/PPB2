import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

daten = 'Beleuchtungsstärke/MoniSi.csv'
df = pd.read_csv(daten)
df['FF'] = np.multiply(df['I_MPP (A)'],df['U_MPP (V)'])/np.multiply(df['U_OC (V)'], df['I_PH (A)'])
df['Wirkungsgrad'] = -np.multiply(df['I_MPP (A)'],df['U_MPP (V)'])/(df['P_LICHT (sun)']*1000*(0.125**2))


daten1 = 'Beleuchtungsstärke/MultiSi.csv'
df1 = pd.read_csv(daten1)
df1['FF'] = np.multiply(df1['I_MPP (A)'],df1['U_MPP (V)'])/np.multiply(df1['U_OC (V)'], df1['I_PH (A)'])
df1['Wirkungsgrad'] = -np.multiply(df1['I_MPP (A)'],df1['U_MPP (V)'])/(df1['P_LICHT (sun)']*1000*(0.125**2))


daten2 = 'Beleuchtungsstärke/CIS.csv'
df2 = pd.read_csv(daten2)
df2['FF'] = np.multiply(df2['I_MPP (A)'],df2['U_MPP (V)'])/np.multiply(df2['U_OC (V)'], df2['I_PH (A)'])
df2['Wirkungsgrad'] = -np.multiply(df2['I_MPP (A)'],df2['U_MPP (V)'])/(df2['P_LICHT (sun)']*1000*(0.06**2)*282/828)



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
plt.title('Wirkungsgrad in Abhängigkeit der Intensität')
plt.xlabel('Intensität (sun)')
plt.ylabel('Wirkungsgrad $\eta$')

#Plotten der Funktionen selbst
#plt.plot(x_achse, mess2, color = 'r',alpha = 0.7, label = 'Übersichtsmessung ohne Filter')
plt.plot(df['P_LICHT (sun)'], df['Wirkungsgrad'], ls = 'None', color = 'r', marker= 'x', label = 'MonoSi')
plt.plot(df1['P_LICHT (sun)'], df1['Wirkungsgrad'],ls = 'None',color = 'b',marker= 'x', label = 'MultiSi')
plt.plot(df2['P_LICHT (sun)'], df2['Wirkungsgrad'],ls = 'None', color = 'y',marker= 'x', label = 'CIS')


#Fehlerbalken
plt.errorbar(df['P_LICHT (sun)'], df['Wirkungsgrad'], yerr=0.044,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.errorbar(df1['P_LICHT (sun)'], df1['Wirkungsgrad'], yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.errorbar(df2['P_LICHT (sun)'], df2['Wirkungsgrad'], yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)



"""
#Benennung des Plots
plt.title('Photostrom in Abhängigkeit der Intensität')
plt.xlabel('Intensität (sun)')
plt.ylabel('Betrag des Photostrom $|I_{PH}|$ (A)')

#Plotten der Funktionen selbst
#plt.plot(x_achse, mess2, color = 'r',alpha = 0.7, label = 'Übersichtsmessung ohne Filter')
plt.plot(df['P_LICHT (sun)'], abs(df['I_PH (A)']), ls = 'None', color = 'r', marker= 'x', label = 'MonoSi')
plt.plot(df1['P_LICHT (sun)'], abs(df1['I_PH (A)']),ls = 'None',color = 'b',marker= 'x', label = 'MultiSi')
plt.plot(df2['P_LICHT (sun)'], abs(df2['I_PH (A)']),ls = 'None', color = 'y',marker= 'x', label = 'CIS')


#Fehlerbalken
plt.errorbar(df['P_LICHT (sun)'], abs(df['I_PH (A)']), yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.errorbar(df1['P_LICHT (sun)'], abs(df1['I_PH (A)']), yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.errorbar(df2['P_LICHT (sun)'], abs(df2['I_PH (A)']), yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)

"""
"""
#Benennung des Plots
plt.title('Leerlaufspannung in Abhängigkeit der Lichtintensität')
plt.xlabel('Lichtintensität (sun)')
plt.ylabel('Betrag der Leerlaufspannung $|U_{OC}|$ (V)')

#Plotten der Funktionen selbst
#plt.plot(x_achse, mess2, color = 'r',alpha = 0.7, label = 'Übersichtsmessung ohne Filter')
plt.plot(df['P_LICHT (sun)'], abs(df['U_OC (V)']), ls = 'None', color = 'r', marker= 'x', label = 'MonoSi')
plt.plot(df1['P_LICHT (sun)'], abs(df1['U_OC (V)']),ls = 'None',color = 'b',marker= 'x', label = 'MultiSi')
plt.plot(df2['P_LICHT (sun)'], abs(df2['U_OC (V)']),ls = 'None', color = 'y',marker= 'x', label = 'CIS')


#Fehlerbalken
plt.errorbar(df['P_LICHT (sun)'], abs(df['U_OC (V)']), yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.errorbar(df1['P_LICHT (sun)'], abs(df1['U_OC (V)']), yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.errorbar(df2['P_LICHT (sun)'], abs(df2['U_OC (V)']), yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
"""
"""
#Benennung des Plots
plt.title('Leistung am $MPP$ in Abhängigkeit der Lichtintensität')
plt.xlabel('Lichtintensität (sun)')
plt.ylabel('Leistung $|P_{max}|$ (W)')

#Plotten der Funktionen selbst
#plt.plot(x_achse, mess2, color = 'r',alpha = 0.7, label = 'Übersichtsmessung ohne Filter')
plt.plot(df['P_LICHT (sun)'], abs(df['U_MPP (V)']*df['I_MPP (A)']), ls = 'None', color = 'r', marker= 'x', label = 'MonoSi')
plt.plot(df1['P_LICHT (sun)'], abs(df1['U_MPP (V)']*df1['I_MPP (A)']),ls = 'None',color = 'b',marker= 'x', label = 'MultiSi')
plt.plot(df2['P_LICHT (sun)'], abs(df2['U_MPP (V)']*df2['I_MPP (A)']),ls = 'None', color = 'y',marker= 'x', label = 'CIS')


#Fehlerbalken
plt.errorbar(df['P_LICHT (sun)'], abs(df['U_MPP (V)']*df['I_MPP (A)']), yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.errorbar(df1['P_LICHT (sun)'], abs(df1['U_MPP (V)']*df1['I_MPP (A)']), yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.errorbar(df2['P_LICHT (sun)'], abs(df2['U_MPP (V)']*df2['I_MPP (A)']), yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
"""


"""#Benennung des Plots
plt.title('Füllfaktor $FF$ ')
plt.xlabel('Lichtintensität (sun)')
plt.ylabel('Füllfaktor $FF$')

#Plotten der Funktionen selbst
#plt.plot(x_achse, mess2, color = 'r',alpha = 0.7, label = 'Übersichtsmessung ohne Filter')
plt.plot(df['P_LICHT (sun)'], abs((df['U_MPP (V)']*df['I_MPP (A)'])/(df['U_OC (V)']*df['I_PH (A)'])), ls = 'None', color = 'r', marker= 'x', label = 'MonoSi')
plt.plot(df1['P_LICHT (sun)'], abs((df1['U_MPP (V)']*df1['I_MPP (A)'])/(df1['U_OC (V)']*df1['I_PH (A)'])),ls = 'None',color = 'b',marker= 'x', label = 'MultiSi')
plt.plot(df2['P_LICHT (sun)'], abs(np.multiply(df2['U_MPP (V)'],df2['I_MPP (A)'])/np.multiply(df2['U_OC (V)'],df2['I_PH (A)'])),ls = 'None', color = 'y',marker= 'x', label = 'CIS')


#Fehlerbalken
plt.errorbar(df['P_LICHT (sun)'], abs((df['U_MPP (V)']*df['I_MPP (A)'])/(df['U_OC (V)']*df['I_PH (A)'])), yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.errorbar(df1['P_LICHT (sun)'], abs((df1['U_MPP (V)']*df1['I_MPP (A)'])/(df1['U_OC (V)']*df1['I_PH (A)'])), yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.errorbar(df2['P_LICHT (sun)'], abs(np.multiply(df2['U_MPP (V)'],df2['I_MPP (A)'])/np.multiply(df2['U_OC (V)'],df2['I_PH (A)'])), yerr=0.04,capsize = 3, ls = 'None',  color = 'black',elinewidth = 0.5)

plt.ylim((0,0.9))"""

#Plotten der Legende
plt.legend()

plt.show()