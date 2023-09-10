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

k=eval(input("Enter a number to check if it is present in the matrix: "))
found=False
for i in range(1,len(l)+1):
    for j in range(1,len(l[0])+1):
        if k==l[i-1][j-1]:
            print(f"{k} is present in the matrix at position {i,j}")
            found=True

if not found:
    print(f"{k} is not present in the matrix")
    
