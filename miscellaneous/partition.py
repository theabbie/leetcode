def partition(arr, k):
    n = len(arr)
    i = -1
    for j in range(n):
        if arr[j] <= k:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return arr

print(partition([10, 5, 6, 7, 3, 5, 7, 2, 8, 2, 4, 3, 7], 5))
