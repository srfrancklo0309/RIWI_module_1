list_passangersN={}
list_passangersI={}
j=0
FLAG=True
while FLAG:
    passanger=input("Ingrese un nombre:\n")
    list_passangersI[passanger]={'total_bill':230000 }
    j+=1
    if j==5:
        break

SFLAG=True
i=0
while SFLAG:
    passanger=input("Ingrese un nombre:\n")
    list_passangersN[passanger]={'total_bill':230000 }
    i+=1
    if i==5:
        break

numberpI=len(list_passangersI)
numberpN=len(list_passangersN)
totalpassanger=numberpI+numberpN

totalsellsN=0
totalsellsI=0

for passanger, national in list_passangersN.items():
    totalsellsN=sum (national['total_bill'])

for passanger, international in list_passangersI.items():
    totalsellsI=sum (international['total_bill'])

totalsells=totalsellsI+totalsellsN

print(totalsells)