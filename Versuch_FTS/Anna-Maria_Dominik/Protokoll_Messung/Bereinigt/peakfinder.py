import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt

element = 'Natrium'
measurement ='einhuellende'
rpath =element+'_'+measurement+'_0.dat'
wpath = 'peaks_'+element+'_'+measurement+'1.txt'
file = open(wpath,'w')
data = np.loadtxt(rpath,skiprows=5)
length = data[:,0]
intensity = data[:,1]
errors = data[:,2]

#print(len(length))

peaks = sp.find_peaks(intensity, prominence=0.003)
peaks_l = sp.find_peaks(errors, prominence=0.01)
peaks_l = peaks_l[0]
peaks = peaks[0]
print(peaks)
file.write('Lenght\tIntensity\tError\n')
for i in peaks:
    file.write(str(length[i])+'\t'+str(intensity[i])+'\t'+str(errors[i])+'\n')
file.close()
print(len(peaks))
print(len(peaks_l))