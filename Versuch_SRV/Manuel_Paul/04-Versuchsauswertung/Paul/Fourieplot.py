import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=15)

data42b = 'Versuch_SRV/Daten/42/b/05_10_2021_13_30_44_G11_sampling_42b_Dreieck_f3kHz_A1V_fs7kHz.dat'

data43aBu = 'Versuch_SRV/Daten/43/a/05_10_2021_14_49_03_G11_filtering_43a_Sinus_f100Hz_A1V_Rau_BW20MHz_AMD120pc_Fil_Bu_Lopa_Or1_Uf1k.dat'
data43aCh = 'Versuch_SRV/Daten/43/a/05_10_2021_14_52_18_G11_filtering_43a_Sinus_f100Hz_A1V_Rau_BW20MHz_AMD120pc_Fil_Ch_Lopa_Or1_Uf1k.dat'
data43aInCh = 'Versuch_SRV/Daten/43/a/05_10_2021_14_54_54_G11_filtering_43a_Sinus_f100Hz_A1V_Rau_BW20MHz_AMD120pc_Fil_InCh_Lopa_Or1_Uf1k.dat'
data43aEl = 'Versuch_SRV/Daten/43/a/05_10_2021_14_56_28_G11_filtering_43a_Sinus_f100Hz_A1V_Rau_BW20MHz_AMD120pc_Fil_El_Lopa_Or1_Uf1k.dat'
data43aBe = 'Versuch_SRV/Daten/43/a/05_10_2021_14_58_20_G11_filtering_43a_Sinus_f100Hz_A1V_Rau_BW20MHz_AMD120pc_Fil_Be_Lopa_Or1_Uf1k.dat'


data = data43aCh
df = pd.read_csv(data, skiprows=3, sep='\s+')
df = df.sort_values(by=['Fqscale-FFT'])

'''
df1 = pd.read_csv(data43aBu, skiprows=3, sep='\s+')
df1 = df1.sort_values(by=['Fqscale-FFT'])

df2 = pd.read_csv(data43aCh, skiprows=3, sep='\s+')
df2 = df2.sort_values(by=['Fqscale-FFT'])

df3 = pd.read_csv(data43aInCh, skiprows=3, sep='\s+')
df3 = df3.sort_values(by=['Fqscale-FFT'])

df4 = pd.read_csv(data43aEl, skiprows=3, sep='\s+')
df4 = df4.sort_values(by=['Fqscale-FFT'])

df5 = pd.read_csv(data43aBe, skiprows=3, sep='\s+')
df5 = df5.sort_values(by=['Fqscale-FFT'])
#'''

#print(df.head())

plt.figure(figsize=(12, 6), dpi=80)
plt.plot(df['Fqscale-FFT'], df['y-FFTcurve'], 'k-')
plt.plot([1000,1000], [-200,0], 'r--')
plt.plot([2000,2000], [-200,0], 'g--')
plt.plot([10000,10000], [-200,0], 'b--')
'''
plt.plot(df1['Fqscale-FFT'], df1['y-FFTcurve'], 'b-', label='Butterworth')
plt.plot(df2['Fqscale-FFT'], df2['y-FFTcurve'], 'g-', label='Chebyshev')
plt.plot(df3['Fqscale-FFT'], df3['y-FFTcurve'], 'r-', label='Inverse Chebyshev')
plt.plot(df4['Fqscale-FFT'], df4['y-FFTcurve'], 'm-', label='Elliptic')
plt.plot(df5['Fqscale-FFT'], df5['y-FFTcurve'], 'k-', label='Bessel')
#'''
plt.xlabel('$f$ in Hz')
plt.ylabel(r'Amplitude (dBV) 1V $U_\mathrm{eff}$ = 1 dBV')
plt.xscale('log')
#plt.legend()
#plt.savefig('Versuch_SRV/Bilder/Paul/43aAll.pdf', bbox_inches = 'tight')
plt.show()