
myDict=[]
temp={}
with open ('problem2Input','r') as f:
    lines=f.readlines()
    for line in lines:
        for word in line.split():
            if word in temp:
                temp[word]+=1
            else:
                temp[word]=1
                
for i in list(temp.keys()):
    myDict.append({'word':i,'frequency':temp[i]})

sorted_myDict=sorted(myDict,key=lambda x:x['frequency'],reverse=True)

import csv
with open('problem2Output.csv', 'w') as csvop: 
    # creating dictionary writer object
    writerObj = csv.DictWriter(csvop, fieldnames = ['word', 'frequency']) 

	# write fieldnames
    writerObj.writeheader()
    writerObj.writerows(sorted_myDict)



