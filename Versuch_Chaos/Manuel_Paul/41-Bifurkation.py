from matplotlib.pyplot import colorbar
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif', size=14)

data = "Versuch_Chaos/Daten/Pendel/3.1/BifurkationPendel.csv"
df = pd.read_csv(data)

#Berechnung
df = df.sort_values(by='Masse [g]')
df['sa'] = df['sUA']
df['sUA'] = np.sqrt(2)*df['sa']
df["Delta^2"] = (df["UAl [V]"] - df["UAr [V]"])**2
df['sDelta^2'] = 4*df['sa']*np.abs(df["UAl [V]"] - df["UAr [V]"])

#print(df.to_latex())


x = df["Masse [g]"]
y1, y2 = df["UAl [V]"], df["UAr [V]"]
plt.plot(x,y1, 'o', color='orange')
plt.plot(x,y2, 'o', color='orange')
plt.xlabel(r'$M$ in g')
plt.ylabel(r'$U_a$ in V')
plt.savefig("Versuch_Chaos/Bilder/Pendel/3.1/BifurkationMass.pdf",bbox_inches='tight')

#plt.show()


x = df['Masse [g]'][7:]
y, y_err = df['Delta^2'][7:], df['sDelta^2'][7:]

# Fit
model, cov = np.polyfit(x,y,1,cov=True)
predict = np.poly1d(model)
x_lin = np.linspace(x.min()-1,x.max(),300)
y_lin = predict(x_lin)

M_k = 14.73/0.7665
y_k, x_k = np.repeat(0,300), np.repeat(M_k,300)
x_s, y_s = np.linspace(x.min()-1,x.max(),300), np.linspace(y.min()-1,y.max(),300)
print(predict, M_k)
print(np.sqrt(np.diag(cov)))

plt.figure(figsize=(12, 8), dpi=80)
plt.xlabel(r'$M$ in g')
plt.ylabel(r'$(\Delta U_a)^2$ in V$^2$')
plt.errorbar(x,y, yerr=y_err, fmt='x', capsize=5, color='darkorange', label='Messreihe')
plt.plot(x_lin,y_lin, 'orange', label=r'Linearer Fit: $(\Delta U_a)^2 = 0.7665 \frac{\mathrm{V}^2}{\mathrm{g}} M - 14.73~\mathrm{V}^2$')
plt.plot(x_k,y_s,'r', linestyle='--',label='Kritische Masse: $M_k = 19.22$ g')
plt.plot(x_s,y_k,'r', linestyle='--')
plt.legend()
#plt.savefig("Versuch_Chaos/Bilder/Pendel/3.1/linearFit.pdf", bbox_inches='tight')
#plt.show()