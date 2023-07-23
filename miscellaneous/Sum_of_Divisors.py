M = 10 ** 9 + 7

n = int(input())

res = 0

if n <= 10 ** 6:
    for i in range(1, n + 1):
        res += i * (n // i)
        res %= M
else:
    for i in range(1, n // (10 ** 6) + 1):
        res += i * (n // i)
        res %= M

print(res)