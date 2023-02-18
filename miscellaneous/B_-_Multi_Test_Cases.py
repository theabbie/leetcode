t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for el in arr:
        if el & 1:
            res += 1
    print(res)