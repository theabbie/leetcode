t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    if 2 * k >= n:
        print(n * (n - 1) // 2)
    else:
        x = 2 * k
        res = k * (k - 1) // 2
        res += n * k - k * (k + 1) // 2
        res += (n - 2 * k) * k
        print(res)