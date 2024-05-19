'''Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).'''
def determinar_dia_semana(numero):
  dias_semana = {1: "Lunes",2: "Martes",3: "Miércoles",4: "Jueves",5: "Viernes",6: "Sábado",7: "Domingo"}
  if numero in dias_semana:
    return dias_semana[numero]
  else:
    return "Número no válido. Por favor introduce un número del 1 al 7"
while True:
  try:
    num = int(input("Introduce un número del 1 al 7\n"))
    print("El día correspondiente al número introducido es: ", determinar_dia_semana(num))
  except ValueError:
    print("Intoruduce un número válido")
