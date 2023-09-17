<<<<<<< HEAD
#method-1
#the following code finds all the roots of a polynomial

=======
>>>>>>> 577dd4b916df2b0c6646f022a2e55450412bd17a
from numpy import roots as r 
n=int(input("Enter the degree of polynomial"))
ls=[]
for i in range (0,n+1):
    ls.append(int(input("Enter the coefficient of x^"+str(i))))
l=r(ls)
print("The roots of the polynomial are:")
for i in l:
    print(i)
<<<<<<< HEAD
    

#method-2
#newton-raphson method 
#only for rational roots


import unicodeit
print('To find the roots of a polynomial . . .') # Function of the Program

f = []
deg = int(input('Enter the highest degree of the polynomial : '))
print('Enter coefficients from the highest degree to the constant . . .')
for i in range(deg + 1) :
    f.append(float(input(unicodeit.replace(f'Enter a coefficient for x^{deg - i}: '))))

def check(val) : 
    result = 0
    for i in range(len(f)) :
        result = result + f[i] * val ** (deg - i)
    return result
roots = []
div = abs(int(f[deg] / f[0]))
for i in range(-1 * div, div + 1) :
    if check(i) == 0 : roots.append(i)
roots = list(set(roots))
print('The integral root(s) of the polynomial is/are . . .')
for i in range(len(roots)) :
    print(roots[i], end = ', ')
print('\b\b ')
=======
    
>>>>>>> 577dd4b916df2b0c6646f022a2e55450412bd17a
