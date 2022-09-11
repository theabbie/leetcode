t = int(input())

def dist(a, b, c, d):
    return abs(c - a) + abs(d - b)

for _ in range(t):
    n, m = map(int, input().split())
    m, n = min(m, n), max(m, n)
    if (m, n) == (1, 1):
        print(0)
        continue
    d = 2 * (m + n - 3)
    print(d - n + 4)