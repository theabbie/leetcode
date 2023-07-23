t = int(input())

for _ in range(t):
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    res = 0
    i = 0
    while i < n:
        ctr = 1
        while i < n - 1 and (arr[i] <= q) == (arr[i + 1] <= q):
            ctr += 1
            i += 1
        if arr[i] <= q and ctr >= k:
            x = ctr - k + 1
            res += x * (x + 1) // 2
        i += 1
    print(res)