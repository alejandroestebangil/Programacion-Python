#Ejercicio 9:  Implementa un programa Python con un método llamado 
# indexContains(String[] tabla, String cadena) que devuelva el índice de la tabla cuyo valor 
# es igual al valor de “cadena”. En caso de no haber ningún valor igual, devuelve -1

tabla = ["hola", "adios", "buenos días", "buenas tardes", "buenas noches"]

def indexContains(tabla, cadena):
    for i in range(len(tabla)):
        if tabla[i] == cadena:
            return i
    return -1

cadena = input("Introduce una cadena de caracteres: ")

print("El índice de la tabla cuyo valor es igual al valor de “cadena” es", indexContains(tabla, cadena))
