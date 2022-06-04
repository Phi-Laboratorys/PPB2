import numpy as np
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=20)

def E(pre, post):
    return 1 - pre/post

def B(pre, post):
    return post/pre

# Data import
path = 'Versuch_FRET/Daten/bleach-data/csv/'
data_files = os.listdir(path)
data_files.sort()
data_files.remove('.DS_Store')
#print(data_files)

df = pd.DataFrame(columns=['Datenreihe', 'ROI 1', 'ROI 2', 'ROI 3'])

string1 = 'CFP'
string2 = 'CY'
string3 = 'S'

for d in data_files:
    
    if ((d.find(string1) == -1) and (d.find(string2) == -1) and (d.find(string3) == -1)):
        #print(d)
        data = path + '/' + d
        dfd = pd.read_csv(data, skiprows=1)
        
        #Pre
        dfpre = dfd.iloc[0:13]

        #Post
        dfpost = dfd.iloc[14:]
        #print(dfpre)

        E1 = B(dfpre['ROI1 []'].mean(), dfpost['ROI1 []'].mean())
        E2 = B(dfpre['ROI2 []'].mean(), dfpost['ROI2 []'].mean())
        E3 = B(dfpre['ROI3 []'].mean(), dfpost['ROI3 []'].mean())

        dfa = pd.DataFrame([[d, E1, E2, E3]], columns=['Datenreihe', 'ROI 1', 'ROI 2', 'ROI 3'])
        df = df.append(dfa, ignore_index=True)

    
print(df.to_latex(index=False))