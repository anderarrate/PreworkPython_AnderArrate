'''Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no.'''
def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False
while True:
  año = int(input("Ingrese un año: "))
  if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
  else:
    print(f"El año {año} no es bisiesto.")