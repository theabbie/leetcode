t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    res = 0
    for i in range(n):
        p = ord(b[i]) - ord(a[i])
        x = p if p >= 0 else 26 + p
        res += x
    d = res // 26
    print(min(res - 26 * d, 26 * (d + 1) - res))