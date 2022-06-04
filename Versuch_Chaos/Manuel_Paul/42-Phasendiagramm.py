import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from matplotlib import rc
from scipy.optimize import curve_fit

rc('text', usetex=True)
rc('font', family='serif')

data = '/Versuch_Chaos/Daten/Shinriki/Aufg-a/AufgA.csv'
df = pd.read_csv(data)

def hyperbel(x,a,b):
    #return b((x**2)/(a**2)**0.5)
    return a/(x**3) + b

def fit(x,y):
    popt, _ = curve_fit(hyperbel, x, y)
    return popt

df2=pd.DataFrame(columns=['Übergang auf', 'a','b'])
#print(df)
farben = ['red', 'green', 'blue','c','m', 'y', 'lime']
for i in range(0,7):
    x = [df['x1'][i], df['x2'][i],df['x3'][i]]
    y = [df['y1'][i], df['y2'][i],df['y3'][i]]
    #print(x)
    a, b = fit(x,y)
    x_line = np.linspace(10,100,100)
    y_line = hyperbel(x_line,a,b)
    plt.plot(x_line, y_line, label=df['Uebergang'][i], color=farben[i], lw=0.5)
    plt.plot(x,y,'x',color=farben[i])
    df3 =pd.DataFrame([[df['Uebergang'][i],a,b]], columns=['Übergang auf', 'a','b'])
    df2 = df2.append(df3)

#dotx = [37,39,40,45,60,66,70,73,74,87,91,100]
#doty = [8.4,8.4,8.4,8.4,8.4,8.4,8.4,8.4,8.4,8.4,8.4,8.4]

plt.plot([0,100], [8.4,8.4], ls='--', lw=0.5, color='gray', label='$R_2 = 8,4 \, k\Omega$')
#plt.plot(dotx, doty, '.', c='k')
plt.xlabel('$R_1$ in k$\Omega$')
plt.ylabel('$R_2$ in k$\Omega$')
plt.xlim(10,100)
plt.ylim(6,20)
#plt.grid(True)
plt.legend()
plt.show()

df2 = df2.round(decimals=2)
print(df2.to_latex(index=False,decimal=','))





