t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    print(m * a * (n // (m + 1)) + b * (n - n // (m + 1)))