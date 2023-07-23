import math

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    if x % 2 == 0:
        print(1 + math.ceil((y - x - 2) / 2))
    elif x % 3 == 0:
        print(1 + math.ceil((y - x - 3) / 2))
    elif x % 5 == 0:
        print(1 + math.ceil((y - x - 5) / 2))
    elif x % 7 == 0:
        print(1 + math.ceil((y - x - 7) / 2))