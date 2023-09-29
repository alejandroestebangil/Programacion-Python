#Ejercicio 5:  Implementa un programa Python que solicite al usuario una cadena de caracteres (String) 
# y muestre por pantalla el número de veces que aparece la sub-cadena “aaa” dentro de dicho String.

cadena = input("Introduce una cadena de caracteres: ")
print("La subcadena 'aaa' aparece", cadena.count("aaa"), "veces en la cadena introducida")
