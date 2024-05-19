'''Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo.'''
def intro_longitud():
  while True:
    try:
      lon = float(input("Introduce longitud de rectángulo en metros: "))
      return lon
    except ValueError:
      print("Introduce un número válido")
def intro_ancho():
  while True:
    try:
      anc = float(input("Introduce ancho de rectángulo en metros: "))
      return anc
    except ValueError:
      print("Introduce un número válido")
def calcular_area(longitud, ancho):
  area = longitud * ancho
  return area
while True:
  l1 = intro_longitud()
  a1 = intro_ancho()
  resultado = calcular_area(l1, a1)
  print("El área del rectángulo es {} metros cuadrados".format(resultado))