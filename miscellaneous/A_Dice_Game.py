t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    if b <= c:
        print("NO")
        continue
    if d <= a:
        print("YES")
        continue
    overlap = min(b, d) - max(a, c)
    alice = 