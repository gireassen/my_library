# -- coding: utf-8 --

import functools
import timeit

def timeoffunction(functiontodecorate):
    """
    Декоратор для измерения времени выполнения функции
    """
    @functools.wraps(functiontodecorate)
    def wrapper(*args, **kwargs):
        result = None
        start_time = timeit.default_timer()
        try:
            result = functiontodecorate(*args, **kwargs)
        finally:
            endtime = timeit.default_timer()
            elapsedtime = endtime - start_time
            print(f"{functiontodecorate.__name__}: O(n) = {elapsedtime}")
        return result

    return wrapper

if __name__ == "__main__":
    print(timeoffunction.__name__)

#решение проблемы с русской локализацией можно решить, добавив строку "# -- coding: utf-8 --" в начало скрипта, 
# чтобы Python мог корректно обрабатывать символы кириллицы

#'functools.wraps()', позволяет копировать метаданные из оригинальной функции в новую функцию-обертку. 
# Это позволяет сохранить название исходной функции, что полезно при выводе сообщений.

#https://docs-python.ru/tutorial/dekoratory-python/dekoratory-argumentami/#class