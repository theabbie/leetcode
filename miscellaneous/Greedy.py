import sys

sys.setrecursionlimit(10 ** 5)

t = int(input())

def pos(s, i, n, prev, d, seq, cache):
    if i >= n:
        return d == 0
    key = (i, prev, d)
    if key in cache:
        return cache[key]
    if i > 0 and s[i] == s[i - 1]:
        seq[i] = '(' if prev == 1 else ')'
        if d + prev >= 0 and pos(s, i + 1, n, prev, d + prev, seq, cache):
            cache[key] = True
            return True
        else:
            seq[i] = -1
            cache[key] = False
            return False
    for x in [-1, 1]:
        if d + x < 0:
            continue
        seq[i] = '(' if x == 1 else ')'
        if pos(s, i + 1, n, x, d + x, seq, cache):
            cache[key] = True
            return True
        else:
            seq[i] = -1
    cache[key] = False
    return False

for _ in range(t):
    n = int(input())
    s = input()
    if n & 1:
        print("NO")
        continue
    seq = [-1] * n
    res = pos(s, 0, n, 0, 0, seq, {})
    if res:
        print("YES")
        print("".join(seq))
    else:
        print("NO")