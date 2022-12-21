from collections import Counter
import random

def check(arr):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        if arr[i] < i + 1:
            return False
    return True

def checktest(arr):
    ctr = Counter(arr)
    M = max(ctr, key = lambda el: (ctr[el], el))
    n = 0
    for el in arr:
        if el < M:
            n += 1
    return M >= n + ctr[M]

for _ in range(10):
    arr = random.choices(range(4, 12), k = 20)
    arr.sort()
    if check(arr) ^ checktest(arr):
        print(arr, check(arr), checktest(arr))