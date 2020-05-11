import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg 
import json

def escribirArchivo(values):
	with open("ListaDeJugadores.json","w")as archivo:
		json.dump(values,archivo)

def elijoJuego():
    layout = [
    [sg.Button("Ahorcado") , sg.Button("TaTeTi") , sg.Button("Reverse")],
    [sg.Exit()]
    ]

    window = sg.Window('JUEGOS').Layout(layout).Finalize()

	while True:
		if event




layout=[
	[sg.Text("INGRESE SU NOMBRE Y APELLIDO")],
    [sg.InputText(key="nombre")],
    [sg.Text("INGRESE SU EDAD")],
    [sg.InputText(key="edad")],
    [sg.Text("INGRESE SU DNI")],
    [sg.InputText(key="dni")],    
    [sg.Button("siguiente"),sg.Exit()]
	]

window=sg.Window("Bienvenido al menu de juego").Layout(layout).Finalize()

while True:
	event,values=window.Read()

	if(event is None or event == "Exit"):
		break
	else:
		if(values["nombre"]=="" or values["edad"]==""or values["dni"]==""):
			sg.Popup("Falta ingresar algun campo")
		else:
			elijoJuego()
	
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
