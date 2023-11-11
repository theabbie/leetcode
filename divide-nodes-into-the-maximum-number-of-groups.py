from collections import defaultdict, deque

class Solution:
    def check(self, graph, i, color):
        for j in graph[i]:
            if color[j] != -1 and color[j] != 1 - color[i]:
                return False
            if color[j] == -1:
                color[j] = 1 - color[i]
                self.currv.add(j)
                if not self.check(graph, j, color):
                    return False
        return True
    
    def count(self, graph, i):
        q = deque([(i, 1)])
        v = {i}
        res = 0
        while len(q) > 0:
            curr, ctr = q.pop()
            res = ctr
            for j in graph[curr]:
                if j not in v:
                    v.add(j)
                    q.appendleft((j, ctr + 1))
        return res
    
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a - 1].add(b - 1)
            graph[b - 1].add(a - 1)
        color = [-1] * n
        res = 0
        for i in range(n):
            if color[i] == -1:
                color[i] = 0
                self.currv = {i}
                if not self.check(graph, i, color):
                    return -1
                curr = 0
                for x in self.currv:
                    curr = max(curr, self.count(graph, x))
                res += curr
        return res