import sys

myDict=[]
temp={}         #temporary dictionary to store the words and their frequencies
if len(sys.argv)==1:            #checks if the filepath is given as command line argument or not
    print("No filepaths given, Please provide filepath as command line argument")
    exit()
    
try:
    #the following is the code for reading the filepaths from command line arguments and storing the words and their frequencies in a dictionary
    filepath=sys.argv[1]
    with open (filepath,'r') as f:
        lines=f.readlines()

        if len(lines)==0:           #checks if the file is empty
            print('File is empty, Please provide a file with text ')
            exit()

        for line in lines:
            for word in line.split():
                if word in temp:
                    temp[word]+=1           #this a counter for words that are repeated
                else:
                    temp[word]=1

except FileNotFoundError or Exception:
    print("Invalid path")                   #checks if the filepath is valid or not
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



