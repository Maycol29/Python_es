texto = input("Ingrese un String : ")
lista = []
texto = texto.lower().replace(" ", "")
print(texto)

indice = 0
for letra in texto:
    n = texto.count(letra)
    cont=0
    divisor=1
    while(divisor <= n) and (cont < 4):
        if n % divisor == 0:
            cont = cont+1
        divisor = divisor +1
    if cont == 2: #AL HACERLO ADENTRO DEL WHILE ME AGREGA DE MAS
       lista.append(letra)
    texto = texto.replace(letra,"") #Como eliminar ocurrencias, preguntar!
    print("La letra " +str(letra) +" aparece " +str(n) +" veces.")
    #print(texto)
print("")
print("Por lo tanto, las letras: " +str(lista) +" son las letras que aparecen un numero primo de veces.")