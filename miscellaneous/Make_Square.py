t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    x = min(a, b, c, d)
    print(abs(a - x) + abs(b - x) + abs(c - x) + abs(d - x))