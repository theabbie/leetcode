import sys

sys.setrecursionlimit(2 * 10 ** 5)

from collections import defaultdict, deque

t = int(input())

def check(s, i, prev, n, curr, l, pos, cache):
    if i >= n:
        return curr == l and (n - prev - 1) % 3 == 0
    key = tuple([i, prev, curr] + sorted(pos.items()))
    if key in cache:
        return cache[key]
    if curr < l and (prev + 1) % 3 == i and (pos.get(l - curr - 1, -1) == -1 or s[i] == pos.get(l - curr - 1, -1)):
        pos[curr] = s[i]
        if check(s, i + 1, i % 3, n, curr + 1, l, pos, cache):
            cache[key] = True
            return True
        del pos[curr]
    if check(s, i + 1, prev, n, curr, l, pos, cache):
        cache[key] = True
        return True
    cache[key] = False
    return False

for _ in range(t):
    n = int(input())
    s = input()
    valid = False
    for i in range(1, 7):
        if check(s, 0, -1, n, 0, i, {}, {}):
            valid = True
            break
    print("YES" if valid else "NO")