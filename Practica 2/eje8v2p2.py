palabra=input("ingrese una palabra ")
print(palabra)
lista=[]
for letra in palabra:
    n=palabra.count(letra)
    cont=0
    div=1
    while (div<=n) and (cont<4):
        if n % div == 0:
            cont=cont+1
        div=div+1
    if cont == 2:
      lista.append(letra)
    palabra=palabra.replace(letra,"") 
    print("La letra " +str(letra) +" aparece " +str(n) +" veces.")
print("Por lo tanto, las letras: " +str(lista) +" son las letras que aparecen un numero primo de veces.")
  