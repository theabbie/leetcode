t = int(input())

def solve(n):
    groups = [[], []]
    for i in range(16):
        a = 1 if i & (1 << 0) else 0
        b = 1 if i & (1 << 1) else 0
        c = 1 if i & (1 << 2) else 0
        d = 1 if i & (1 << 3) else 0
        groups[((a & b) | c) ^ d].append((a, b, c, d))
    pos = 0
    a = b = c = d = 0
    for x in range(32):
        if n & (1 << x):
            i, j, k, l = groups[1][pos % 8]
        else:
            i, j, k, l = groups[0][pos % 8]
        if i == 1:
            a |= (1 << x)
        if j == 1:
            b |= (1 << x)
        if k == 1:
            c |= (1 << x)
        if l == 1:
            d |= (1 << x)
        pos += 1
    if len(set([a, b, c, d])) != 4:
        print(-1)
        return
    print(a, b, c, d)

for _ in range(t):
    n = int(input())
    solve(n)