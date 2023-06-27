# -- coding: utf-8 --

import bisect
import sys
sys.path.insert(1, 'lib\\useful_functions\\')
import time_of_func

@time_of_func.timeoffunction
def binary_search(end: int, step: int, item: int) -> int:
    '''
    бинарный поиск\n
    log2n
    \n
    print(binary_search(40000, 3, 198))
    -------------
    '''
    my_list = list(range(0, end, step))
    low, high = 0, len(my_list)-1           #нижняя и верхняя граница
    

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

@time_of_func.timeoffunction
def binary_search_2(end: int, step: int, item: int) -> int:
    my_list = list(range(0, end, step))
    index = bisect.bisect_left(my_list, item)
    if index != len(my_list) and my_list[index] == item:
        return index
    return -1

if __name__ == "__main__":
    print(binary_search(400000, 3, 19800))