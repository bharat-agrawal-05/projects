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

#this prints the 2d list in matrix format
for i in l:
    print(i)
            

