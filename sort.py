import random

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

array = []
n = int(input("Enter number of elements: "))
for i in range(n):
    array.append(random.randint(-2 * n, 2 * n))
print(f"Randomly generated list of {n} elements:\n{array}")
print("Sorted list:\n" + str(selectionSort(array)))
