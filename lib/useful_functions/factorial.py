def factorial(n): # Определяем функцию
    if n == 0 or n == 1: # Базовый случай
        return 1
    else: # Рекуррентный случай
        print(n)
        return factorial(n-1) * n # Вызываем эту же функцию, но с меньшим аргументом
    
# ((((2-1)* 2)* 3)* 4) = 24

if __name__ == "__main__":
    print(factorial.__name__)