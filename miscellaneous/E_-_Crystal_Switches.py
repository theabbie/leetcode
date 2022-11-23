from collections import deque

n, m, k = map(int, input().split())

passable = {}
impassable = {}

for i in range(1, n + 1):
    passable[i] = set()
    impassable[i] = set()

for _ in range(m):
    u, v, a = map(int, input().split())
    if a == 0:
        impassable[u].add(v)
        impassable[v].add(u)
    else:
        passable[u].add(v)
        passable[v].add(u)

switches = set(map(int, input().split()))

beg = (1, k, 0)

v = {(beg[0], beg[1])}

q = deque([beg])

res = float('inf')

while len(q) > 0:
    curr, rem, d = q.pop()
    if curr == n:
        rem = min(rem, d)
    for j in passable[curr]:
        if (j, rem) not in v:
            v.add((j, rem))
            q.appendleft((j, rem, d + 1))
    if curr in switches:
        for j in impassable[curr]:
            if (j, rem) not in v:
                v.add((j, rem))
                q.appendleft((j, rem - 1, d + 1))

print(res if res != float('inf') else -1)