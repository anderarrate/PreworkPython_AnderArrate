'''Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.'''
def obtener_edad():
    while True:
        try:
          edad = int(input('Introduce la edad:'))
          return edad
        except ValueError:
            print('Por favor inserte un número válido')

def menu():
    print('1. Verificación de edad')
    print('2.Salir')

while True:
    menu()
    opcion = input('Selecciona una opción (1 o 2)')
    if opcion == "1":
        edad = obtener_edad()
        if edad < 18:
            print('Lo siento, no puedes acceder hasta que no cumplas 18 años')
            break
        else:
              print('Gracias por confirmar que eres mayor de edad. ¡Bienvenido!')
              break
    elif opcion == "2":
        print('¡Muhcas gracias y hasta la próxima!')
        break
    else:
        print('Opción no válida. Por favor elige entre 1 y 2')