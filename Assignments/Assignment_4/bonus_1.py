from numpy import roots as r 
n=int(input("Enter the degree of polynomial"))
ls=[]
for i in range (0,n+1):
    ls.append(int(input("Enter the coefficient of x^"+str(i))))
l=r(ls)
print("The roots of the polynomial are:")
for i in l:
    print(i)
    