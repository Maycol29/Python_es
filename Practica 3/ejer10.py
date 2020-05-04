from functools import reduce
def funcion(operacion,*args,**kwargs):
    if (operacion=="+"):  
        for k in kwargs.values():  
             print(str(k)+": "+str((reduce(lambda x,y:x+y,args))))
    if (operacion=="*"):    
        for k in kwargs.values():  
            print(k+": "+str((reduce(lambda x,y:x*y,args))))


operacion=input("ingresar la operacion a usar (* o +) ")
print ("The sum of the list elements is : ",end="") 
funcion(operacion,1,2,3,4,5,6,7,8,9,nombre1="emilio",nombre2="tobias") 