import sys

myDict=[]
temp={}         #temporary dictionary to store the words and their frequencies
if len(sys.argv)==1:
    print("No filepaths given, Please provide filepaths as command line arguments")
    exit()
    
try:
    #the following is the code for reading the filepaths from command line arguments and storing the words and their frequencies in a dictionary
    filepath=sys.argv[1]
    with open (filepath,'r') as f:
        lines=f.readlines()
        for line in lines:
            for word in line.split():
                word = word.lower()
                if word in temp:
                    temp[word]+=1
                else:
                    temp[word]=1

except FileNotFoundError or Exception:
    print("Invalid path")
    exit()
                    
for i in list(temp.keys()):
    myDict.append({'word':i,'frequency':temp[i]})       #storing the words and their frequencies in a list of dictionaries


sorted_myDict=sorted(myDict,key=lambda x:x['frequency'],reverse=True)      #the Key is the function that is applied to each element of the iterable (list) and the return value of the function is used for sorting.

import csv
with open('problem2Output.csv', 'w') as csvop: 
    # creating dictionary writer object
    writerObj = csv.DictWriter(csvop, fieldnames = ['word', 'frequency']) 

	# write fieldnames
    writerObj.writeheader()
    writerObj.writerows(sorted_myDict)



