from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10 ** 6)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.find(a)


def kruskal(n, U, V, W):
    union = UnionFind(n)
    cost, merge_cnt = 0, 0
    mst_u, mst_v = [], []
    order = sorted(range(len(W)), key=lambda x: W[x])
    for i in range(len(W)):
        u, v = U[order[i]], V[order[i]]
        find_u, find_v = union.find(u), union.find(v)
        if find_u != find_v:
            cost += W[order[i]]
            merge_cnt += 1
            union.parent[find_v] = find_u
            mst_u.append(u), mst_v.append(v)
    return cost, mst_u, mst_v, n == 1 + merge_cnt

n, m = map(int, input().split())

graph = defaultdict(set)

U = []
V = []
W = []

for _ in range(m):
    u, v = map(int, input().split())
    U.append(u - 1)
    V.append(v - 1)
    W.append(1)

cost, mstu, mstv, flag = kruskal(n, U, V, W)

for i in range(len(mstu)):
    graph[mstu[i]].add(mstv[i])
    graph[mstv[i]].add(mstu[i])

q = deque([(0, 1)])
v = {0}

res = 0

while len(q) > 0:
    curr, l = q.pop()
    paths = 0
    for j in graph[curr]:
        if j not in v:
            paths += 1
            v.add(j)
            q.appendleft((j, l + 1))
    if paths == 0:
        print(curr, l)
        res += 1 << (len(graph) - l)
    else:
        res -= (paths - 1) * l

print(min(res, 10 ** 6))