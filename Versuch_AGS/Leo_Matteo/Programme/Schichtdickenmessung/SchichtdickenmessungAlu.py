import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

#Variablen dekalration

mu = 0.85 #cm⁻1
Index_Max = 40

def schichtdicke(I, I_0):
    return -np.log(I/I_0)/mu


#Daten einlesen
daten = 'Versuch_Alpha_Gamma_Spektroskopie/Daten/CSV/SChichtdickenmessung.csv'
df = pd.read_csv(daten)

std_I_0 = np.std(df['I_0'])
std_I = np.std(df['I'])

I_0 = np.mean(df['I_0'])
I = np.mean(df['I'])

relativ = std_I/I

gesamtfehler = np.sqrt((-1/I*std_I/2)**2+(I_0/I**2*std_I_0/2)**2)

print(schichtdicke(I, I_0))
print('Fehler: '+ str(gesamtfehler))