import json
import time
import PySimpleGUI as sg

archivo = open('Lista_Metereologica.json', "w")

fecha = time.strftime("%d %b %Y, %H:%M.", time.localtime())

#Definimos Layout

layout = [
    [sg.Text("Temperatura: "),sg.Input(key="Temperatura:")],
    [sg.Text("Humedad:"),sg.Input(key="Humedad:")],
    [sg.Button("Añadir"), sg.Button("Cargar en json"), sg.Exit()]
]

window = sg.Window('Ejercicio 1').Layout(layout).Finalize()

def escribirArchivo(listaMetereologica):
    with open('Lista_Metereologica.json', 'w') as archivo:
        json.dump(listaMetereologica,archivo)

listaMetereologica = []
ok = True
while ok:
    event, values = window.Read()
    lista = []
    #sg.Print(event)
    #sg.Print(values)

    #window.FindElement()

    if event is None or event == 'Exit':
        escribirArchivo(listaMetereologica)
        archivo.close()
        ok = False
    elif event == 'Añadir':
        if values['Temperatura:'] == '' or values['Humedad:'] == '':
            sg.Popup('Falta completar algun campo')
        else:
            datos = (str("Temperatura "+values['Temperatura:']+' *C.'),str("Humedad " +values['Humedad:']+"%"), str(fecha))
            lista.extend(datos)
            listaMetereologica.append(str(lista))
    elif event == 'Cargar en json':
        escribirArchivo(listaMetereologica)
        archivo.close()