t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    k = max(abs(x), abs(y)) - min(abs(x), abs(y))
    print(2 * min(abs(x), abs(y)) + k + max(k - 1, 0))