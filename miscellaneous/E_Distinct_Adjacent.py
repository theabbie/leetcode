M = 998244353

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())

m * (m - 1) ^ (n - 2) * (m - 2)

res = 0

for i in range(n):
    res += pow(m - 1, gcd(i, n - 2), M)
    res %= M

res *= pow(n, M - 2, M)

res %= M

print(res)