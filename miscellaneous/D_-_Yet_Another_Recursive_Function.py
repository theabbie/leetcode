n = int(input())

cache = {}

def fn(n):
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    res = fn(n // 2) + fn(n // 3)
    cache[n] = res
    return res

print(fn(n))