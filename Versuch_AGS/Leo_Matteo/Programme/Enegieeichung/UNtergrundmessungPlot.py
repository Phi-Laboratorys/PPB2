import numpy as np
import pandas as pd
#from scipy import optimize as opt
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr



def func(x, pos):  # formatter function takes tick label and tick position
    s = str(x)
    ind = s.index('.')
    return s[:ind] + ',' + s[ind+1]   # change dot to comma

y_format = tkr.FuncFormatter(func)  # make formatter


daten = 'Daten/CSV/EnergieeichungCs137.csv'
d1 = pd.read_csv(daten)

daten2 = 'Daten/CSV/Energieeichung_Am.csv'
d2 = pd.read_csv(daten2)

daten3 = 'Daten/CSV/EnergieeichungCo60.csv'
d3 = pd.read_csv(daten3)

d1['Count'] = d1['Count']/np.max(d1['Count'])
d2['Count'] = d2['Count']/np.max(d2['Count'])
d3['Count'] = d3['Count']/np.max(d3['Count'])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#ax.spines['left'].set_position('center')
#ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_major_formatter(y_format)  # set formatter to needed axi
ax.yaxis.set_major_formatter(y_format)
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')
#plt.ylim((0,0.5))
#plt.xlim((0,:))


#Bennenung des Plots
plt.title('Spektrallinien Energieeichung')
plt.xlabel('Energie in MeV')
plt.ylabel('Anzahl der Zerfälle (normiert auf 1)')


#Plot machen
plt.plot(d1['Energie']/1e9,d1['Count'],label = 'Cs-137')
plt.plot(d2['Energie']/1e6,d2['Count'], label = 'Am-241')
plt.plot(d3['Energie']/1e6,d3['Count'], label = 'Co-60')


#plt.errorbar(df['Dicke'],df['Zaehlrate (1/s)'],xerr= 0.1, yerr=popt[2],capsize = 2, ls = 'None',  color = 'black',elinewidth = 0.5)
plt.legend()
plt.show()

