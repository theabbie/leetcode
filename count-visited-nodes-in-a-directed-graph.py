from collections import deque, defaultdict

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        res = [0] * n
        v = set()
        q = deque()
        vs = set()
        graph = defaultdict(set)
        for i in range(n):
            graph[edges[i]].add(i)
        for node in range(n):
            i = 0
            pos = {}
            curr = []
            while node != -1 and node not in v:
                pos[node] = i
                curr.append(node)
                v.add(node)
                node = edges[node]
                i += 1
            if node != -1 and node in pos:
                for j in range(1, i - pos[node] + 1):
                    res[curr[-j]] = i - pos[node]
                    q.appendleft((curr[-j], i - pos[node]))
                    vs.add(curr[-j])
        while len(q) > 0:
            curr, d = q.pop()
            res[curr] = d
            for j in graph[curr]:
                if j not in vs:
                    vs.add(j)
                    q.appendleft((j, d + 1))
        return res