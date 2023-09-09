#part-a
def sort_(l):
    l.sort()
    print("Sorted list: ",l )
    l.sort(reverse=True)
    print('reverse sorted list: ', l)

sort_(eval(input("q2 part a input (list): ")))


#part-b
def replicate(l):
    return l*3

print(replicate(eval(input("q2 part b input (list): "))))

#part-c

def min_max(l):
    return min(l),max(l)

print(min_max(eval(input("q2 part c input (list): "))))

#part-d

def position(l):
    k=eval(input("q2 part d input (element): "))
    if k not in l:
        return "element not in list"
    posi=l.index(k)
    return posi


print(position(eval(input("q2 part d input (list): "))))

#part-e
def sum(l):
    s=0
    for i in l:
        s+=i
    return s

print(sum(eval(input("q2 part e input (list): "))))


