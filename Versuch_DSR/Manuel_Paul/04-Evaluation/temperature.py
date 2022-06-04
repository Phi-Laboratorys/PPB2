import numpy as np
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc
from scipy.signal import argrelextrema
from scipy.optimize import curve_fit
import scipy.constants as const

rc('text', usetex=True)
rc('font', family='serif', size=24)

# Data import
path = 'Versuch_DSR/Daten/Data_Trendless/allPeak'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files]
data.sort()

st, end, temp = [500, 250, 350], [900, 500, 700], [24,38,56]

for i,s,e,t in zip(data,st,end,temp):
    df = pd.read_csv(i, index_col=0)
    df = df[:][s:e]
    
    x = df['freq(THz)']
    yai1, yai3 = df['yai1(V)'], df['yai3(V)']

    n = 50    
    df['min'] = df.iloc[argrelextrema(df['yai3(V)'].values, np.less_equal,order=n)[0]]['yai3(V)']
    
    df_mean = df[['freq(THz)','min']].dropna().reset_index()
    m = df_mean['freq(THz)'][0]
    a = df_mean['min'][0]
    
    def gaussian(x, sigma):
        return a * np.exp(-((x - m) / (sigma))**2)

    popt, _ = curve_fit(gaussian, x, yai3)

    sigma = popt[0]
    
    #print(np.sqrt(4/np.pi)*((sigma*const.c)/(m)))
    #print((1.44322e-25/(2*const.k))*((sigma*const.c)/(m))**2)
    
    plt.figure(figsize=(12, 8), dpi=80)
        
    plt.plot(x, gaussian(x, *popt), label='gaussian fit') # for peak 2 at temp '+str(t))
    plt.fill_between(x,0,gaussian(x, *popt),alpha=0.5)
    
    #plt.plot(x,yai1)
    plt.plot(x,yai3, label='reference beam', color='black') #at temp '+str(t)+'$^\circ$C', color='black')
    #plt.plot(x,df['min'],'o')
    plt.xlabel('frequncy in THz')
    plt.ylabel('amplitude in V')
    plt.ticklabel_format(useOffset=False)    
    plt.legend()
    plt.savefig('Versuch_DSR/Bilder/Aufg-5/gaussFitTemp'+str(t)+'.pdf',bbox_inches='tight')
    plt.show()