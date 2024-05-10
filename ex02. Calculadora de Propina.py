'''Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.'''
def introducir_menus():
  while True:
    try:
      menus = int(input('Introduce el número de menús:'))
      return menus
    except ValueError:
      print('Introduce un número válido')
menus = introducir_menus()
Precio_Menu = 10
IVA = 0.21
Propina = 0.15
Total = menus * Precio_Menu * (1 + IVA) * (1 + Propina)
print(f'El total de la factura es: {Total}euros')
