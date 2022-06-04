import numpy as np
import pandas as pd  
import matplotlib.pylab as plt
from matplotlib import rc
from scipy.optimize import curve_fit

rc('text', usetex=True)
rc('font', family='serif', size=18)

data = 'Versuch_DSR/Daten/Data_Trendless/allPeak/DataTrendless_allPeak_Temp24.csv'
df = pd.read_csv(data)

x,y = df['x(A/Hz/V/nm)'],df['yai3(V)']
x_data = [df['x(A/Hz/V/nm)'][0:450],df['x(A/Hz/V/nm)'][451:900],
          df['x(A/Hz/V/nm)'][901:1380],df['x(A/Hz/V/nm)'][1381:]]
y_data = [df['yai3(V)'][0:450],df['yai3(V)'][451:900],
          df['yai3(V)'][901:1380],df['yai3(V)'][1381:]]  
mean   = [119.4429,125.0267,131.8581,134.7829]

fig = plt.figure(figsize=(12, 8), dpi=80)
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

ax1.plot(x,y,color = 'black', label = 'reference beam')  
ax2.plot(x,y,color = 'black', label = 'reference beam')  

x_fit, y_fit = [],[]
n = 1

for i, j, m in zip(x_data, y_data, mean):
    
    def gaussian(x, amplitude, stddev):
        return amplitude * np.exp(-((x - m) / (np.sqrt(2) * stddev))**2)

    popt, _ = curve_fit(gaussian, i, j)

    print(*popt)

    ax1.plot(x, gaussian(x, *popt), label='gaussian fit for peak '+str(n))
    ax1.fill_between(x,0,gaussian(x, *popt),alpha=0.5)
    n += 1
    

#ax2.plot(df['relx(A)'], df['yai3(V)'], 'o', label='reference beam\n($\Delta\omega_{\mathrm{FSR}}$)', color='orange')

axis1 = df['relx(A)'].dropna().values.tolist()[::10]
axis2 = df['relFreq(THz)'].dropna().values.tolist()[::10]
axis2 = [ '%.0f' % elem for elem in axis2 ]

ax2.set_xticks(axis1)
ax2.set_xticklabels(axis2)
ax2.set_xlabel('$n\cdot\Delta\omega_{\mathrm{FSR}}$ in THz', labelpad=10)
ax1.set_xlabel('laser current in mA')

plt.ylabel('amplitude in V')  
ax1.legend()
#plt.savefig('Versuch_DSR/Bilder/Aufg-3/gaussFit.pdf', bbox_inches='tight')
plt.show()