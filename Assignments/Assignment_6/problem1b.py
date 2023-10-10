import numpy as np
import matplotlib.pyplot as plt
import sys 

#part-b

def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

for i in range(1,4):
    try:
        filepath=sys.argv[i]
        with open(filepath,'r') as f:
            l=f.readlines()
            x=l[0].split()
            y=l[1].split()
            x1=[]
            y1=[]
            for i in range(1,len(x)):
                if is_int(x[i]):
                    x1.append(int(x[i]))
                else:
                    continue
            for i in range(1,len(y)):
                if is_int(y[i]):
                    y1.append(int(y[i]))
                else:
                    continue

            plt.scatter(x1,y1)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.show()


    except FileNotFoundError or IndexError:
        print("File not found")
