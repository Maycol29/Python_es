import PySimpleGUI as sg
import json

def leer_archivo():
    # Tarea: Pensar como manejar exceptions aca
    try:
        with open('jugadores.json', 'r') as archivo:
            datos = json.load(archivo)
        return datos  
    
    except FileNotFoundError:
        with open('jugadores.json', 'w') as archivo:
            datos={}
            json.dump(datos, archivo)        
        return datos


def escribir_archivo(datos):
    with open('jugadores.json' , 'w') as archivo:
        json.dump(datos,archivo)

def cargar_datos(values):

    jugadores = leer_archivo()
    
    nombre = str(values['__nombre__']).lower()
    jugadores[nombre] = {
        'Puntaje': int(values['__puntaje__']),
        'Nivel': int(values['__nivel__']),
        'Tiempo': int(values['__tiempo__'])
    }

    escribir_archivo(jugadores)

def modificar(values):
    
    jugadores = leer_archivo()
    nombre = str(values['__nombre__']).lower()
 
    if nombre in jugadores.keys():
        jugadores[nombre] = {
        'Puntaje': int(values['__puntaje__']),
        'Nivel': int(values['__nivel__']),
        'Tiempo': int(values['__tiempo__'])
        }

    escribir_archivo(jugadores)

def incompleto(values):
    if values['__nombre__'] == '' or values['__nivel__'] == '' or values['__puntaje__'] == '' or values['__tiempo__'] == '':
        return True
    else:
        return False


def modificar_datos():
    
    layout = [
    [sg.Text("Nombre") , sg.Input(key='__nombre__')],
    [sg.Text('Nivel') , sg.Input(key='__nivel__')],    
    [sg.Text('Puntaje') , sg.Input(key='__puntaje__')],    
    [sg.Text('Tiempo') , sg.Input(key='__tiempo__')],    
    [sg.Button("Modifico datos guardados") , sg.Exit()]
    ]

    window = sg.Window('Editar datos jugadores').Layout(layout).Finalize()

    while True:
        event, values = window.Read()
    
        if event is None or event == 'Exit':      
            break
        elif event == 'Modifico datos guardados':
            modificar(values)
            if incompleto(values):                  
                sg.Popup('Falta completar algun campo')                              
            else:                      
                modificar(values)
    window.Close()

#PROGRAMA PRINCIPAL

#Definimos la ventana
layout = [
    [sg.Text("Nombre") , sg.Input(key='__nombre__')],
    [sg.Text('Nivel') , sg.Input(key='__nivel__')],    
    [sg.Text('Puntaje') , sg.Input(key='__puntaje__')],    
    [sg.Text('Tiempo') , sg.Input(key='__tiempo__')],    
    [sg.Button('Guardo en json') , sg.Exit()]
]
window = sg.Window('Ventana de datos').Layout(layout).Finalize() 
# Loop para capturar los eventos de window

while True:
    event, values = window.Read()
    
    if event is None or event == 'Exit':      
        break
    elif event == 'Guardo en json':
        print(values)
        
        if incompleto(values):                  
            sg.Popup('Falta completar algun campo') 
        else:         
            cargar_datos(values)
window.Close()

modificar_datos()