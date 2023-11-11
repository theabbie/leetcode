from collections import Counter, defaultdict, deque

m, n = map(int, input().split())

grid = []

chars = set()

for _ in range(m):
    grid.append(input())
    for c in grid[-1]:
        chars.add(c)

graph = defaultdict(set)

revgraph = defaultdict(set)

indegree = Counter()

imp = set()

for j in range(n):
    ctr = Counter()
    for i in range(m):
        ctr[grid[i][j]] += 1
    for c in ctr:
        if ctr[c] > 1:
            for cc in ctr:
                if cc == c:
                    continue
                graph[("c", j, cc)].add(("c", j, c))
                revgraph[("c", j, c)].add(("c", j, cc))
                indegree[("c", j, c)] += 1
        else:
            imp.add(("c", j, c))

for i in range(m):
    ctr = Counter()
    for j in range(n):
        ctr[grid[i][j]] += 1
    for c in ctr:
        if ctr[c] > 1:
            for cc in ctr:
                if cc == c:
                    continue
                graph[("r", i, cc)].add(("r", i, c))
                revgraph[("r", i, c)].add(("r", i, cc))
                indegree[("r", i, c)] += 1
        else:
            imp.add(("r", i, c))

q = deque()

for i in range(n):
    for c in chars:
        if indegree[("c", i, c)] == 0:
            q.appendleft(("c", i, c))

for i in range(m):
    for c in chars:
        if indegree[("r", i, c)] == 0:
            q.appendleft(("r", i, c))

order = []

while len(q) > 0:
    curr = q.pop()
    order.append(curr)
    for j in graph[curr]:
        indegree[j] -= 1
        if indegree[j] == 0:
            q.appendleft(j)

done = set()

for el in order:
    curr = True
    for j in revgraph[el]:
        if j not in done:
            curr = False
            break
    if el in imp:
        curr = False
    if curr:
        done.add(el)

res = 0

for i in range(m):
    for j in range(n):
        if ("c", j, grid[i][j]) not in done and ("r", i, grid[i][j]) not in done:
            res += 1

print(res)