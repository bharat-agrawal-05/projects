#part-a

def leap_year(year):
    if year%4==0:
        if year%400==0:
            return(True)
        elif year%100==0:
            return(False)
        else:
            return(True)
    else:
        return(False)
    
print(leap_year(int(input('q6 part a input (int):'))))
    
#part-b

def triangle(a,b,c):
    
    if a>b+c or b>a+c or c>b+a:
        if a==b==c:
            return 'equilateral triangle'

        elif a==b and b==c and c!=a:
            return 'isoceles triangle'

        elif a!=b!=c:
            return 'scalene triangle' 

    else:
        return 'triangle does not exist' 
    
side1=int(input('q6 part b input (side 1):'))
side2=int(input('q6 part b input (side 2):'))
side3=int(input('q6 part b input (side 3):'))
print(triangle(side1,side2,side3))

      

