frase = "anita lava la tina"

frase = frase.upper().replace(' ','')

esPalindromo = "NO"
if frase == frase[::-1]:
    esPalindromo = " Sí "

print(f"La cadena {frase} {esPalindromo} es un palindromo!")
