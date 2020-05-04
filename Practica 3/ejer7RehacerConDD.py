def datos(lista):
    nombre=input("ingresa id del jugador ")
    lista.append(nombre)
    if (nombre!="zzz"):
        nivel=int(input("ingresar el nivel del jugador "))
        pun=int(input("ingresar puntaje maximo "))
        tiem=int(input("ingresar tiempo de juego en horas "))
        lista.append(nivel)
        lista.append(pun)
        lista.append(tiem)

##hacer dic.keyspara la ubicacion
dic={}
lista=[]
datos(lista)
while(lista[0] != "zzz"):
    nom=lista[0]
    lista.remove(nom)
    dic[nom]=lista[:]
    lista.clear()
    datos(lista)
lista.clear()
print(str(dic))
ranking=sorted(dic.values(),key=lambda puntajes:puntajes[1])
lista1=sorted(dic.keys(),key=lambda niv:niv[0])
usuarios=sorted(dic.keys(),key=lambda usuario:usuario[0])
porNivel=sorted(dic.values(),key=lambda nivel:nivel[0])
print("-"*50+"\n"+str(ranking))
print("-"*50+"\n"+str(usuarios))
print("-"*50+"\n"+str(lista1)+"\n"+str(porNivel))
#hacer de cero ya q el ejercicio era un diccionario adentro de otro
#sino dudo q pueda resolverlo de la manera mas optima
