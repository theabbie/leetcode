def getPrice(price, rem, n, cache):
    if rem < 0:
        return float('-inf')
    if rem == 0:
        return 0
    if rem in cache:
        return cache[rem]
    res = 0
    for i in range(1, n + 1):
        curr = price[i - 1] + getPrice(price, rem - i, n, cache)
        res = max(res, curr)
    cache[rem] = res
    return res
        
def cutRod(price, n):
    cache = {}
    return getPrice(price, n, n, cache)

print(cutRod([2, 5, 7, 8, 10], 5))
