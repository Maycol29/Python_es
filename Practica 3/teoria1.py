print("\n Hola {0}!! \n\nHoy es  {dia} de {mes}".format("chicos", dia=14, mes="abril"))
contactos = {"Juan":12345, "Pedro":54321, "Maria":12121212}
for nom, celu in contactos.items():
        print("{0:15}==> {1:10d}".format(nom, celu))