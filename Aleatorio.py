import csv
import random

Numale = random.random()
print("Su numero es: ",Numale)

fields = ['NUMERO']
  
rows = [[Numale]]
 

filename = "NumerosAleatorios.csv"
 

with open(filename, 'w') as csvfile:
   
    csvwriter = csv.writer(csvfile)
     
    
    csvwriter.writerow(fields)
     
    
    csvwriter.writerows(rows)
    
csvfile.close()
    

while True:
    Numale1 = random.random()
    
