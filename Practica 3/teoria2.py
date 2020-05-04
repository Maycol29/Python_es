def codifico(cadena):
        cadena_secreta = map(lambda c: chr(ord(c)+1), cadena)
        return "".join(cadena_secreta)
def decodifico(cadena):
        cadena_original = map(lambda c: chr(ord(c)-1), cadena)
        return "".join(cadena_original)


cadena = input("Ingresá una cadena: ")
secreto = codifico(cadena)
print(secreto)
print("-" * 30)
print(decodifico(secreto))
  