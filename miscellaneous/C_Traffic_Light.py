from collections import defaultdict
import bisect

t = int(input())

for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()
    if c == 'g':
        print(0)
        continue
    pos = defaultdict(list)
    for i in range(2 * n):
        pos[s[i % n]].append(i)
    res = 0
    for i in pos[c]:
        j = bisect.bisect_right(pos['g'], i)
        if j < len(pos['g']):
            res = max(res, pos['g'][j] - i)
    print(res)