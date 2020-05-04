tam = ['im1 4,14', 'im2 33,15', 'im3 6,34', 'im4 410,134'] 
print('ingresar un numero')

num= input()
high=[]
low=[]

for i in tam:
   #separamos el primer string 
   name, space, tuplaStr = i.partition(" ")
   x = int(tuplaStr.split(",")[0])
   tupla = (int(tuplaStr.split(",")[0])),(int(tuplaStr.split(",")[1]))
   if x > int(num):
      high.extend([name,tupla])
   else:
      low.extend([name,tupla])
      
print(high)
print (low)