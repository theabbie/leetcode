import sys

sys.setrecursionlimit(10 ** 7)

def count(num, i, n, tight, pos, curr, c, s):
    if i >= n:
        return curr
    key = (i, tight, pos, curr)
    # if key in c:
    #     return c[key]
    maxdigit = 9
    if tight:
        maxdigit = int(num[i])
    res = 0
    for d in range(maxdigit + 1):
        if int(s[pos]) == d:
            newpos = pos + 1
            newcurr = curr
            if newpos >= len(s):
                newpos = 0
                newcurr += 1
            res += count(
                num, i + 1, n, tight and (d == maxdigit), newpos, newcurr, c, s
            )
        res += count(num, i + 1, n, tight and (d == maxdigit), 0, curr, c, s)
    c[key] = res
    return res

t = int(input())

for _ in range(t):
    s, l, r = input().split()
    print(
        count(r, 0, len(r), True, 0, 0, {}, s)
        , count(l, 0, len(l), True, 0, 0, {}, s)
        , l.count(s)
    )