t = int(input())

for _ in range(t):
    n = int(input())
    res = (2 * n - n % 2) + 2 * (n // 3)
    print(res)