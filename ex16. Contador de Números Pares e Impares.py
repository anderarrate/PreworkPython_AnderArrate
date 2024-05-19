'''Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.'''
def contar_pares_impares(lista_numeros):
  pares = 0
  impares = 0
  for numero in lista_numeros:
    if numero % 2 == 0:
      pares +=1
    else:
      impares +=1
  return pares, impares
entrada = input("Ingrese una lista de números separados por espacios: ")
lista_numeros = list(map(int, entrada.split()))
pares, impares = contar_pares_impares(lista_numeros)
print(f"En la lista ingresada hay {pares} números pares y {impares} números impares.")
