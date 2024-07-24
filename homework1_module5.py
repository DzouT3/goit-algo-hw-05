def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        #  Якщо n <= 0, повернути 0
        if n <= 0:
            return 0
        # Якщо n == 1, повернути 1
        elif n == 1:
            return 1
        # Якщо n у cache, повернути cache[n]
        elif n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        return cache[n]

    
    return fibonacci
fib = caching_fibonacci()
print(fib(19))  
print(fib(77))  
print(fib(100))  
print(fib(950))
print(fib(0))
print(fib(1))