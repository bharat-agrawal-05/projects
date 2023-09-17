######### code starts ###########
import pandas as pd
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
