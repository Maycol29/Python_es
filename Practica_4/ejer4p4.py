import PySimpleGUI as sg 
import json

layout=[[sg.Input(visible=True, enable_events=False, key="color"),sg.FileBrowse("Elija el archivos de colores")],
[sg.Input(visible=True, enable_events=False, key="coordenadas"),sg.FileBrowse("Elija el archivos de coordenadas")],
[sg.Button("siguiente"),sg.Button("Exit"),sg.Button("Nuevo_ejer")]]

def panel(color,coordenadas):
    layout=[[sg.Graph(canvas_size=(500, 500), graph_bottom_left=(0,0), graph_top_right=(500, 500), background_color='green', key='graph')],
    [sg.Button("dibujar"),sg.Button("Exit")]]

    window = sg.Window('Graph test', layout)
    graph = window['graph']
    dic={}
    colores=color.read()
    coorde=coordenadas.read()
    c1=colores.split(",")
    for i in range(0,len(c1)): 
        if c1[i]=="rojo":
            c1[i]="red"

        elif c1[i]=="blanco":
            c1[i]="white"

        elif c1[i]=="negro":
            c1[i]="black"

        elif c1[i]=="amarillo":
            c1[i]="yellow"

        elif c1[i]=="azul":
            c1[i]="blue"

            
    f = open("coordenadas.txt","r")
    cadena=f.read()
    cadena=cadena.replace("(","").replace(")","").replace("[","").replace("]","")
    cadena=cadena.split(",")
    j=0
    for i in range(0,len(c1)):  
        dato=(int(cadena[j]),int(cadena[j+1]))
        print(dato)
        dic[c1[i]]=dato
        j=j+2
    print(dic)
     


    print(dic)
    while True:
        event,values=window.read()
        if(event=="dibujar"):
            for dato in dic:
                print(dato)
                graph.draw_point(dic[dato], size=15 , color=dato) 

        if(event=="Exit"):
            break
    window.close()


def leer_archivo():
    # Tarea: Pensar como manejar exceptions aca
    try:
        with open('color_cordenada.json', 'r') as archivo:
            datos = json.load(archivo)
        return datos  
    
    except FileNotFoundError:
        with open('color_cordenada.json', 'w') as archivo:
            datos={}
            json.dump(datos, archivo)        
        return datos

def escribirArchivo(datos):
    with open("color_cordenada.json" , 'w') as archivo:
        json.dump(datos,archivo)


def Cargar_datos(datos):
    archivo=leer_archivo()
    archivo[len(archivo)]=datos
    escribirArchivo(archivo)
    


def combo(color):
    colorines=color.read()
    colorines=colorines.split(",")
    layout=[
        [sg.InputCombo(colorines,size=(10,100),default_value="white",key="eleccion")],
        [sg.Frame('coordenadas X e Y',[[
        sg.Slider(range=(1, 200), orientation='h', size=(13, 25), default_value=13,key="x"),
        sg.Slider(range=(1, 200), orientation='h', size=(13, 25), default_value=13,key="y"),
     ]])],
     [sg.Listbox([],select_mode=True,size=(30,20),key="listbox")],
        [sg.Button("Añadir"),sg.Button("Cargar"),sg.Button("Exit")]
    ]
    
    window=sg.Window("ejer_6").layout(layout).finalize()
    lista=[]
    while True:
        event,values=window.read()
        if(event=="Exit"):
                break
        elif(event=="Añadir"):
            # print(values)  {'eleccion': 'rojo', 'x': 121.0, 'y': 65.0} eso sin listbox
            # dic[values["eleccion"]]=(values["x"],values["y"])
            # Cargar_datos(dic)
            lista.append({"Color":values["eleccion"],"Coordenadas":(values["x"],values["y"])})
            window["listbox"].update(lista)

        elif(event=="Cargar"):
            datos=values["listbox"][0]
            Cargar_datos(datos)
    window.close()


window=sg.Window("Bienvenido").layout(layout).finalize()
while True:
    event,values=window.read()
    if(event=="Exit"):
       break
    elif(event=="siguiente"):
        color=open ((values["color"]),"r")
        coordenadas=open(values["coordenadas"],"r")
        panel(color,coordenadas)
        break
    elif(event=="Nuevo_ejer"):
        color=open ((values["color"]),"r")
        window.close()
        combo(color)
        break
    window.close()