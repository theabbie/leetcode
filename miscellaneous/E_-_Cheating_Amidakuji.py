from collections import deque

n, m = map(int, input().split())

arr = list(map(int, input().split()))

b = list(range(n))

swaps = []

pos = 0

pf = [0]

for j in range(m):
    x, y = arr[j] - 1, arr[j]
    if x == pos:
        pos = y
    elif y == pos:
        pos = x
    pf.append(pos)
    swaps.append((x, y))

q = deque()
v = set()

for i in range(n):
    q.appendleft((i, 0))
    v.add((i, 0))

mp = {}
parent = {}

while len(q) > 0:
    pos, spos = q.pop()
    ogpos = pos
    if spos < m:
        x, y = swaps[spos]
        if pos == x:
            pos = y
        elif pos == y:
            pos = x
        if (pos, spos + 1) not in v:
            v.add((pos, spos + 1))
            parent[(pos, spos + 1)] = (ogpos, spos)
            q.appendleft((pos, spos + 1))
    else:
        top = (pos, spos)
        while top in parent:
            top = parent[top]
        curr = (pos, spos)
        while curr in parent:
            mp[curr] = top
            curr = parent[curr]

print(mp)