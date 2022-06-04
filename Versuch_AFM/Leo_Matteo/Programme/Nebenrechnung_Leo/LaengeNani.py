import pandas as pd
import numpy as np

daten = 'Programme/Nebenrechnung_Leo/LaengeNanotube.csv'
df = pd.read_csv(daten, delimiter= '\t')

df['Länge (nm)'] =1e9*np.sqrt(np.multiply(df['x[m]'],df['x[m]'])+np.multiply(df['y[m]'],df['y[m]']))

dprint = df['Länge (nm)'] 


#print(dprint.to_latex())
print(np.min(dprint)/np.max(dprint))