t = int(input())

for _ in range(t):
    n, k, b, s = map(int, input().split())
    if s - s % k != b * k:
        print(-1)
    else:
        res = [s // n] * (n - 1) + [s - (s // n) * (n - 1)]
        print(*res)