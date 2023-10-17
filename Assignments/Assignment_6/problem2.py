import sys

myDict=[]
temp={}         #temporary dictionary to store the words and their frequencies
if len(sys.argv)==1:
    print("No filepaths given, Please provide filepaths as command line arguments")
    exit()

#the following is the code for reading the filepaths from command line arguments and storing the words and their frequencies in a dictionary
for i in range(1,len(sys.argv)):
    filepath=sys.argv[i]
    with open (filepath,'r') as f:
        lines=f.readlines()
        for line in lines:
            for word in line.split():
                word = word.lower()
                if word in temp:
                    temp[word]+=1
                else:
                    temp[word]=1
                
for i in list(temp.keys()):
    myDict.append({'word':i,'frequency':temp[i]})       #storing the words and their frequencies in a list of dictionaries

def freq(item):
    return item['frequency']

sorted_myDict=sorted(myDict,key=freq,reverse=True)      #the Key is the function that is applied to each element of the iterable (list) and the return value of the function is used for sorting.

import csv
with open('problem2Output.csv', 'w') as csvop: 
    # creating dictionary writer object
    writerObj = csv.DictWriter(csvop, fieldnames = ['word', 'frequency']) 

	# write fieldnames
    writerObj.writeheader()
    writerObj.writerows(sorted_myDict)



