import csv
with open('texts.csv','r') as f:
    data=csv.reader(f)
    text=list(data)
print("First record of texts,",text[0][0],"texts",text[0][1],"at time",text[0][2])

with open('calls.csv','r') as f:
    data=csv.reader(f)
    text=list(data)
print("Last record of calls,",text[len(text)-1][0],"calls",text[len(text)-1][1],"at time",text[len(text)-1][2],"lasting",text[len(text)-1][3],"seconds")
