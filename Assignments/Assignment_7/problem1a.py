import sys
import numpy as np

def check_input(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

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
if len(input)!=4:
    print("Matrix sizes are not correct \nplease enter 4 command line arguments as: \npython problem1a.py r1 c1 r2 c2 \nwhere r1,c1 are the size of matrix A \nr2,c2 are the size of matrix B")
    exit()

for i in input:
    if check_input(i)==False:
        print('Please enter integers only')
        exit()

r1=int(input[0])
c1=int(input[1])
r2=int(input[2])
c2=int(input[3])
matA=np.random.randint(0,10,size=(r1,c1))
matB=np.random.randint(0,10,size=(r2,c2))
writing(matA,'MatA.txt') 
writing(matB,'MatB.txt')
