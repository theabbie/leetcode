from collections import defaultdict
import bisect

n, k = map(int, input().split())

arr = list(map(int, input().split()))

poseven = defaultdict(list)
posodd = defaultdict(list)

for i in range(n):
    if i & 1:
        posodd[arr[i]].append(i)
    else:
        poseven[arr[i]].append(i)

res = 0

for i in range(n):
    l = max(i, k - i - 1)
    r = min(i + k, 2 * n - k - i + 1, n) - 1
    if l > r:
        continue
    if i & 1:
        ctr = bisect.bisect_right(posodd[arr[i]], r) - bisect.bisect_left(posodd[arr[i]], l)
        res += (r + 1) // 2 - l // 2 - ctr
    else:
        ctr = bisect.bisect_right(poseven[arr[i]], r) - bisect.bisect_left(poseven[arr[i]], l)
        res += r - l + 1 - (r + 1) // 2 + l // 2 - ctr

print(res)