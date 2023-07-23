t = int(input())

for _ in range(t):
    n, a, b, c, d = map(int, input().split())
    beg = min(a, b, n + 1 - a, n + 1 - b)
    end = min(c, d, n + 1 - c, n + 1 - d)
    print(abs(beg - end))