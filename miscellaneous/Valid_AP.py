t = int(input())

for _ in range(t):
    a, b, n = map(int, input().split())
    print("YES" if (b - a) % (n + 1) == 0 else "NO")