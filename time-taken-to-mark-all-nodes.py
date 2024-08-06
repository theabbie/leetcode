class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        f = [0] * n
        s = [0] * n
        c = [0] * n
        def dfs(i, p):
            for j in graph[i]:
                if j != p:
                    cost = 1 if j & 1 else 2
                    dfs(j, i)
                    if f[j] + cost > f[i]:
                        s[i] = f[i];
                        f[i] = f[j] + cost
                        c[i] = j
                    elif f[j] + cost > s[i]:
                        s[i] = f[j] + cost
        dfs(0, -1)
        res = [0] * n
        def sdfs(i, p):
            for j in graph[i]:
                if j != p:
                    cost = 1 if i & 1 else 2
                    if c[i] == j:
                        if f[j] < s[i] + cost:
                            s[j] = f[j]
                            f[j] = s[i] + cost
                            c[j] = i
                        else:
                            s[j] = max(s[j], s[i] + cost)
                    else:
                        s[j] = f[j]
                        f[j] = f[i] + cost
                        c[j] = i
                    sdfs(j, i)
        sdfs(0, -1)
        return f