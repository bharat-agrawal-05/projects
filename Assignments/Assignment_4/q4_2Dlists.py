#part-a

def create_2d_matrix(rows,cols):    #this creates a 2D matrix by taking number of rows and columns 
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
for i in range(1,len(l)+1):         #this checks if a certain element exists in a list
    for j in range(1,len(l[0])+1):
        if k==l[i-1][j-1]:
            print(f"{k} is present in the matrix at position {i,j}")   #prints the position of the element if it exists
            found=True

if not found:
    print(f"{k} is not present in the matrix")
    

#part-b

def transpose(l,n):         #transposes the matrix
    L=[]
    for i in range(n):
        L.append([])       #creates empty 2D list

    for i in l:
        a=0
        for j in i:
            L[a].append(j)
            a+=1

    return L

def skew_check(l,n):    #checks for skew symmetric
    for i in range(n):
        for j in range(n):
            if l[i][j]!=-l[j][i]:
                return False
    return True



l=eval(input("Enter a 2d list: "))
n=int(input("Enter the size of the 2d list: "))
transposed_matrix=transpose(l,n)

if transposed_matrix==l:
    print("The matrix is symmetric")

elif skew_check(l,n):
    print("The matrix is skew-symmetric")

else:
    print("The matrix is neither symmetric nor skew-symmetric")

