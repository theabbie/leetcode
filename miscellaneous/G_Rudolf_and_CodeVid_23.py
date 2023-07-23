import sys

sys.setrecursionlimit(1500)

t = int(input())

def mindays(meds, i, n, curr, cache):
    if i >= n:
        if curr == 0:
            return 0
        return float('inf')
    key = (i, curr)
    if key in cache:
        return cache[key]
    a = mindays(meds, i + 1, n, curr, cache)
    b = meds[i][0] + mindays(meds, i + 1, n, (curr & meds[i][1]) | meds[i][2], cache)
    res = min(a, b)
    cache[key] = res
    return res

for _ in range(t):
    n, m = map(int, input().split())
    s = int(input(), 2)
    meds = []
    for _ in range(m):
        d = int(input())
        a = input()
        b = input()
        a = "".join(str(1 - int(c)) for c in a)
        meds.append((d, int(a, 2), int(b, 2)))
    meds.sort(key = lambda x: (s & x[1]) | x[2])
    res = mindays(meds, 0, m, s, {})
    if res != float('inf'):
        print(res)
        continue
    meds.sort(key = lambda x: (s & x[1]) | x[2], reverse = True)
    res = mindays(meds, 0, m, s, {})
    if res == float('inf'):
        print(-1)
    else:
        print(res)