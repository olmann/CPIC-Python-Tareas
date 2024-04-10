import os

os.system("clear")

def ejercicio01():
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
    texto = "Ingrese un texto: "    
    while True:
        cadena = input(texto)
        if len(cadena) > 0:
            break;
    for i in range(0,10):
        print(f"Repetición {i + 1}, palabra {cadena}")
    return
def ejercicio02():
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
    while True:
        edad = int(input("Ingrese su edad: "))
        if edad > 0:
            break;
    for i in range(0,edad):
        print(f"Edades cumplidas {i + 1}")

def ejercicio03():
#scribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares 
#desde 1 hasta ese número separados por comas.
    while True:
        numero = int(input("Ingrese el número: "))
        if numero > 0:
            break;
    for i in range(0,numero):
        contador = i + 1
        if contador % 2 != 0:
            print(f"{contador}")

def ejercicio04():
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número 
#hasta cero separados por comas
    valor = ""
    while True:
        numero = int(input("Ingrese el número: "))
        if numero > 0:
            break;
    for i in range(0,numero):
        contador = i + 1
        valor = str(contador) + ", " + valor
    print(valor)

def ejercicio05():
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
    while True:
        numero = int(input("Ingrese el número: "))
        if numero > 0:
            break;
    for i in range(0,numero):
        print("*" * (i + 1))
def ejercicio06():
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
    for i in range(1,11):
        print(f"{i} por 10 es {i*10}")

def ejercicio07():
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la 
#contraseña hasta que introduzca la contraseña correcta.
    clave = "PYTHON"
    while True:
        clave_ingresada = input("Ingrese su clave: ")
        if len(clave_ingresada) > 0 and clave.upper() == clave_ingresada.upper():
            print("Contraseña ingresada correctamente!!!")
            break;
        else:
            print("Contraseña Incorrectamente!!!")
    
def es_primo(pNumero):
    contador = 0;
    for i in range(1,pNumero):
        if pNumero % i == 0:
            contador += 1
    if contador == 1:
        return True
    else:
        return False

def ejercicio08():
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
    while True:
        numero = int(input("Ingrese el número: "))
        if numero > 0:
            break;

    if es_primo(numero):
        print("Es primo!!!")
    else:
        print("No es primo!!!")

def ejercicio09():
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra 
#introducida empezando por la última
    while True:
        palabra = input("Ingrese la palabra: ")
        if len(palabra) > 0:
            break;
    largo = len(palabra)
    palabra_invertida = palabra[::-1]
    for i in range(0,largo):
        print(palabra_invertida[i])

def ejercicio10():
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que 
#aparece la letra en la frase.
    totalOcurrencias = 0
    while True:
        frase = input("Ingrese una frase de texto: ")
        if len(frase) != 0:
            break;
    while True:
        letra = input("Ingrese una letra para contabilizar: ")
        if len(letra) != 0:
            break;
    largo = len(frase)
    for i in range(largo):
        if frase[i].upper() == letra.upper():
            totalOcurrencias += 1

    print(f"Para la frase {frase}, la letra {letra} aparece un total de {totalOcurrencias}")

def ejercicio11():
#Escribir un programa que muestre loop de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
    while True:
        frase = input("Ingrese una frase de texto: ")
        if len(frase) != 0 and frase.upper() == "SALIR":
            print("Fin del programa!!!")
            break;
        else:
            print(frase)

ejercicio01()
ejercicio02()
ejercicio03()
ejercicio04()
ejercicio05()
ejercicio06()
ejercicio07()
ejercicio08()
ejercicio09()
ejercicio10()
ejercicio11()