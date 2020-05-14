import operator
import csv
with open('calls.csv','r') as f:
    data=csv.reader(f)
    text=list(data)
ph=[]
call=[]
receive=[]
dur=[]
for i in range(len(text)):
    call.append(text[i][0])
    
for i in range(len(text)):
    receive.append(text[i][1])
    
for i in range(len(call)):
    for j in range(len(receive)):
        if(call[i]==receive[j]):
            ph.append(call[i])
            
for i in range(len(text)):
    dur.append(text[i][3])
for i in range(len(dur)):
    dur[i]=int(dur[i])

            
d={}
for each in ph:
    i1=call.index(each)
    i2=receive.index(each)
    t=dur[i1]+dur[i2]
    
    d[each]=t
d = sorted(d.items(), key=operator.itemgetter(1))
t=list(d[len(d)-1])
print(t[0],"spent the longest time",t[1],"seconds, on the phone during September 2016.")
