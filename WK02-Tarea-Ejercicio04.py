# Ejercicio 4
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele
# hacer venta por correo y la empresa de logística les cobra por peso de cada paquete
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada
# paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un
# programa que lea el número de payasos y muñecas vendidos en el último pedido y
# calcule el peso total del paquete que será enviado.

import os

os.system("clear")

pesoPayaso = 112
pesoMunneca = 75

numeroPayasos = int(input("Digite el total de payasos por enviar:"))
numeroMunnecas = int(input("Digite el total de muñecas por enviar:"))

totalPeso = (pesoPayaso * numeroPayasos) + (pesoMunneca * numeroMunnecas)

mensaje = f"Para un total de {numeroPayasos} y de {numeroMunnecas} el peso total es de {totalPeso}"

print(mensaje)