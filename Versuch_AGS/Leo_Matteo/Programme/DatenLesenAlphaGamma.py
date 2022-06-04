import pandas as pd

daten = 'Energieeichung_Am.RPT'

#Daten importiernen
df = pd.read_csv(daten,delimiter='\\', skiprows= 10, names=['Kanal', 'Dump', 'Count'])
del df['Dump']



daten = daten.replace('RPT', 'csv')

df.to_csv(daten, index= False)


