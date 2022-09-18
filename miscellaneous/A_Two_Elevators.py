t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    x = abs(a - 1)
    y = abs(b - c) + abs(c - 1)
    if x < y:
        print(1)
    elif x > y:
        print(2)
    else:
        print(3)