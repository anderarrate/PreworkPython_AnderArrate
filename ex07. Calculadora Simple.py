'''Crea un programa que realice operaciones aritméticas simples (suma, resta,multiplicación, división) según la elección del usuario.'''
def menu():
  print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n")
def suma(num1, num2):
  sum = num1 + num2
  return sum
def resta(num1, num2):
  res = num1 - num2
  return res
def multiplicacion(num1, num2):
  mul = num1 * num2
  return mul
def division(num1, num2):
  div = num1 / num2
  return div
def intro_num1():
  while True:
    try:
      numero1 = int(input('Introduce primer número: '))
      return numero1
    except ValueError:
      print("Por favor introduce un número válido")
def intro_num2():
  while True:
    try:
      numero2 = int(input('Introduce segundo número: '))
      return numero2
    except ValueError:
      print("Por favor introduce un número válido")
while True:
  n1 = intro_num1()
  n2 = intro_num2()
  menu()
  opcion = input("Selecciona una opción (1,2,3 o 4)")
  if opcion == "1":
    resultado = suma(n1, n2)
    print("El resultado de la suma es: {}".format(resultado))
  elif opcion == "2":
    resultado = resta(n1, n2)
    print("El resultado de la resta es: {}".format(resultado))
  elif opcion == "3":
    resultado = multiplicacion(n1, n2)
    print("El resultado de la multiplicación es: {}".format(resultado))
  elif opcion == "4":
    resultado = division(n1, n2)
    print("El resultado de la división es: {}".format(resultado))
  else:
    print("Opción no válida. Elige 1,2,3 o 4")
