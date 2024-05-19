'''Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos.'''
def intro_minutos():
  while True:
    try:
      min = int(input("Introduce número de minutos:"))
      return min
    except ValueError:
      print("Introduce un número válido")
def convertir_tiempo(minutos):
  horas = minutos // 60
  min_res = minutos % 60
  return horas, min_res
while True:
  m1 = intro_minutos()
  h1, mr1 = convertir_tiempo(m1)
  print("El tiempo introducido son {}horas y {}minutos".format(h1, mr1))