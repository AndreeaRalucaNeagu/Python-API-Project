operations = {}

def register_operation(name, func):
    operations[name] = func

# înregistrăm operațiile disponibile
register_operation("pow", lambda x: x**2)

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

register_operation("factorial", factorial)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

register_operation("fibonacci", fibonacci)
