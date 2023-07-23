def maxscore(arr, i, n, k):
    if i >= n:
        return 0
    a = maxscore(arr, i + 1, n, k)
    b = int(arr[i] == k) + maxscore(arr, i + 1, n, k + 1)
    res = max(a, b)
    return res

n = int(input())

arr = list(map(int, input().split()))

print(maxscore(arr, 0, n, 1))