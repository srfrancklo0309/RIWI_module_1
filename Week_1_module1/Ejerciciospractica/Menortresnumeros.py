'''
    Pide tres números al usuario.
    Usa condicionales (if) para decir cuál es el más pequeño.
'''
number1=float(input("Ingrese el primer número: "))

number2=float(input("Ingrese el segundo número: "))

number3=float(input("Ingrese el tercer número: "))

if number1<number2 and number1<number3:
    print(f"El número más pequeño es: {number1}")
    
elif number2<number1 and number2<number3:
    print(f"El número más pequeño es: {number2}")
    
elif number3<number2 and number3<number1:
    print(f"El número más pequeño es: {number3}")
