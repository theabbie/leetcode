import math

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    x = 1
    for el in arr:
        if el == x:
            x += 1
    print(math.ceil((n + 1 - x) / k))