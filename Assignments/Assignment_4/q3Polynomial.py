#part-a

def coff_poly(l):
    degree=int(input('Enter the degree of the polynomial: '))
    if degree>len(l)-1:
        return('Degree is too high')
        

    degree=-degree-1
    return l[degree]

print(coff_poly('q3 part a input (list): '))

#part-b

def poly(x):
    return 4*(x**3)-6*(x**2)+0*x-1

print(poly('q3 part b input (integer): '))

#part-c 




