# Leonhard Schatt
import pandas as pd
import numpy as np

daten = 'MPP/NeuMessung3_3CIS_180_Result_FitData.txt'
df = pd.read_csv(daten, delimiter='\t', names=['U','I'])

df['P'] = - np.multiply(df['U'], df['I'])
Maximum = np.max(df['P'])
MPPindex = int(np.where(Maximum== df['P'])[0])

#MPP Werte

for i in range(len(df['U'])):
    if (df.iloc[i,1]>0):
        U_OC = df.iloc[i,0]

        break


for i in range(len(df['U'])):
    if (df.iloc[i,0]>0):
        I_PH = df.iloc[i,1]
        break

FF = Maximum/(-I_PH*U_OC)


print(daten)
        
print('U_MPP:'+str(df.iloc[MPPindex,0]))
print('I_MPP:'+str(df.iloc[MPPindex,1]))

print('U_OC: '+ str(U_OC))
print('I_PH: '+ str(I_PH))
print('FF: '+ str(FF))