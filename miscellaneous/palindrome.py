MAX = 10 ** 9 + 7

t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gen(s, c, res, beg):
    n = len(s)
    if s == s[::-1] and not beg:
        c += 1
    if n == 0:
        res.append(c)
        return
    for i in range(n):
        gen(s[:i] + s[i + 1:], c, res, False)

for tt in range(1, 1 + t):
    n = int(input())
    s = input()
    res = []
    gen(s, 0, res, True)
    a, b = sum(res), len(res)
    mul = gcd(a, b)
    if mul != 0:
        a, b = a // mul, b // mul
    if b == 0:
        op = 0
    elif a % b == 0:
        op = a // b
    else:
        k = MAX // b
        while True:
            if (k * b) % MAX == a:
                op = k
                break
            k += 1
    print(f"Case #{tt}: {op}")
