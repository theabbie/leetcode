t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    print("YES" if x * x * x * x + 4 * y * y == 4 * x * x * y else "NO")