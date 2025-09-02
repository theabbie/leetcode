def solve(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    ans = [0] * n
    removed = [False] * n
    size = [0] * n

    def dfs_size(u, p):
        size[u] = 1
        for v in g[u]:
            if v != p and not removed[v]:
                dfs_size(v, u)
                size[u] += size[v]

    def dfs_centroid(u, p, total):
        for v in g[u]:
            if v != p and not removed[v] and size[v] * 2 > total:
                return dfs_centroid(v, u, total)
        return u

    def dfs_collect(u, p, depth, sid, buf):
        buf.append((u, depth, sid))
        for v in g[u]:
            if v != p and not removed[v]:
                dfs_collect(v, u, depth + 1, sid, buf)

    def decompose(start):
        dfs_size(start, -1)
        c = dfs_centroid(start, -1, size[start])
        removed[c] = True
        buf = []
        max1 = max2 = 0
        best = -1
        sid = 0
        for v in g[c]:
            if removed[v]:
                continue
            tmp = []
            dfs_collect(v, c, 1, sid, tmp)
            lm = max(d for _, d, _ in tmp)
            if lm > max1:
                max2, max1 = max1, lm
                best = sid
            elif lm > max2:
                max2 = lm
            buf.extend(tmp)
            sid += 1
        ans[c] = max(ans[c], max1)
        for u, d, s in buf:
            use = max1 if s != best else max2
            ans[u] = max(ans[u], use + d)
        for v in g[c]:
            if not removed[v]:
                decompose(v)

    decompose(0)
    return ans

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        res = solve(n, edges)
        m = min(res)
        return [i for i in range(n) if res[i] == m]