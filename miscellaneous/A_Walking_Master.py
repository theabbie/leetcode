t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    if b > d:
        print(-1)
        continue
    a += d - b
    if a < c:
        print(-1)
        continue
    print(a - c + d - b)