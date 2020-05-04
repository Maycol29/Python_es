tam= ["Auto", "123", "Viaje", "50", "120"]

nuevo=[]


for i in tam:
    if((i.isdecimal())== True):
        numero=int(i)
        nuevo.extend([numero])
    else:
        pass
nuevo.sort()
print(nuevo)




