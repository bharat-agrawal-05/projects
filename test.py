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

def checking_skew(matrix):
    


l=eval(input("Enter a 2d list: "))
n=int(input("Enter the size of the 2d list: "))
transposed_matrix=(transpose(l,n))

if transposed_matrix==l:
    print("The matrix is symmetric")

elif transposed_matrix==-:
    print("The matrix is skew-symmetric")

else:
    print("The matrix is neither symmetric nor skew-symmetric")
