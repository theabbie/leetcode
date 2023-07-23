t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    x = y = 1
    while (x + 1) * (x + 2) // 2 <= a:
        x += 1
    while (y + 1) * (y + 2) // 2 <= b:
        y += 1
    dx = a - x * (x + 1) // 2 
    dy = b - y * (y + 1) // 2
    print(dx + dy + 2 * max(x, y))