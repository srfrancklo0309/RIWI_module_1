#Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto.

number= 8

guessnumber=int(input("Ingrese el número que cree que es: "))

if guessnumber== 8:
    print(f"Felicidades, adivinó el número ({number})")
    
elif guessnumber <8:
    print(f"El número ({guessnumber}) que ingresaste, es menor al número a adivinar.")
    
else:
   print(f"El número ({guessnumber}) que ingresaste, es mayor al número a adivinar.") 