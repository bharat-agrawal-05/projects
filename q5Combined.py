#part-a

def prime(N):
    if N==1:
        return False
    
    for i in range(2,N):
        if N%i==0:
            return False
    return True
    
print(prime(int(input('q5 part a input (natural number):'))))

#part-b

q5part_b=input('q5 part b input (string):')
vowel=0
consonant=0
for char in q5part_b:
    if char in 'aeiou':
        vowel+=1
    else:
        consonant+=1
    
if vowel>consonant:
    print('String is vowel-dominated')

elif vowel<consonant:
    print('String is consonant-dominated')

else:
    print('String has equal number of vowels and consonants')

#part-c

def digits(string):
    digits=0
    for char in string:
        if char.isdigit():
            digits+=1
        else:
            continue
    return digits



print(digits(input('q5 part c input (string):')))

#part-d

def alphabets(n):
    letters=0
    for char in n:
        if char.isalpha():
            letters+=1
        else:
            continue
    return letters

print(alphabets(input('q5 part d input (string):')))

#part-e

def divisor(n):
    divisors=[]
    for i in range(1,n+1):
        if n%i==0:
            divisors.append(i)
        else:
            continue
    return divisors

print(divisor(int(input('q5 part e input (intf):'))))

