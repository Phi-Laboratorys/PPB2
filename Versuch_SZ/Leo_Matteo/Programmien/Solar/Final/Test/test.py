
import pandas as pd

daten = 'Test/NeuMessung3_3CIS_130.txt'
df = pd.read_csv(daten, delimiter='\t', names=['U','I'])

print(df)
df['U']= df['U']*10
df['I']= df['I']/10

df.to_csv('test.txt', sep='\t',header=False,index=False)

