#Ejercicio 10:  Implementa un método Python llamado mayorYmenor, el cual recibe como parámetro 
# una tabla de Strings y muestra por pantalla el String con mayor longitud y el String con menor longitud.

tabla = ["hola", "adios", "buenos días", "buenas tardes", "buenas noches"]

def mayorYmenor(tabla):
    mayor = menor = tabla[0]

    for cadena in tabla:
        if len(cadena) > len(mayor):
            mayor = cadena
        elif len(cadena) < len(menor):
            menor = cadena

    print(f"El string con mayor longitud es: '{mayor}' y el string con menor longitud es: '{menor}'")

mayorYmenor(tabla)




