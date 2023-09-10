#part-a

def create_2d_matrix(rows,cols):
    L=[]
    for i in range (1,rows+1):
        L1=[]
        for j in range (1,cols+1):
            k=eval(input(f"Enter a element for position{i,j}: "))
            L1.append(k)
        
        L.append(L1)
    return L

rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
l=(create_2d_matrix(rows,cols))    #this creates a 2d list and stores it in a variable l


for i in l:             #this prints the 2d list in matrix format
    print(i)
            
#part-b

def transpose(l,n):
    L=[]
    for i in range(n):
        L.append([])

    for i in l:
        a=0
        for j in i:
            L[a].append(j)
            a+=1

    return L


l=eval(input("Enter a 2d list: "))
n=int(input("Enter the size of the 2d list: "))
transposed_matrix=(transpose(l,n))

if transposed_matrix==l:
    print("The matrix is symmetric")

elif transposed_matrix==-l:
    print("The matrix is skew-symmetric")

else:
    print("The matrix is neither symmetric nor skew-symmetric")

