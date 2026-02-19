def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def add(*numbers):
    return sum(numbers)

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b