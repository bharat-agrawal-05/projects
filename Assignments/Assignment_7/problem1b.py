import numpy as np
import sys


def writing(input,file):
    with open(file,'w') as f:
        f.write(str(len(input))+' '+str(len(input[1]))+'\n')
        a=1     #this is a counter to check if we are at the last row or not
        for i in input:
            row=''
            for j in i:
                row=row+str(j)+' '
            row=row.rstrip()
            if a!=len(input):
                row=row+'\n'
            f.write(row)
            a+=1

input=sys.argv[1:]
if len(input)!=2:
    print("Please give 2 files input as: \npython problem1b.py MatA.txt MatB.txt")
    exit()

i=input[0]
try:  
    with open(i,'r') as f:
        matA=[]
        for i in f.readlines()[1:]:
            numbers=i.split()
            line=[]
            for j in numbers:
                line.append(int(j))
            matA.append(line)

except:
    print('File 1 not found')
    exit()

i=input[1]
try:
    with open(i,'r') as f:
        matB=[]
        for i in f.readlines()[1:]:
            numbers=i.split()
            line=[]
            for j in numbers:
                line.append(int(j))
            matB.append(line)

except:
    print('file 2 not found')
    exit()

try:
    ad=np.add(matA,matB)
    writing(ad,'addOp.txt')

except:
    print('matrices are not compatible for addition')

try:
    mul=np.matmul(matA,matB)
    writing(mul,'multOp.txt')

except:
    print('matrices not compatible for multiplication')
    