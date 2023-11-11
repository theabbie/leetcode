import sys

sys.setrecursionlimit(10 ** 5)

M = 998244353

def count(arr, i, n, j, k):
    if i >= n:
        print(j, k)
        return int(j > 0 and k == 0)
    res = 0
    res += count(arr, i + 1, n, j, k)
    res += count(arr, i + 1, n, j + 1, (k * j + arr[i]) % (j + 1))
    return res

# def count(arr, i, n, curr, mod, rem, cache):
#     if rem == 0:
#         return int(curr == 0)
#     if i >= n:
#         return int(rem == 0 and curr == 0)
#     key = (i, curr, rem)
#     if key in cache:
#         return cache[key]
#     res = 0
#     if rem > 0:
#         res += count(arr, i + 1, n, (curr + arr[i]) % mod, mod, rem - 1, cache)
#     res += count(arr, i + 1, n, curr, mod, rem, cache)
#     res %= M
#     cache[key] = res
#     return res

n = int(input())

arr = list(map(int, input().split()))

print(count(arr, 0, n, 0, 0))