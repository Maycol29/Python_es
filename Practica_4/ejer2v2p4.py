import json
import PySimpleGUI as sg 

layout=[[sg.Text("ingresa id del jugador "),sg.InputText(key="nombre")],
[sg.Text("ingresa el nivel del jugador"),sg.InputText(key="nivel")],
[sg.Text("ingresar puntaje maximo "),sg.InputText(key="puntaje")],
[sg.Text("ingrese tiempo de juego en horas"),sg.InputText(key="tiempo")],
[sg.Button("Añadir o modificar"),sg.Exit()]]

def escribirArchivo(jugadores):
    with open ("ListaJ.json","w") as archivo: 
        json.dump(jugadores,archivo)

def leerArchivo():
    with open ("ListaJ.json","r")as archivo:
        datos= json.load(archivo)
    return datos


def carga(values):
    jugador=leerArchivo()
    nombre=values["nombre"]
    if nombre in jugador.keys():
        jugador[nombre]={
            "nivel":values["nivel"],
            "puntaje":values["puntaje"],
            "tiempo":values["tiempo"]
              }
    else:
        jugador[nombre]={
            "nivel":values["nivel"],
            "puntaje":values["puntaje"],
            "tiempo":values["tiempo"]
              }
    escribirArchivo(jugador)

window=sg.Window("ingrese jugador a modificar o añadir").Layout(layout).Finalize()


while True:
    event,values=window.Read()
    if event is None or event == 'Exit':
        break
    elif event == 'Añadir o modificar':
        if values["nombre"]== "" or values["nivel"]=="" or values["puntaje"]=="" or values["tiempo"]=="":
            sg.Popup('Falta completar algun campo')
        else:
            carga(values)
