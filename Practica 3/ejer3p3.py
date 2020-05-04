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
print("mismo ejer c"+"\n"+ "-"*50)
print( "-" *25 + "Jugadores" + "-" * 26 + "\n" + str(dic.keys()).replace("dict_keys","")+"\n"+"-"*60)


print("ejer b"+"\n"+ "-"*50)
print("elegir uno de los usuarios de arriba")
nom=str(input("ingresar el nombre  "))
print(dic[nom])


print("mismo d"+"\n"+ "-"*50)
max=0
for nom in dic:
    if(dic[nom][1]>max):
        max =dic[nom][1]
        usu=nom
print("el q tuvo mas puntaje es "+str(usu)+" con "+str(max)+" puntos")


print("ejer d"+"\n"+ "-"*50)
print("Un jugador a batido el record y logro un puntaje de 9999")
vicio=str(input("el jugador q batio el record fue  "))
dic[vicio][1]=9999
print(dic[vicio])

print("lambda")
ranking= sorted(dic.items(), key=lambda usuario: usuario[1][1],reverse=True)[:10]
print("-"*50 +"\n"+"este es el ranking ")
i=1
print(ranking)  ##con esto ya me tiraria el ranking con los datos invertidos
                ##aun asi de la otra forma de la primera me funcionaba igual
for nom in ranking:
    print(str(i)+": "+nom+" a conseguido "+str(dic[nom][1]) +" pts  "+"\n"+ "-"*50)
    i=i+1