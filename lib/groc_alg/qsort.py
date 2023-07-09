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

def quicksort_mid(array: list) -> list:
    '''
    быстрая сортировка
    '''
    if len(array) < 2:
        return array
    else:
        pivot = array[(len(array)//2)-1]
        array.remove(pivot)
        less = [i for i in array if i < pivot] # подмассив ввсех эл-ов ниже опроного(pivot)
        greater = [i for i in array if i > pivot] # подмассив ввсех эл-ов выше опроного(pivot)
        return quicksort_mid(less) + [pivot] + quicksort_mid(greater)
   
asd2 = quicksort_mid([123, 12, 541, 13, 151, 11, 1, 99, 101, 31, 44])
print(asd2)