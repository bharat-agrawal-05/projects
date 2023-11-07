def binearsearch(x,l):
    mid=(len(l)-1)//2
    end=len(l)
    start=0
    found=False
    while x!=l[mid]:
        mid=(end+start)//2 
        if x == l[mid]:
            found=True
            break
        if x<l[mid]:
            end=mid
        
        if x>l[mid]:
            start=mid
        if mid==end or mid==start:
            break
    if not(found):
        return 'word was not in array'
    return mid