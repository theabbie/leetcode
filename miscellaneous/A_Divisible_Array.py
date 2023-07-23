t = int(input())

for _ in range(t):
    n = int(input())
    if n & 1:
        print(*list(range(1, n + 1)))
    else:
        print(*list(range(2, 2 * n + 1, 2)))