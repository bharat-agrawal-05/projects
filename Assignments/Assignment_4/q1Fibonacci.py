#part-a
def fibonacci(n):
    a=0
    b=1
    c=0
    for i in range(n):
        print(c,end=" ")
        a=b
        b=c
        c=a+b
        
fibonacci(int(input("q1 part a input (integer): ")))    

#part-b

def majority_element(l):
    for i in l:
        if l.count(i)>len(l)/2:
            return i
    
    return -1
        
print(majority_element(eval(input('q1 part b input (list): '))))

#part-c
def repeating_element(l):
    for i in l:
        a=[]
        for i in l:
            if i not in a:
                a.append(i)
            else:
                return i
            
    return 'no repeating element exists'

print(repeating_element(eval(input('q1 part c input (list): '))))

#part-d
def pattern(n):
    for i in range(n):
        print(" "*(n-i),end="")
        for j in range(1,i+1):
            print(j,end="")
        for k in range(i-1,0,-1):
            print(k,end="")

        print()
            
pattern(int(input('q1 part d input (integer): ')))

#part-e
def remove_repeated_elements(l):
    a=[]
    for i in l:
        if i not in a:
            a.append(i)
    return a

print(remove_repeated_elements(eval(input('q1 part e input (list): '))))

