import PySimpleGUI as sg 

layout=[[sg.Input(visible=True, enable_events=False, key="color"),sg.FileBrowse("Elija el archivos de colores")],
[sg.Input(visible=True, enable_events=False, key="coordenadas"),sg.FileBrowse("Elija el archivos de coordenadas")],
[sg.Button("siguiente"),sg.Button("Exit")]]

def panel(color,coordenada):
    layout=[[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0,0), graph_top_right=(400, 400), background_color='green', key='graph')],
    [sg.Button("dibujar"),sg.Button("Exit")]]

    window = sg.Window('Graph test', layout)
    graph = window['graph']
    dic={}
    colores=color.read()
    coorde=coordenadas.read()
    c1=colores.split(",")
    f = open("coordenadas.txt","r")
    cadena=f.read()
    cadena=cadena.replace("(","").replace(")","").replace("[","").replace("]","")
    cadena=cadena.split(",")
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

     
    j=0
    print(cadena)
    for i in range(0,len(c1)):  
        dato=(int(cadena[j]),int(cadena[j+1]))
        print(dato)
        dic[c1[i]]=dato
        j=j+2
    print(dic)
     
   
    # while True:
    #     event,values=window.read()
    #     if(event=="dibujar"):
    #         for dato in dic:
    #             print(dato)
    #             graph.draw_point(dic[dato], size=15 , color=dato) 

    #     if(event=="Exit"):
    #         break
    # window.close()
            
             



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
window.close()  