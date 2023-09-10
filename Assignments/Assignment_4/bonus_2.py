def sorting(l):
    length=len(l)
    for i in range(length):
        for j in range(i+1,length):
            if l[i]>l[j]:                  
                l[i],l[j]=l[j],l[i]         #this line is used to swap the values

    return l       

l=eval(input("Enter the list: "))
print(sorting(l))