t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    prices = [1]
    while prices[-1] <= n:
        prices.append(prices[-1] * 2)
    m = len(prices)
    res = 0
    if sum(prices) <= n:
        res += pow(2, m)
    if sum(prices[:-1]) <= n:
        res += pow(2, m - 1)
    print(res)