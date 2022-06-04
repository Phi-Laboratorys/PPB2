import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc, rcParams

# Format of the plot
rc('text', usetex=True)
rc('font', family='serif', size=18)

d = {'current(mA)':[107,128.5,129.5,149.5],'lambda(nm)': [780.23125,780.25125,780.234,780.2535]}
df = pd.DataFrame(data=d)

df.to_csv('Versuch_DSR/Daten/currentTuning_points.csv', encoding='utf-8', index=False)

plt.figure(figsize=(12, 8), dpi=80)
plt.plot(df['current(mA)'],df['lambda(nm)'])
plt.ticklabel_format(useOffset=False)
plt.xlabel('laser current in mA')
plt.ylabel('wavelength in nm')
plt.grid(color='grey')
plt.savefig('Versuch_DSR/Bilder/Aufg-1/currentTuning.pdf',bbox_inches='tight')
#plt.show()

# create data from points
def getEquidistantPoints(p1, p2, parts):
    return zip(np.linspace(p1[0], p2[0], parts+1), np.linspace(p1[1], p2[1], parts+1))

anzahl = 100000
lin = list(getEquidistantPoints((df['current(mA)'][0],df['lambda(nm)'][0]), (df['current(mA)'][1],df['lambda(nm)'][1]), anzahl)) + list(getEquidistantPoints((df['current(mA)'][1],df['lambda(nm)'][1]), (df['current(mA)'][2],df['lambda(nm)'][2]), anzahl)) + list(getEquidistantPoints((df['current(mA)'][2],df['lambda(nm)'][2]), (df['current(mA)'][3],df['lambda(nm)'][3]), anzahl))

x, y = [], []
for i in lin:
    x.append(i[0])
    y.append(i[1])

d = {'current(mA)':x,'lambda(nm)':y}
df = pd.DataFrame(data=d)
df.drop_duplicates()
print(df)

df.to_csv('Versuch_DSR/Daten/currentTuning.csv', encoding='utf-8', index=False)

#plt.plot(x,y)
#plt.show()