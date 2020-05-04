import random
preguntas= [["el 2do nombre de tobi es nahuel?","no"],["fiore es igual al gato?","si"],["keila vive en fincas 2?","si"],["luchi tiene dengue? ","si"]]

for i in preguntas:
    print(preguntas[0])
    print(preguntas[1])
    print(preguntas[2])
    print(preguntas[3])
lista= range(len(preguntas))
print(list(lista))
puntaje=0
for i in lista:
    num = random.randrange(0,len(preguntas))
    print(preguntas[num][0])
    respuesta=input("ingrese la respuesta  ")
    if ((respuesta.lower())==preguntas[num][1]):
        puntaje=puntaje+1
        print("correcto")
    else:
        print("incorrecto")
    del preguntas[num]
print("contestaste " + str(puntaje) + " respuestas correctamente ")        
