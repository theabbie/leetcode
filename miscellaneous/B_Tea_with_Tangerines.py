t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    k = min(arr)
    res = 0
    for el in arr:
        res += el // (2 * k - 1)
        if el % (2 * k - 1) == 0:
            res -= 1
    print(res)