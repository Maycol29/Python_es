import PySimpleGUI as sg 
import json



archivo=open("Jugadores.json","w")
layout=[[sg.Text("ingresa id del jugador "),sg.InputText(key="nombre")],
[sg.Text("ingresa el nivel del jugador"),sg.InputText(key="nivel")],
[sg.Text("ingresar puntaje maximo "),sg.InputText(key="puntaje")],
[sg.Text("ingrese tiempo de juego en horas"),sg.InputText(key="tiempo")],
[sg.Button("Añadir o modificar"),sg.Exit()]]


def leerArchivo():
    # Tarea: Pensar como manejar exceptions aca
    try:
        with open("jugadores.json", 'r') as archivo:
            datos = json.load(archivo)
        return datos  
    
    except FileNotFoundError:
        with open("jugadores.json", 'w') as archivo:
            datos={}
            json.dump(datos, archivo)        
        return datos

def escribirArchivo(datos):
    with open("jugadores.json" , 'w') as archivo:
        json.dump(datos,archivo)


    

def cargar(values):
    jugadores=leerArchivo()
    nombre=str(values["nombre"]).lower()
    if nombre in jugadores.keys():
        if (int(values["puntaje"]<jugadores["nombre"]["puntaje"])):
            values["puntaje"]=jugadores["nombre"]["puntaje"]
        jugadores[nombre] = {
        'puntaje': int(values['puntaje']),
        'nivel': int(values['nivel']),
        'tiempo': int(values['tiempo'])}
    else:
        jugadores[nombre] = {
                'puntaje': int(values['_puntaje_']),
                'nivel': int(values['_nivel_']),
                'tiempo': int(values['_tiempo_'])
            }
    escribirArchivo(jugadores)



window=sg.Window("Añadir o modificar Jugadores").Layout(layout).Finalize()
jugadores={}
ok=True
dic={}
while ok:
    event,values=window.Read()
    #print(event)
    #print(values)
    jugador={}
    if event is None or event == 'Exit':
        archivo.close()
        ok = False
    elif event == 'Añadir o modificar':
          if values["nombre"]== "" or values["nivel"]=="" or values["puntaje"]=="" or values["tiempo"]=="":
            sg.Popup('Falta completar algun campo')
          else:
            cargar(values)