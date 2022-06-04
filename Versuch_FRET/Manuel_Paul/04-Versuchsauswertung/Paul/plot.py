import numpy as np
import pandas as pd
import os
import matplotlib.pylab as plt
from matplotlib import rc

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=15)

dataD = 'Versuch_FRET/Daten/bleach-data/csv/CY-2-D.csv'
dataS = 'Versuch_FRET/Daten/bleach-data/csv/CY-2-S.csv'

data = dataS

df = pd.read_csv(data, skiprows=1)

print(df.head())
plt.plot(df['Axis [s]'], df['ROI1 []'], label='ROI 1')
plt.plot(df['Axis [s]'], df['ROI2 []'], label='ROI 2')
plt.plot(df['Axis [s]'], df['ROI3 []'], label='ROI 3')
plt.grid()
plt.xlabel('Zeit in s')
plt.legend(loc=7)
plt.show()