'''Escribe un programa que calcule la suma de todos los números pares del 1 al 100'''
def suma_pares():
  num = suma = 0
  while num <= 100:
    if num % 2 == 0:
      suma = num + suma
      num +=1
    else:
      num +=1
  return suma
suma_pares_1_a_100 = suma_pares()
print ("La suma de los pares del 1 al 100 es: {}".format(suma_pares_1_a_100))
