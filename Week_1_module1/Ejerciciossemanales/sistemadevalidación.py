#Funciones para validar las decisiones y el ingreso de datos
def validate_price(p_price):
    while(True):#Ciclo while para que el usuario si o si tenga que ingresar un dato correctamente
        try:
            v_price=float(input(p_price))#Creacion de nueva variable para así evaluar si es un tipo de dato diferente al solicitado
            if v_price>0:
                return v_price#En caso de que el dato sea correcto lo de vuelva al programa y pueda ser usado para una operación o almacenado en los diccionarios, esta misma estructura se usa en todos
            else:
                print("Este número es negativo")
        except ValueError:
            print("Ingrese un número válido")

def validate_unit(p_units):
    while(True):
        try:
            v_unit=int(input(p_units))
            if v_unit>0:
                return v_unit
            else:
                print("Este número es negativo")
        except ValueError:
            print("Ingrese un número válido")

def desicion_discount(p_discount):
    while(True):
        try:
            opt_discount=int(input(p_discount))
            if p_discount!= 0 or p_discount!= 1:
                return opt_discount
            else:
                print("Esta opción no es válida")
        except ValueError:
            print("Ingrese una opción válida")

def validate_discount(value_discount):
    while(True):
        try:
            v_discount=float(input(value_discount))
            if v_discount>0 and v_discount<100:
                return v_discount
            else:
                print("Este porcentaje no cumple con las condiciones")
        except ValueError:
            print("Ingrese un porcentaje válido")

def validate_numberproducts(p_numbers):
    while(True):
        try:
            numberproduct=int(input(p_numbers))
            if numberproduct>=0:
                return numberproduct
            else:
                print("Este número es negativo o es 0.")
        except ValueError:
            print("Ingrese un número válido")

#Espacios para estética mejor

print()
print()

#Mensaje de bienvenida

print("**Bienvenido al sistema de validación**\n")

print("-------------------------------------------------")

print("")

p_numbers=validate_numberproducts("Ingrese el número de productos a los cuales desea realizar el procesos\n ") #Ingreso de número de productos


print("-------------------------------------------------")

lis_discount=[]#Lista de productos con descuento
lis_outdiscount=[]#Lista de productos sin descuento

for i in range(0,p_numbers, 1 ):#Ciclo for para pedir datos el número de veces de los productos
    #Pedida de información de los productos
    print("Ahora deberá ingresar la información del siguiente producto\n")
    p_name=input("Ingrese el nombre del producto\n")
    print("-------------------------------------------------")

    p_price=validate_price("Ingrese el precio del producto\n ")
    
    print("-------------------------------------------------")
    
    p_units=validate_unit("Ingrese la cantidad de unidades del producto\n")
    

    p_discount=desicion_discount("El producto tiene descuento? \n0.Si \n1.No \n ")
    if p_discount==0:#Condicional para aplicar operación de descuento al producto
        value_discount=validate_discount("Ingrese el valor del descuento\n ")
        

        value_discount=value_discount/100

        total_bill = p_price * p_units

        total_billwdiscount= total_bill-(total_bill*value_discount)

        value_discount=value_discount*100

        product={#Diccionario para almacenar la información del producto
            "name": p_name,
            "price": p_price,
            "units": p_units,
            "total_bill": total_bill,
            "value_discount": value_discount,
            "billdiscount": total_billwdiscount
        }
    
        lis_discount.append(product)
    
    else:#Incumplimiento de condición se cambian la información del producto


        product={
            "name": p_name,
            "price": p_price,
            "units": p_units,
            "total_bill": p_price * p_units,
            "discount": p_discount
            
                }
        
        product["product_discount"]=0
        lis_outdiscount.append(product)
    



print("A continuación se le mostrarán los productos con descuento:")

for product in lis_discount:#Ciclo for para recorrer la lista de los productos con descuento
    
    print("-------------------------------------------------")

    print(f"{product["name"]} y vale ${product["price"]:.2f}\nEste producto tiene un descuento de {product["value_discount"]}%\nEl precio de su producto con descuento: ${product["billdiscount"]:.2f}.")#Mensaje que se le da al usuario de la información que necesita

    print("-------------------------------------------------")

print("Ahora se le mostrará los productos sin descuento:")

for productod in lis_outdiscount:#Ciclo for para recorrer la lista de productos que no tienen descuento

    print("-------------------------------------------------")

    print(f"{productod["name"]} y el costo total es de: ${productod["total_bill"]:.2f}.")#Mensaje que se le da al usuario de la información que necesita

    print("-------------------------------------------------")