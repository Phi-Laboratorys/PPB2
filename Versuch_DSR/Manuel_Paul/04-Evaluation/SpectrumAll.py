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
rc('font', family='serif', size=18)

# Data import
path = 'Versuch_DSR/Daten/Data_Raw/allPeak'
data_files = os.listdir(path)
data = [path + '/' + i for i in data_files]
data.sort()

# transform data in wavelength mit current tuning 
cu_data = 'Versuch_DSR/Daten/currentTuning_points.csv'
cu = pd.read_csv(cu_data)
    
x_cu, y_cu = cu['current(mA)'], cu['lambda(nm)']

# create linear function between data points
i = 0
m, t = [], []
while i < len(x_cu)-1:
    m.append((y_cu[i+1]-y_cu[i])/(x_cu[i+1]-x_cu[i]))
    t.append(y_cu[i]-m[i]*x_cu[i])
    i += 1

#print(m,t)

# data cut
cut = [70, 468, 285]
dis = [200, 60, 100]
fit = [1000, 550, 750]
temp = [24,38,56]

for i, j, k, f, q in zip(data,cut,dis, fit, temp):
    df = pd.read_csv(i, delim_whitespace=True, skiprows=4)
    df = df[:][j:len(df)-j]
    df = df.drop(columns='yai2(V)')
    
    '''Remove Trend'''
    
    x = df['x(A/Hz/V/nm)']
    yai0, yai1, yai3, yai4 = df['yai0(V)'], df['yai1(V)'], df['yai3(V)'], df['yai4(V)']

    yai3 = yai3+abs(yai1[j+k]-yai3[j+k])

    # Fit for Spektrum
    x_fit = [x[j],x[j+1],x[j+f]]
    y_fit = [yai3[j],yai3[j+1], yai3[j+f]]
    model, cov = np.polyfit(x_fit,y_fit,1,cov=True)
    predict = np.poly1d(model)
    y_lin = predict(x)

    yai3 = yai3-y_lin
    yai1 = yai1-y_lin

    # Fit for signal
    model, cov = np.polyfit(x,yai4,1,cov=True)
    predict = np.poly1d(model)
    y_sig = predict(x)

    yai4 = yai4-y_sig

    df['yai0(V)'], df['yai1(V)'], df['yai3(V)'], df['yai4(V)'] = yai0, yai1, yai3, yai4
    
    ######### Trendfree!!!! ##########
    
    n = 5
    
    # Elimate Points betweeen peaks caused by converting the wavelength to frequency
    df['yext(V)'] = df.iloc[argrelextrema(df['yai3(V)'].values, np.less_equal,order=n)[0]]['yai3(V)']
    df['yext(V)'].loc[df['yext(V)'] > -0.003] = np.nan
    
    # Maxima fabry-perot
    df['yai4_max(V)'] = df.iloc[argrelextrema(df['yai4(V)'].values, np.greater_equal,order=n)[0]]['yai4(V)']
    
    print(df[['x(A/Hz/V/nm)','yai4_max(V)']].dropna())
    print(df['yai4_max(V)'].count())
    
    # transformation
    x1 = x.loc[(x >= x_cu[0]) & (x < x_cu[1])]
    result1 = x1.transform(func = lambda x : m[0]*x + t[0])
    x2 = x.loc[(x >= x_cu[1]) & (x < x_cu[2])]
    result2 = x2.transform(func = lambda x : m[1]*x + t[1])
    x3 = x.loc[(x >= x_cu[2]) & (x < x_cu[3])]
    result3 = x3.transform(func = lambda x : m[2]*x + t[2])
    
    result = result1.append(result2).append(result3)
    
    df['lambda(nm)'] = result
    
    #df = df.sort_values(by=['lambda(nm)'])
    
    #df = df.drop_duplicates()
    
    #df.to_csv('Versuch_DSR/Daten/Data_Trendless/allPeak/DataTrendless_allPeak_Temp'+str(q)+'.csv', encoding='utf-8', index=False)

    plt.figure(figsize=(12, 8), dpi=80)
    #plt.plot(x, yai0)
    plt.plot(x, yai3, label='reference beam')
    plt.plot(x, yai4, label='fabry-pérot')
    plt.plot(x,df['yai4_max(V)'],'o')
    plt.show()

    #plt.plot(x,y_sig)
    #plt.plot(x, y_lin, label='linear fit')

    #plt.plot(x_lambda, y_mini, 'o', color='r')

    #plt.xlabel('laser current in mA')
    #plt.ylabel('amplitude in V')
    #plt.legend()
    
    #plt.plot(x_freq, yai1, label='sample beam')
    #plt.plot(x_freq, yai3, label='reference beam')
    #plt.plot(x_freq, yai4, label='fabry-pérot')
    
    df['max'] = df.iloc[argrelextrema(df['yai3(V)'].values, np.greater_equal,order=n)[0]]['yai3(V)']
    
    df = df[df['max'].isnull()]
    
    df = df.sort_index().reset_index()
    df = df.drop(columns=['max'])
    
    df['freq(THz)'] = const.c/(1000*df['lambda(nm)'])
    
    df.to_csv('Versuch_DSR/Daten/Data_Trendless/allPeak/DataTrendless_allPeak_Temp'+str(q)+'.csv', encoding='utf-8', index=False)
    
    #print(df.dropna().sort_values(by=['freq(THz)']).diff())
    
    mini = df['freq(THz)'].idxmin()
    maxi = df['freq(THz)'].idxmax()
    
    x_freq = df['freq(THz)']
    
    x_lambda = df['lambda(nm)']
    yai0, yai1, yai3, yai4 = df['yai0(V)'], df['yai1(V)'], df['yai3(V)'], df['yai4(V)']

    '''Frequency Plot'''
    
    #plt.figure(figsize=(12, 8), dpi=80)
    #plt.plot(x_freq[0:mini-1], yai1[0:mini-1], color='g', label='sample beam')
    #plt.plot(x_freq[maxi:], yai1[maxi:], color='g')
    
    #plt.plot(x_freq[0:mini-1], yai3[0:mini-1], color='orange', label='reference beam')
    #plt.plot(x_freq[maxi:], yai3[maxi:], color='orange')
    #plt.plot(x_freq,df['yext(V)'],'o')
    
    #plt.plot(df['freq(THz)'], df['max'],'.')
    #plt.plot(x_lambda, yai4, label='fabry-pérot')
    #plt.xlabel(r'frequency in THz')
    #plt.ylabel(r'amlitude in V')
    
    #plt.ticklabel_format(useOffset=False)
    #plt.legend()
    #plt.savefig('Versuch_DSR/Bilder/Aufg-2/frequency_allPeak_Temp'+str(q)+'.pdf', bbox_inches='tight')
    #plt.show()