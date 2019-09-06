def binary_search(list, item):
    low = 0
    high = len(list) - 1
    i = 0
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        i += 1
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


item = int(input('Загадайте число'))
my_list = list(range(1, 10000001))
print(binary_search(my_list, item))
