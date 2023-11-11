t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if len(set(arr)) == 1:
        print(-1)
        continue
    c = max(arr)
    x = arr.count(c)
    arr = [el for el in arr if el != c]
    pos = True
    for el in arr:
        if el % c == 0:
            pos = False
            break
    if not pos:
        print(-1)
    else:
        print(len(arr), x)
        print(*arr)
        print(*([c] * x))