# Ejercicio 5
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
# interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
# año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que
# comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
# introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la
# cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a
# dos decimales.

import os

os.system("clear")

interesAnual = 0.04

dineroDepositado = float(input("Ingrese el dinero depositado en la cuenta: "))

primerAnno = round(dineroDepositado * (1 + interesAnual),2)
segundoAnno = round(primerAnno * (1 + interesAnual),2)
tercerAnno = round(segundoAnno * (1 + interesAnual),2)


resultado = f"""
Para un total depositado de {dineroDepositado}
Con un interes de {interesAnual}
Ganancias en el primer año {primerAnno}
Ganancias para el segundo año {segundoAnno}
Ganancias para el tercer año {tercerAnno}
"""

print(resultado)