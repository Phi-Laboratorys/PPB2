import numpy as np
from scipy import constants as co

#Berechen an der Stelle I=0

T = 411.3
k = co.Boltzmann
q = co.e
I_PH = 0.7349
I_0 = 2.672e-07
U_OC = 0.52637
R_P = 21.69


n = (q*U_OC)/((np.log((I_PH-U_OC/R_P)/(I_0)+1)*k*T))

print(n)