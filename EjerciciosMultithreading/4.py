#Exercise 4: Cree un programa que ejecute 10 hilos, cada uno de los 
#cuales sumará 100 números aleatorios entre el 1 y el 1000. Muestre 
# el resultado de cada hilo. Ganará el hilo que consiga el número mas alto

import threading
import random

# Lista compartida para almacenar los resultados de cada hilo
results = []

# Lock para acceso a la lista
results_lock = threading.Lock()

# Función que suma 100 números aleatorios y almacena el resultado en la lista
def sum_numbers(thread_id):
    sum_result = sum(random.randint(1, 1000) for _ in range(100))
    with results_lock:
        results.append((thread_id, sum_result))

# Crear e iniciar los 10 hilos
threads = []
for i in range(1, 11):
    thread = threading.Thread(target=sum_numbers, args=(i,))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()

# Encontrar el hilo ganador con el número más alto
winner_id, winner_sum = max(results, key=lambda x: x[1])

# Imprimir los resultados de cada hilo y el ganador
print("Resultados de cada hilo:")
for thread_id, sum_result in results:
    print(f"Hilo {thread_id}: {sum_result}")

print(f"\nHilo ganador: Hilo {winner_id} con suma {winner_sum}")
