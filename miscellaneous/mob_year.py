t = int(input())

for _ in range(t):
    n, m, k, x = map(int, input().split())
    x -= 1
    x = x % (k * n + m)
    print("YES" if x >= (k - 1) * n else "NO")