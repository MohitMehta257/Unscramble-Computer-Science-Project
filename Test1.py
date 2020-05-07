
import csv
with open('texts.csv','r') as f:
    data=csv.reader(f)
    text=list(data)
l=[]
for i in range(len(text)):
    l.append(text[i][0])

t=0
for each in l:
    count=0
    for num in l:
        if(num==each):
            count+=1
    if(count>1):
        t+=1

m=[]
for i in range(len(text)):
    m.append(text[i][1])

s=0
for each in l:
    count=0
    for num in l:
        if(num==each):
            count+=1
    if(count>1):
        s+=1
                
with open('calls.csv','r') as f:
    data=csv.reader(f)
    text=list(data)

n=[]
for i in range(len(text)):
    n.append(text[i][0])

u=0
for each in n:
    m=0
    for num in n:
        if(num==each):
            m+=1
    if(m>1):
        u+=1

m=[]
for i in range(len(text)):
    m.append(text[i][1])
k=0
for each in m:
    p=0
    for num in m:
        if(num==each):
            p+=1
    if(p>1):
        k+=1
print("There are",u+t+k+s,"different telephone numbers in the records.")
