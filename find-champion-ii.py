class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        for a, b in edges:
            parent[b] = find(a)
        res = []
        for i in range(n):
            if find(i) == i:
                res.append(i)
        if len(res) > 1 or len(res) == 0:
            return -1
        return res[0]