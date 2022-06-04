import numpy as np
import pandas as pd
#from scipy import optimize as opt
import matplotlib.pyplot as plt
import locale
locale.setlocale(locale.LC_ALL, "deu_deu")
import matplotlib as mpl
mpl.rcParams['axes.formatter.use_locale'] = True



daten = 'Daten/CSV/EnergieeichungCo60.csv'
df = pd.read_csv(daten)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#ax.spines['left'].set_position('center')
#ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')
ax.xaxis.set_major_formatter(x_format)  # set formatter to needed axi
#ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
#ax.xaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
#plt.ylim(0,8000)
#plt.xlim((1.15,1.2))


#Bennenung des Plots
plt.title('Comptonkanten im Co-60-Spektrum')
plt.xlabel('Energie in MeV')
plt.ylabel('Anzahl')

#Plot machen
plt.plot(df['Energie']/1e6,df['Count'], color = 'r', label = 'Aufgenommenes Spektrum')
#plt.plot([1.1,1.3],[ 6500/2,  6500/2], label = 'Halbe Peakhöhe')



#plt.errorbar(df['Dicke'],df['Zaehlrate (1/s)'],xerr= 0.1, yerr=popt[2],capsize = 2, ls = 'None',  color = 'black',elinewidth = 0.5)

plt.show()

