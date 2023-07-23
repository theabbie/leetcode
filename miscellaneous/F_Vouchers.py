import heapq

n, m = map(int, input().split())

p = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

mp = {}

for el in p + c + d:
    mp[el] = 0

for i, el in enumerate(sorted(mp)):
    mp[el] = i

discounts = []

for i in range(m):
    discounts.append((c[i], d[i]))

discounts.sort()

p.sort()

res = 0

heap = []

i = 0

for el in p:
    while i < m and discounts[i][0] <= el:
        heapq.heappush(heap, -discounts[i][1])
        i += 1
    if len(heap) > 0:
        res += el + heapq.heappop(heap)
    else:
        res += el

print(res)