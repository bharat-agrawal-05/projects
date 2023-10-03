######### code starts ###########
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
plt.xlabel("percentage of woemen in the overall workforce")
plt.ylabel("per capita income")
plt.title("percentage of women in the overall workforce vs per capita income")
plt.show()
            
#part-2

xValues=np.arange(50)
yValues=xValues**2
plt.plot(xValues,yValues,label='square function graph')
plt.xlabel('X-Values',fonsize=16)
plt.ylabel('Y-Values',fonsize=16)
plt.title('Graph for Square Function',fonsize=16)
plt.show()


