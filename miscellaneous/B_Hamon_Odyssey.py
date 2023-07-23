t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    x = arr[0]
    for el in arr:
        x &= el
    res = 0
    xx = arr[0]
    for el in arr:
        xx &= el
        if xx == x:
            res += 1
    print(res - 1)