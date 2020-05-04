palabra=input("ingrese una palabra ")
print(palabra)
lista=[]
num=0
indice=0
for letra in palabra:
    n=palabra.count(letra)
    cont=0
    div=1
    while(div<=n)and(cont<4):
        if n % div == 0:
            cont=cont+1
            div=div+1
        palabra=palabra.replace(letra,"")
    if cont==2:
      lista.append(letra) 
    print("La letra " +str(letra) +" aparece " +str(cont) +" veces.")
print("Por lo tanto, las letras: " +str(lista) +" son las letras que aparecen un numero primo de veces.")
  