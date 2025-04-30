#Una pequeña biblioteca necesita registrar sus libros en un sistema muy simple.

def create():
    while True:
        id_book=input("Ingrese el ID del libro: \n")

        if id_book in books :
            print("El libro ya está en la biblioteca.")
            continue

        title_book=print("Ingrese el título del libro: \n")

        author_book=print("Ingrese el autor del libro: \n")

        publication_year=int(input("Ingrese el año de publicación: \n"))

        id_book={'Title':title_book, 'Autor':author_book, 'Año de publicación':publication_year}

        decision=int(input("¿Desea ingresar otro libro? \n1.Si\n0.No"))

        if decision == 1:
            continue
        else:
            break

def update():
    id_book=input("Ingrese el ID del libro: \n")

    title_book=print("Ingrese el título del libro: \n")

    author_book=print("Ingrese el autoy del libro: \n")

    publication_year=int(input("Ingrese el año de publicación: \n"))

    books[id_book]={'Title':title_book, 'Autor':author_book, 'Año de publicación':publication_year}

def delete():
    delete=input("Ingrese el id del libro que desea eliminar: \n")
    if not delete in books:
        print("ID no válido.")
    del books[delete]

def search_byone():
    opt=int(input("¿Cómo desea realizar la busquéda?\n1.ID\n2.Nombre\n"))
    if opt==1:
        id_book=input("Ingrese el ID del libro: \n")
        print(books[id_book])
    elif opt==2:
        title_book=input("Ingrese el título del libro: \n")
        for _, book in books.items():
            if title_book== book['Title']:
                print(f"El título del libro es: {book['Title']}, su autor es: {book['Autor']} y su año de publicación es: {book['Año de publicación']}")
    else:
        print("Opción inválida.")

books={}

while True:
    opt=int(input("¿Qué desea hacer?\n1.Agregar un nuevo libro.\n2.Ver todos los libros ingresados.\n3.Actualizar un libro.\n4.Eliminar un libro.\n5.Ver libro por su ID o título\n6.Salir\n"))

    match opt:
        case 1:
            create()
        case 2:

            for _,book in books.items():
                print(f'El título del libro es: {book['Title']}, su autor es:{book['Autor']} y su año de publicación es: {book['Año de publicación']}.')

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