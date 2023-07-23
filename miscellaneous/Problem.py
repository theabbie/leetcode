t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    print("YES" if (m + n) % 2 == 0 else "NO")