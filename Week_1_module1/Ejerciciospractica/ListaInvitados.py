'''
    Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
    Pide al usuario su nombre.
    Usa if para decir si está en la lista de invitados o no.
'''

list_guests=["Ana", "Luis", "Sofía"]

name=str(input("Ingrese su nombre: "))

if name in list_guests:
    print("Estás en la lista de invitados.")
    
else:
    print("No estás en la lista de invitados.")