'''Exercise 2: Using the multithreading module, write a python program as follows:
● Create a pool of threads to run concurrent tasks.
● The pool size should be 3.
● Create and fill an array of 100 random integer numbers.
● Run all 3 threads to parse the vector data. One of them must show the mean, another
the maximum and minimum value, and the last one the standard deviation. Note that
although these processes share the vector, they only do so for reading. None of them
must modify any value of the vector.
'''
import threading
import random
import math

# Shared array of 100 random integers
shared_array = [random.randint(1, 100) for _ in range(100)]

# Variables to store results
mean_result = 0
min_max_result = (float('inf'), float('-inf'))
std_dev_result = 0

# Locks to ensure thread-safe access to shared variables
mean_lock = threading.Lock()
min_max_lock = threading.Lock()
std_dev_lock = threading.Lock()

def calculate_mean():
    global mean_result
    with mean_lock:
        mean_result = sum(shared_array) / len(shared_array)

def calculate_min_max():
    global min_max_result
    with min_max_lock:
        min_max_result = (min(shared_array), max(shared_array))

def calculate_std_dev():
    global std_dev_result
    with std_dev_lock:
        mean = sum(shared_array) / len(shared_array)
        squared_diff = sum((x - mean) ** 2 for x in shared_array)
        std_dev_result = math.sqrt(squared_diff / len(shared_array))

def main():
    # Create threads
    mean_thread = threading.Thread(target=calculate_mean)
    min_max_thread = threading.Thread(target=calculate_min_max)
    std_dev_thread = threading.Thread(target=calculate_std_dev)

    # Start threads
    mean_thread.start()
    min_max_thread.start()
    std_dev_thread.start()

    # Wait for all threads to finish
    mean_thread.join()
    min_max_thread.join()
    std_dev_thread.join()

    # Print results
    print("Mean:", mean_result)
    print("Min and Max:", min_max_result)
    print("Standard Deviation:", std_dev_result)

if __name__ == "__main__":
    main()
