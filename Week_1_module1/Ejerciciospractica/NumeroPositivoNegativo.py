#Pide un número al usuario. Di si es positivo, negativo o si es cero.

number=int(input())

if number<0:    
    print("El número ingresado es negativo.")
    
elif number>0:
    print("El número es positivo.")
    
else:
    print("El número es cero.")