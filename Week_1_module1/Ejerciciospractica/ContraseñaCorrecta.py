#Pide una contraseña al usuario. Si coincide con "python123", imprime "Acceso concedido", de lo contrario, "Contraseña incorrecta".

password=str(input("Ingrese la contraseña "))

if password == "python123":
    print("Acceso concedido.")
    
else:
    print("Contraseña incorrecta.")