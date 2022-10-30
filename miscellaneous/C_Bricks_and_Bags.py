import bisect

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    res = float('-inf')
    for i in range(n - 2):
        res = max(res, abs(arr[n // 2] - arr[i]) + abs(arr[n - i - 1] - arr[n // 2]))
    print(res)