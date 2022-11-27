from collections import defaultdict

class Solution:
    def DFS(self, curr, stones, rows, cols, v):
        v.add(curr)
        x, y = stones[curr]
        for j in rows[x]:
            if j not in v:
                self.DFS(j, stones, rows, cols, v)
        for j in cols[y]:
            if j not in v:
                self.DFS(j, stones, rows, cols, v)
    
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rows = defaultdict(set)
        cols = defaultdict(set)
        for i in range(n):
            x, y = stones[i]
            rows[x].add(i)
            cols[y].add(i)
        res = 0
        v = set()
        for i in range(n):
            if i not in v:
                currv = set()
                self.DFS(i, stones, rows, cols, currv)
                res += len(currv) - 1
                v.update(currv)
        return res