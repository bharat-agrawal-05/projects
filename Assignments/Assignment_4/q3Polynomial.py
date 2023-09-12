#part-a

def coff_poly(l):
    degree=int(input('Enter the degree of the polynomial: '))
    if degree>len(l)-1:    #checking if degree is greater than length of list

        return 'Degree is too high'

    degree=-degree-1
    return f'The Coefficient of the required degree is {l[degree]}'

print(coff_poly(eval(input('q3 part a input (list): '))))

#part-b

def poly(x):
    return f'value of the polynomial for the given value is {4*(x**3)-6*(x**2)+0*x-1}'

print(poly(int(input('q3 part b input (integer): '))))

#part-c 

def polynomial(degree):    #for inputting the coefficients of polynomial
    coefficients = []
    for i in range(degree + 1):
        coefficients.append(float(input(f"Enter coefficient for x^{i}:")))
    return coefficients

def addition_poly(f1,f2):
    m=max(len(f1),len(f2))
    if len(f1)>len(f2):        #for cases in which 1st degree>2nd degree
        diff=len(f1)-len(f2)
        for i in range(diff):  
            f2.append(0)       #appending the greater degree coefficients as it is
    
    elif len(f2)>len(f1):      #for cases in which 1st degree<2nd degree
        diff=len(f2)-len(f1)
        for i in range(diff):
            f1.append(0)      #appending the greater degree coefficients as it is

    f3=[]
    for i in range(m):    
        f3.append([])
    for i in range (m):
        f3[i]=f1[i]+f2[i]
    return f3



f1=polynomial(int(input("Enter the degree of the first polynomial:")))
f2=polynomial(int(input("Enter the degree of the second polynomial:")))

a=addition_poly(f1,f2)

output=''
for i in range(len(a)-1,-1,-1):
    if i == 0:
        output+=(f"({a[i]}x^{i})")
    else:
        output+=(f"({a[i]}x^{i}) + ")

print(output.replace("x^0",""))

