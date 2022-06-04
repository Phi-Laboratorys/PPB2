import numpy as np
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc
import matplotlib.cm as cm
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from matplotlib.patches import Rectangle
from scipy.signal import argrelextrema
from scipy.optimize import curve_fit
import scipy.constants as const

rc('text', usetex=True)
rc('font', family='serif', size=22)

'''
#############################
##                         ##
##      Teilaufgabe a      ##
##                         ##
#############################

path = 'Versuch_SRV/Daten/41/a'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files if 'dat' in i]
data.sort()

#data_sinus = [i for i in data if 'Sinus' in i]
#data_sqare = [i for i in data if 'Rechteck' in i]
#data_tri  =  [i for i in data if 'Dreieck' in i]

fig = plt.figure(figsize=(12,18), dpi=80)
gs = fig.add_gridspec(3, hspace=0, height_ratios= [2,2,1])
ax = gs.subplots(sharex=True)

for i in data:
    df = pd.read_csv(i, skiprows=4, delim_whitespace= True)
    df = df[:][:4500]
    
    n = 50
    df['max/dB'] = df.iloc[argrelextrema(df['y-FFTcurve'].values, np.greater_equal,order=n)[0]]['y-FFTcurve']
    
    x = df['Fqscale-FFT']
    y, y_max = df['y-FFTcurve'], df['max/dB']
    y_V = 1 * 10**(y/20) * np.sqrt(2) 
    x_t, y_g = df['time'], df['y-generator']
    
    df_max = df[['Fqscale-FFT', 'y-FFTcurve', 'max/dB']].dropna()
    df_max = df_max[:][:-1]
    #df_max['max/dB'] = df_max['max/dB'] + 120
    
    # df_max['diff'] = df_max['max'].diff().abs()
    
    df_max['max/V'] = 1 * 10**(df['max/dB']/20) * np.sqrt(2) 
        
    if 'Sinus' in i:
        print('Sinus')
        #df_max['max/V'] = 1000 * 10**(df['max/dB']/20) * np.sqrt(2)
        theo = [1.000000]
        k = 1
        while k < len(df_max):
            theo.append(0)
            k+=1
        
        df_max['Theo/V'] = theo
        
        df_max['diff/V'] = abs(-df_max['Theo/V'] + df_max['max/V'])
        df_max.index = np.arange(1, len(df_max) + 1)
            
        #print(df_max[0:35].to_latex())
        
    if 'Rechteck' in i:
        print('Rechteck')
        #df_max['max/V'] = 1000 * 10**(df['max/dB']/20) * np.sqrt(1)
        theo = []
        k = 1
        while k < len(df_max)+1:
            theo.append(4/np.pi * 1/(2*k-1))
            k+=1
        
        df_max['Theo/V'] = theo
        
        df_max['diff/V'] = abs(-df_max['Theo/V'] + df_max['max/V'])
        df_max.index = np.arange(1, len(df_max) + 1)
        
        theo_dB = 20* np.log10(df_max['Theo/V']/np.sqrt(2))
            
        print(df_max.to_latex())
        ax[0].plot(x/1000,y,color = '#ff7f0e', label='Rechteck')
        ax[0].plot(df_max['Fqscale-FFT']/1000,theo_dB,'o',color = 'red',  label = 'Theorie')
        ax[2].plot(df_max['Fqscale-FFT']/1000,df_max['diff/V']*1E6,'o',label='Rechteck', color='#ff7f0e')
        
    if 'Dreieck' in i:
        print('Dreieck')
        #df_max['max/V'] = 1000 * 10**(df['max/dB']/20) * np.sqrt(3)
        theo = []
        k = 1
        while k < len(df_max)+1:
            theo.append(8/(np.pi**2) * 1/((2*k-1)**2))
            k+=1
        
        df_max['Theo/V'] = theo
        
        df_max['diff/V'] = abs(-df_max['Theo/V'] + df_max['max/V'])
        df_max.index = np.arange(1, len(df_max) + 1)
        
        theo_dB = 20* np.log10(df_max['Theo/V']/np.sqrt(2))
            
        print(df_max.to_latex())
        ax[1].plot(x/1000,y,color = '#1f77b4', label='Dreieck')
        ax[1].plot(df_max['Fqscale-FFT']/1000,theo_dB,'o',color = 'red', label = 'Theorie')
        ax[2].plot(df_max['Fqscale-FFT']/1000,df_max['diff/V']*1E6,'o',label='Dreieck', color='#1f77b4')

ax[0].tick_params(direction = "in")

axT = ax[0].secondary_xaxis('top')
axT.tick_params(direction = "in")
axT.xaxis.set_ticklabels([])

axR = ax[0].secondary_yaxis('right')
axR.tick_params(direction = "in")
axR.yaxis.set_ticklabels([])

ax[1].tick_params(direction = "in")

axT = ax[1].secondary_xaxis('top')
axT.tick_params(direction = "in")
axT.xaxis.set_ticklabels([])

axR = ax[1].secondary_yaxis('right')
axR.tick_params(direction = "in")
axR.yaxis.set_ticklabels([])

ax[2].tick_params(direction = "in")

axT = ax[2].secondary_xaxis('top')
axT.tick_params(direction = "in")
axT.xaxis.set_ticklabels([])

axR = ax[2].secondary_yaxis('right')
axR.tick_params(direction = "in")
axR.yaxis.set_ticklabels([])

ax[0].set_ylabel(r'$A$ in dB')  
ax[1].set_ylabel(r'$A$ in dB')  
ax[2].set_ylabel(r'$\Delta A$ in $\mu$V')
ax[2].set_xlabel(r'$f$ in kHz')  
ax[0].legend(loc = 'lower right')
ax[1].legend(loc = 'lower right')      
ax[2].legend(loc='center right')
plt.savefig('Versuch_SRV/Bilder/Manuel/41/Residuum.pdf',bbox_inches='tight')
#plt.show()
'''
'''
#############################
##                         ##
##      Teilaufgabe b      ##
##                         ##
#############################

path = 'Versuch_SRV/Daten/41/b'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files if 'dat' in i]
data.sort()

df = pd.read_csv(data[1], skiprows=4, delim_whitespace= True)
#df = df[:][:4500]
df = df[:][:700]

#print(df)

x, y = df['Fqscale-FFT']/1000, df['y-FFTcurve']
fig, ax = plt.subplots(figsize=(12,8), dpi=80)
ax.plot(x,y, color = 'black')

ax.tick_params(direction = "in")
ax.set_ylabel(r'$U$ in V')
ax.set_xlabel(r'$f$ in kHz')

axT = ax.secondary_xaxis('top')
axT.tick_params(direction = "in")
axT.xaxis.set_ticklabels([])

axR = ax.secondary_yaxis('right')
axR.tick_params(direction = "in")
axR.yaxis.set_ticklabels([])

ax.set_ylabel(r'$A$ in dB')
ax.set_xlabel(r'$f$ in kHz')
plt.savefig('Versuch_SRV/Bilder/Manuel/41/FourierSinus.pdf', bbox_inches='tight')
plt.show()
'''
#'''
#############################
##                         ##
##      Teilaufgabe c      ##
##                         ##
#############################

path = 'Versuch_SRV/Daten/41/c'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files if 'dat' in i]
data.sort()

data = [data[3],data[0],data[2],data[1]]

N = [0, 10, 50, 100]
colors = ['blue', 'orange', 'red', 'black']

median = []

fig, ax1 = plt.subplots(figsize=(12,8), dpi=80)
for i, N, c in zip(data, N, colors):
    df = pd.read_csv(i, skiprows=4, delim_whitespace= True)
    #df = df[:][:4500]
    df = df[:][:300]
    
    n = 50
    df['max/dB'] = df.iloc[argrelextrema(df['y-FFTcurve'].values, np.greater_equal,order=n)[0]]['y-FFTcurve']
    
    x, y = df['Fqscale-FFT']/1000, df['y-FFTcurve']
    
    medi = np.repeat(y.median(),len(y))
    maxi = df['max/dB']
    
    median.append(y.median())
    
    ax1.plot(x,y, label = '$N$= '+str(N), color = c)
    ax1.plot(x,medi, linestyle = '--', color = c)

ax1.plot(x,maxi, 'o', color = 'g', label='Maxima')
    
ax1.tick_params(direction = "in")

ax1T = ax1.secondary_xaxis('top')
ax1T.tick_params(direction = "in")
ax1T.xaxis.set_ticklabels([])

ax1R = ax1.secondary_yaxis('right')
ax1R.tick_params(direction = "in")
ax1R.yaxis.set_ticklabels([])    

ax1.set_ylabel(r'$A$ in dB')
ax1.set_xlabel(r'$f$ in kHz')
ax1.legend()
#plt.savefig('Versuch_SRV/Bilder/Manuel/41/Mittelung.pdf', bbox_inches='tight')
plt.show()

fig, ax2 = plt.subplots(figsize=(12,8), dpi=80)

maxima = maxi.dropna()
N = [0,10,50,100]

abstand = abs(median - maxima[36])

#abstand = []
#
#for i in maxima:
#    abstand[:] = [abs(j - i) for j in median]
#    print(abstand)

def ln(x,a,t):
    return a * np.log(np.sqrt(x+1)) + t

def sqrt(x,a,t):
    return a * np.sqrt(x) + t

x_lin = np.linspace(0,100, 1000)

popt1, _ = curve_fit(ln, N, abstand)
a1, t1 = popt1

popt2, _ = curve_fit(sqrt, N, abstand)
a2, t2 = popt2

print(popt1, popt2)

ax2.plot(N,abstand, 'o',color = 'black', label = 'Messreihe')
ax2.plot(x_lin, ln(x_lin,a1,t1), label = r'$d(N) = 8,77\,\mathrm{dB}\cdot\ln(\sqrt{N+1}) + 60,24\,\mathrm{dB}$')
#ax2.plot(x_lin, sqrt(x_lin,a2,t2), label = 'Wurzel-Fit')

ax2.tick_params(direction = "in")

ax2T = ax2.secondary_xaxis('top')
ax2T.tick_params(direction = "in")
ax2T.xaxis.set_ticklabels([])

ax2R = ax2.secondary_yaxis('right')
ax2R.tick_params(direction = "in")
ax2R.yaxis.set_ticklabels([])    

ax2.set_xlabel(r'$N$')
ax2.set_ylabel(r'$d$ in dB')
ax2.legend()

plt.savefig('Versuch_SRV/Bilder/Manuel/41/MittlungAbstand.pdf', bbox_inches='tight')
plt.show()
#'''
'''
#############################
##                         ##
##      Teilaufgabe d      ##
##                         ##
#############################

path = 'Versuch_SRV/Daten/41/d'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files if 'dat' in i]
data.sort()

data = [data[2],data[1],data[3],data[0]]

n = ['10\,\%', '50\,\%', '100\,\%', '120\,\%']
colors = ['red', 'orange', 'black', 'blue']

fig, ax = plt.subplots(figsize=(12,8), dpi=80)

#rect = Rectangle((0.17, 0.22), 0.65, 0.47, facecolor='white', ec='none', alpha=1, transform=fig.transFigure, zorder=-1)

axins = inset_axes(ax, 6,3 , loc='center') # insert pic
mark_inset(ax,axins,loc1=2,loc2=1)

y_winmin, y_winmax = 0.5, 0.5

for i, n, c in zip(data, n, colors):
    df = pd.read_csv(i, skiprows=4, delim_whitespace= True)
    #df = df[:][:4500]
    df = df[:][:251]
    #df = df[:][2:125]

    df_win = df[:][2:125]
    
    #x, y = df['Fqscale-FFT']/1000, df['y-FFTcurve']
    x, y = df['time'], df['y-generator']
    x_win, y_win = df_win['time'], df_win['y-generator']
    
    if y_win.min() < y_winmin:
        y_winmin =  y_win.min()
        
    if y_win.max() > y_winmax:
        y_winmax = y_win.max()
    
    ax.plot(x,y, label = '$V_{\mathrm{SR}}$ = '+n, color = c)
    axins.plot(x,y, label = '$V_{\mathrm{SR}}$ = '+n, color = c)

axins.set_xlim(x_win.min(),x_win.max())
axins.set_ylim(y_winmin,y_winmax)
axins.tick_params(direction = "in")

#axins.patch.set_facecolor('white')
#axins.patch.set_alpha(0.5)
#axins.patches.append(rect)

#axins.set_ylabel(r'$U$ in V')
#axins.set_xlabel(r'$f$ in kHz')

axinsT = axins.secondary_xaxis('top')
axinsT.tick_params(direction = "in")
axinsT.xaxis.set_ticklabels([])

axinsR = axins.secondary_yaxis('right')
axinsR.tick_params(direction = "in")
axinsR.yaxis.set_ticklabels([])

ax.tick_params(direction = "in")
ax.set_ylabel(r'$U$ in V')
ax.set_xlabel(r'$f$ in kHz')

axT = ax.secondary_xaxis('top')
axT.tick_params(direction = "in")
axT.xaxis.set_ticklabels([])

axR = ax.secondary_yaxis('right')
axR.tick_params(direction = "in")
axR.yaxis.set_ticklabels([])

axins.legend(loc = (0.81,0.88)) 
#ax.legend()

#plt.savefig('Versuch_SRV/Bilder/Manuel/41/SignalRauschAbstandKomplett.pdf', bbox_inches='tight')
#plt.savefig('Versuch_SRV/Bilder/Manuel/41/SignalRauschAbstand.pdf', bbox_inches='tight')
plt.savefig('Versuch_SRV/Bilder/Manuel/41/SignalRauschAbstandAll.pdf', bbox_inches='tight')
plt.show()
'''
'''
#############################
##                         ##
##      Teilaufgabe e      ##
##                         ##
#############################

path = 'Versuch_SRV/Daten/41/e'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files if 'dat' in i]
data.sort()

data = [data[5],data[4],data[3],data[1],data[2],data[0]]

n = ['1\,kHz', '10\,kHz', '100\,kHz', '5\,MHz', '10\,MHz', '20\,MHz']
colors = ['black', 'purple', 'grey', 'orange', 'red', 'blue']

fig, ax = plt.subplots(figsize=(12,8), dpi=80)

#rect = Rectangle((0.17, 0.11), 0.48, 0.44, facecolor='white', ec='none', alpha=1, transform=fig.transFigure, zorder=-1)

#axins = inset_axes(ax, 5, 3 , loc='center', bbox_to_anchor=(0.4,0.34),  bbox_transform=ax.transAxes) # insert pic
#mark_inset(ax,axins,loc1=2,loc2=1)

y_winmin, y_winmax = 0.5, 0.5

for i, n, c in zip(data, n, colors):
    df = pd.read_csv(i, skiprows=4, delim_whitespace= True)
    #df = df[:][:4500]
    df = df[:][:252]
    #df = df[:][2:125]
    df_win = df[:][2:125]
    
    x_F, y_F = df['Fqscale-FFT']/1000, df['y-FFTcurve']
    x, y = df['time'], df['y-generator']
    x_win, y_win = df_win['time'], df_win['y-generator']
    
    if y_win.min() < y_winmin:
        y_winmin =  y_win.min()
        
    if y_win.max() > y_winmax:
        y_winmax = y_win.max()
    
    ax.plot(x_F,y_F, label = r'$f_\mathrm{Band}$ = '+n, color = c)
    #ax.plot(x,y, label = r'$f_\mathrm{Band}$ = '+n, color = c)
    #axins.plot(x,y, label = r'$f_\mathrm{Band}$ = '+n, color = c)
    
#axins.set_xlim(x_win.min(),x_win.max())
#axins.set_ylim(y_winmin,y_winmax)
#axins.tick_params(direction = "in")

#axins.patch.set_facecolor('white')
#axins.patch.set_alpha(0.5)
#axins.patches.append(rect)

#axinsT = axins.secondary_xaxis('top')
#axinsT.tick_params(direction = "in")
#axinsT.xaxis.set_ticklabels([])

#axinsR = axins.secondary_yaxis('right')
#axinsR.tick_params(direction = "in")
#axinsR.yaxis.set_ticklabels([])

#axins.set_ylabel(r'$U$ in V')
#axins.set_xlabel(r'$f$ in kHz')

ax.tick_params(direction = "in")
ax.set_ylabel(r'$U$ in V')
ax.set_xlabel(r'$f$ in kHz')

ax.set_ylabel(r'$A$ in dB')
ax.set_xlabel(r'$f$ in kHz')

axT = ax.secondary_xaxis('top')
axT.tick_params(direction = "in")
axT.xaxis.set_ticklabels([])

axR = ax.secondary_yaxis('right')
axR.tick_params(direction = "in")
axR.yaxis.set_ticklabels([])

#axins.legend(loc = (0.97,0.93)) 
ax.legend()
    
#plt.savefig('Versuch_SRV/Bilder/Manuel/41/BandbreiteKomplett.pdf', bbox_inches='tight')
#plt.savefig('Versuch_SRV/Bilder/Manuel/41/Bandbreite.pdf', bbox_inches='tight')
#plt.savefig('Versuch_SRV/Bilder/Manuel/41/BandbreiteAll.pdf', bbox_inches='tight')
plt.savefig('Versuch_SRV/Bilder/Manuel/41/BandbreiteFourier.pdf', bbox_inches='tight')
plt.show()
'''