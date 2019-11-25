
def binary_search(list, find_item):
    low = 0
    high = len(list)-1

    while low <= high:
        middle = (low + high) // 2
        current_item = list[middle]
        if current_item == find_item:
            return middle
        if current_item < find_item:
            low = middle + 1
        else:
            high = middle - 1

    return None

my_list = [1, 3, 5, 7, 15, 33, 41, 54, 59, 66, 128, 333]

print(binary_search(my_list, 333))
print(binary_search(my_list, -1))

