class Solution:
    def sumOfDistancesInTree(self, n, edges):
        res = [0] * n
        subctr = [0] * n
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def dfs(root, prev):
            s = 0
            ctr = 1
            for j in graph[root]:
                if j != prev:
                    currs, currctr = dfs(j, root)
                    ctr += currctr
                    s += currs + currctr
            subctr[root] = ctr
            return s, ctr
        res[0], tmp = dfs(0, -1)
        stack = [(0, -1)]
        while len(stack) > 0:
            curr, prev = stack.pop()
            for j in graph[curr]:
                if j != prev:
                    res[j] = n + res[curr] - 2 * subctr[j]
                    stack.append((j, curr))
        return res