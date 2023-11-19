import pandas as pd
import csv
import sys

#part-a
df=pd.read_csv('Cars93.csv')
a=list(df['Model'].sort_values(ascending=True))
header=['Model Sorted']
df=pd.DataFrame(a,columns=header)
df.index=df.index+1
df.to_csv('problem1a.csv')

#part-b

df=pd.read_csv('Cars93.csv')
types=df['Type'].unique()
with open('problem1b.csv','w') as f:
    w=csv.writer(f)
    w.writerow(df.columns)

for i in types:
    data=df.groupby('Type').get_group(i)
    required_data=pd.DataFrame(data[data['Max.Price']==data['Max.Price'].max()])
    with open('problem1b.csv','a') as f:
        writer=csv.writer(f)
        writer.writerows(required_data.values)
    
#part-c

if len(sys.argv)!=2:
    print('Enter Name of the Manufacturer as command line argument')
    exit()

input=sys.argv[1]
df=pd.read_csv('Cars93.csv')
required_data=df[df['Manufacturer']==input]['Model']
print(required_data)

#part-d
df=pd.read_csv('Cars93.csv')
required_data=df.groupby('Manufacturer').size().sort_values(ascending=False)
header=['Count']
df=pd.DataFrame(required_data,columns=header)
df.to_csv('problem1d.csv')