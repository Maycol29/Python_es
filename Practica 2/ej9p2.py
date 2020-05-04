import random
print("Bienvenido al juego de adivinanza ")
num=str(input("ingresa un numero menor a 50  " ))
divino=str(random.randrange(0,50))
while(num!=100):
    if(divino == num):
        print("Es correcto ")
        break
    if divino < num:
        print("el numero es mas bajo  ")        
    if (divino > num):
        print ("el numero es mas alto")
    num = input("ingresa un numero menor a 50, si ingresas 100 es xq te rendiste.  ")    

print(divino)

