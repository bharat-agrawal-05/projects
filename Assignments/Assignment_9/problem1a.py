import pandas as pd

df=pd.read_csv('Cars93.csv')
a=list(df['Model'].sort_values(ascending=True))
header=['Model Sorted']
df=pd.DataFrame(a,columns=header)
df.index=df.index+1
df.to_csv('problem1a.csv')
