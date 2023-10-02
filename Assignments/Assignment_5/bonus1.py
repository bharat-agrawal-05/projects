import numpy as np
import matplotlib.pyplot as plt

######### code starts ###########
import pandas as pd
# Use pandas to read the CSV
csvData = pd.read_csv("Data.csv", sep=",")
# Convert dataframe into a numpy array
csvDataNum = csvData[["State","A","B","C","D","E","F","G","H","I","J","K"]].to_numpy() # Convert numpy array into a list (of lists)
data = csvDataNum.tolist()
# Access values as usual from data # For eg. data[0][3] is 25 print(data[0][3])

perFarmer = [i[2] for i in data]    # percentage of farmers taking loan
perFarmer=np.array(perFarmer)
perCapital = [i[9] for i in data]   # per capita income
perCapital=np.array(perCapital)

meanFarmer=np.mean(perFarmer)
meanCapital=np.mean(perCapital)

rNum = np.sum((perFarmer-meanFarmer)*perCapital-meanCapital)
rDen = np.sqrt(np.sum((perFarmer-meanFarmer)**2)*np.sum((perCapital-meanCapital)**2))
r=rNum/rDen


