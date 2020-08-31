def calcular_caracteres_unicos(pal):
    lista=[]
    for i in pal:
        aux=pal.count(i)
        if(aux==1):
            lista.append(i)
    return lista

def gen_informacion(lis):
    lista_de_tuplas=[]
    for i in lis:
        aux=calcular_caracteres_unicos(i)
        tupla=(len(aux),i.upper())
        lista_de_tuplas.append(tupla)
    return lista_de_tuplas


def ordenar_informacion(lista,criterio):
    criterio.lower()
    listaNueva=[]
    listaFinal=[]
    if(criterio=="cantidad"):
        lista.sort()
    #elif (criterio=="palabra"):
      #  for i in lista:
     #       listaNueva.append(i[1])        
    #listaNueva.sort()
   # print(listaNueva)

    return lista


def calcular_max_palabra(lista):
    tupla=()
    max=0
    nomMax=""
    for i in lista:
        if(max<i[0]):
            max=i[0]
            nomMax=i[1]
    tupla=max,nomMax
    return tupla

def calcular_min_palabra(lista):
    tupla=()
    min=99
    nomMin=""
    for i in lista:
        if(min>i[0]):
            min=i[0]
            nomMin=i[1]
    tupla=min,nomMin
    return tupla

print(calcular_caracteres_unicos("casa"))

lis=["holaa","zasa","hogar"]

lista=gen_informacion(lis)
print(lista)
print("maximo"+str(calcular_max_palabra(lista)))
print("min"+str(calcular_min_palabra(lista)))
criterio="palabra"
print(ordenar_informacion(lista,criterio))
