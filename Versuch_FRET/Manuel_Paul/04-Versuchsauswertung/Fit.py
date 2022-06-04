import numpy as np
from numpy.core.numeric import moveaxis
from numpy.lib.function_base import append
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc
from pandas.core.algorithms import diff
from scipy.signal import argrelextrema
from scipy.optimize.minpack import curve_fit
from scipy.signal import argrelextrema
from scipy.signal import convolve
import scipy.special
import scipy.constants as const

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=20)



'''Single Exponential Fit'''
'''
# Data import
path = 'Versuch_FRET/Daten/TCSPC-data/Aufg-1'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files]
data.sort()

data_CFP = [i for i in data if 'CFP' in i]
data_YFP = [i for i in data if 'YFP' in i]
data_CY  = [i for i in data if 'CY'  in i]

def fitSingleExp(data, picname, start, end, t_dead): 
    
    # Fitting Functions
    def singleExp(x, t):
        return amp*np.exp(-(x-x0)/t)
    
    for j,i in zip(data,picname):
        df = pd.read_csv(j, delim_whitespace=True, skiprows=11, encoding='Windows 1252')
        df = df.apply(pd.to_numeric, errors='coerce')
        df = df[:][start:end].reset_index()

        x = df['Time[ns]']
        y = df['Decay']

        n = 200
        df['max'] = df.iloc[argrelextrema(df['Decay'].values, np.greater_equal,order=n)[0]]['Decay']

        fit_start = df['max'].dropna().index.values[0]

        df_fit = df[['Time[ns]','Decay','Fit']]
        df_fit = df_fit[df_fit['Time[ns]']>=t_dead].reset_index()

        amp, x0 = df_fit['Decay'][0], df_fit['Time[ns]'][0]

        popt, _ = curve_fit(singleExp, df_fit['Time[ns]'], df_fit['Decay'])
        print(j, x0, amp, *popt)

        plt.figure(figsize=(12, 8), dpi=80)
        plt.plot(x,y, label = 'Messreihe')
        plt.plot(df_fit['Time[ns]'], singleExp(df_fit['Time[ns]'], *popt), label = 'Exponentieller Fit', lw=2)
        plt.xlabel('$t$ in ns')
        plt.ylabel('Intensität')
        plt.legend()
        plt.savefig('Versuch_FRET/Bilder/Lebenszeit/SingleExp/'+i+'.pdf',bbox_inches='tight')
        #plt.show()

filename = ['CFP1-c1','CFP1-c2','CFP2-c1','CFP2-c2','CFP3-c1','CFP3-c2']
fitSingleExp(data_CFP, filename, 90, 1550, 5)
filename = ['YFP1-c1','YFP1-c2','YFP2-c1','YFP2-c2','YFP3-c1','YFP3-c2']
fitSingleExp(data_YFP, filename, 90, 1550, 5)
filename = ['CY1-c1','CY1-c2','CY2-c1','CY2-c2','CY3-c1','CY3-c2','CY4-c1','CY4-c2','CY5-c1','CY5-c2']
fitSingleExp(data_CY, filename, 90, 1550, 5)
'''



'''Double Exponential Fit'''
'''
path = 'Versuch_FRET/Daten/TCSPC-data/Aufg-2'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files]
data.sort()

def fitDoubleExp(data, picname, start, end, t_dead, amp, amp_guess, k): 
    
    # Fitting Functions
    def doubleExp(x, t1, t2):
        return amp*(np.exp(-x/t1)+amp_guess*np.exp(-x/t2)) # b = A2/A1, a = A1
    
    df = pd.read_csv(data, delim_whitespace=True, skiprows=11, encoding='Windows 1252')
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df[:][start:end].reset_index()

    x = df['Time[ns]']
    y = df['Decay']

    n = 200
    df['max'] = df.iloc[argrelextrema(df['Decay'].values, np.greater_equal,order=n)[0]]['Decay']

    fit_start = df['max'].dropna().index.values[0]

    df_fit = df[['Time[ns]','Decay','Fit']]
    df_fit = df_fit[df_fit['Time[ns]']>=t_dead].reset_index()

    popt, _ = curve_fit(doubleExp, df_fit['Time[ns]'], df_fit['Decay'])

    plt.figure(figsize=(12, 8), dpi=80)
    plt.plot(x,y, label = 'Messreihe')
    plt.plot(df_fit['Time[ns]'], doubleExp(df_fit['Time[ns]'], *popt), label = 'Doppel Exponentieller Fit', lw=2)
    plt.xlabel('$t$ in ns')
    plt.ylabel('Intensität')
    plt.legend()
    
    plt.savefig('Versuch_FRET/Bilder/Lebenszeit/DoubleExp/'+picname+str(k)+'.pdf',bbox_inches='tight')
    #plt.show()
    
    delta_yq = (df_fit['Decay'] - doubleExp(df_fit['Time[ns]'], *popt))**2
    return delta_yq.sum(), *popt
    
        
filename = 'CY5-c12'
Amp_guess = np.linspace(0, 30, 50)

list_delta_y = []
list_t1, list_t2 = [], []
k = 1

for i in Amp_guess:
    delta_y, t1, t2 = (fitDoubleExp(data[4], filename, 90, 1550, 5, 22002, i, k))
    list_delta_y.append(delta_y)
    list_t1.append(t1)
    list_t2.append(t2)
    k += 1

d = {'Amp':Amp_guess,  'delta_y':list_delta_y, 't1':list_t1, 't2':list_t2}
df_opt = pd.DataFrame(d)

df_opt['delta_y'] = df_opt['delta_y']/1e10
df_opt = df_opt[:][0:41]

mini = df_opt.iloc[[df_opt[['delta_y']].idxmin()[0]]]

print(df_opt.to_latex())

plt.figure(figsize=(12, 8), dpi=80)
plt.plot(df_opt['Amp'], df_opt['delta_y'], 'o', label = 'Berechnete Werte')
plt.plot(mini['Amp'], mini['delta_y'], 'o', label = 'Minimum', color = 'r')
plt.xlabel(r'$\frac{N_2}{N_1}$')
plt.ylabel(r'$\sum(\Delta y)^2$')
plt.legend()
plt.savefig('Versuch_FRET/Bilder/Lebenszeit/DoubleExp/Optimize.pdf', bbox_inches='tight')
plt.show()
'''



'''Convolution'''

data = 'Versuch_FRET/Daten/TCSPC-data/Aufg-3/CY1-c1.dat'

df = pd.read_csv(data, delim_whitespace=True, skiprows=12, encoding='Windows 1252')
df = df.apply(pd.to_numeric, errors='coerce')
df = df[:][90:1550].reset_index()
#df['IRF'] = df['IRF'].shift(periods = 25)

# IRF cut
x_IRF, y_IRF = df['Time[ns]'][:100], df['IRF'][:100]
x_IRFcut, y_IRFcut = df['Time[ns]'][:75], df['Decay'][:75]

# Spiegeln des IRF
x_IRFmir, y_IRFmir = df['Time[ns]'][:150], y_IRFcut.append(y_IRFcut[::-1])

# Gaussian
def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-((x - mean) / (np.sqrt(2) * stddev))**2)

popt, _ = curve_fit(gaussian, x_IRF, y_IRF)
amplitude, mean, sigma = popt

y_IRFgauss = gaussian(x_IRF, *popt)

print(popt)
# Plot
#plt.figure(figsize=(12, 8), dpi=80)
#plt.plot(x_IRF, y_IRF, label = 'IRF', color = 'black')
#plt.plot(x_IRF, y_IRFgauss, label = 'Gauß-Kurve Fit')
#plt.plot(x_IRFmir, y_IRFmir, label = 'Gespiegeltes IRF')
#plt.plot(x_IRFcut, y_IRFcut, label = 'Cut IRF')
#plt.plot(x_IRFcon, y_IRFcon)
#plt.xlabel('$t$ in ns')
#plt.ylabel('Intensität')
#plt.legend()
#plt.savefig('Versuch_FRET/Bilder/Lebenszeit/Convolution/IRF.pdf', bbox_inches='tight')
#plt.savefig('Versuch_FRET/Bilder/Lebenszeit/Convolution/IRFmirror.pdf', bbox_inches='tight')
#plt.savefig('Versuch_FRET/Bilder/Lebenszeit/Convolution/IRFgauss.pdf', bbox_inches='tight')
#plt.savefig('Versuch_FRET/Bilder/Lebenszeit/Convolution/IRFfit.pdf', bbox_inches='tight')
#plt.show()

#d_IRF = {'Mirror':y_IRFmir.values, 'Gauss':y_IRFgauss.values}

#df_IRF = pd.DataFrame(d_IRF)
#df = df.join(df_IRF)

def convo(df, tau, name, irf):

    def singleExp(x, t, amp, x0):
            return amp*np.exp(-(x-x0)/t)

    n = 200
    df['max'] = df.iloc[argrelextrema(df['Decay'].values, np.greater_equal,order=n)[0]]['Decay']

    fit_start = df['max'].dropna().index.values[0]
    amp, x0 = df['Decay'][fit_start], df['Time[ns]'][fit_start]

    df_fit = df[['Time[ns]','Decay']][fit_start:]

    k = 1
    delta_y = []

    for i in tau:
        df_fit['Decay_Fitted'+str(k)] = singleExp(df_fit['Time[ns]'], i, amp, x0)
        df = df.join(df_fit['Decay_Fitted'+str(k)])

        df['Decay_Fitted'+str(k)] = df['Decay_Fitted'+str(k)].fillna(0)
        df['Con'+str(k)] = convolve(df['Decay_Fitted'+str(k)], irf, mode = 'same')/sum(irf)

        x = df['Time[ns]']
        
        plt.figure(figsize=(12, 8), dpi=80)

        plt.plot(x, df['Decay'], label = 'Messreihe')
        plt.plot(x, df['Con'+str(k)], label = 'Faltung')
        plt.ylabel('Intensität')
        plt.xlabel('$t$ in ns')
        plt.savefig('Versuch_FRET/Bilder/Lebenszeit/Convolution/'+name+'/'+name+str(k)+'.pdf', bbox_inches='tight')
        #plt.clf()
        
        delta_y.append((sum(df['Decay']-df['Con'+str(k)])**2)/1e12)
        k+=1
    
    return delta_y

tau = np.linspace(2,5,50)
irf = y_IRFmir
name = 'Mirror'

delta_y = convo(df, tau, name, irf)
d_opt = {'delta_y':delta_y, 'tau':tau}
df_opt = pd.DataFrame(d_opt)

mini = df_opt.iloc[[df_opt[['delta_y']].idxmin()[0]]]

print(mini)

plt.figure(figsize=(12, 8), dpi=80)

plt.plot(tau, delta_y, 'o', label = 'Berechnete Werte')
plt.plot(mini['tau'].values,mini['delta_y'].values,'o', color = 'r', label = 'Minimum')
plt.xlabel(r'$\tau$ in ns')
plt.ylabel(r'$\sum(\Delta y)^2$')
plt.legend()
plt.savefig('Versuch_FRET/Bilder/Lebenszeit/Convolution/'+name+'/Optimize.pdf', bbox_inches='tight')
plt.show()