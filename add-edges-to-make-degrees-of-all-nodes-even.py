from collections import defaultdict

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        degree = [0] * n
        for a, b in edges:
            degree[a - 1] += 1
            degree[b - 1] += 1
        oddctr = 0
        for d in degree:
            if d & 1:
                oddctr += 1
        if oddctr == 0:
            return True
        if oddctr != 2 and oddctr != 4:
            return False
        graph = defaultdict(set)
        for a, b in edges:
            graph[a - 1].add(b - 1)
            graph[b - 1].add(a - 1)
        oddset = set()
        evenset = set()
        for i in range(n):
            if degree[i] & 1:
                oddset.add(i)
            else:
                evenset.add(i)
        if oddctr == 2:
            i, j = min(oddset), max(oddset)
            if j not in graph[i]:
                return True
            elif len(evenset - (graph[i] | graph[j])) > 0:
                return True
        if oddctr == 4:
            a, b, c, d = sorted(oddset)
            print(a, b, c, d)
            if b not in graph[a] and d not in graph[c]:
                return True
            if c not in graph[a] and d not in graph[b]:
                return True
            if d not in graph[a] and c not in graph[b]:
                return True
        return False