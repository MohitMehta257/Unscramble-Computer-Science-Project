
import csv
with open('calls.csv','r') as f:
    data=csv.reader(f)
    text=list(data)
calls=[]
for i in range(len(text)):
    calls.append(text[i][0])
calls1=[] 
for i in range(len(text)):
    calls1.append(text[i][1])
bang=[]

for each in calls:
    if each.count("080")==1:
        bang.append(each)

rece=[]
for each in bang:
    rece.append(calls1[calls.index(each)])

bangalore=[]
for each in rece:
    if each[0]=="(":
        index=each.index(")")
        bangalore.append(each[0:index+1])
    if each[0]=="140":
        bangalore.append(each[0:3])
    else:
        bangalore.append(each[0:4])
        

bangalore2=[]
for each in bangalore:
    if bangalore2.count(each)==0:
        bangalore2.append(each)
        



numerator=0
for i in range(len(text)):
    if(calls[i].count("080")==1 and calls1[i].count("080")==1):
        numerator+=1

denum=0

for each in calls:
    if(each.count("080")==1):
        denum+=1
 
per=(numerator/denum)*100
   
print("The numbers called by people in Bangalore have codes:",sorted(bangalore2))
print("{:.2f}".format(per),"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")       
        
        
