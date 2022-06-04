import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

daten = 'Versuch_Alpha_Gamma_Spektroskopie/Programme/Umschreiben/Energieeichungkorr.csv'
df = pd.read_csv(daten)



parameter = np.polyfit(df['Topf'], df['Energie'],1)

print(parameter)

x = np.linspace(30, 800, 100)
y = x*parameter[0]+parameter[1]

#Plot an sich
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
plt.title('Energieeichgerade')
plt.xlabel('Kanalnummer')
plt.ylabel('Energie (eV)')


#Plot machen
plt.plot(df['Topf'], df['Energie'], color = 'r', marker = 'x', ls = 'None', label = 'Isotope')
plt.plot(x,y, label = 'Eichgerade')


#plt.errorbar(df['Dicke'],df['Zaehlrate (1/s)'],xerr= 0.1, yerr=popt[2],capsize = 2, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.legend()
plt.show()



