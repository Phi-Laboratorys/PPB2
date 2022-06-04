# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:11:20 2021

@author: froes
"""
name = '_spol90.dat'
path='CHBr3'
name = path+name
rpath =path+'/Raman-Spectrum_'+name
offset = 0.6

import numpy as np
a = np.array([1,2,3,4])
a=a-1
print(a)
file = open(name, 'w')

data = np.loadtxt(rpath,skiprows=6)
wavelength = data[:,0]
intensity = data[:,1]
errors = data[:,2]

print(np.shape(wavelength.reshape(-1)))

wavelength = wavelength+offset

file.write('Waveleght\tIntensity\tError\n')
for i in range(len(wavelength)):
    file.write(str(wavelength[i])[:6]+'\t'+str(intensity[i])+'\t'+str(errors[i])+'\n')
file.close()
