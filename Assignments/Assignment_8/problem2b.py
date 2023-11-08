import sys,time

if len(sys.argv[1:])!= 1:
    print('please enter one file path as command line argument')
    exit()

try:
    with open(sys.argv[1],'r') as f:
        lines=f.readlines()
        word=int(lines[0])
        array=lines[1]
        arr=[int(i) for i in array.split()]
        
except:
    print('File not found')
    exit()
found=False
start=time.time()

for i in range(len(arr)):
    if arr[i] == word:
        print(f'word {word} was found at index {i}')
        found=True
        break
end=time.time()
if not(found):
    print(f'word was not in array')

print('time taken was',end-start)