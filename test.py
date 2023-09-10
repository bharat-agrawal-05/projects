def polynomial(degree):
    l=[]
    for i in range(degree+1):
        l.append([0,0])
    for j in range(degree+1):
        l[j][0]=j
        l[j][1]=int(input(f'Enter the coefficient of x^{j}: '))

    return l


def addi_(f1,f2):
    l=[]
    m=max(len(f1),len(f2))
    n=min(len(f1),len(f2))
    for i in range(m):
        l.append([0,0])
        
    for j in range(n):
        if f1[j][0]==f2[j][0]:
            l[j][0]=f1[j][0]
            l[j][1]=f1[j][1]+f2[j][1]
        
        else:
            if f1[j][0]>f2[j][0]:
                l[j][0]=f1[j][0]
                l[j][1]=f1[j][1]
            else:
                l[j][0]=f2[j][0]
                l[j][1]=f2[j][1]

    print(l)
        

f1=polynomial(int(input('degree for polynomial 1 ')))
f2=polynomial(int(input('degree for polynomial 2 ')))
addi_(f1,f2)




