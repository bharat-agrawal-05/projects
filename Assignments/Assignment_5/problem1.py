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
population_density=[]
for i in data:
    population_density.append(i[6])

print(population_density)

#part-a

def median(population_density):
    n = len(population_density)
    population_density.sort()
    if n % 2 == 0:
        median1 = population_density[int((n+1)/2)]
        median2 = population_density[int((n-1)/2)]
        median = (median1 + median2)/2
    else:
        median = population_density[n//2]
    return median

def average(population_density):
    return sum(population_density)/len(population_density)

def mode(population_density):
    j=0
    mode=0
    for i in population_density:
        if population_density.count(i)>j:
            j=population_density.count(i)
            mode=i

    return mode

highest=max(population_density)
highest_state=population_density.index(highest)
print("Highest population density is",highest,"in",data[highest_state][0])

lowest=min(population_density)
lowest_state=population_density.index(lowest)
print("Lowest population density is",lowest,"in",data[lowest_state][0])

print("Median population density is",median(population_density))
print("Average population density is",average(population_density))

print("Mode of population density is",mode(population_density))

#part-b

xvalues=[]
yvalues=[]
for i in data:              #loop for adding values to the following lists
    xvalues.append(i[0])
    yvalues.append(i[4])

x_axis=np.arange(len(xvalues))

plt.bar(x_axis-0.2,yvalues,width=0.4,label='Average Percentage area with > 30% slope')

xvalues=[]
yvalues=[]
for i in data:                  #loop for adding values to the following lists
    xvalues.append(i[0])
    yvalues.append(i[5]*100)

plt.bar(x_axis+0.2,yvalues,width=0.4,label='road density*100')      #multiplying the road density by 100 for better visibility 
plt.xticks(x_axis,xvalues,rotation='vertical')            #rotating the x-axis labels by 90 degrees and setting the x-axis labels
plt.legend()
plt.show()

#part-c

perArea30=[]
roadDen=[]
states=[]
for i in data:
    perArea30.append(i[4])      #loop for adding values to the following lists

perArea30.sort()
for i in perArea30:
    for j in data:
        if i in j:
            roadDen.append(j[5])
            states.append(j[0])

xValues=np.arange(len(roadDen))
plt.bar(xValues,roadDen,width=0.4,label='road density')
plt.xticks(xValues,states,rotation='vertical')              #rotating the x-axis labels by 90 degrees and setting the x-axis labels
plt.xlabel('States',fontsize=24)
plt.ylabel('road density',fontsize=24)
plt.title('Road density in increasing order of percentage area with slope > 30%',fontsize=24)
plt.legend()
plt.show()


