import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif', size=35)

data = ['Versuch_Chaos/Daten/Pendel/3.3a/0,165Hz/06_09_2021_17_14_32_Richter_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,198Hz/06_09_2021_17_12_04_Richter_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,233Hz/06_09_2021_17_09_31_Richter_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,411Hz/06_09_2021_17_01_56_Richter_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,733Hz/06_09_2021_16_44_55_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,847Hz/06_09_2021_16_00_06_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,882Hz/06_09_2021_15_56_30_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/0,939Hz/06_09_2021_16_36_11_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/1,000Hz/06_09_2021_16_31_30_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/1,201Hz/06_09_2021_15_48_53_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/1,499Hz/06_09_2021_16_18_06_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/1,702Hz/06_09_2021_16_15_44_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/1,802Hz/06_09_2021_16_13_46_G11_pendel_0.dat',
        'Versuch_Chaos/Daten/Pendel/3.3a/2,100Hz/06_09_2021_16_11_42_G11_pendel_0.dat']

freq = ['0,165Hz','0,198Hz','0,233Hz','0,411Hz','0,733Hz','0,847Hz','0,882Hz','0,939Hz',
        '1,000Hz','1,201Hz','1,499Hz','1,702Hz','1,802Hz','2,100Hz']

for i,j in zip(data, freq):
    df = pd.read_csv(i, delim_whitespace=True, skiprows=7, decimal=',')
    df = df.dropna()
     
    x_p, y_p = df['Ua(V)'], df['-dUa/dt(V)']
    
    df = df= df[df['DFT-Ua(V)'] != 0]
    x_s, y_s1, y_s2 = df['F(Hz)'], df['DFT-Ua(V)'], df['DFT-dUa/dt(V)']
    
    plt.rcParams['axes.titley'] = 0.94  # y is in axes-relative coordinates.
    plt.rcParams['axes.titlepad'] = -14  # pad is in points...

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(22, 8), dpi=80)
    
    ax1.plot(x_p, y_p, linewidth=0.7)
    ax1.set_title(r'\textbf{(a)}', loc='right')
    ax1.set_xlabel(r'$U_a$ in V')
    ax1.set_ylabel(r'$\dot{U_a}$ in $\frac{\mathrm{V}}{\mathrm{s}}$')
    
    ax2.semilogy(x_s, y_s1, linewidth=0.7)
    ax2.set_title(r'\textbf{(b)}', loc='right')
    ax2.set_xlabel(r'$f$ in Hz')
    ax2.set_ylabel(r'$U_a$ in V')
    
    plt.subplots_adjust(wspace=0.35)    
    plt.savefig("Versuch_Chaos/Bilder/Pendel/3.3a/"+j+".pdf",bbox_inches='tight')
    #plt.show()