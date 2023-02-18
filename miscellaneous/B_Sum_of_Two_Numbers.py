t = int(input())

def sumd(n):
    res = 0
    while n:
        res += n % 10
        n //= 10
    return res

def solve(n):
    d = str(n)
    a = b = 0
    p = True
    for c in d:
        x = int(c)
        if p:
            a = 10 * a + x // 2
            b = 10 * b + x - x // 2
        else:
            a = 10 * a + x - x // 2
            b = 10 * b + x // 2
        if x & 1:
            p = not p
    return (a, b)

for _ in range(t):
    n = int(input())
    print(*solve(n))