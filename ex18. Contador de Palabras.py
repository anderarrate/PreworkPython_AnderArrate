'''Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario'''
def contar_palabras (oracion):
  palabras = oracion.split()
  return len(palabras)
while True:
  oracion = input ("Introduce una oración: ")
  resultado = contar_palabras (oracion)
  print ("En la oración hay {} palabras".format(resultado))
    