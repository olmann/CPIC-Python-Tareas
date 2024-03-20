# Ejercicio 6
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
# un descuento del 60%. Escribir un programa que comience leyendo el número de
# barras vendidas que no son del día. Después el programa debe mostrar el precio
# habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste
# final total.

import os

os.system("clear")

precioPan = 3.49
descuentoPan = 0.60
totalBarrasVendidas = int(input("Cuántas barras de pan fueron vendidas y no son frescas? "))
montoTotal = (precioPan - (precioPan * descuentoPan) * totalBarrasVendidas)

mensaje = f"""
El precio para el pan fresco es de {precioPan}
El descuento aplicado a cada barra por no ser del día es de {descuentoPan*100}%
El costo total por la compra de pan que no es el día es de {montoTotal:.2f}
"""
print(mensaje)