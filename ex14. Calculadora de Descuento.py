'''Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%'''
def intro_precio():
  while True:
    try:
      pre = float(input("Introduce precio: "))
      return pre
    except ValueError:
      print("Introduce un número válido")
def calcular_descuento(precio):
  nuevo_precio = (1 - 0.2) * precio
  return nuevo_precio
while True:
  p1 = intro_precio()
  resultado = calcular_descuento(p1)
  print("El nuevo precio con descuento del 20% es {}".format(resultado))