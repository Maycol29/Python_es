import json
def leer(Datos):
    nombre = input("Ingrese el nombre del jugador:  ")
    if nombre != "ZZZ":
        Datos[nombre]={}
        Datos[nombre]["nivel"] = (int(input("Ingrese el nivel del jugador:  ")))
        Datos[nombre]["puntaje"] = (int(input("Ingrese el puntaje max del jugador:  ")))
        Datos[nombre]["tiempo"] = (input("Ingrese tiempo de juego:  "))
    return nombre

def escribirArchivo(jugadores):
    with open('ListaJ.json', 'w') as archivo:
        json.dump(jugadores,archivo)

#Lleno la estrutura de datos
jugadores = {}
def cargoJugadores(jugadores):
    nombre = leer(jugadores)
    while nombre != "ZZZ":
        nombre = leer(jugadores)
    escribirArchivo(jugadores)
    return jugadores

cargoJugadores(jugadores)