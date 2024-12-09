def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    return base ** exponent

def factorial(n):
    if n < 0:
        raise ValueError("Cannot calculate factorial of a negative number")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result