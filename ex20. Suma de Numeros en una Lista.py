'''Crea un programa que sume todos los números en una lista ingresada por el usuario'''
def suma_numeros(lista_numeros):
  suma = 0
  for numero in lista_numeros:
      suma = suma + numero
  return suma
while True:
  entrada = input("Ingrese una lista de números separados por espacios: ")
  lista_numeros = list(map(int, entrada.split()))
  resultado = suma_numeros(lista_numeros)
  print("La suma de los números de la lista es {}".format(resultado))