import bisect

n = int(input())

arr = list(map(int, input().split()))

pos = {}
pospref = {}

res = 0

for i in range(n):
    if arr[i] not in pos:
        pos[arr[i]] = []
        pospref[arr[i]] = [0]
    pos[arr[i]].append(i)
    pospref[arr[i]].append(pospref[arr[i]][-1] + n - i)

def getcount(vals, l, r):
    if l >= r:
        return 0
    return r - l - bisect.bisect_right(vals, r - 1) + bisect.bisect_left(vals, l)

for i in range(n):
    res += (i + 1) * getcount(pos[arr[i]], i + 1, n - i)
    l, r = max(n - i, i + 1), n
    if l < r:
        res += n * (r - l) - r * (r - 1) // 2 + l * (l - 1) // 2
        a = bisect.bisect_left(pos[arr[i]], l)
        b = bisect.bisect_right(pos[arr[i]], r - 1)
        res -= pospref[arr[i]][b] - pospref[arr[i]][a]

print(res)