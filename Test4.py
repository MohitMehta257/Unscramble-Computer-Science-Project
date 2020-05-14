

import csv
with open('calls.csv','r') as f:
    data=csv.reader(f)
    text=list(data)
    
    
outcall=[]
for i in range(len(text)):
    outcall.append(text[i][0])
    
receivecall=[]
for i in range(len(text)):
    receivecall.append(text[i][1])


with open('texts.csv','r') as f:
    data=csv.reader(f)
    text=list(data)
    
sendtext=[]
for i in range(len(text)):
    sendtext.append(text[i][0])
    
receivetext=[]
for i in range(len(text)):
    receivetext.append(text[i][1])


l1=[]
for i in range(len(outcall)):
    count=0
    for j in range(len(sendtext)):
        if(outcall[i]==sendtext[j]):
            count+=1
    if(count==0):
        l1.append(outcall[i])
        

        
l2=[]
for i in range(len(l1)):
    count=0
    for j in range(len(sendtext)):
        if(l1[i]==receivetext[j]):
            count+=1
    if(count==0):
        l2.append(l1[i])


l3=[]
for i in range(len(l2)):
    count=0
    for j in range(len(receivecall)):
        if(l2[i]==receivecall[j]):
            count+=1
    if(count==0):
        l3.append(l2[i])

l4=[]
for each in l3:
    if(l4.count(each)==0):
        l4.append(each)
l4=sorted(l4)
print("These numbers could be telemarketers: ")
for each in l4:
    print(each)
       

    
