import sys

sys.setrecursionlimit(10**6)

M = 10 ** 9 + 7

t = int(input())

def extended_gcd(a, b):
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0


def modinv(a, m):
    g, x, _ = extended_gcd(a % m, m)
    return x % m if g == 1 else None

for _ in range(t):
    n, z = map(int, input().split())
    res = 0
    prev = 1
    for i in range(n, z + 1):
        if i > n:
            prev = (prev * (i - 2) * modinv(i - n, M)) % M
        res = (res + prev * (z // i)) % M
    print(res)