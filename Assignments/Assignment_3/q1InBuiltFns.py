#part-a-b
import math

x=23.5312

#the following statements prints the required output

print(math.ceil(x))
print(math.floor(x))
print(round(x,3))
print(type(round(x)))
print(format(x,'.3f'))
print(type(format(x)))
print(round(x,3)-float(format(x,'.3f')))

#part-b

L=[' ','23','q1b']

for i in L:
    if i.isalpha():   #checks for alphabets
        print(i,'is alphabetic')
        
    elif i.isnumeric():     #checks for numbers
        print(i,'is numeric')
        
    elif i.isalnum():    #checks for alpha-numeric
        print(i,'is alpha-numeric')
        
    elif i.isspace():   #checks for spaces
        print(i,'is a space')

    
        




