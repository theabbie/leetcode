t = int(input())

for _ in range(t):
    n = int(input())
    res = [i for i in range(2, n - 1)] + [1] + [n - 1, n]
    print(*res)