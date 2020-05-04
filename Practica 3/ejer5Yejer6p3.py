import random
colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
dic={}
#for i in range(len(colores)):
   # colo = colores[random.randrange(len(colores))]
    #dic[coordenadas[i]]=colo
print(dic)
print("parte 2")
lista=colores[:]
print(lista)
for i in range(len(colores)):
    colo = lista[random.randrange(len(lista))]
    dic[coordenadas[i]]=colo
    lista.remove(colo)
print(dic)
print(colores)
def imprimoA():
    num1=random.randrange(10)
    num2=random.randrange(10)
    result=num1+num2
    res=int(input("cuanto es "+str(num1)+" + "+str(num2)+"?"+"\n"))
    if(res==result):
        print("correcto")
    else:
        print("incorrecto")
def imprimoB():
    palabras = [('grave',['molesto']), ('aguda',['ratón']), ('esdrujula',['murciélago'])] 
    pos=random.randrange(len(palabras))
    print(str(palabras[pos][1])+" de q tipo es?")
    res=input()
    if(res==palabras[pos][0]):
        print("correcto")
    else:
        print("incorrecto")

funciones={'azul':imprimoA,'amarillo':imprimoB,'rojo':imprimoA,'blanco':imprimoB,'negro':imprimoA}

coor = input('decime una coordenada separada por comas (por ej 5,6): ')
x, y = coor.split(',')
funciones[dic[(int(x),int(y))]]()