# Ejercicio 2
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
# la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números
# introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera
# respectivamente.

import os

os.system('clear')


n = int(input("Digite el primer número: "))
m = int(input("Digite el segundo número: "))

c = n // m
r = n % m
resultado = f"""
Cociente: {c} y un Residuo: {r}
"""

print(resultado)

