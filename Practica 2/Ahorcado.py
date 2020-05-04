import random
#Preparo el juego
#Defino conjunto de palabras a trabajar por temas
def inicializar():
    palabras = {1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3:['milanesa','pure','pizza','salchicha']}
    tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))
    pal = palabras[tema][random.randrange(len(palabras[tema]))]
    return pal

#Comienza el proceso del juego

#armo la estructura de la palabra sobre la cuál se irá armando con las letras 
#que se ingresen. Comienza con tantas rayas como letras tiene la palabra a adivinar
def separar(pal):
    pal_separada = []
    for i in pal:
     pal_separada.append("_")
    print ("- "*len(pal))
    return pal_separada


#comienza la interacción con el jugador

def jugar(palabra,pal_separada,ahorcado,sigue):
    #introducción de letras por parte del jugador
    cantidad_letras_adivinadas = 0
    sigue=True
    cantidad_partes_cuerpo = 0
    while (sigue==True):
        letra = input("Ingresa una letra: ")
    # Si hay al menos una aparición de la letra..
        if letra in palabra:

        #Coloco en pal_separada la letra en las posiciones donde se encuentra
        # e incremento la cantidad de letras adivinadas
            for pos in range(len (palabra)):

                if palabra[pos] == letra:
                    pal_separada[pos] = letra
                    cantidad_letras_adivinadas = cantidad_letras_adivinadas + 1

        #armo la palabra a mostrar al jugador con su letra elegida
            pal_imprime = " "
            for y in pal_separada:
              pal_imprime = pal_imprime + y + " "
            print (pal_imprime)

        #averiguo si terminó o debe continuar
            if cantidad_letras_adivinadas == len(palabra):
                print ("Ganaste")
                sigue=False

        else:
        #si se equivocó completo el cuerpo
            cantidad_partes_cuerpo = cantidad_partes_cuerpo + 1
            for x in range(cantidad_partes_cuerpo):
                print (ahorcado[x])
            if cantidad_partes_cuerpo == 3:
                print ("Perdiste!. La palabra era:", palabra)
                sigue=False


sigue=True
while(sigue==True):
    palabra= inicializar()  
    ahorcado =  [" O ", "/|\\","/ \\ "]
    cantidad_letras_adivinadas = 0
    cantidad_partes_cuerpo = 0
    pal_separada=separar(palabra)
    jugar(palabra,pal_separada,ahorcado,sigue)
    x=int(input("Gracias por jugar.\ningresa 1 si quieres seguir jugando   "))
    if (x==1):
        sigue = True
    else:    
        sigue=False
print("Gracias por jugar")