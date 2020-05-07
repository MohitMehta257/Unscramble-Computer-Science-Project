
import csv
with open('calls.csv','r') as f:
    data=csv.reader(f)
    text=list(data)
l=[]
for i in range(len(text)):
    l.append(text[i][1])

ban=[]
for i in range(len(l)):
    if(l[i].count("(080)")==1):
        ban.append(l[i])

index=[]
for i in range(len(ban)):
    index.append(l.index(ban[i]))

call=[]
for each in index:
    call.append(text[each][0])

code=[]
for each in call:
    if(each[0]=='('):
        t=each.index(')')
        code.append(each[1:t])
    if(each.count("140")==1):
        code.append(each[0:3])
    else:
        code.append(each[0:4])
code1=[]
     
for each in code:
    if(each[0]=='('):
        code1.append(each[1:])
    else:
        code1.append(each)
 

code2=[]
for each in code1:
    if(code2.count(each)==0):
        code2.append(each)

print("The numbers called by people in Bangalore have codes:",sorted(code2))
n=len(sorted(code2))

bang=code2.count("080")

per=(bang/n)*100
print("{:.2f}".format(per),"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

 
