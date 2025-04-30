#Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).

year=int(input("Ingrese un año: "))

if year % 4 == 0 or year % 400 ==0 :
    print("El año es bisiesto")
else:
    print("El año es bisiesto")