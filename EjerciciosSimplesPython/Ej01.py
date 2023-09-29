# Ejercicio 1: Implementa un programa Python que PREGUNTE al usuario por dos números enteros (x, y) 
# y muestre por pantalla la suma, resta, multiplicación, división y resto de ambos, con este formato:
#           x + y = …
#           x – y = …
#           x * y = …
#           x / y = …
#           x % y = …

x = int(input("Introduce un número entero: "))
y = int(input("Introduce otro número entero: "))

print(x, "+", y, "=", x+y)
print(x, "-", y, "=", x-y)
print(x, "*", y, "=", x*y)

if y == 0:
    print("No se puede dividir por 0")
else:
    print(x, "/", y, "=", x/y)
    print(x, "%", y, "=", x%y)


