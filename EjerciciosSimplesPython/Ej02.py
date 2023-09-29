#Ejercicio 2:  Escribe un programa Python que pregunte al usuario por 10 números enteros 
# y muestre por pantalla el número total de veces que el usuario ha introducido el 0, 
# el número total de enteros mayores que 0 introducidos y el número total de enteros 
# menores que 0 introducidos.

numZero = 0
numPositivo = 0
numNegativo = 0

for i in range(10):
    x = int(input("Introduce un número entero: "))
    if x == 0:
        numZero += 1
    elif x > 0:
        numPositivo += 1
    else:
        numNegativo += 1
        
print("Has introducido", numZero, "ceros,", numPositivo, "números positivos y", numNegativo, "números negativos")