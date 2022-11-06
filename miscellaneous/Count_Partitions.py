import sys

sys.setrecursionlimit(10**6)

t = int(input())

def numparts(arr, maxyet, i, n):
    if i >= n:
        return 1
    j = i
    res = 0
    maxsofar = arr[j]
    while j < n - 1 and arr[j] < arr[j + 1]:
        j += 1
        maxsofar = max(maxsofar, arr[j])
        if maxsofar >= maxyet[j]:
            res += numparts(arr, maxyet, j, n)
    return res

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    maxyet = [float('-inf')] * n
    maxyet[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        maxyet[i] = max(arr[i], maxyet[i + 1])
    print(numparts(arr, maxyet, 0, n) % 998244353)