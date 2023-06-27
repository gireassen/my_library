def factorial(n): # Определяем функцию
    if n == 0 or n == 1: # Базовый случай
        return 1
    else: # Рекуррентный случай
        return factorial(n-1) * n # Вызываем эту же функцию, но с меньшим аргументом

print(factorial.__name__)