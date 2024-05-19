'''Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''
def verificar_palindromo(palabra):
  palabra = palabra.lower()
  if palabra == palabra[::-1]:
    return True
  else:
    return False
palabra_usuario = input("introduce palabra: ")
if verificar_palindromo(palabra_usuario):
  print("La palabra {} es palíndromo".format(palabra_usuario))
else:
  print("La palabra {} no es palíndromo".format(palabra_usuario))
