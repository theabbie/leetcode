t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ctr = [0] * 31
    for el in arr:
        for b in range(31):
            if el & 1:
                ctr[b] += 1
            el //= 2
    res = 0
    rem = n
    for i in range(30, -1, -1):
        if ctr[i] % 2 == 0 and rem > 0:
            res += 1
            rem -= 1
    print(res)