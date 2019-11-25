
# левый подмассив - опорный элемент - правый подмассив
def quick_sort(array: list):
    if len(array) < 2:
        return array
    else:
        pivot = array[0] # Рекурсивный случай
        less = [array[i] for i in range(1, len(array)) if array[i] <= pivot] # Левый подмассив
        greater = [array[i] for i in range(1, len(array)) if array[i] > pivot] # Правый подмассив

        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([10, 5, 2, 3, 17, 1, 255]))