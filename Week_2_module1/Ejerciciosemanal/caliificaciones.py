def validation_q(note):#Funcion para validar la nota inicial
    try:#Try except para capturar errores
        note=int(note)
        if note < 0 or note>100:
            print("Deber ser entre 0 y 100")
            return False
        return True
    except ValueError:
        print("Calificación no válida")
        return False

def qualification(c_qualification):#Funcion principal donde se pide la nota inicial 
    while True:#Ciclo while para que si el usuario ingresa datos incorrectos, pida los datos hasta que sean validos
        print('-----------------------')
        limit_q=input("Ingrese una calificación de 0 a 100 donde se determine si se aprueba o reprueba una nota:\n")
        print('-----------------------')
        if not validation_q(limit_q):#Llamada de la funcion validation_q
            continue
        limit_q=int(limit_q)
        addition_q=sum(c_qualification)
        number_q=len(c_qualification)
        average_q=addition_q/number_q
        if average_q < limit_q:
            print('-----------------------')
            print('El estudiante reprobó.')
            print('-----------------------')
            break
        print('-----------------------')
        print("El estudiante aprobó.")
        print('-----------------------')
        break
        break

def search_q(c_qualification):#Funcion que busca calificaciones que son mayores a una nota ingresada pore el usuario
    while True:
        try:
            print('-----------------------')
            value=input("Ingrese el valor por el cual quiere buscar las notas mayores al mismo:\n")
            print('-----------------------')
            value=int(value)
            c=0
            for i in c_qualification:#Ciclo for para recorrer la lista de calificaciones y las compara por medio del if
                c+=1
                if i> value:
                    print('-----------------------')
                    print(f"Calificación {c}. {i}")
                    continue
            break
        except ValueError:
            print("Valor no válido.")


def searchbyone(c_qualification):#Funcion para buscar calificacion o calificaciones determinadas por el usuario
    while True:
        try:#Validación de nota 
            print('-----------------------')
            value_2=input("Ingrese el valor de la nota que desea buscar:\n")
            print('-----------------------')
            value_2=int(value_2)
            c=0
            for i in c_qualification:#Ciclo for para recorrer la lista e imprimir las nota o notas que fue determinada por el usuario
                c+=1
                if i ==value_2:
                    print('-----------------------')
                    print(f"Calificación {c}. {i}")
                    continue
            break
        except ValueError:
            print("Valor no válido.")

def menu():#Función menú donde se hace el promedio de todas las notas y define si el estudiante aprobo o reprobo
    c_qualification=indent_q()
    while True:
        try:
            decision=input('\n¿Desea buscar alguna nota?\n1.Si\n2.No\n')
            decision=int(decision)
            match decision:
                case 1:
                    decision2=input("¿Desea buscar una nota especifica o las calificaciones mayores a un valor\n1.Nota específica\n2.Calificaciones mayores\n")
                    decision2=int(decision2)
                    match decision2:
                        case 1:
                            searchbyone(c_qualification)
                            continue
                        case 2:
                            search_q(c_qualification)
                            continue
                case 2:
                    qualification(c_qualification)
                    break
        except ValueError:
            print("Opción no válida.")

def indent_q():#Funcion para pedir todas las notas, valida las notas y las añade a una lista
    while True:
        print('-----------------------')
        inputuser= input("Ingrese las notas del 0 al 100 separadas por comas sin espacios:\n")
        print('-----------------------')
        try:
            inputreplace=inputuser.replace(' ', '')#Replace usado para reemplazar los espacios agregados innceseriamente por el usuario
            qualifications=inputreplace.split(',')#Por medio del split cada que el usuario ingrese una coma el dato posterior a la coma se tomara como un dato diferente
            c_qualification=[]
            has_invalid_notes = False
            for note in qualifications:#Ciclo for para castear todas las notas y agregarlas a una lista
                if not validation_q(note):
                    has_invalid_notes = True
                note=int(note)
                c_qualification.append(note)

            if has_invalid_notes:
                print("Por favor ingrese notas entre 0 y 100")
                continue
            
            return c_qualification
        
            
        except ValueError:
            print("Calificación no válida")

menu()#Ejecución de función principal