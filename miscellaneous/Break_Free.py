t = int(input())

M = 10 ** 9 + 7

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ev = od = 0
    for el in arr:
        if el % 2 == 0:
            ev += 1
        else:
            od += 1
    x = 0
    if od == 0:
        x = 1
    print((M + pow(2, ev, M) - x) % M)