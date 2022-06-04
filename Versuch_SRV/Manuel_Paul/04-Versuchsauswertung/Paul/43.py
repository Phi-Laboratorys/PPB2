import numpy as np
from numpy.lib.function_base import append
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc
from scipy.signal import argrelextrema
import scipy.constants as const

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=22)

'''
#############################
##                         ##
##      Teilaufgabe a      ##
##                         ##
#############################

path = 'Versuch_SRV/Daten/43/a'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files if 'dat' in i]

dataOr1  = [i for i in data if 'Or1_'  in i]
dataOr2  = [i for i in data if 'Or2_'  in i]
dataOr5  = [i for i in data if 'Or5_'  in i]
dataOr7  = [i for i in data if 'Or7_'  in i]
dataOr8  = [i for i in data if 'Or8_'  in i]
dataOr10 = [i for i in data if 'Or10_' in i]

dataOr = [dataOr1, dataOr2, dataOr5, dataOr10]
name = ['43aAllOr1','43aAllOr2','43aAllOr5','43aAllOr10']
title = [r'\textbf{(a)}',r'\textbf{(b)}',r'\textbf{(c)}',r'\textbf{(d)}']

fig = plt.figure(figsize=(12,12), dpi=80)
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex=True, sharey=True)

plt.rcParams['axes.titley'] = 0.96 
plt.rcParams['axes.titlepad'] = -14

axis = [ax1, ax2, ax3, ax4]

for i,n,ax,t in zip(dataOr,name,axis,title):    
    
    for j in i:
        
        df = pd.read_csv(j, skiprows=3, sep='\s+')
        df = df.sort_values(by=['Fqscale-FFT'])

        if '_Bu_' in j:
            ax.plot(df['Fqscale-FFT'], df['y-FFTcurve'], label='Butterworth', color='#1f77b4')
        elif '_Ch_' in j:
            ax.plot(df['Fqscale-FFT'], df['y-FFTcurve'], label='Chebyshev', color='#ff7f0e')
        elif '_InCh_' in j:
            ax.plot(df['Fqscale-FFT'], df['y-FFTcurve'], label='Inverse Chebyshev', color='red')
        elif '_El_' in j:
            ax.plot(df['Fqscale-FFT'], df['y-FFTcurve'], label='Elliptic', color='grey')
        elif '_Be_' in j:
            ax.plot(df['Fqscale-FFT'], df['y-FFTcurve'], label='Bessel', color='green')
               
    ax.set_xscale('log')

    ax.tick_params(which = 'major', direction = "in")
    ax.tick_params(which = 'minor', direction = "in")
    ax.set_xlabel(r'$f$ in Hz')
    ax.set_ylabel(r'$A$ in dB')
    
    ax.set_title(t, loc = 'right')
    
    axT = ax.secondary_xaxis('top')
    axT.tick_params(which = 'major', direction = "in")
    axT.tick_params(which = 'minor', direction = "in")
    axT.xaxis.set_ticklabels([])

    axR = ax.secondary_yaxis('right')
    axR.tick_params(direction = "in")
    axR.yaxis.set_ticklabels([])

    if ax == ax3:
        ax.legend(loc='lower left')
        
    ax.label_outer()

    #ax.legend()

    #plt.savefig('Versuch_SRV/Bilder/Paul/'+n+'.pdf', bbox_inches = 'tight')
    #plt.show()

plt.savefig('Versuch_SRV/Bilder/Paul/43aAllOrAll.pdf', bbox_inches = 'tight')
plt.show()
    
'''

'''
#############################
##                         ##
##      Teilaufgabe b      ##
##                         ##
#############################

data = ['Versuch_SRV/Daten/43/b/05_10_2021_15_02_04_G11_filtering_43b_Rechteck_f100Hz_A1V_Fil_Bu_Lopa_Or1_Uf1k.dat',
        'Versuch_SRV/Daten/43/b/05_10_2021_15_02_51_G11_filtering_43b_Rechteck_f100Hz_A1V_Fil_Bu_Hipa_Or1_Uf1k.dat',
        'Versuch_SRV/Daten/43/b/05_10_2021_15_06_57_G11_filtering_43b_Rechteck_f100Hz_A1V_Fil_InCh_Lopa_Or1_Uf1k.dat',
        'Versuch_SRV/Daten/43/b/05_10_2021_15_07_48_G11_filtering_43b_Rechteck_f100Hz_A1V_Fil_InCh_Hipa_Or1_Uf1k.dat']

#        'Versuch_SRV/Daten/43/b/05_10_2021_15_05_08_G11_filtering_43b_Rechteck_f100Hz_A1V_Fil_Ch_Lopa_Or1_Uf1k.dat',
#        'Versuch_SRV/Daten/43/b/05_10_2021_15_08_41_G11_filtering_43b_Rechteck_f100Hz_A1V_Fil_E_Lopa_Or1_Uf1k.dat',
#        'Versuch_SRV/Daten/43/b/05_10_2021_15_10_27_G11_filtering_43b_Rechteck_f100Hz_A1V_Fil_Be_Lopa_Or1_Uf1k.dat']


dname = ['43bBuLo1','43bBuHi1','43bInChLo1','43bInChHi1']

for i,j in zip(data,dname):
    
    df = pd.read_csv(i, skiprows=3, sep='\s+')

    #Plot Signal
    t = 2500
    fig, ax = plt.subplots(figsize=(12, 6), dpi=80)
    
    ax.plot(df['time'].iloc[:t], df['y-generator'].iloc[:t], 'g--', label='Ungefiltert')
    ax.plot(df['time'].iloc[:t], df['y-behind'].iloc[:t], 'k-', label='Gefiltert')
    
    ax.tick_params(direction = "in")
    ax.set_xlabel('$t$ in ms')
    ax.set_ylabel('$U$ in V')
    
    axT = ax.secondary_xaxis('top')
    axT.tick_params(direction = "in")
    axT.xaxis.set_ticklabels([])
    axR = ax.secondary_yaxis('right')
    axR.tick_params(direction = "in")
    axR.yaxis.set_ticklabels([])

    ax.legend()
    plt.savefig('Versuch_SRV/Bilder/Paul/'+j+'S.pdf', bbox_inches = 'tight')
    #plt.show()
    

    #Plot Fourie
    df = df.sort_values(by=['Fqscale-FFT'])
    
    fig, ax = plt.subplots(figsize=(12, 6), dpi=80)
    
    ax.plot(df['Fqscale-FFT'], df['y-FFTcurve'], 'k-')
    ax.set_xscale('log')
    
    ax.tick_params(which = 'major', direction = "in")
    ax.tick_params(which = 'minor', direction = "in")
    ax.set_xlabel('$f$ in Hz')
    ax.set_ylabel('$A$ in dB')
    
    axT = ax.secondary_xaxis('top')
    axT.tick_params(which = 'major', direction = "in")
    axT.tick_params(which = 'minor', direction = "in")
    axT.xaxis.set_ticklabels([])
    axR = ax.secondary_yaxis('right')
    axR.tick_params(direction = "in")
    axR.yaxis.set_ticklabels([])
    
    plt.savefig('Versuch_SRV/Bilder/Paul/'+j+'F.pdf', bbox_inches = 'tight')
    #plt.show()
'''
'''
#############################
##                         ##
##      Teilaufgabe c      ##
##                         ##
#############################

dataRoh = 'Versuch_SRV/Daten/43/d/05_10_2021_15_48_11_G11_filtering_43d_Rechteck_f1kHz_A1V_Rau_BW20MHz_AMD70pc_Roh.dat'
data = ['Versuch_SRV/Daten/43/d/05_10_2021_15_49_43_G11_filtering_43d_Rechteck_f1kHz_A1V_Rau_BW20MHz_AMD70pc_DigiFil_Bu_Bapa_Or4_Lf500Hz_Uf1500Hz.dat',
        'Versuch_SRV/Daten/43/d/05_10_2021_15_52_43_G11_filtering_43d_Rechteck_f1kHz_A1V_Rau_BW20MHz_AMD70pc_DigiFil_Bu_Bapa_Or4_Lf700Hz_Uf1300Hz.dat',
        'Versuch_SRV/Daten/43/d/05_10_2021_16_04_08_G11_filtering_43d_Rechteck_f1kHz_A1V_Rau_BW20MHz_AMD70pc_DigiFil_Bu_Bapa_Or4_Lf10mHz_Uf55kHz.dat']

dname = ['43cLf500Hf1500','43cLf700Hf1300','43cLf10mHz55kHz']

for i,j in zip(data,dname):

    df = pd.read_csv(i, skiprows=3, sep='\s+')

    dateipfad = 'Versuch_SRV/Bilder/Paul/'

    #Plot Signal
    t = 277
    fig1, ax1 = plt.subplots(figsize=(12, 6), dpi=80)
    
    ax1.plot(df['time'].iloc[:t], df['y-generator'].iloc[:t], 'g--', label='Ungefiltert')
    ax1.plot(df['time'].iloc[:t], df['y-behind'].iloc[:t], 'k-', label='Gefiltert')
    
    ax1.tick_params(direction = "in")
    ax1.set_xlabel('$t$ in ms')
    ax1.set_ylabel('$U$ in V')
    
    axT = ax1.secondary_xaxis('top')
    axT.tick_params(direction = "in")
    axT.xaxis.set_ticklabels([])
    
    axR = ax1.secondary_yaxis('right')
    axR.tick_params(direction = "in")
    axR.yaxis.set_ticklabels([])
    
    ax1.legend()
    plt.savefig(dateipfad+j+'S.pdf', bbox_inches = 'tight')
    plt.show()

    #Plot Fourie
    df = df.sort_values(by=['Fqscale-FFT'])
    
    fig2, ax2 = plt.subplots(figsize=(12, 6), dpi=80)
    
    ax2.plot(df['Fqscale-FFT'], df['y-FFTcurve'], 'k-')
    
    ax2.tick_params(which = 'major', direction = "in")
    ax2.tick_params(which = 'minor', direction = "in")
    ax2.set_xlabel('$f$ in Hz')
    ax2.set_ylabel(r'$A$ in dB')
    ax2.set_xscale('log')
    
    axT = ax2.secondary_xaxis('top')
    axT.tick_params(which = 'major', direction = "in")
    axT.tick_params(which = 'minor', direction = "in")
    axT.xaxis.set_ticklabels([])
    axR = ax2.secondary_yaxis('right')
    axR.tick_params(direction = "in")
    axR.yaxis.set_ticklabels([])
    
    plt.savefig(dateipfad+j+'F.pdf', bbox_inches = 'tight')
    plt.show()
'''
#'''
#############################
##                         ##
##      Teilaufgabe d      ##
##                         ##
#############################

path = 'Versuch_SRV/Daten/43/a'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files if 'dat' in i]

dataBu    = [i for i in data if '_Bu_'   in i]
dataCh    = [i for i in data if '_Ch_'   in i]
dataInCh  = [i for i in data if '_InCh_' in i]
dataEl    = [i for i in data if '_El_'   in i]
dataBe    = [i for i in data if '_Be_'   in i]

#dataFil = [dataBu, dataCh, dataInCh, dataEl, dataBe]
name = ['43dAllBu','43dAllCh','43dAllInCh','43dAllEl','43dAllBe']

dataFil = [dataBu, dataCh, dataInCh, dataBe]
title = [r'\textbf{(a)}',r'\textbf{(b)}',r'\textbf{(c)}',r'\textbf{(d)}']

fig = plt.figure(figsize=(12,12), dpi=80)
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex=True, sharey=True)

plt.rcParams['axes.titley'] = 0.96 
plt.rcParams['axes.titlepad'] = -14

axis = [ax1, ax2, ax3, ax4]

for i,n,ax,t in zip(dataFil,name,axis,title):    
#for i,n in zip(dataFil,name):    
    
    #fig, ax = plt.subplots(figsize=(12,6), dpi=80)
    
    sorted_i = [0,0,0,0]
    
    for j in i:
        if '_Or1_' in j:
            sorted_i[0] = j
        elif '_Or2_' in j:
            sorted_i[1] = j
        elif '_Or5_' in j:
            sorted_i[2] = j
        elif '_Or10_' in j:
            sorted_i[3] = j
    
    for j in sorted_i:
        
        df = pd.read_csv(j, skiprows=3, sep='\s+')
        df = df.sort_values(by=['Fqscale-FFT'])

        if '_Or1_' in j:
            ax.plot(df['Fqscale-FFT'], df['y-FFTcurve'], label='Ordnung 1', color='#1f77b4')
        elif '_Or2_' in j:
            ax.plot(df['Fqscale-FFT'], df['y-FFTcurve'], label='Ordnung 2', color='#ff7f0e')
        elif '_Or5_' in j:
            ax.plot(df['Fqscale-FFT'], df['y-FFTcurve'], label='Ordnung 5', color='red')
        elif '_Or10_' in j:
            ax.plot(df['Fqscale-FFT'], df['y-FFTcurve'], label='Ordnung 10', color='grey')
    
    ax.set_xscale('log')

    ax.tick_params(which = 'major', direction = "in")
    ax.tick_params(which = 'minor', direction = "in")
    ax.set_xlabel(r'$f$ in Hz')
    ax.set_ylabel(r'$A$ in dB')
    
    ax.set_title(t, loc = 'right')
    
    axT = ax.secondary_xaxis('top')
    axT.tick_params(which = 'major', direction = "in")
    axT.tick_params(which = 'minor', direction = "in")
    axT.xaxis.set_ticklabels([])

    axR = ax.secondary_yaxis('right')
    axR.tick_params(direction = "in")
    axR.yaxis.set_ticklabels([])           
    

    if ax == ax3:
        ax.legend(loc='lower left')
        
    ax.label_outer()

    #ax.legend()

    #plt.savefig('Versuch_SRV/Bilder/Paul/'+n+'.pdf', bbox_inches = 'tight')
    #plt.show()

plt.savefig('Versuch_SRV/Bilder/Paul/43dAllFilAll.pdf', bbox_inches = 'tight')
plt.show() 
#'''
'''
#############################
##                         ##
##      Teilaufgabe e      ##
##                         ##
#############################

dataASin = 'Versuch_SRV/Daten/43/c/05_10_2021_15_26_32_G11_filtering_43c_Sinus_f2kHz_A1V_AnalFil_Bu_Bapa_Or1_Lf1kHz_Uf4kHz.dat'
dataDSin = 'Versuch_SRV/Daten/43/c/05_10_2021_15_28_23_G11_filtering_43c_Sinus_f2kHz_A1V_DigiFil_Bu_Bapa_Or1_Lf1kHz_Uf4kHz.dat'
dataARe = 'Versuch_SRV/Daten/43/c/05_10_2021_15_27_23_G11_filtering_43c_Rechteck_f2kHz_A1V_AnalFil_Bu_Bapa_Or1_Lf1kHz_Uf4kHz.dat'
dataDRe = 'Versuch_SRV/Daten/43/c/05_10_2021_15_28_55_G11_filtering_43c_Rechteck_f2kHz_A1V_DigiFil_Bu_Bapa_Or1_Lf1kHz_Uf4kHz.dat'

df1 = pd.read_csv(dataDRe, skiprows=3, sep='\s+')
df2 = pd.read_csv(dataARe, skiprows=3, sep='\s+')


dname = '43eA'
dateipfad = 'Versuch_SRV/Bilder/Paul/'

Plot Signal
t = 277
plt.figure(figsize=(12, 6), dpi=80)
plt.plot(df['time'].iloc[:t], df['y-generator'].iloc[:t], 'g--', label='Ungefiltert')
plt.plot(df['time'].iloc[:t], df['y-behind'].iloc[:t], 'k-', label='Gefiltert')
plt.xlabel('$t$ in ms')
plt.ylabel('y')
plt.legend()
#plt.savefig(dateipfad+dname+'S.pdf', bbox_inches = 'tight')
plt.show()

#Plot Fourie
df1 = df1.sort_values(by=['Fqscale-FFT'])
df2 = df2.sort_values(by=['Fqscale-FFT'])

fig, ax = plt.subplots(figsize=(12, 6), dpi=80)
#ax.plot(df1['Fqscale-filter'], df1['y-filtercurve'], 'k--', label='digitale Filterung Simu')
#ax.plot(df1['Fqscale-FFT'], df1['y-FFTcurve'], 'k-', label='digitale Filterung')
ax.plot(df2['Fqscale-FFT'], df2['y-FFTcurve'], 'b-', label='analoge Filterung')

ax.set_xscale('log')

ax.tick_params(which = 'major', direction = "in")
ax.tick_params(which = 'minor', direction = "in")
ax.set_xlabel(r'$f$ in Hz')
ax.set_ylabel(r'$A$ in dB')
    
axT = ax.secondary_xaxis('top')
axT.tick_params(which = 'major', direction = "in")
axT.tick_params(which = 'minor', direction = "in")
axT.xaxis.set_ticklabels([])

axR = ax.secondary_yaxis('right')
axR.tick_params(direction = "in")
axR.yaxis.set_ticklabels([])

#plt.legend()
plt.savefig(dateipfad+dname+'F.pdf', bbox_inches = 'tight')
plt.show()
'''