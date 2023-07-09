def quicksort(array: list) -> list:
    '''
    быстрая сортировка
    '''
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot] # подмассив ввсех эл-ов ниже опроного(pivot)
        greater = [i for i in array[1:] if i > pivot] # подмассив ввсех эл-ов выше опроного(pivot)
        return quicksort(less) + [pivot] + quicksort(greater)
    
asd = quicksort([123, 12, 541, 13, 151, 11, 1, 99, 101, 31, 44])
print(asd)