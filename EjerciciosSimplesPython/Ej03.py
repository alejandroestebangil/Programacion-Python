#Ejercicio 3:  ¡IMPLEMENTA TU PRIMER JUEGO! Realiza un programa Python que adivine el número. 
# El programa generará un número aleatorio entre 0 y 20 y luego irá pidiendo números al usuario 
# indicando “mayor” o “menor” según sea mayor o menor con respecto al número generado aleatoriamente. 
# El proceso termina cuando el usuario acierta, y deberá mostrar un mensaje de felicitaciones 
# junto al número de intentos que ha necesitado el usuario.

import random

numAleatorio = random.randint(0, 20)
numIntentos = 0
numJugador = 0

while numJugador != numAleatorio:
    numJugador = int(input("Introduce un número: "))
    numIntentos += 1
    if numJugador > numAleatorio:
        print("El número es menor")
    elif numJugador < numAleatorio:
        print("El número es mayor")
    else:
        print("¡Has acertado!")
        print("Has necesitado", numIntentos, "intentos")
