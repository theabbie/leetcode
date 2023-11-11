t = int(input())

for _ in range(t):
    b, c, h = map(int, input().split())
    k = c + h
    print(min(k + 1, b) + min(k, b - 1))