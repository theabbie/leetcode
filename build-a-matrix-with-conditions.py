from collections import defaultdict, deque

class Solution:
    def getSort(self, edges, k):
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
        indegree = [0] * (k + 1)
        for a in graph:
            for b in graph[a]:
                indegree[b] += 1
        res = []
        q = deque()
        for i in range(1, k + 1):
            if indegree[i] == 0:
                q.append(i)
        while len(q) > 0:
            curr = q.pop()
            res.append(curr)
            for j in graph[curr]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.appendleft(j)
        return res
    
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * k for _ in range(k)]
        colsort = self.getSort(colConditions, k)
        rowsort = self.getSort(rowConditions, k)
        if len(colsort) < k or len(rowsort) < k:
            return []
        pos = {}
        for i in range(k):
            pos[rowsort[i]] = i
        for i in range(k):
            matrix[pos[colsort[i]]][i] = colsort[i]
        return matrix