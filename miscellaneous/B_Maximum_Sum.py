t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] += p[i] + arr[i]
    res = float('-inf')
    for i in range(k + 1):
        res = max(res, p[n - i] - p[2 * (k - i)])
    print(res)