import numpy as np
import pandas as pd
from scipy import optimize as opt
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr


#Deklaration
#Komma im Plot
def func(x, pos):  # formatter function takes tick label and tick position
    s = str(x)
    ind = s.index('.')
    return s[:ind] + ',' + s[ind+1]   # change dot to comma

y_format = tkr.FuncFormatter(func)  # make formatter



daten = 'Daten/CSV/Pilze.csv'
df = pd.read_csv(daten)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#ax.spines['left'].set_position('center')
#ax.spines['bottom'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
ax.xaxis.set_major_formatter(y_format)  # set formatter to needed axi
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')
#plt.ylim((0,0.5))


#Bennenung des Plots
plt.title('Gammaspektum der Pilze')
plt.xlabel('Energie in MeV')
plt.ylabel('Anzahl der Zerfälle')


#Plot machen
plt.plot(df['Energie']/1e6,df['Count'], color = 'r')


#plt.errorbar(df['Dicke'],df['Zaehlrate (1/s)'],xerr= 0.1, yerr=popt[2],capsize = 2, ls = 'None',  color = 'black',elinewidth = 0.5)

plt.show()

