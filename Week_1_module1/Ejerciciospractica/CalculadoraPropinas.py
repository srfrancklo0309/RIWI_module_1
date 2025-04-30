#Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.

bill=float(input("Ingrese el total de la cuenta: "))

tip=float(input("Ingrese el porcentaje de propina que desea dejar (10, 15 o 20): "))

tip= tip/100

totalbill=(bill*tip) +bill

totaltip=(bill*tip) 

print(f"El total de la cuenta es de: {totalbill}. El valor de la propina es de: {totaltip}")