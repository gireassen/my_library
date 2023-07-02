def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

def sum_2(arr: list):
    if arr == []:
        return 0
    return 1 + sum_2(arr[1:])

orig1 = sum_2([1,2,3,4,5,6])
print(orig1)