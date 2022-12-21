import math

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    x = arr.pop(0)
    arr.sort()
    for el in arr:
        if el >= x and math.ceil((el + x) / 2) <= arr[-1]:
            x = math.ceil((el + x) / 2)
    print(x)