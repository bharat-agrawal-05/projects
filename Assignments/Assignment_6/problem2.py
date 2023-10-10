import csv

myDict=[]
with open('problem2input','r') as f:
    d=f.read()
    l=d.split()

    s=set(l)
    for i in s:
        myDict.append({'word':i,'frequency':l.count(i)})

    myDict.sort(key=lambda x:x['frequency'],reverse=True)


with open('problem2Output.csv', 'w') as csvop: 
    # creating dictionary writer object
    writerObj = csv.DictWriter(csvop, fieldnames = ['word', 'frequency']) 
	# write fieldnames
    writerObj.writeheader()
    writerObj.writerows(myDict)
