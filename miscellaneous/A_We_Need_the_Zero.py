t = int(input())

for _ in range(t):
    n = int(input())
    xor = 0
    arr = list(map(int, input().split()))
    for el in arr:
        xor ^= el
    if n & 1:
        print(xor)
    else:
        if xor == 0:
            print(0)
        else:
            print(-1)