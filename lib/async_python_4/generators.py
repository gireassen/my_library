                                                # Основы асинхронности в Python #4: Генераторы и событийный цикл Round Robin
from time import time

def gen(s):                                                         # простой генератор
    for i in s:
        yield i

g = gen('ayrat')                                                    # функция-генератор отдаёт не только своё значение, которое он сгенерировал, но и контроль выполнения программы
                                                                    # и отдаёт его в то место, где была вызвана функция next
                                                                    # next(g)

def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int((time() * 1000))                                    #время в секундах
        yield pattern.format(str(t))

x = gen_filename() 
# функция next сдвигает выполнение программы до след-го yield

def gen_2():
    yield 1
    yield 2
    yield 3

if __name__ =="__main__":
    print()