# Ejercicio 3
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
# el número de años, y muestre por pantalla el capital obtenido en la inversión.
# cantidad por (interés dividido 100 más 1) elevado años

import os

os.system("clear")

cantidadInvertir = int(input("Ingrese la cantidad a invertir:"))
interesAnual = float(input("Ingrese el interes anual:"))
numeroAnnos = int(input("Ingrese el número de años:"))

capitalObtenido = (cantidadInvertir * (interesAnual / 100 + 1)) ** numeroAnnos

mensaje = f"""
Para una inversión de {cantidadInvertir} con un interes anual de {interesAnual} y por un total de años de {numeroAnnos}
El capital obtenido es de {capitalObtenido}
"""

print(mensaje)