
import sys,time

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


i=sys.argv[1:]
if len(i)!=1:
    print('please enter a single file path as command line argument')
    exit()

try:
    with open(sys.argv[1],'r') as f:
        lines=f.readlines()
        word=lines[0]
        array=lines[1]
        arr=[]
        for i in array.split():
            arr.append(int(i))
except:
    print('File not found')
    exit()
start=time.time()
a=binearsearch(int(word),arr)
end=time.time()

if a!='word was not in array':
    print(f"the word {word} was found at {a} index")
else:
    print(a)

print('time taken was',end-start)


