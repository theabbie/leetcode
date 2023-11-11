t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    res = 0
    arr = list(map(int, input().split()))
    arr = [(arr[i], i + 1) for i in range(n)]
    arr.sort()
    res = (float('-inf'), -1, -1, -1)
    for i in range(n - 1):
        x = arr[i][0]
        y = arr[i + 1][0]
        curr = 0
        for b in range(k):
            xb = 1 if x & (1 << b) else 0
            yb = 1 if y & (1 << b) else 0
            if xb == yb == 0:
                curr |= (1 << b)
        res = max(res, ((curr ^ x) & (curr ^ y), arr[i][1], arr[i + 1][1], curr))
    print(res[1], res[2], res[3])