
def find_min(arr):
    min = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_index = i
    return min_index

def selection_sort(arr):
    new_array = []
    for i in range(len(arr)):
        min_index = find_min(arr)
        new_array.append(arr.pop(min_index)) # array.pop(index) ищет элемент в массиве с указанным индексом и удаляет этот элемент
    return new_array



print(selection_sort([5, 3, 6, 2, 10]))