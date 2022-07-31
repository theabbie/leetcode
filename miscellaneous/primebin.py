def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def biggestPrime(s, i, n, curr, cache):
    print(s, i, n)
    if i >= n:
        if isPrime(curr):
            return curr
        return float('-inf')
    if (i, curr) in cache:
        return cache[(i, curr)]
    a = biggestPrime(s, i + 1, n, curr * 2 + int(s[i]), cache)
    b = biggestPrime(s, i + 1, n, curr, cache)
    res = max(a, b)
    cache[(i, curr)] = res
    return res

s = input()
n = len(s)

print(biggestPrime(s, 0, n, 0, {}))