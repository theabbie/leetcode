import math

t = int(input())

for _ in range(t):
    n = int(input())
    neg = pos = 0
    arr = list(map(int, input().split()))
    for el in arr:
        if el == -1:
            neg += 1
        else:
            pos += 1
    req = math.ceil(n / 2)
    res = 0
    while pos < req:
        pos += 1
        neg -= 1
        res += 1
    if neg & 1:
        res += 1
    print(res)