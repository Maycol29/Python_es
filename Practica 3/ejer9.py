def imprimir(*args):
    cont=1
    for i in args:
        print(str(cont)+": "+str(i))
        cont=cont+1

lista=["tobias","lucio","leandro"]
imprimir("tobias","ajenjo","lean","lucio")