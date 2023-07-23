t = int(input())

for _ in range(t):
    n = int(input())
    if n <= 2:
        print(*list(range(n, 0, -1)))
        continue
    xx = [i for i in range(1, n + 1) if i not in {1, 2, 3}]
    p = len(xx)
    print(*([2] + xx[:p//2] + [1] + xx[p//2:] + [3]))