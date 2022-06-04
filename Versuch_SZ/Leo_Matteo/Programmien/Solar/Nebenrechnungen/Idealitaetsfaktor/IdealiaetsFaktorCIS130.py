import numpy as np
from scipy import constants as co

#Berechen an der Stelle I=0

T = 799.9
k = co.Boltzmann
q = co.e
I_PH = 0.004194
I_0 = 0.0001329
U_OC = 0.23965
R_P = 3193


n = (q*U_OC)/((np.log((I_PH-U_OC/R_P)/(I_0)+1)*k*T))

print(n)