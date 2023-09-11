#part-a
def sort_(l):
    l.sort()
    print("Sorted list: ",l )
    l.sort(reverse=True)         #sorting in reverse order 
    print('reverse sorted list: ', l)

sort_(eval(input("q2 part a input (list): ")))


#part-b
def replicate(l,x):
    return l*x     #replication x times
l=eval(input("q2 part b input (list): "))
x=int(input("q2 part b input (number): "))
print(replicate(l,x))

#part-c

def min_max(l):
    return f'minimum of list is {min(l)}, maximum of list is {max(l)}'      #using min and max functions

print(min_max(eval(input("q2 part c input (list): "))))

#part-d

def position(l):
    k=eval(input("q2 part d input (element): "))
    if k not in l:          #checks if element not present in list
        return "element not in list"
    posi=l.index(k)
    return f'element found at index {posi}'


print(position(eval(input("q2 part d input (list): "))))

#part-e
def sum(l):
    s=0
    for i in l:
        s+=i    #sum of elements
    return f'sum of list is {s}'

print(sum(eval(input("q2 part e input (list): "))))


