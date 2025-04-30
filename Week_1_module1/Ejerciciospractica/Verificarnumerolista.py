'''
    Crea una lista con 5 números.
    Pide un número al usuario y verifica si está en la lista usando in.
'''

list=[1.0, 2.0, 3.0, 4.0, 5.0]

number=float(input("Ingrese un número: "))

if number in list:
    print("El número está dentro de la lista")
    
else:
    print("El número no está dentro de la lista")