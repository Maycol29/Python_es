import csv
import PySimpleGUI as sg


layout=[[sg.Text("informacion de los egresados")],
        [sg.Button("Mostrar")],
        # [sg.Input(visible=False, enable_events=True, key="file"),sg.FileBrowse("")],
        [sg.Text("lista"),sg.Listbox([],select_mode=True,size=(50,20),key="listbox")],

        [sg.Button("Exit")]]

try:
    archi = open("mujeresEncarrera.csv", "r")
except (FileNotFoundError):
    sg.popup("no se encuentra el archivo")

csvreader = csv.reader(archi)
def mujeres_universidad():
    dic_m={}
    lista_mujer=[]
    universidad_actual=""
    try:
        for fila in csvreader:
                if fila[2]==universidad_actual:
                    cont = cont +1    
                else:
                    if(universidad_actual!=""):
                        print("-"*30)
                        print('La {} tiene {} egresadas'.format(fila[2],cont))
                        dic_m[fila[2]]=fila[10]
                        print("-"*30)
                    universidad_actual=fila[2]
                    cont = 1
    except UnicodeDecodeError:
        print("Salta error ")
    return(dic_m)

def hombres_universidad():
    dic_h={}
    lista_hombre=[]
    universidad_actual=""
    try:
        for fila in csvreader:
                if fila[2]==universidad_actual:
                    cont = cont +1    
                else:
                    if(universidad_actual!=""):
                        print("-"*30)
                        print('La {} tiene {} egresados'.format(fila[2],cont))
                        dic_h[fila[2]]=fila[9]
                        print("-"*30)
                    universidad_actual=fila[2]
                    cont = 1
    except UnicodeDecodeError:
        print("Salta error ")
    return (dic_h)
   

def informacion(dic_hombre,dic_mujer):
    lista=[]
    for k,v in dic_hombre.items():
        print(k)
        print(v)
        print(dic_mujer.items[v])
        lista.append({"Facultad":k,"Alumnos_varones":v,"Alumnos_mujeres":dic_mujer[v]})
    print(lista)
    return lista


window=sg.Window("Bienvenido").layout(layout).finalize()

while True:
    event,values=window.read()
    dic_hombre=hombres_universidad()
    dic_mujer=mujeres_universidad()
    if(event== "Exit"):
        window.close()
        break
    elif(event=="Mostrar"):
        lista_completa=informacion(dic_hombre,dic_mujer)
        window["listbox"].update(lista_completa)
window.close()

#aclaro tuve q hacer el programa de cero,noe ncontre el error a la key 