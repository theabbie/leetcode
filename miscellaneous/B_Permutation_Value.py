t = int(input())

for _ in range(t):
    n = int(input())
    res = [1] + list(range(n, 1, -1))
    print(*res)