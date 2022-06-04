import numpy as np
from scipy import constants as co

#Berechen an der Stelle I=0

T = 540.6
k = co.Boltzmann
q = co.e
I_PH = 0.2805
I_0 = 5.549e-06
U_OC = 0.50686
R_P = 1e+05



n = (q*U_OC)/(np.log((I_PH-U_OC/R_P)/(I_0)+1)*k*T)

print(n)