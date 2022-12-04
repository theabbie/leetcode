t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    pos = False
    for el in arr:
        if el % 2 == 1:
            pos = True
            break
    if total % 2 == 0 and pos:
        print("YES")
    else:
        print("NO")