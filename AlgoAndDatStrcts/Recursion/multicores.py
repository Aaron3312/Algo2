import multiprocessing

# Usamos un diccionario para almacenar los resultados de Fibonacci ya calculados
fib_cache = {}

def fibonacci_memo(n):
    if n in [0, 1]:
        return n
    if n not in fib_cache:
        fib_cache[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    return fib_cache[n]

def parallel_fibonacci(n):
    num_cores = multiprocessing.cpu_count()
    
    with multiprocessing.Pool(processes=num_cores) as pool:
        results = pool.map(fibonacci_memo, [n])
    
    return results[0]

if __name__ == "__main__":
    print(parallel_fibonacci(950))
