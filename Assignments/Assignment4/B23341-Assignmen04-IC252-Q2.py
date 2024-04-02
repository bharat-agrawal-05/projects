import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



'''
We define 2 Random variables:
X = Number of LED's
Y = Defective or Non-Defective

I have not considered permutations of the defective and non-defective LED's 
as the order we pick the bulbs does not matter.
'''

incad_prob = 0.1
led_prob = 0.05

df = pd.DataFrame(columns = ['0','1','2'],index=['0','1','2'])
df.columns.name = 'X/Y'
df.loc['2'] = [0.27075,0.01425,0.00075]
df.loc['0'] = [0.081,0.009,0.001]
df.loc['1'] = [0.513,0.084,0.003]

df = df.astype(float)
print('Joint Distribution Table:')
print(df)
print()
plt.imshow(df.values, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(np.arange(len(df.columns)), df.columns)
plt.yticks(np.arange(len(df.index)), df.index)
plt.xlabel('Y (Number of Defective Bulbs)')
plt.ylabel('X (Number of LEDs)')
plt.title('Joint Probability Distribution')
plt.show()

marginalX,marginalY =[],[]
for i in df.index:
    print(f"Marginal Distribution for X = {i} is {(df.loc[i].sum())}")
    marginalX.append(df.loc[i].sum())

print()
for i in df.columns:
    print(f"Marginal Distribution for Y = {i} is {(df[i].sum())}")
    marginalY.append(df[i].sum())


plt.subplot(1,2,1)
plt.bar(df.index,marginalX,width=0.5,align='center',alpha=0.7,color='red')
plt.xticks([0,1,2],[0,1,2])
plt.title('Marginal Distribution for X')
plt.xlabel('X')
plt.ylabel('Probability')
plt.grid(True)
plt.subplot(1,2,2)
plt.bar(df.columns,marginalY,width=0.5,align='center',alpha=0.7)
plt.title('Marginal Distribution for Y')
plt.xlabel('Y')
plt.ylabel('Probability')
plt.grid(True)
plt.subplots_adjust(wspace=0.3)
plt.show()

plt.bar([0,1,2],marginalX,width=0.5,align='center',alpha=0.7)
plt.xlabel('Number of LEDs (X)')
plt.ylabel('Probability')
plt.title('PMF of Random Variable X')
plt.grid(True)
plt.show()

"let A be the event that the first bulb is incandescent."
"let B be the event of getting one defective bulb."
"P(A)=(2c2/5c2) + (2c1*3c1/5c2)"
"P(B)=Marginal probability at y=1 i.e. P(Y=1)"
"P(A/B)=P(A∩B)/P(A)=[1/10*0.09 + 6/10*(0.045+0.095)]/[(2c2/5c2)+ 2c1*3c1/5c2]"

print("the Conditional probability of getting one defective \n bulb given the first chosen is incandescent",0.248)
print()
'''
The Random Variables X and Y, I have chosen are not independent as the fxy(x,y) != fx(x)*fy(y)
for instance fxy(0,0) = 0.081 but fx(0)*fy(0) = 0.091*0.86475 = 0.0787

'''
df_replacement = pd.DataFrame(columns = ['0','1','2'],index=['0','1','2'])
df_replacement.columns.name = 'X/Y'
df_replacement.loc['0'] = [0.1296,0.0072,0.0008]
df_replacement.loc['1'] = [0.2052,0.0336,0.0012]
df_replacement.loc['2'] = [0.3249,0.0171,0.0009]

df_replacement = df_replacement.astype(float)
print('Joint Distribution Table with Replacement:')
print(df_replacement)
print()

print(f"Marginal Distribution for X = 0 is {(df_replacement.loc['0'].sum())}")
print(f"Marginal Distribution for X = 1 is {(df_replacement.loc['1'].sum())}")
print(f"Marginal Distribution for X = 2 is {(df_replacement.loc['2'].sum())}")
print()
print(f"Marginal Distribution for Y = 0 is {(df_replacement['0'].sum())}")
print(f"Marginal Distribution for Y = 1 is {(df_replacement['1'].sum())}")
print(f"Marginal Distribution for Y = 2 is {(df_replacement['2'].sum())}")

'''
The new X and Y Random Variables are still not independent events 
as seen by their joint distribution as fxy(x,y) != fx(x)*fy(y)
'''
# print(f'{df_replacement.loc['0'].sum() * df_replacement['0'].sum()} != {df_replacement.loc['0']['0']}')

plt.bar(df_replacement.index,[df_replacement.loc[f'{i}'].sum() for i in range(3)],width=0.5,align='center',alpha=0.7)
plt.xlabel('Number of LEDs (X)')
plt.ylabel('Probability with replacement')
plt.title('PMF of Random Variable X with Replacement')
plt.grid(True)
plt.show()



