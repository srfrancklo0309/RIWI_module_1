def validation_q(limit_q):
    try:
        limit=int(limit_q)
        if limit < 0 or limit>100:
            print("Deber ser entre 0 y 100")
            return False
        return True
    except ValueError:
        print("Calificación no válida")
        return False
            

def qualification():
    while True:
        print('-----------------------')
        limit_q=input("Ingrese una calificación de 0 a 100 donde se determine si se aprueba o reprueba una nota:\n")
        print('-----------------------')
        if not validation_q(limit_q):
            continue
        limit_q=int(limit_q)
        c_qualification = indent_q()

        addition_q=sum(c_qualification)
        number_q=len(c_qualification)
        average_q=addition_q/number_q
        search_q(c_qualification)
        searchbyone(c_qualification)

        if average_q < limit_q:
            print('-----------------------')
            print('El estudiante reprobó.')
            print('-----------------------')
            break
        print('-----------------------')
        print("El estudiante aprobó.")
        print('-----------------------')
        break

def search_q(c_qualification):
    while True:
        try:
            print('-----------------------')
            value=input("Ingrese el valor por el cual quiere buscar sus notas mayores:\n")
            print('-----------------------')
            value=int(value)
            c=0
            for i in c_qualification:
                c+=1
                if i> value:
                    print('-----------------------')
                    print(f"Calificación {c}. {i}")
                    continue
                break
            break
        except ValueError:
            print("Valor no válido.")


def searchbyone(c_qualification):
    while True:
        try:
            print('-----------------------')
            value_2=input("Ingrese el valor de la nota que desea buscar:\n")
            print('-----------------------')
            value_2=int(value_2)
            c=0
            for i in c_qualification:
                c+=1
                if i ==value_2:
                    print('-----------------------')
                    print(f"Calificación {c}. {i}")
                    continue
                break
            break
        except ValueError:
            print("Valor no válido.")



def indent_q():
    while True:
        print('-----------------------')
        inputuser= input("Ingrese las notas del 0 al 100 separadas por comas sin espacios:\n")
        print('-----------------------')
        try:
            inputreplace=inputuser.replace(' ', '')
            qualifications=inputreplace.split(',')
            c_qualification=[]
            for note in qualifications:
                note=int(note)
                c_qualification.append(note)
            return c_qualification
            
        except ValueError:
            print("Calificación no válida")



qualification()

