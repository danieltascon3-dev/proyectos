diccionario = {}


def ingreso():
    continuar = False
    while not continuar:
        nombres = input("ingrese el nombre")
        emails = input("ingrese el email")
        diccionario[nombres] = emails
        agregar = input("quieres agregar otro contacto").upper()

        if agregar == 'Y':
            continuar = False
        elif agregar == 'N':
            continuar = True
        else:
            print("opcion no valida")
            agregar = input("quieres agregar otro contacto").upper()

    with open("Agenda.txt", "a") as archivo:
        for nombres,emails in diccionario.items():
            archivo.write(f"nombre: {nombres}, email {emails} \n")


def lectura():
    with open("Agenda.txt", "r") as archivo:
        for linea in archivo:
            print(linea.strip())
        archivo.close()


def buscar():
    with open("Agenda.txt", "r") as archivo:
        busqueda = input("ingrese el nombre a busacar")
        for linea in archivo:
            separar = linea.split(",")
            if busqueda in separar[0]:
                print(linea)
                break
        else:
            print("no se encontro el nombre")

def menu():
    condicion = False
    while not condicion:
        print("""menu de carga
        1 ingresar nombre y email
        2 ver todos los contactos
        3 buscar por nombre
        0 cerrar el programa""")
        eleccion = int(input("ingrese la opcion que quiera"))
        match eleccion:
            case 1:
                ingreso()
            case 2:
                lectura()
            case 3:
                buscar()
            case 0:
                condicion = True
            case _:
                print("opcion no valida")

menu()
