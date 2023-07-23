t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    x = abs(a - b)
    print(min(x, 7 - x))