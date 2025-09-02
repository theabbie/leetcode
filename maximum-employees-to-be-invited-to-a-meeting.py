class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        graph = [[] for _ in range(n)]
        for i in range(n):
            graph[i].append(favorite[i])
            graph[favorite[i]].append(i)
        def longest(i, p):
            res = 1
            for j in graph[i]:
                if j == p:
                    continue
                res = max(res, 1 + longest(j, i))
            return res
        res = 0
        v = set()
        for node in range(n):
            i = 0
            pos = {}
            curr = []
            while node not in v:
                pos[node] = i
                curr.append(node)
                v.add(node)
                node = favorite[node]
                i += 1
            if node in pos:
                res = max(res, i - pos[node])
        extra = 0
        for i in range(n):
            if i < favorite[i] and favorite[favorite[i]] == i:
                extra += longest(i, favorite[i]) + longest(favorite[i], i)
        res = max(res, extra)
        return res