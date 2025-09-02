from collections import defaultdict

class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for a, b, w in edges:
            graph[a].add((b, w))
            graph[b].add((a, w))
        LOG = 1 + len("{:0b}".format(n + 1))
        level = [0] * n
        nodectr = [Counter() for _ in range(n)]
        parent = [[_] * LOG for _ in range(n)]
        stack = [(0, -1, -1, 0, Counter())]
        while len(stack) > 0:
            curr, prev, weight, l, ctr = stack.pop()
            level[curr] = l
            nodectr[curr] = ctr
            if prev != -1:
                parent[curr][0] = prev
            for j, w in graph[curr]:
                if j != prev:
                    newctr = Counter(ctr)
                    newctr[w] += 1
                    stack.append((j, curr, w, l + 1, newctr))
        for d in range(1, LOG):
            for i in range(n):
                parent[i][d] = parent[parent[i][d - 1]][d - 1]
        def ancestor(i, k):
            ac = i
            p = 0
            while k:
                if k & 1:
                    ac = parent[ac][p]
                k //= 2
                p += 1
            return ac
        def lca(u, v):
            if level[u] < level[v]:
                u, v = v, u
            diff = level[u] - level[v]
            i = 0
            while diff:
                if diff & 1:
                    u = parent[u][i]
                diff //= 2
                i += 1
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if parent[u][i] != parent[v][i]:
                    u = parent[u][i]
                    v = parent[v][i]
            return parent[u][0]
        res = []
        for x, y in queries:
            pathctr = nodectr[x] + nodectr[y]
            LCA = lca(x, y)
            for el in nodectr[LCA]:
                pathctr[el] -= 2 * nodectr[LCA][el]
            if len(pathctr) > 0:
                res.append(sum(pathctr.values()) - max(pathctr.values()))
            else:
                res.append(0)
        return res