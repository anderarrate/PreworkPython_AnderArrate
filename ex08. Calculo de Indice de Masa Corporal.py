'''Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.'''
def indice_mc(peso, altura):
  imc = peso / (altura * altura)
  return imc
def intro_peso():
  while True:
    try:
      pes = float(input('Introduce el peso en Kg: '))
      return pes
    except ValueError:
      print("Por favor introduce un número válido")
def intro_altura():
  while True:
    try:
      alt = float(input('Introduce la altura en metros: '))
      return alt
    except ValueError:
      print("Por favor introduce un número válido")
while True:
  p1 = intro_peso()
  a1 = intro_altura()
  resultado = indice_mc(p1, a1)
  print("El IMC es: {}".format(resultado))