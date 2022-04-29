from collections import defaultdict

class Solution:
    def root(self, x, parent):
        if parent[x] == x:
            return x
        parent[x] = self.root(parent[x], parent)
        return parent[x]
    
    def connect(self, x, y, parent):
        x = self.root(x, parent)
        y = self.root(y, parent)
        if x != y:
            parent[x] = y
    
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        graph = defaultdict(list)
        pos = {}
        for i in range(n):
            pos[row[i]] = i
        for i in range(n // 2):
            a = row[2 * i]
            a = a + 1 - 2 * (a % 2)
            b = row[2 * i + 1]
            b = b + 1 - 2 * (b % 2)
            graph[i].append(pos[a] // 2)
            graph[i].append(pos[b] // 2)
        parent = list(range(n // 2))
        for i in graph:
            for j in graph[i]:
                self.connect(i, j, parent)
        for i in graph:
            parent[i] = self.root(i, parent)
        ctr = 0
        for i in range(n // 2):
            if parent[i] != i:
                ctr += 1
        return ctr