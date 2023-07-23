t = int(input())

M = 10 ** 9 + 7

for _ in range(t):
    n = int(input())
    s = input()
    res = 0
    stars = [0] * (n + 1)
    fours = [0] * (n + 1)
    zeroes = [0] * (n + 1)
    for i in range(n):
        st = 1 if s[i] == "*" else 0
        f = 1 if s[i] == "4" else 0
        z = 1 if s[i] == "0" else 0
        stars[i + 1] += stars[i] + st
        fours[i + 1] += fours[i] + f
        zeroes[i + 1] += zeroes[i] + z
    for i in range(n):
        if s[i] == "0" or s[i] == "*":
            lfour = fours[i]
            lstar = stars[i]
            rfour = fours[n] - fours[i + 1]
            rstar = stars[n] - stars[i + 1]
            res += (lfour + lstar) * (rfour + rstar)
            res %= M
    print(res)