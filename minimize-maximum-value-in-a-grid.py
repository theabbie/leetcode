from collections import *

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        
    def find(self, a):
        if a == self.parent[a]:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
        
    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            if self.size[parent_a] < self.size[parent_b]:
                parent_a, parent_b = parent_b, parent_a
            self.parent[parent_b] = parent_a
            self.size[parent_a] += self.size[parent_b]

class Solution:
    def minScore(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        res = [[0] * n for _ in range(m)]
        pos = lambda i, j: n * i + j
        dsu = DSU(m * n)
        for i in range(m):
            prev = {}
            for j in range(n):
                if matrix[i][j] in prev:
                    dsu.union(pos(i, j), pos(i, prev[matrix[i][j]]))
                prev[matrix[i][j]] = j
        for j in range(n):
            prev = {}
            for i in range(m):
                if matrix[i][j] in prev:
                    dsu.union(pos(i, j), pos(prev[matrix[i][j]], j))
                prev[matrix[i][j]] = i
        groups = defaultdict(set)
        for i in range(m):
            for j in range(n):
                groups[(matrix[i][j], dsu.find(pos(i, j)))].add((i, j))
        rowmax = [(float('-inf'), 0)] * m
        colmax = [(float('-inf'), 0)] * n
        for val, g in sorted(groups):
            rank = 1
            for x, y in groups[(val, g)]:
                rank = max(rank, int(val > rowmax[x][0]) + rowmax[x][1])
                rank = max(rank, int(val > colmax[y][0]) + colmax[y][1])
            for x, y in groups[(val, g)]:
                res[x][y] = rank
                rowmax[x] = max(rowmax[x], (val, rank))
                colmax[y] = max(colmax[y], (val, rank))
        return res