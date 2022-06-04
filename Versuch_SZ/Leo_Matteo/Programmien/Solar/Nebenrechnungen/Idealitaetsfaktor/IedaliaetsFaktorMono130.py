import numpy as np
from scipy import constants as co

#Berechen an der Stelle I=0

T = 406.1
k = co.Boltzmann
q = co.e
I_PH = 0.3223
I_0 = 1.812e-07
U_OC = 0.50312
R_P = 19.28


n = (q*U_OC)/(np.log((I_PH-U_OC/R_P)/(I_0)+1)*k*T)

print(n)