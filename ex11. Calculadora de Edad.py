'''Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual'''
def intro_anyo_nacimiento():
  while True:
    try:
      nac = int(input("Introduce año de nacimiento: "))
      return nac
    except ValueError:
      print("Introduce un número válido")
def calcular_edad(anyo):
  import datetime
  fecha_actual = datetime.datetime.now()
  anyo_actual = fecha_actual.year
  edad = anyo_actual - anyo
  return edad
while True:
  n1 = intro_anyo_nacimiento()
  resultado = calcular_edad(n1)
  print("La edad es: {}".format(resultado))
