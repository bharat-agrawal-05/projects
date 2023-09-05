#part a

def rev(q4part_a):
    b=''
    for i in range(-1,-len(q4part_a)-1,-1):
        b+=q4part_a[i]
        
    return b

print(rev(input('q4 part a input (string):')))

#part b

N=int(input('q4 part b input (integer):'))
oddSum=0
evenSum=0
for i in range (1,N,2):
    oddSum+=i

for i in range(0,N,2):
    evenSum+=i

print(oddSum+evenSum)

#part c

def factorial(N):
    fact=1
    i=1
    while i<=N:
        fact*=i
        i+=1
        
    return fact

print(factorial(int(input('q4 part c input (integer):'))))


    