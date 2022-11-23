t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    n, m = map(int, input().split())
    res = n * m
    for l in range(20, 0, -1):
        M = 10 ** l
        curr = M // gcd(n, M)
        if curr <= m:
            res = n * curr * int(m // curr)
            break
    print(res)