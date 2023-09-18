#part-b

def scatSubStr(w,s):
    l=''
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
        
    
print(scatSubStr("cadbebb","cadbebb"))

