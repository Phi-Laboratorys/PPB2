import numpy as np
from numpy.lib.function_base import append
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc
from scipy.signal import argrelextrema
import scipy.constants as const
import math as m

rc('text', usetex=True)
rc('font', family='serif', size=18)

data = 'Versuch_DSR/Daten/Data_Trendless/allPeak/DataTrendless_allPeak_Temp24.csv'
df = pd.read_csv(data)

x = df['x(A/Hz/V/nm)']
yai0, yai1, yai3, yai4 = df['yai0(V)'], df['yai1(V)'], df['yai3(V)'], df['yai4(V)']

'''relative Frequency axis'''
rel = []
relx = []
k  = 0
for i,j in zip(df['yai4_max(V)'],df['x(A/Hz/V/nm)']):
    #print(m.isnan(i))
    if m.isnan(i)==True:
        rel.append(i)
        relx.append(i)
    else:
        rel.append(k)
        relx.append(j)
        k+=1

df['relFreq(THz)'] = rel
df['relx(A)'] = relx

df_rel = df[['x(A/Hz/V/nm)','yai3(V)','yai4_max(V)','relFreq(THz)']].dropna()

#transformation
m = (df_rel['relFreq(THz)'][df_rel['x(A/Hz/V/nm)'].idxmax()]-df_rel['relFreq(THz)'][df_rel['x(A/Hz/V/nm)'].idxmin()])/(df_rel['x(A/Hz/V/nm)'][df_rel['x(A/Hz/V/nm)'].idxmax()]-df_rel['x(A/Hz/V/nm)'][df_rel['x(A/Hz/V/nm)'].idxmin()])

t = df_rel['relFreq(THz)'][df_rel['x(A/Hz/V/nm)'].idxmin()] - m * df_rel['x(A/Hz/V/nm)'][df_rel['x(A/Hz/V/nm)'].idxmin()]
print(m, t)

#### relative frequency in table ########
df.to_csv('Versuch_DSR/Daten/Data_Trendless/allPeak/DataTrendless_allPeak_Temp24.csv', encoding='utf-8', index=False)

print(df)

x_rel = df['relFreq(THz)']

'''Plot relfreqency'''

fig = plt.figure(figsize=(12, 8), dpi=80)
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

ax2.plot(x, yai3, label = 'reference beam')
ax2.plot(df['relx(A)'], yai3, 'o', label='reference beam\n($\Delta\omega_{\mathrm{FSR}}$)', color='orange')

axis1 = df['relx(A)'].dropna().values.tolist()[::10]
axis2 = df['relFreq(THz)'].dropna().values.tolist()[::10]
axis2 = [ '%.0f' % elem for elem in axis2 ]

ax2.set_xticks(axis1)
ax2.set_xticklabels(axis2)
ax2.set_xlabel('$n\cdot\Delta\omega_{\mathrm{FSR}}$ in THz', labelpad=10)
ax1.set_xlabel('laser current in mA')

plt.ylabel('amplitude in V')
ax2.legend()
plt.savefig('Versuch_DSR/Bilder/Aufg-2/relfrequencyallPeakTemp24.pdf', bbox_inches='tight')
plt.show()