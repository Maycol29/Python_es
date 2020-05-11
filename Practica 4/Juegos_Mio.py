import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg 
import json


def escribirArchivo(values):
	with open("ListaDeJugadores.json","w") as archivo:
		json.dump(values,archivo)


def leerArchivo():
    try:
     with open("ListaDeJugadores.json","r") as archivo:
         datos=json.load(archivo)
     return datos

    except FileNotFoundError:
        with open("ListaDeJugadores.json","w") as archivo:
            datos={}
            json.dump(datos, archivo)        
        return datos


def cargarArchivo(values):
    jugador=leerArchivo()
    nombre=str(values["nombre"]).lower()
    if nombre not  in jugador.keys(): 
        jugador[nombre] = {   
        "juego": "",
        "edad" : values["edad"]
        }   
    escribirArchivo(jugador)

def modificar(jugador,event):
    jugadores=leerArchivo()
    nombre=str(jugador).lower()
    jugadores[nombre]["juego"]=event
    escribirArchivo(jugadores)



def elijoJuego(nombre):
    layout = [
    [sg.Button("Ahorcado") , sg.Button("TaTeTi") , sg.Button("Reverse")],
    [sg.Exit()]
    ]

    window = sg.Window('JUEGOS').Layout(layout).Finalize()
    ok=True
    while ok:
        event,values=window.Read()
        if event is None or event=="Exit":
            ok=False
        else:
            if event=="Ahorcado":
                modificar(nombre,event)
                window.Close()
                hangman.main()
                break
            elif event=="TaTeTi":
                modificar(nombre,event)
                window.Close()
                tictactoeModificado.main()
                break
                
            elif event=="Reverse":
                modificar(nombre,event)
                window.Close()
                reversegam.main()
                break 
       
  
  


layout = [
	[sg.Text("INGRESE SU NOMBRE Y APELLIDO")],
    [sg.InputText(key="nombre")],
    [sg.Text("INGRESE SU EDAD")],
    [sg.InputText(key="edad")],
    [sg.Button("siguiente"),sg.Exit()]]

window=sg.Window("Bienvenido").Layout(layout).Finalize()

ok=True
while ok:
    event,values=window.Read()


    if event is None or event== "Exit":
        ok=False
        window.Close()
    else:
        if values["nombre"]==""or values["edad"]=="":
            sg.Popup("Falta un campo")
        else:
            cargarArchivo(values)
            window.Close()
            elijoJuego(values["nombre"])
            break
        
#Preguntas teoricas
 #justificar la estructura de datos a utilizar
 # utilize un diccionario de diccionarios ya que es mas facil acceder a los datos dependiendo cual dato necesite,si es el nombre por la key,sino con el nombre sacar edad y el juego que jugo
 
 # Elegir y justificar el formato de archivo a utilizar.
 # utilize json ya que es una manera muy facil de manejar los datos del mismo, ya sea para leer o escribir       
    









