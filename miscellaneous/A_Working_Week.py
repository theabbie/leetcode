t = int(input())

for _ in range(t):
    n = int(input())
    k = max(n - 6, 0)
    b = [1] * 3
    b[1] += k // 3
    b[2] += 2 * k // 3
    print(min(abs(b[0] - b[1]), abs(b[1] - b[2]), abs(b[2] - b[0])))