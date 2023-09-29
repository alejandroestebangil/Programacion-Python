#Ejercicio 8:  Implementa un programa Python con un método llamado sum(int [] tabla) 
# que muestre por pantalla el resultado de sumar todos los elementos de la tabla pasada como parámetro.

tabla = [1, 2, 3, 4, 5]

def sum(tabla):
    suma = 0
    for i in tabla:
        suma += i
    return suma

print("La suma de los elementos de la tabla es:", sum(tabla))

