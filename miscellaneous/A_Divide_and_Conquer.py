t = int(input())

def countodd(el):
    res = 0
    while el % 2 != 0:
        res += 1
        el //= 2
    return res

def counteven(el):
    res = 0
    while el > 0 and el % 2 != 1:
        res += 1
        el //= 2
    return res

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if sum(arr) % 2 == 0:
        print(0)
        continue
    res = float('inf')
    for el in arr:
        if el & 1:
            res = min(res, countodd(el))
        else:
            res = min(res, counteven(el))
    print(res)