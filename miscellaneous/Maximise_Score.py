t = int(input())

for _ in range(t):
    n = int(input())
    res = float('inf')
    arr = list(map(int, input().split()))
    for i in range(n):
        l = r = float('-inf')
        if i > 0:
            l = max(l, abs(arr[i] - arr[i - 1]))
        if i < n - 1:
            r = max(r, abs(arr[i + 1] - arr[i]))
        res = min(res, max(l, r))
    print(res)