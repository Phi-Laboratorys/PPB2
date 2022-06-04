# Leonhard Schatt

import numpy as np
import matplotlib as plt
import scipy as sp
from scipy import constants as const
import pandas as pd

# Definiere die Shockley-Gleichung
def shockley(x, R_Reihe, R_Paralell, I_Ph, I_S, n)
    return I_S*(np.exp((const.e*(X - R_Reihe))))
# Importiere Daten
filename = 'Messung3_3SiMulti_130.csv'
df = pd.read_csv(filename)
