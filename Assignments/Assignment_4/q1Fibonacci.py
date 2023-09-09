def fibonacci(n):
    a=0
    b=1
    c=0
    for i in range(n):
        print(c,end=" ")
        a=b
        b=c
        c=a+b
        


#fibonacci(int(input("q1 part a input (integer): ")))    

def majority_element(l):
    for i in l:
        if l.count(i)>len(l)/2:
            return i
    
    return -1
        
print(majority_element(eval(input('q1 part b input (list): '))))

    