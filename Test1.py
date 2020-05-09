import csv
l=[]
with open('texts.csv','r') as f:
    data=csv.reader(f)
    text=list(data)
for i in range(len(text)):
    l.append(text[i][0])
for i in range(len(text)):
    l.append(text[i][1])
    
with open('calls.csv','r') as f:
    data=csv.reader(f)
    text=list(data)
for i in range(len(text)):
    l.append(text[i][0])
for i in range(len(text)):
    l.append(text[i][1])
g=[]
for i in range(len(l)):
    if(g.count(l[i])==0):
        g.append(l[i])
        
print("There are", len(g), "different telephone numbers in the records.")
