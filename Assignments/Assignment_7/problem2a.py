import sys
import numpy as np

def adjointfnc(matrix):
    # Calculate the cofactor matrix
    cofactor_matrix = np.zeros(matrix.shape)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cofactor_matrix[i, j] = ((-1) ** (i + j)) * np.linalg.det(minor)

    # Transpose the cofactor matrix to get the adjoint
    adjoint = cofactor_matrix.T
    return adjoint


input=sys.argv[1:]
if len(input)!=2:
    print('Please provide 2 file names as command line arguments')
    exit()
i=input[0]
try:
    with open(i,'r') as f:
        MatA=[]
        lines=f.readlines()
        for line in lines[1:]:
            numbers=line.split()
            numbers=[int(i) for i in numbers]
            MatA.append(numbers)
except:
    print(f'File {i} not found')
    exit()

i=input[1]
try:
    with open(i,'r') as f:
        MatB=[]
        lines=f.readlines()
        for line in lines[1:]:
            numbers=line.split()
            numbers=[int(i) for i in numbers]
            MatB.append(numbers)
except:
    print(f'File {i} not found')
    exit()

a=np.array(MatA)
b=np.array(MatB)
adja=adjointfnc(a)
x=np.matmul(adja,b)
if np.linalg.det(a)!=0 :
    with open('problem2aOp.txt','w') as f:
        f.write('Unique solution')

elif x==0 and np.linalg.det(a)==0:
    with open('problem2aOp.txt','w') as f:
        f.write('Infinite solutions')

elif x!=0 and np.linalg.det(a)==0:
    with open('problem2aOp.txt','w') as f:
        f.write('No solution')
    


    



