#part-a
def fibonacci(n):
    a=0             #assign initial value as 0
    b=1             #assign second value as 0
    c=0     
    for i in range(n):
        print(c,end=" ")
        a=b                     #number swapping
        b=c
        c=a+b                   #storing numbers in fibonacci form
        
fibonacci(int(input("q1 part a input (integer): ")))   
print()        #creating a new line
#part-b

def majority_element(l):
    for i in l:
        if l.count(i)>len(l)/2:        #checks for majority element
            return i
    
    return -1
        
print(majority_element(eval(input('q1 part b input (list): '))))

#part-c
def repeating_element(l):
    for i in l:
        a=[]    #creating empty list
        for i in l:
            if i not in a:          
                a.append(i)     #appending non repeating elements in a
            else:
                return i
            
    return 'no repeating element exists'

print(repeating_element(eval(input('q1 part c input (list): '))))

#part-d
def pattern(n):
    for i in range(n+1):
        print(" "*(n-i),end="")
        for j in range(1,i+1):
            print(j,end="")
        for k in range(i-1,0,-1):
            print(k,end="")

        print()
            
pattern(int(input('q1 part d input (integer): ')))

#part-e
def remove_repeated_elements(l):
    a=[]     #creating empty list
    for i in l:
        if i not in a:
            a.append(i)    #appending only if element not already present
    return a

print(remove_repeated_elements(eval(input('q1 part e input (list): '))))

