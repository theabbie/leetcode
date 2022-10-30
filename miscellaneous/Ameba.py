from collections import defaultdict, deque
from re import A


n = int(input())

arr = list(map(int, input().split()))

tree = defaultdict(list)

for i in range(n):
    tree[arr[i]].append(2 * (i + 1))
    tree[arr[i]].append(2 * (i + 1) + 1)

q = deque([1])
dist = defaultdict(lambda: float('inf'))
dist[1] = 0

while len(q) > 0:
    curr = q.pop()
    for j in tree[curr]:
        if dist[j] > dist[curr] + 1:
            dist[j] = dist[curr] + 1
            q.appendleft(j)

for curr in range(1, 2 * n + 2):
    k = curr
    res = 0
    while k > 1:
        if k in dist:
            res += dist[k]
            break
        else:
            res += 1
            k //= 2
    print(res)