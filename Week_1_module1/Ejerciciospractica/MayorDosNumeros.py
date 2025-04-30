#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.

number1=float(input("Ingrese el primer número: "))

number2=float(input("Ingrese el segundo número: "))

if number1<number2:
    print(f"El número 2 ({number2}) es mayor al número 1 ({number1})")
    
elif number1>number2:
    print(f"El número 1 ({number1}) es mayor al número 2 ({number2})")
    
else:
    print(f"Los números son iguales")
    
    