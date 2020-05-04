imagenes=['im1','im2','im3'] 
lista=imagenes[:]
print(len(imagenes))

for i in range(0,len(imagenes)):
    cordenadax=input("ingrese cordenada x ")
    cordenaday=input("ingrese cordenada y ")

    while cordenadax==cordenaday:
         cordenadax=input("ingrese cordenada x denuevo ")

    lista[i]=lista[i]+" "+cordenadax+" "+cordenaday
    lista[i]=lista[i].split(" ")
    

print(lista)


