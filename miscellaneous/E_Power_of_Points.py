t = int(input())

for _ in range(t):
    n = int(input())
    res = [0] * n
    arr = list(map(int, input().split()))
    arr = sorted([(arr[i], i) for i in range(n)])
    for i in range(n):
        for j in range(i):
            res[arr[i][1]] += (arr[j + 1][0] - arr[j][0]) * (i - j)
        for j in range(i, n - 1):
            res[arr[i][1]] += (arr[j + 1][0] - arr[j][0]) * (n - j - 1)
    print(*res)