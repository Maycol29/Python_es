def funcion1(*args):
    cont=0
    for arg in args:
         cont=cont+1
    return cont


def funcion2(**kwargs): 
    for kw in kwargs:  
        print("{} : {}".format(kw,kwargs[kw]))


lista=["tobias","ajenjo",20,"lucio","molina",19,"lean","mika",28]
print(funcion1("tobias","ajenjo",20,"lucio","molina",19,"lean","mika",28))
funcion2(nro1="tobias",nro2="ajenjo",nro3=20,nro4="lucio",nro5="molina",nro6=19,nro7="lean",nro8="mika",nro9=28)
