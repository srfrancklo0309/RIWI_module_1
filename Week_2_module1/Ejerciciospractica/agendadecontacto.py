#Vas a construir una agenda que guarda información de contactos personales.

def create():
    while True:
        name=input("Ingrese el nombre del contacto: \n")

        if name in contacts :
            print("Este contacto ya existe.")
            continue

        number=input("Ingrese el número de su contacto: \n")

        email=input("Ingrese el email de su contacto: \n")

        contacts[name]={'Number':number, 'Email':email}

        decision=int(input("¿Desea ingresar otro contacto? \n1.Si\n0.No\n"))

        if decision == 1:
            continue
        else:
            break

def update():
    while True:
        name=input("Ingrese el nombre del contacto que desea actualizar: \n")
        if not name in contacts:
            print("Este contacto no existe.")
            continue
        else:
            number=input("Ingrese el nuevo número del contacto: \n")

            email=input("Ingrese el nuevo email del contacto: \n")

            new_name=input("Ingrese el nombre nuevo del contacto: \n")
            
            del contacts[name]

            contacts[new_name]={'Number':number, 'Email':email}
            break


def delete():
    delete=input("Ingrese el nombre del contacto que desea eliminar: \n")
    if not delete in contacts:
        print("Contacto no existe.")
    del contacts[delete]

def search_byone():
    name=input("Ingrese el nombre del contacto: \n")
    for name ,contact in contacts.items():
        if not name in contacts:
            print("El contacto no existe.")
        else:
            print(f"El nombre del contacto es: {name}, el número es: {contact['Number']} y el email es: {contact['Email']}")
            break
contacts={}

while True:
    opt=int(input("¿Qué desea hacer?\n1.Agregar un nuevo contacto.\n2.Ver todos los contactos.\n3.Actualizar un contacto.\n4.Eliminar un contacto.\n5.Ver contacto en específico\n6.Salir\n"))

    match opt:
        case 1:
            create()
        case 2:

            for name ,contact in contacts.items():
                print(f"El nombre del contacto es: {name}, el número es: {contact['Number']} y el email es: {contact['Email']}")

        case 3:
            update()


        case 4:
            delete()

        case 5:
            search_byone()
        
        case 6:
            print("Tenga un buen día.")
            break
        
        case _:
            print("Opción no válida.")
            continue