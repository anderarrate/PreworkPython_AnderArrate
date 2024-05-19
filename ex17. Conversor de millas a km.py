'''Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.'''
def intro_millas ():
  while True:
    try:
      mil = float(input("Introduce distancia en millas: "))
      return mil
    except ValueError:
      print ("Introduce un número válido")
def conv_milla_a_km (millas):
  kms = millas * 1.60934
  return kms
while True:
  m1 = intro_millas()
  resultado = conv_milla_a_km (m1)
  print ("La distancia equivale a {}kms".format(resultado))