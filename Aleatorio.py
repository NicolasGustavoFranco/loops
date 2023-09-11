import random,time,csv


while True:
 Numale = random.randint(1, 300)
 print("Su numero es: ",Numale)
 time.sleep(2)



import csv
import random

path="/home/eocampo/Escritorio/porque_pregunta_6.csv"
file=open(path,newline='')
reader=csv.reader(file)
data=[row for row in reader]
reader = csv.reader(data[0], delimiter=',')

randomList=[]
for row in reader:
    randomList.append(row)

newVar=random.choice(randomList)
print(newVar)
