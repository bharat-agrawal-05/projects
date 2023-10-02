
#part-a

def perfRevCapStr(s,n):

    if n==1:
        return s[0]
    
    else:
        return f'{(s[n-1]+perfRevCapStr(s,n-1)).upper()}'


string=input("Enter a string: ")
revS=print(f'{perfRevCapStr(string,len(string))} -> {string}')



# part-b

def scatSubStr(w,s):
    if w == '' :
        return True
    if w[0] in s :
        return scatSubStr(w[1 :], s[s.find(w[0]) + 1:])
    else:
        return False

w=input("Enter a word: ")
s=input("Enter a string: ")
if scatSubStr(w,s):
    print(f'{w} is a scattered substring of {s}')
else:
    print(f'{w} is not a scattered substring of {s}')
