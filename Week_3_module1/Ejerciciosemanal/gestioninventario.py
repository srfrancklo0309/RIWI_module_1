products={}

def menu():
    while True:
        try:
            options=input("\nBIENVENIDO AL SISTEMA DE GESTIÓN DE INVENTARIO\n¿Qué operación desea realizar?\n1.Añadir productos\n2.Consultar productos\n3.Actualizar precios\n4.Eliminar productos\n5.Calcular el valor total del inventario\n6.Salir\n")
            options=int(options)

            match options:
                case 1:
                    add()
                    continue
                case 2:
                    search()
                    continue
                case 3:
                    update()
                    continue
                case 4:
                    delete()
                case 5:
                    total_value()
                case 6:
                    show_all()
                    break
                case _:
                    print("Opción no válida.")
        except ValueError:
            print("Opción no válida")

def add():
    print('------------------------------------')
    while True:
        name=input("Ingrese el nombre del producto:\n")
        if name in products:
            print("Este producto ya está en el sistema de inventario")
            break
        try:

            price=input("Ingrese el precio del producto:\n")

            price=float(price)

            units=input("Ingrese las unidades del producto:\n")

            units=int(units)

            products[name]=(price,units)
            break

        except ValueError:
            print("Valor no válido")

def search():
    if len(products) == 0:
        print("No hay productos dentro de la lista")
        return
    print('------------------------------------')
    name= input("Ingrese el nombre del producto del cual desea consultar:\n")

    if not name in products:
        print("El producto ingresado no se encuentra en el inventario")
        return
    price, units = products[name]
    print(f"Nombre del producto: {name}\nInformación del producto:\n{units} unidades.\n{price:,.2f}$")

def update():
    if len(products) == 0:
        print("No hay productos dentro de la lista")
        return
    print('------------------------------------')
    while True:
        name=input("Ingrese el nombre del producto que desea actualizar:\n")
        if not name in products:
            print("El producto ingresado no se encuentra en el inventario.")
            break
            
        price=input("Ingrese el nuevo precio del producto:\n")
        try:
            _, amount = products[name]
            price=float(price)
            products[name]=(price,amount)
            show_all()
            break

        except ValueError:
            print("Valor Ingresado no válido.")

def delete():
    if len(products) == 0:
        print("No hay productos dentro de la lista")
        return
    print('------------------------------------')
    name=input("Ingrese el nombre del producto que desea eliminar:\n")
    if not name in products:
        print("El producto ingresado no se encuentra en el inventario.")
        return
    products.pop(name)
    show_all()

def total_value():
    if len(products) == 0:
        print("No hay productos dentro de la lista")
        return
    total=0
    mult=lambda a,p: a*p
    for name,(amount, price) in products.items():
        value= mult(amount, price)
        total+=value
        print(f"{name}: {value:,.2f}$ ")
    print (f"El valor total de todos los productos es de: {total:,.2f}$")

def show_all():
    print("\nProductos existentes en el inventario:\n")
    for name,info in products.items():
        price, units = info
        print(f"Nombre del producto: {name}\nInformación del producto:\n{units} unidades.\n{price:,.2f}$")

menu()