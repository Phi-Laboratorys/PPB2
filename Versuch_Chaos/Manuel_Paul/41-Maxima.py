import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc
from scipy.signal import argrelextrema
from scipy.optimize import curve_fit

rc('text', usetex=True)
rc('font', family='serif', size=20)

data = "Versuch_Chaos/Daten/Pendel/3.2a/06_09_2021_14_41_30_G11_pendel_0.dat"
df = pd.read_csv(data, delim_whitespace=True, skiprows=7, decimal=',')
df = df.dropna()

n = 5  # number of points to be checked before and after
df['data'] = df['Ua(V)']
# Find local peaks

#df['min'] = df.iloc[argrelextrema(df.data.values, np.less_equal,order=n)[0]]['data']
df['max'] = df.iloc[argrelextrema(df.data.values, np.greater_equal,order=n)[0]]['data']

df = df.dropna()
df = df.drop(0)
df = df.drop_duplicates(subset=['max'], keep='last')

df['dt(s)'] = df.diff(axis = 0, periods = 1)['t(s)']

#Mittelwerte für gleiche Zeiten
df2 = df[['dt(s)', 'max']]
df2 = df2.round({'dt(s)': 2})
df2 = df2.dropna()
df2 = df2.groupby(by='dt(s)').mean()
#print(df2.to_latex())

#df = df.drop_duplicates(subset=['dt(s)'], keep='last')
#print(df)
#df = df.diff(axis = 0, periods = 1)
#df = df.loc[(df>=0.1).any(axis=1)]
# Plot results
#plt.scatter(df['t(s)'], df['min'], c='r')
#plt.scatter(df['t(s)'], df['max'], c='g')
#plt.plot(df['t(s)'], df['Ua(V)'])
#plt.hist(df['dt(s)'])
#plt.plot(df['Ua(V)'],df['dt(s)'],'.')
#plt.ylim(2,2.5)

x, y = df2['max'], df2.index

# Fit
def log(x,a,b):
    return a*np.log(x) + b

def fit(x,y):
    popt, _ = curve_fit(log, x, y)
    return popt

a, b = fit(x,y)
print(a,b)
x_line = np.linspace(x.min(),x.max(),100)
y_line = log(x_line,a,b)

plt.figure(figsize=(12, 8), dpi=80)
plt.plot(x_line, y_line, label=r'Logaritmischer Fit: $T=-1.0190$ s $\log(U_{a,max}) + 2.8810$ s')
plt.plot(x, y, 'o',label=r'Messreihe gruppiert nach $T$ mit Mittelwert von $U_{a,max}$')
plt.xlabel(r'$U_{a,max}$ in V')
#plt.ylabel(r'$\omega=\frac{2\pi}{T}$ in $\frac{1}{\mathrm{s}}$',size=12)
plt.ylabel(r'$T$ in s')
plt.legend()
plt.savefig("Versuch_Chaos/Bilder/Pendel/3.2a/AbhSchwingung.pdf",bbox_inches='tight')
plt.show()