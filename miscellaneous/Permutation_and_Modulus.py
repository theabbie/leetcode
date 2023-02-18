t = int(input())

for _ in range(t):
    n = int(input())
    res = list(range(2, n + 1)) + [1]
    print(*res)