import pandas as pd
import numpy as np

daten = 'Versuch_Alpha_Gamma_Spektroskopie/Daten/CSV/Pilze.csv'
df = pd.read_csv(daten)
IndexMaxTopf = np.where(df['Count']== np.max(df['Count']))[0][0]  #Sucht Index
MaxTopf = df.iloc[IndexMaxTopf,0]
print(MaxTopf)