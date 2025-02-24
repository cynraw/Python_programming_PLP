def bubbleSort(arr, size):
    for i in range(size):
        for j in range(i+1, size):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
size = len(arr)
print(bubbleSort(arr, size))