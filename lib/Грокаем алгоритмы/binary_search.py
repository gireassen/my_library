import time
import bisect

def time_of_function(function_to_decorate):
    '''
    время выполнения функции
    '''
    def wrapper(arg1, arg2, arg3):
        start = time.time()
        result = function_to_decorate(arg1, arg2, arg3)
        end = time.time() - start
        print(f'{function_to_decorate.__name__}: O(n) = {end}')
        return result
    return wrapper

@time_of_function
def binary_search(end: int, step: int, item: int) -> int:
    '''
    бинарный поиск\n
    log2n
    \n
    print(binary_search(40000, 3, 198))
    -------------
    '''
    # my_list: list = []
    # my_list = [i for i in range(0, end, step)]
    # low: int = 0                            #нижняя граница
    # high: int = len(my_list)-1              #верхняя граница

    my_list = list(range(0, end, step))
    low, high = 0, len(my_list)-1
    

    while  low <= high:                     #пока часть не сократится до 1го эл-та
        mid = (low + high) /2               #проверяем средний эл-т
        mid = int(mid)
        guess = my_list[mid]               
        if guess == item:                   #значение найдено
            return mid
        if guess > item:                    #значение большое
            high = mid - 1
        else:                               #значение малое
            low = mid + 1
    return None                             #значение не существует

@time_of_function
def binary_search_2(end: int, step: int, item: int) -> int:
    my_list = list(range(0, end, step))
    index = bisect.bisect_left(my_list, item)
    if index != len(my_list) and my_list[index] == item:
        return index
    return -1

if __name__ == "__main__":
    print(binary_search(400000, 1, 19800))