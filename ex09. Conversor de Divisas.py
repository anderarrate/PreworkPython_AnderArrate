'''Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.'''
def conv_dol_a_eur(dolares):
  euros = dolares * 0.85
  return euros
def intro_dol():
  while True:
    try:
      dol = float(input("Introduce valor en dólares: "))
      return dol
    except ValueError:
      print("Introduce un número válido")
while True:
  d1 = intro_dol()
  resultado = conv_dol_a_eur(d1)
  print("El valor de {}dólares equivale a {}euros".format(d1,resultado))