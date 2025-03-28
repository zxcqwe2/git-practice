def add_numbers(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract_numbers(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply_numbers(a, b):
    """Умножение двух чисел"""
    return a * b

def divide_numbers(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Калькулятор запущен!")