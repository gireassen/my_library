def find_small(arr):
    '''
    поиск наименьшего эл-та
    '''
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    '''
    сортировка выбором
    '''
    newArr = []
    for i in range(len(arr)):
        smallest = find_small(arr)
        newArr.append(arr.pop(smallest))
    return newArr

if __name__ == "__main__":
    print(selection_sort([1,8,2,3,6,9,122,11]))