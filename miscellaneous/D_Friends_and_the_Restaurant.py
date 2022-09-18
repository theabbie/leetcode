t = int(input())

for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    diff = [y[i] - x[i] for i in range(n)]
    diff.sort()
    i = 0
    j = n - 1
    res = 0
    while i < j:
        if diff[i] + diff[j] >= 0:
            res += 1
            i += 1
            j -= 1
        else:
            i += 1
    print(res)