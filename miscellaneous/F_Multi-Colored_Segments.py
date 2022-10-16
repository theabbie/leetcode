from collections import defaultdict
import bisect

t = int(input())

for _ in range(t):
    n = int(input())
    segs = defaultdict(list)
    for __ in range(n):
        l, r, c = map(int, input().split())
        bisect.insort(segs[c], (l, r))
        