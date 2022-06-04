import numpy as np
from scipy import constants as co

#Berechen an der Stelle I=0

T = 435
k = co.Boltzmann
q = co.e
I_PH = 1.327
I_0 = 8.83e-07
U_OC = 0.53584
R_P = 25.2


n = (q*U_OC)/(np.log((I_PH-U_OC/R_P)/(I_0)+1)*k*T)

print(n)