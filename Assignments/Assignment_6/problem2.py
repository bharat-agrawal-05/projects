import sys

myDict=[]
temp={}
if len(sys.argv)==1:
    print("No filepaths given, Please provide filepaths as command line arguments")
    exit()

for i in range(1,len(sys.argv)):
    filepath=sys.argv[i]
    with open (filepath,'r') as f:
        lines=f.readlines()
        for line in lines:
            for word in line.split():
                if word in temp:
                    temp[word]+=1
                else:
                    temp[word]=1
                
for i in list(temp.keys()):
    myDict.append({'word':i,'frequency':temp[i]})

def freq(item):
    return item['frequency']

sorted_myDict=sorted(myDict,key=freq,reverse=True)

import csv
with open('problem2Output.csv', 'w') as csvop: 
    # creating dictionary writer object
    writerObj = csv.DictWriter(csvop, fieldnames = ['word', 'frequency']) 

	# write fieldnames
    writerObj.writeheader()
    writerObj.writerows(sorted_myDict)



