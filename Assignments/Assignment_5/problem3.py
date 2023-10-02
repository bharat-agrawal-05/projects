#part-a

def perfRevCapStr(s,n):

    if n==1:
        return s[0]
    
    else:
        news= s[n-1]+perfRevCapStr(s,n-1)

    return news.upper()


string=input("Enter a string: ")
revS=perfRevCapStr(string,len(string))
print(f'{revS} -> {string}')


# part-b

def scatSubStr(w,s):
    l=''
    if len(w)==0:
        return True
    
    try:
        if len(w)==1:
            if w==s[0]:
                l+=w
                return True
            
            elif len(s)>1 and w!=s[0]:
                s=s[1:]
                return scatSubStr(w,s)

            elif len(s)==1 and w!=s:
                return False
            
        if w[0] == s[0]:
            l+=w[0]
            w=w[1:]
            s=s[1:]
            return scatSubStr(w,s)
        else:
            s=s[1:]
            return scatSubStr(w,s)
    
    except IndexError:
        return False
        
    
w=input("Enter a word: ")
s=input("Enter a string: ")
if scatSubStr(w,s):
    print(f'{w} is a scattered substring of {s}')
else:
    print(f'{w} is not a scattered substring of {s}')
