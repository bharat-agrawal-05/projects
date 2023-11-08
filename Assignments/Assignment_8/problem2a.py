
import sys,time

def binearsearch(x,l):
    end=len(l)-1
    start=0
    while start<=end:
        mid=(end+start)//2 
        if x == l[mid]: 
            return mid   
        if x<l[mid]:
            end=mid-1
        if x>l[mid]:
            start=mid+1
    
    return 'word was not in array'

i=sys.argv[1:]
if len(i)!=1:
    print('please enter a single file path as command line argument')
    exit()

try:
    with open(sys.argv[1],'r') as f:
        lines=f.readlines()
        word=int(lines[0])
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


