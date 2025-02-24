
def missingPositive(arr):
    size = len(arr)
    for i in range(size):
        while 1 <= arr[i] <= size and arr[arr[i]-1] != arr[i]:
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]

    for i in range(size):
        if arr[i] != i+1:
            return i+1
        
    return size + 1

print(missingPositive([4,6,5,2,1]))
        

