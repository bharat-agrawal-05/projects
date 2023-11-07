import numpy as np
import subprocess as sb

arr=[]
for i in range(100000):
    arr.append(i)

with open('problem2aInput.txt','w') as f:
    word=arr[np.random.randint(1,len(arr)-1)]
    f.write(str(word)+'\n')
    for i in arr:
        f.write(str(i)+' ')

result=sb.run('python3 problem2a.py problem2aInput.txt',shell=True,stdout=sb.PIPE,text=True)
print(result.stdout)

result=sb.run('python3 problem2b.py problem2aInput.txt',shell=True,stdout=sb.PIPE,text=True)
print(result.stdout)




