t = int(input())

for _ in range(t):
    s = input()
    n = len(s)

    p = [0] * (n + 1)

    for i in range(n):
        p[i + 1] += p[i]
        if s[i] == '+':
            p[i + 1] += 1
        else:
            p[i + 1] -= 1

    pos = {}

    for i in range(n + 1):
        if p[i] not in pos:
            pos[p[i]] = i + 1

    res = 0

    for i in range(n):
        res += pos.get(-i, 0)

    print(res)