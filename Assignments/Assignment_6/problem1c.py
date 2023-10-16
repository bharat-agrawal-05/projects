import numpy as np
import sys 

def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
    
c=open("Output1c.txt","w")

if len(sys.argv)==1:
    print("No filepaths given, Please provide filepaths as command line arguments")
    exit()

n=len(sys.argv)-1
for i in range(1,n+1):
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
            xsum=np.sum(x1)
            ysum=np.sum(y1)
            xysum=np.sum(np.multiply(x1,y1))
            
            rNum=(len(x1)*xysum)-(xsum*ysum)
            rDen=np.sqrt((len(x1)*np.sum(np.square(x1))-np.square(xsum))*(len(y1)*np.sum(np.square(y1))-np.square(ysum)))
            r=rNum/rDen
            c.write(str(r)+' ')

    except FileNotFoundError or FileExistsError:
        print("Invalid path")

c.close()