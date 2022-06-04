import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

from scipy.signal import argrelextrema

rc('text', usetex=True)
rc('font', family='serif')

#Daten Aufg a)
datALoch = 'Versuch_REM/Daten/a/EDX/Loch.txt'
datAFlae = 'Versuch_REM/Daten/a/EDX/Oberflaeche.txt'
#Daten Aufg d)
datDD2 = 'Versuch_REM/Daten/d/EDX/Dunkel2.txt'
datDmW = 'Versuch_REM/Daten/d/EDX/DunklerfleckMitWei.txt'
datH1 = 'Versuch_REM/Daten/d/EDX/Hell1.txt'
datN1 = 'Versuch_REM/Daten/d/EDX/Normal1.txt'
#Daten Aufg e)
datE = 'Versuch_REM/Daten/e/EDX/chip.txt'

#Elementmarker
Name = ['O K alpha', 'C K alpha','Fe K alpha', 'Fe K beta', 'Ni K alpha', 'W L alpha', 'W M alpha']
Energie = [0.5249, 0.277, 6.40384, 7.05798, 7.47815, 8.3976, 1.7754]
Farbe = ['g', 'k', 'r', 'm', 'b', 'c', 'y']

data = datN1
df = pd.read_csv(data, delim_whitespace=True, skiprows=24)

n=5 #Alle Werte dopen, die kleiner sind als 50(?)
#df2 = df.copy()
#df2['Impulse'] = df2['Impulse'].rolling(50).mean()
#df2['max'] = df2.iloc[argrelextrema(df2.Impulse.values, np.greater_equal,order=n)[0]]['Impulse']
#df2 = df2.dropna()
#df2 =df2.drop()
#print(df2.head())

fig, ax = plt.subplots()
ax.plot(df['Energie'], df['Impulse'], color='k')
#ax.scatter(df2['Energie'], df2['max'], c='r')
ax.set(xlabel='Energie/keV', ylabel='cps/eV', xlim=(-0.49,11))
ax.grid()

for i in range(0,len(Energie)):
    ax.plot([Energie[i],Energie[i]], [0,800], label=Name[i], lw=1, color=Farbe[i])

plt.legend()
plt.show()