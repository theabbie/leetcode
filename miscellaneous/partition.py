import random

def partition(arr, k):
    n = len(arr)
    i = -1
    for j in range(n):
        if arr[j] <= k:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return i

def sort(arr, beg, end, d = 4):
    if d == 0:
        return
    mid = (beg + end) // 2
    partition(arr, mid)
    sort(arr, beg, mid, d - 1)
    sort(arr, mid, end, d - 1)

arr = list(range(1000))
random.shuffle(arr)
print(arr)
sort(arr, min(arr), max(arr), d = 12)
print(arr)
