class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        r = set(restricted)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        l = lambda x, p: 0 if x in r else 1 + sum(l(y, x) for y in g[x] if y != p)
        return l(0, -1)