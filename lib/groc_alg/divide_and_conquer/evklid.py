                                        # Алгоритм Евклида - нахождение наибольшего общего делителя

def evklid_div(a: int, b: int):
    '''
    Алгоритм нахождения НОД делением.\n
    ------
    1) Большее число делим на меньшее.\n
    2) Если делится без остатка, то меньшее число и есть НОД (следует выйти из цикла).\n
    3) Если есть остаток, то большее число заменяем на остаток от деления.\n
    4) Переходим к пункту 1.\n
    ''' 
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    
    return a + b

def evklid_deduc(a: int, b: int):
    '''
    Алгоритм нахождения НОД вычитанием\n
    ---
    1) Из большего числа вычитаем меньшее.\n
    2) Если получается 0, значит, числа равны друг другу и являются НОД (следует выйти из цикла).\n
    3) Если результат вычитания не равен 0, то большее число заменяем на результат вычитания.\n
    4) Переходим к пункту 1.\n
    '''
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    return a

if __name__ == "__main__":
    asd = evklid_deduc(1680, 640)
    print(asd)