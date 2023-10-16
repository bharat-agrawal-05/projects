import matplotlib.pyplot as plt
import sys 

#part-b

def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
    
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
                
            for i in range(1,len(y)):
                if is_int(y[i]):
                    y1.append(int(y[i]))
                
            plt.scatter(x1,y1)
            plt.xlabel("X-Values",fontsize=18)
            plt.ylabel("Y-Values",fontsize=18)
            plt.title(f'Graph for {filepath}',fontsize=18)
            plt.savefig(f'{filepath}.png')
            plt.show()


    except FileNotFoundError or Exception:
        print(f"File with Filepath - '{filepath}' , not found")
