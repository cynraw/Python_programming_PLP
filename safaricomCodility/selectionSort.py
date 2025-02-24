def selectionSort(arr, size):
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
                    # Swap elements
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
size = len(arr)
print(selectionSort(arr, size))  # Output: [11, 12, 22, 25, 64]
