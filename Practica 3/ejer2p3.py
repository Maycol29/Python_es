frase = '''Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple PALABRATEST13.'''

lista= frase.lower().replace(".","").replace(",","").split(" ")
print(lista)
conjunto=set(lista)
print("-"*25)
print(conjunto)
di={}
for i in conjunto:
    if len(i) not in di.keys():
        di[len(i)]=[] 
    di[len(i)].append(i)
print("\n"+str(di))

