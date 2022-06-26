import random

def isPossible(arr, i, n, k, cache):
    if k < 0:
        return False
    if k == 0:
        return True
    if i == n - 1:
        return arr[i] == k
    if (i, k) in cache:
        return cache[(i, k)]
    res = isPossible(arr, i + 1, n, k, cache) or isPossible(arr, i + 1, n, k - arr[i], cache)
    cache[(i, k)] = res
    return res

def subsetSumToK(n, k, arr):
    cache = {}
    return isPossible(arr, 0, n, k, cache)

n = 750
arr = list(random.sample(range(n), n))
arrcpy = arr[:]
random.shuffle(arrcpy)
k = sum(arrcpy[:n])

print(arr)
print(k)
print(subsetSumToK(len(arr), k, arr))
