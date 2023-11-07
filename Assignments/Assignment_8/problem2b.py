import sys,time


if len(sys.argv[1:])!= 1:
    print('please enter one file path as command line argument')
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
found=False
start=time.time()

for i in range(len(arr)):
    if arr[i] == word:
        print('word was found at index',i)
        found=True
        break
end=time.time()
if not(found):
    print('word was not in array')


print('time taken was',end-start)