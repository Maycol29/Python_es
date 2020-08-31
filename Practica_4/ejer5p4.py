import PySimpleGUI as sg
import json


layout=[[sg.Text("ingrese id del jugador")],
        [sg.InputText()],
        [sg.Text("ingrese nivel del jugador")],
        [sg.InputText()],
        [sg.Text("ingrese puntaje maximo del jugador")],
        [sg.InputText()],
        [sg.Text("ingrese tiempo invertido del jugador")],
        [sg.InputText()],
        [sg.Submit(),sg.Cancel()]]
data={}
data["people"]={}

window= sg.Window("Ingrese la informacion del jugador ").Layout(layout)
while True:
    event,values = window.Read()

    sg.Print(event)
    sg.Print(values)

    if event is None or event == "Exit":
        break
    elif event == "coord":
        if values["nombre"] == "" or values["puntaje"] == "":
            sg.Popup("Falta algun campo")
        else:
            data["people"].append({{"Nombre":values[0]},{"Nivel":values[1]},{"maximoPun":values[2]},{"Tiempo":values[3]}})


data['text'] = 'JUGADORES DEL VLAHIR'

with open('jugadores.json', 'w') as outfile:
    json.dump(data["people"], outfile)


with open('jugadores.json') as json_file:
    data = json.load(json_file)
    for p in data["people"]:
        print("Nombre: " + p['Nombre'])
        print("Nivel: " + p['Nivel '])
        print("maximoPun: " + p['maximoPun'])
        print("Tiempo: "+p['Tiempo'])

    print(data['text'])