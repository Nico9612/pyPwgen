#!/usr/bin/python3
from random import randint as ri 

char = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!?&$"

numero_caratteri = 0
while(numero_caratteri > 78 or numero_caratteri < 8):
    numero_caratteri = int(input("Inserire il numero di caratteri della password devono essere compresi tra 8 e 78: "))


lenriga = 78
passperriga = 78//numero_caratteri
numrighe = 20

passListList = []
for n in range(numrighe):
    passList = []
    for j in range(0,passperriga):
        pw = []
        for i in range(0,numero_caratteri):
            c = char[ri(0,(len(char)-1))]
            pw.append(c)
        pw = "".join(pw)
        passList.append(pw)
        
    passListList.append(passList)



for n in range(numrighe):
    for m in range(passperriga):
        print(passListList[n][m],end = " ")
    print()
