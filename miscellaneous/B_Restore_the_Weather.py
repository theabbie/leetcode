t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        a[i] = [a[i], i]
    a.sort()
    b.sort()
    i = 0
    res = [-1] * n
    for el, x in a:
        while i < n and b[i] < el - k:
            i += 1
        if i < n and b[i] <= el + k:
            res[x] = b[i]
            i += 1
    print(*res)