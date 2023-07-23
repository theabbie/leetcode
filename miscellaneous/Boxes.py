t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    res = 0
    x = 0
    for el in arr:
        if el > x:
            res += 1
            x = el
        else:
            x ^= el
    print(res)