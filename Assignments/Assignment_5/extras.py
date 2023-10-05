######### code starts ###########
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
# Use pandas to read the CSV
csvData = pd.read_csv("Data.csv", sep=",")
# Convert dataframe into a numpy array
csvDataNum = csvData[["State","A","B","C","D","E","F","G","H","I","J","K"]].to_numpy() # Convert numpy array into a list (of lists)
data = csvDataNum.tolist()
# Access values as usual from data # For eg. data[0][3] is 25 print(data[0][3])


#part-1
women=[i[11] for i in data]
perCap=[i[9] for i in data]


plt.bar(women,perCap)
plt.xlim(0,50)
plt.ylim(0,300000)
plt.xlabel("percentage of woemen in the overall workforce",fontsize=20)
plt.ylabel("per capita income",fontsize=20)
plt.title("percentage of women in the overall workforce vs per capita income",fontsize=20)
plt.show()
            
#part-2

xValues=np.arange(50)
yValues=xValues**2
plt.plot(xValues,yValues,label='square function graph')
plt.xlabel('X-Values',fontsize=20)
plt.ylabel('Y-Values',fontsize=20)
plt.title('Graph for Square Function',fontsize=24)
plt.show()

xValues=np.arange(5)
yValues=[]
for i in xValues:
    yValues.append(math.exp(i))

plt.plot(xValues,yValues,label='exponential function graph')
plt.xlabel('X-Values',fontsize=20)
plt.ylabel('Y-Values',fontsize=20)
plt.title('Graph for Exponential Function',fontsize=24)
plt.show()


#part-3
def scatSubStr(w,s):
        if w == '' :
            return True
        if w[0] in s :
            return scatSubStr(w[1 :], s[s.find(w[0]) + 1:])
        else:
            return False
        

def count_occurance(w,s,count=0):
    
    if scatSubStr(w,s):
        count+=1
        a=''
        b=w
        for i in range(len(s)):
            if len(b)!=0 and b[0] == s[i]:
                b=b[1:]
                continue

            else:
                a+=s[i]
        
        return count_occurance(w,a,count)

    else:
        return count
    
w=input("Enter the word to be searched: ")
s=input("Enter the string: ")
print(f'Number of occurances of {w} in {s} is {count_occurance(w,s)}') 


