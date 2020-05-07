
import csv
with open('calls.csv','r') as f:
    data=csv.reader(f)
    text=list(data)

l=[]
for i in range(len(text)):
    l.append(text[i][3])
for i in range(len(l)):
    l[i]=int(l[i])

dur=sorted(l)
t=dur[len(l)-1]
print(text[l.index(t)][0],"spent the longest time",text[l.index(t)][3],"seconds, on the phone during September 2016.")

