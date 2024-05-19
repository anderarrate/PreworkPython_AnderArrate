'''Escribe un programa que determine si un número ingresado por el usuario es primo o no.'''
def intro_num():
  while True:
    try:
      num = int(input("Introduce un número entero: "))
      return num
    except ValueError:
      print("Introduce un número válido")
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
while True:
   n1 = intro_num()
   if es_primo(n1):
      print("El número es primo")
   else:
      print("El número no es primo")




