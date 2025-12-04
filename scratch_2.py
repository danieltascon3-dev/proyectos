catalogo = [{"id": 1, "nombre": "Laptop", "precio": 1000.0, "stock": 5},
            {"id": 2, "nombre": "Mouse", "precio": 25.0, "stock": 20}]

def agregar():
    producto = {}
    ultimo_id = catalogo[-1]['id']
    nombre = input("ingrese el nombre del producto")
    precio = float(input("ingrese el precio"))
    stock = int(input("ingrese el stock"))
    producto['id'] = ultimo_id + 1
    producto['nombre'] = nombre
    producto['precio'] = precio
    producto['stock'] = stock
    catalogo.append(producto)


def mostrar():
    for elemento in catalogo:
        print(f"{elemento}")


def buscar():
    buscador = input("ingrese el nombre del producto que desea buscar")
    for i in catalogo:
        if buscador == i['nombre']:
            print(f"el ID {i['id']} es el producto")
            break
    else:
        print("no esta en la lista")


def actualizar():
    condicion = False
    while not condicion:
        buscador = int(input("ingrese el ID del producto que desea buscar para actualizar sus datos"))
        for i in catalogo:
            if buscador == i['id']:
                print(f"{i['id']}, {i['nombre']}, {i['precio']}, {i['stock']}")
                pregunta = int(input("es el producto que buscaba\n"
                                     "presione 1 para si\n"
                                     "presione 2 para no"))
                match pregunta:
                    case 1:
                        i['nombre'] = input("ingrese el nuevo nombre")
                        i['precio'] = float(input("ingrese el nuevo precio"))
                        i['stock'] = int(input("ingrese el nuevo stock"))
                        condicion = True
                    case 2:
                        print("sabe el id del producto a encontrar?")
                        consulta = int(input("1 para si\n"
                                             "2 para no\n"
                                             ">"))
                        if consulta == 1:
                            print("ingrese el id nuevamente")
                        else:
                            print("use la opcion buscar para saber cual es el id")
                            condicion = True
        else:
            condicion = True
            print("no esta el producto")
def eliminar():
    condicion = False
    while not condicion:
        buscador = int(input("ingrese el ID del producto que desea buscar para eliminar sus datos"))
        for i in catalogo:
            if buscador == i['id']:
                print(f"{i['id']}, {i['nombre']}, {i['precio']}, {i['stock']}")
                pregunta = int(input("es el producto que desea eliminar\n"
                                     "presione 1 para si\n"
                                     "presione 2 para no"))

                match pregunta:
                    case 1:
                        catalogo.remove(i)
                        condicion = True
                    case 2:
                        print("sabe el id del producto a encontrar?")
                        consulta = int(input("1 para si\n"
                                             "2 para no\n"
                                             ">"))

def menu():
    condicion = False
    while not condicion:
        print(""" opcion 1 agregar
        opcion 2 mostrar
        opcion 3 buscar
        opcion 4 actualizar
        opcion 5 eliminar
        opcion 0 salir""")
        eleccion = int(input(""))
        match eleccion:
            case 1:
                agregar()
            case 2:
                mostrar()
            case 3:
                buscar()
            case 4:
                actualizar()
            case 5:
                eliminar()
            case 0:
                condicion = True
            case _:
                print("opcion no valida")

menu()