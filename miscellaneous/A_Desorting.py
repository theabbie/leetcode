t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = float('inf')
    for i in range(n - 1):
        if arr[i] <= arr[i + 1]:
            res = min(res, 1 + (arr[i + 1] - arr[i]) // 2)
        else:
            res = 0
    print(res)