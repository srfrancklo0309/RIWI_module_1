list_passangersN=[]
list_passangersI=[]

import random

while True:
        print("**Bienvenido al sistema de costeo de equipaje Aéreo**").upper
        name=input("\nIngrese su nombre:\n")
        type_t=input("\n¿Su viaje es Nacional o Internacional?\n1.Nacional\n2.Internacional\n")
        type_t=int(type_t)
        luggage=input("\n¿Su equipaje es de mano?\n1.Si\n2.No\n")
        luggage=int(luggage)

        if luggage == 1:
            weight=input("\nIngrese el peso en Kilogramos de su equipaje:\n")
            weight=float(weight)
            if weight >13:
                print("Peso rechazado")
                luggage='Sin Equipaje'
                price_lugagge= 1
            else:
                luggage='Equipaje de mano'
                price_lugagge= 1
        else:
            weight=input("\nIngrese el peso en Kilogramos de su equipaje:\n")
            weight=float(weight)
            if weight > 50 and weight < 0:
                print("Peso no permitido.")
                luggage='Sin Equipaje'
                price_lugagge= 1
            elif weight < 20 and weight>0:
                luggage='Equipaje costo adicional'
                price_lugagge= 50000
            elif weight < 20 and weight>30:
                luggage='Equipaje costo adicional'
                price_lugagge= 70000
            elif weight < 30 and weight>50:
                luggage='Equipaje costo adicional'
                price_luggage= 110000

        date_t=input("\nIngrese la fecha del viaje.\n")

        passanger=random.random()

        match type_t:
            case 1:
                passanger={
                'name':name,
                'type_t':'Nacional',
                'weight':weight,
                'type of luggage':luggage,
                'date':date_t,
                'total_bill':230000+price_lugagge
                }
                list_passangersN.append(passanger)
            case 2:
                passanger={
                'name':name,
                'type_t':'Internacional',
                'weight':weight,
                'type of luggage':luggage,
                'date':date_t,
                'total_bill':4200000+price_lugagge
                }
                list_passangersI.append(passanger)

        decision=input("\n¿Desea agregar otro pasajero?\n1.Si\n2.No\n")
        decision=int(decision)

        match decision:
            case 1:
                continue
            case 2:
                for passanger, national in list_passangersN.items():
                    print(f"Pasajero Nacional #{passanger}:\nNombre: {national['name']}.\nDestino: Bogotá a Medellín.\nTipo de equipaje: {national['type of luggage']}.\nFecha de vuelo: {national['date']}.\nCosto total incluido equipaje: {national['total_bill']}")

                for passanger, international in list_passangersI.items():
                    print(f"Pasajero Internacional #{passanger}:\nNombre: {international['name']}.\nDestino: Bogotá a España.\nTipo de equipaje: {international['type of luggage']}.\nFecha de vuelo: {international['date']}.\nCosto total incluido equipaje: {international['total_bill']}")
                break

admins=input("\n**Admins**\n")
admins=int(admins)

match admins:
    case 1:
        SystemExit
    case 2:
        SystemExit
    case 3:
        numberpI=len(list_passangersI)
        numberpN=len(list_passangersN)
        totalpassanger=numberpI+numberpN

        totalsellsN=0
        totalsellsI=0

        for passanger, national in list_passangersN.items():
            totalsellsN=+ national['total_bill']

        for passanger, international in list_passangersI.items():
            totalsellsI=+ international['total_bill']

        totalsells=totalsellsI+totalsellsN