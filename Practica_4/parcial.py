from functools import reduce

def suma(n):
    lis=[]
    n=int(n)
    while(n!=0):
        res=int(n % 10)
        n=int(n/10)
        lis.append(res)
    total=reduce(lambda x,y:x+y,lis)
    return total

def esColega(n):
    n=int(n)
    lis=[]
    while(n!=0):
        res=int(n % 10)
        n=int(n/10)
        lis.append(res)
    for x in lis:
        aux=lis.count(x)
    if(aux>=2):
         return True
    return False


#def esColega(n):
 #   n = str(n)
  #  for digito in n:
   #     aux = n.count(digito)
    #    if(aux>=2):
     #       return True
      #  else:
       #     return False

def esPrimo(num):
    num=int(num)
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def esCapicua(n):
    n = str(n)
    n1 = n[::-1]
    if(n==n1):
        return True
    else:
        return False




def gen_informacion(info):
    dic={}
    lis=info.split(" ")
    for i in lis:
       if(esColega(i)==True):
            dic[i]={}
            dic[i]["esCapicua"]=esCapicua(i)
            total=suma(i)
            dic[i]["suma_es_primo"]=esPrimo(total)
    return dic
            




info=str("11 2 33 4 5 111")
n=32 
print(esColega(n))
print(esPrimo(13))
print(esCapicua(2332))
print(gen_informacion(info))