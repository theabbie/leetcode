import sys

sys.setrecursionlimit(10 ** 6)

t = int(input())

def maxsub(arr, i, n, rem, minp, curr, x, cache):
    if i >= n:
        if rem == 0:
            return curr - minp
        return float('-inf')
    res = float('-inf')
    if i + rem < n:
        res = max(res, maxsub(arr, i + 1, n, rem, min(minp, curr + arr[i] - x), curr + arr[i] - x, x, cache))
    if rem > 0:
        res = max(res, maxsub(arr, i + 1, n, rem - 1, min(minp, curr + arr[i] + x), curr + arr[i] + x, x, cache))
    return res

for _ in range(t):
    n, k, x = map(int, input().split())
    arr = list(map(int, input().split()))
    print(maxsub(arr, 0, n, k, float('inf'), 0, x, {}))