'''Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.'''

def contar_vocales(palabra):
  palabra = palabra.lower()
  contador_a = contador_e = contador_i = contador_o = contador_u = 0
  for letra in palabra:
    if letra == 'a':
      contador_a +=1
    elif letra == 'e':
      contador_e +=1
    elif letra == 'i':
      contador_i +=1
    elif letra == 'o':
      contador_o +=1
    elif letra =='u':
      contador_u +=1
  total_vocales = contador_a + contador_e + contador_i + contador_o + contador_u
  return total_vocales

palabra_usuario = input('Introduce palabra: ')
numero_vocales = contar_vocales(palabra_usuario)
print("El número de vocales de la palabra {} es: {}".format(palabra_usuario,numero_vocales))


