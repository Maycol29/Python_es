# 9. Generar un tablero A con casilleros de 10 x 10 y un tablero B con una
# única fila que contenga 5 letras al azar. El objetivo del ejercicio es que se
# puedan situar una por una, las letras del tablero B al tablero A haciendo
# clic sobre cada una de las letras. La mecánica sugerida es la de utilizar un
# clic para elegir una letra del B y otro clic sobre algún casillero del tablero
# A. Nota: no se debe permitir que se pueda agregar una letra sobre un
# casillero ocupado. Se deberán agregar todas las letras disponibles.

import PySimpleGUI as sg
import random
abecedario="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
print(abecedario)
abecedario=abecedario.split(",")
print(abecedario)
sg.theme('Dark Purple 1')
letras=[]

for i in range(1,8):
    a=random.randrange(1,len(abecedario))
    letras.append(abecedario[a])
print(letras)

def contador(nro):
    print(nro)
    nro=nro-1

header =  [[sg.Text('  ')] + [sg.Text("ScrabbleAr", size=(14,1),key="menu")]]

board =[[sg.Button("", size=(2, 1),key=(i,j), pad=(0,0)) for i in range(15)] for j in range(15)]



fichas = [
    [sg.Button(letras[0], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20)),
    sg.Button(letras[1], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20)),
    sg.Button(letras[2], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20)),
    sg.Button(letras[3], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20)),
    sg.Button(letras[4], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20)),
    sg.Button(letras[5], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20)),
    sg.Button(letras[6], button_color=('white', 'black'), size=(3, 1), font=("Helvetica", 20))],
    [sg.Button('Save'),sg.Button("Exit")]
      ]



layout = header + board + fichas

window = sg.Window('ScrabbleAr', layout, font='Courier 12')


posicion=[]
ok=True
while ok:
    sg.popup("elige una ficha")
    eventNum = window.read()
    if eventNum[0] == 'Exit':
        ok=False
        break
    elif eventNum is letras[0] or letras[1]or letras[2] or letras[3] or letras[4]or letras[5]:
        print(eventNum[0])
        sg.popup("elige una posicion")
        eventPos= window.read()
        print(eventPos[0])
        window[eventPos[0]].update(eventNum[0])
    
        

       
        
        

        