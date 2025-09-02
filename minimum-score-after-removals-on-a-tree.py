class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parent = [-1] * n
        tin = [0] * n
        tout = [0] * n
        subtree = [0] * n
        time = 0
        def dfs(u, p):
            nonlocal time
            tin[u] = time
            time += 1
            subtree[u] = nums[u]
            for v in adj[u]:
                if v == p: continue
                parent[v] = u
                dfs(v, u)
                subtree[u] ^= subtree[v]
            tout[u] = time
        dfs(0, -1)
        total = subtree[0]
        children = []
        for u, v in edges:
            if parent[u] == v:
                children.append(u)
            else:
                children.append(v)
        m = len(children)
        ans = float('inf')
        for i in range(m):
            for j in range(i + 1, m):
                c1 = children[i]
                c2 = children[j]
                s1 = subtree[c1]
                s2 = subtree[c2]
                if tin[c1] <= tin[c2] < tout[c1]:
                    a = s2
                    b = s1 ^ s2
                    c = total ^ s1
                elif tin[c2] <= tin[c1] < tout[c2]:
                    a = s1
                    b = s1 ^ s2
                    c = total ^ s2
                else:
                    a = s1
                    b = s2
                    c = total ^ s1 ^ s2
                curr = max(a, b, c) - min(a, b, c)
                ans = min(ans, curr)
        return ans