import numpy as np
import subprocess as sb

result=sb.run('python3 problem2a.py problem2aInput.txt',shell=True,stdout=sb.PIPE,text=True)
print('using binary search: ')
print(result.stdout)

result=sb.run('python3 problem2b.py problem2aInput.txt',shell=True,stdout=sb.PIPE,text=True)
print('using linear search: ')
print(result.stdout)




