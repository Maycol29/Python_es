
frase = input('ingrese una frase')
palabra=input('ingrese una palabra')
lista=frase.split(' ')
print(lista)
palabras_buscadas = [s for s in lista if palabra in s]
print(len(palabras_buscadas))
print(' '.join(lista))