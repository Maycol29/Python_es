import json

import PySimpleGUI as sg




#Definimos Layout

layout = [
    [sg.Text("Temperatura: "),sg.Input(key="Temperatura")],
    [sg.Text("Humedad:"),sg.Input(key="Humedad")],
    [sg.Listbox([],select_mode=True,size=(30,30),key="listbox")],
    [sg.Button("Añadir"), sg.Button("Cargar"), sg.Exit()]
]

window = sg.Window('Ejercicio 1').Layout(layout).Finalize()

def leer_archivo():
    # Tarea: Pensar como manejar exceptions aca
    try:
        with open('Lista_Metereologica.json', 'r') as archivo:
            datos = json.load(archivo)
        return datos  
    
    except FileNotFoundError:
        with open('Lista_Metereologica.json', 'w') as archivo:
            datos={}
            json.dump(datos, archivo)        
        return datos

def escribirArchivo(datos):
    with open("Lista_Metereologica.json" , 'w') as archivo:
        json.dump(datos,archivo)

def Cargar_datos(datos):
    archivo=leer_archivo()
    archivo[len(archivo)]=datos
    escribirArchivo(archivo)


listaMetereologica = []
ok = True
while ok:
    event, values = window.Read()
    lista = []
    print(event,values)
    if event is None or event == 'Exit':
        ok = False
    elif(event=="Añadir"):
        listaMetereologica.append({"Temperatura":values["Temperatura"],"Humedad":values["Humedad"]})
        window["listbox"].update(listaMetereologica)
    elif(event=="Cargar"):
        datos=values["listbox"][0]
        print(values)
        Cargar_datos(datos)
