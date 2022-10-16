t = int(input())

sumofn = lambda n: n * (n + 1) // 2

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arrset = set(arr)
    res = 0
    if k == 1:
        i = 1
        while i in arrset:
            i += 1
        print(max(arr) - i)
        continue
    if 2 * n not in arrset:
        k -= 1
    for i in range(1, 2 * n + 1):
        if k:
            if i not in arrset:
                res += 2 * n - i
                k -= 1
    print(res)